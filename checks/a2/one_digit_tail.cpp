// A2-F01 independent coefficient reader. Every exponent is represented by
// its complete multiplicative period; there is no height cutoff.
// Signed __int128 is used for all polynomial arithmetic. With the stated
// tag bounds and T mod p < 241, the absolute intermediate bound is < 2^70.
// Periods are individually < 909. No product of periods is constructed.

#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>

using Wide = __int128_t;

struct Constraint {
    int period;
    std::vector<int> allowed;
};

std::vector<int> orbit(int modulus) {
    assert(std::gcd(modulus, 10) == 1);
    const int first = 100 % modulus;
    std::vector<int> values{first};
    int value = first * 10 % modulus;
    while (value != first) {
        values.push_back(value);
        value = value * 10 % modulus;
    }
    return values;
}

int residue(Wide value, int p) {
    const int answer = static_cast<int>(value % p);
    return answer < 0 ? answer + p : answer;
}

bool joint_empty(std::vector<Constraint> constraints) {
    // Reverse pair order makes this a separately implemented propagation.
    bool changed = true;
    while (changed) {
        changed = false;
        for (int i = static_cast<int>(constraints.size()) - 1; i >= 0; --i) {
            auto& current = constraints[i];
            for (int j = static_cast<int>(constraints.size()) - 1; j >= 0; --j) {
                const auto& other = constraints[j];
                const int common = std::gcd(current.period, other.period);
                std::vector<bool> possible(common);
                for (int r : other.allowed) possible[r % common] = true;
                const auto old_size = current.allowed.size();
                std::erase_if(current.allowed, [&](int r) { return !possible[r % common]; });
                if (current.allowed.empty()) return true;
                changed |= current.allowed.size() != old_size;
            }
        }
    }
    return false;
}

int main() {
    std::vector<int> primes;
    std::map<int, std::vector<int>> powers;
    std::map<int, std::vector<bool>> squares;
    for (int p = 3; p <= 241; ++p) {
        bool prime = p != 5;
        for (int d = 2; d * d <= p; ++d) if (p % d == 0) prime = false;
        if (!prime) continue;
        primes.push_back(p);
        powers[p] = orbit(p);
        squares[p] = std::vector<bool>(p);
        for (int n = 0; n < p; ++n) squares[p][n * n % p] = true;
    }
    int tags = 0, integrality = 0, single_prime = 0, joint = 0;
    for (int A : {2, 4, 6, 8}) for (int b : {7, 9}) {
        for (int a = 10; a < 2 * b; ++a) {
            if (std::gcd(a, b) != 1) continue;
            for (int c = 1; c <= b; ++c) {
                if (b % c) continue;
                for (int k = 10 * c + 1; k < 101 * c; k += 2) {
                    if (std::gcd(k, 10 * b) != 1) continue;
                    ++tags;
                    const auto tk = orbit(k);
                    Constraint integral{static_cast<int>(tk.size()), {}};
                    for (int i = 0; i < integral.period; ++i) {
                        if ((10 * tk[i] + b) % k == 0) integral.allowed.push_back(i);
                    }
                    if (integral.allowed.empty()) { ++integrality; continue; }
                    const Wide h = Wide(k + 10 * c) * (k + 10 * c) - Wide(100 * c) * (100 * c);
                    const Wide C = A * A * b * b + a * a;
                    // Expanded coefficients, independently of Python's
                    // factored expression in T.
                    const Wide p2 = 100 * (Wide(k) * k * b * b * A * A - h * C);
                    const Wide p1 = 20 * (Wide(k) * k * b * b * A * a - h * C * b);
                    const Wide p0 = Wide(k) * k * b * b * a * a - h * C * b * b;
                    std::vector<Constraint> constraints{integral};
                    bool empty = false;
                    for (int p : primes) {
                        const auto& ts = powers[p];
                        Constraint gate{static_cast<int>(ts.size()), {}};
                        for (int i = 0; i < gate.period; ++i) {
                            const Wide value = (p2 * ts[i] + p1) * ts[i] + p0;
                            if (squares[p][residue(value, p)]) gate.allowed.push_back(i);
                        }
                        if (gate.allowed.empty()) { empty = true; ++single_prime; break; }
                        constraints.push_back(std::move(gate));
                    }
                    if (empty) continue;
                    if (!joint_empty(std::move(constraints))) {
                        std::cerr << "uncovered tag " << A << ' ' << b << ' ' << a
                                  << ' ' << c << ' ' << k << '\n';
                        return 1;
                    }
                    ++joint;
                }
            }
        }
    }
    assert(tags == 11544 && integrality + single_prime + joint == tags);
    std::cout << "OK: A2-F01 independent coefficient reader: " << tags << " / " << tags << " tags excluded\n";
    std::cout << "integrality=" << integrality << " single-prime=" << single_prime << " joint-periods=" << joint << '\n';
    std::cout << "__int128 arithmetic; all m2 >= 2 covered by complete periods\n";
}
