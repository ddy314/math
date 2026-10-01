// Complete fixed-suffix DD certificate; see core.md section 27.7.5.
// --tail-one covers the complementary n3=1 slice in global-framework §10.7.
// All b1 and numerator heights are covered by the proved bounds.
// g++ -O2 -std=c++20 this-file.cpp -o /tmp/check_dd_last_two_single_digit
// No floating point. Checked 256-bit arithmetic; every discriminant is <2^190
// under the coarser boxes checked below. This is not a full DD closure.
#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>

using namespace boost::multiprecision;
using I = number<cpp_int_backend<256, 256, signed_magnitude, checked, void>>;
using U = number<cpp_int_backend<256, 256, unsigned_magnitude, checked, void>>;
using u64 = std::uint64_t;
using Triple = std::array<int, 3>;

void require(bool condition, const char* message) {
    if (!condition) throw std::runtime_error(message);
}
u64 ten(int n) {
    require(n >= 0 && n <= 18, "decimal exponent outside checked bound");
    u64 result = 1;
    while (n--) result *= 10;
    return result;
}
int depth(u64 x, int p) {
    require(x > 0, "valuation of zero");
    int e = 0;
    while (x % p == 0) { x /= p; ++e; }
    return e;
}
int digits(u64 x) {
    int n = 0;
    do { ++n; x /= 10; } while (x);
    return n;
}
u64 strict_cap(u64 numerator, u64 denominator) {
    require(numerator > 0 && denominator > 0, "nonpositive rational bound");
    return (numerator - 1) / denominator;
}
std::vector<int> prime_support(u64 q) {
    std::vector<int> result;
    for (int p = 2; u64(p)*p <= q; ++p) {
        if (q % p) continue;
        result.push_back(p);
        while (q % p == 0) q /= p;
    }
    if (q > 1) result.push_back(int(q));
    return result;
}

std::vector<Triple> denominator_states() {
    std::vector<Triple> result;
    int divisor_count = 0;
    for (int b2 = 1; b2 <= 9; ++b2) for (int b3 = 1; b3 <= 9; ++b3) {
        const u64 bound = std::lcm(std::lcm(u64(b2), u64(b3)), u64(10*b2+b3));
        require(bound <= 8019, "first denominator bound");
        for (u64 b1 = 1; b1 <= bound; ++b1) {
            if (bound % b1) continue;
            ++divisor_count;
            const u64 qword = 10*b1+b2, d = 10*qword+b3;
            if (10*qword % b3) continue;
            std::array<int, 3> es{depth(b1, 2), depth(b2, 2), depth(b3, 2)};
            const int e = *std::max_element(es.begin(), es.end());
            if (e > 0 && (std::count(es.begin(), es.end(), e) != 1 ||
                          b3 % 2 || depth(d, 2) != e)) continue;
            if (e >= 2 && std::count(es.begin(), es.end(), e-1) == 1) continue;
            bool impossible = false;
            const u64 q = std::lcm(std::lcm(b1, u64(b2)), u64(b3));
            for (int p : prime_support(q)) {
                es = {depth(b1, p), depth(b2, p), depth(b3, p)};
                const int maximum = *std::max_element(es.begin(), es.end());
                const int multiplicity = std::count(es.begin(), es.end(), maximum);
                if ((multiplicity == 1 || (multiplicity == 2 && p % 4 == 3)) &&
                    depth(d, p) < maximum) { impossible = true; break; }
            }
            if (impossible) continue;
            const int content = std::min({depth(b1, 3), depth(b2, 3), depth(b3, 3)});
            u64 common = 1;
            for (int i = 0; i < content; ++i) common *= 3;
            const u64 c1 = b1/common, c2 = b2/common, c3 = b3/common;
            const u64 pair_sum = (c1*c2+c1*c3+c2*c3) % 9;
            if (pair_sum == 3 || pair_sum == 6) continue;
            // Q=4 mod5 is necessary for all n3>=1. It yields the same 19
            // states as the stronger DD condition Q=24 mod25.
            if (b3 == 5 && b1*b2 % 5 && qword % 5 != 4) continue;
            result.push_back({int(b1), b2, b3});
        }
    }
    require(divisor_count == 994, "divisor state coverage differs");
    require(result.size() == 19, "denominator projection differs");
    std::cout << "994 divisor triples -> 19 denominator states\n";
    return result;
}

U integer_sqrt(U value) {
    // Restoring integer square root, independent of Python's math.isqrt.
    U result = 0, bit = U(1) << 254;
    while (bit > value) bit >>= 2;
    while (bit != 0) {
        if (value >= result + bit) {
            value -= result + bit;
            result = (result >> 1) + bit;
        } else result >>= 1;
        bit >>= 2;
    }
    return result;
}
bool square_possible(const I& x) {
    if (x < 0) return false;
    for (int modulus : {64, 63, 65}) {
        const int residue = (x % modulus).convert_to<int>();
        bool found = false;
        for (int j = 0; j < modulus; ++j) if (j*j % modulus == residue) {
            found = true; break;
        }
        if (!found) return false;
    }
    return true;
}
std::vector<I> roots(u64 q, u64 d, u64 cx, u64 weight, u64 known, I rest, bool standard) {
    const I a = I(q)*q*weight*weight-I(d)*d*cx*cx;
    const I b = 2*I(q)*q*weight*known;
    const I c = I(q)*q*known*known-I(d)*d*rest;
    require(a != 0, "unexpected quadratic degeneracy");
    I radicand = standard ? I(b*b-4*a*c) : I(I(q)*q*cx*cx*known*known+a*rest);
    if (!square_possible(radicand)) return {};
    const I z = I(integer_sqrt(U(radicand)));
    if (z*z != radicand) return {};
    std::vector<I> output;
    for (int sign : {-1, 1}) {
        const I numerator = standard ? I(-b+sign*z) : I(-I(q)*q*weight*known+sign*I(d)*z);
        const I denominator = standard ? I(2*a) : a;
        if (numerator % denominator == 0 && numerator / denominator > 0) {
            const I root = numerator / denominator;
            if (std::find(output.begin(), output.end(), root) == output.end()) output.push_back(root);
        }
    }
    return output;
}

struct Plan { int first_tail, second_cap, tail_cap; u64 first_cap; };
Plan high_plan(int b1, int b2, int b3) {
    const u64 d = 100*b1+10*b2+b3, q = std::lcm(std::lcm(b1, b2), b3);
    int n = 2;
    while (ten(n)*b2 <= d) ++n;
    const u64 y = ten(n);
    int second = 0;
    while (ten(second+1)*b3*b1*y < d*(b1*y+b3)) ++second;
    const u64 a1 = strict_cap(d*b1*y, b3*(10*b1*y-d));
    const u64 a2 = ten(second)-1;
    const u64 a3 = strict_cap(b3*q*(a1*a1*b2*b2+a2*a2*b1*b1), 2*u64(b1)*b1*b2*b2);
    require(n <= 4 && second <= 4 && a1 <= 2557 && digits(a3) <= 9, "high box size");
    return {n, second, digits(a3), a1};
}
std::pair<u64, int> low_plan(int b1, int b2, int b3, u64 y) {
    const u64 d = 100*b1+10*b2+b3, q = std::lcm(std::lcm(b1, b2), b3);
    const u64 a1 = strict_cap(d*b1*(10*b3+(y-1)*b2), b2*b3*(10*y*b1-d));
    const u64 a2 = strict_cap(b2*q*(a1*a1*b3*b3+(y-1)*(y-1)*b1*b1), 2*u64(b1)*b1*b3*b3);
    require(a1 <= 2868 && digits(a2) <= 9 && y <= 1000, "low box size");
    return {a1, digits(a2)};
}

u64 tail_one_certificate(Triple bs, bool standard) {
    const auto [b1,b2,b3] = bs;
    const u64 d = 100*b1+10*b2+b3, q = std::lcm(std::lcm(b1,b2),b3);
    const u64 c1=q/b1, c2=q/b2, c3=q/b3;
    const u64 uniform = strict_cap(d*b1*(100*b3+9*b2), b2*b3*(1000*u64(b1)-d));
    const u64 a2cap = strict_cap(b2*q*(uniform*uniform*b3*b3+81*u64(b1)*b1),
                                2*u64(b1)*b1*b3*b3);
    const int second_cap = digits(a2cap);
    require(uniform <= 823 && second_cap <= 5, "tail-one box size");
    u64 rows = 0;
    auto solution = [&](I a1, I a2, I a3, u64 x) {
        const I word = (a1*x+a2)*10+a3;
        const I sphere = I(c1)*c1*a1*a1+I(c2)*c2*a2*a2+I(c3)*c3*a3*a3;
        require(I(q)*q*word*word == I(d)*d*sphere, "tail-one original equation");
        throw std::runtime_error("tail-one exact solution found");
    };
    for (int n2=2; n2<=second_cap; ++n2) {
        const u64 x=ten(n2);
        const u64 cap = strict_cap(d*b1*(x*b3+9*b2), b2*b3*(10*x*b1-d));
        require(cap<=uniform, "tail-one tightening");
        for (u64 a1=1; a1<=cap; ++a1) {
            if (std::gcd(a1,u64(b1))!=1) continue;
            for (u64 a3=1; a3<=9; ++a3) {
                if (std::gcd(a3,u64(b3))!=1) continue;
                ++rows;
                for (const I& z:roots(q,d,c2,10,a1*x*10+a3,
                                     I(c1)*c1*a1*a1+I(c3)*c3*a3*a3,standard)) {
                    if (z<x/10 || z>=x) continue;
                    const u64 a2=z.convert_to<u64>();
                    if (std::gcd(a2,u64(b2))==1) solution(I(a1),z,I(a3),x);
                }
            }
        }
    }
    for (u64 a2=1; a2<=9; ++a2) {
        if (std::gcd(a2,u64(b2))!=1) continue;
        for (u64 a3=1; a3<=9; ++a3) {
            if (std::gcd(a3,u64(b3))!=1) continue;
            ++rows;
            // Recover every positive a1; no height cutoff or narrow cast.
            for (const I& z:roots(q,d,c1,100,a2*10+a3,
                                 I(c2)*c2*a2*a2+I(c3)*c3*a3*a3,standard)) {
                const u64 residue=(z%b1).convert_to<u64>();
                if (std::gcd(residue,u64(b1))==1) solution(z,I(a2),I(a3),10);
            }
        }
    }
    return rows;
}

int main(int argc, char** argv) {
    try {
        bool standard=false, tail_one=false;
        for (int i=1; i<argc; ++i) {
            if (std::string(argv[i])=="--standard") standard=true;
            else if (std::string(argv[i])=="--tail-one") tail_one=true;
            else require(false,"supported flags: --standard, --tail-one");
        }
        // Test edge cases of the independent integer square-root algorithm.
        for (U n : {U(0), U(1), U(3), U(7), U(123456789), (U(1)<<80)+17}) {
            require(integer_sqrt(n*n) == n, "sqrt perfect square");
            if (n > 0) require(integer_sqrt(n*n-1) == n-1, "sqrt below square");
        }
        u64 total = 0;
        for (auto bs : denominator_states()) {
            const auto [b1, b2, b3] = bs;
            require(b1 <= 280, "filtered denominator size");
            if (tail_one) {
                const u64 rows=tail_one_certificate(bs,standard);
                total+=rows;
                std::cout << '(' << b1 << ',' << b2 << ',' << b3 << "): " << rows
                          << " tail-one rows, hits=0\n";
                continue;
            }
            const u64 d = 100*b1+10*b2+b3, q = std::lcm(std::lcm(b1, b2), b3);
            require(d <= 28056 && q <= 840, "integer width bound");
            const u64 c1 = q/b1, c2 = q/b2, c3 = q/b3;
            const Plan high = high_plan(b1, b2, b3);
            u64 rows = 0;
            auto accept = [&](u64 a1, u64 a2, u64 a3, u64 x, u64 y) {
                require(std::gcd(a1,u64(b1)) == 1 && std::gcd(a2,u64(b2)) == 1 &&
                        std::gcd(a3,u64(b3)) == 1, "candidate reducedness");
                require(x/10 <= a2 && a2 < x && y/10 <= a3 && a3 < y, "candidate length");
                const I word = I(a1)*x*y+I(a2)*y+a3;
                const I sphere = I(c1)*c1*a1*a1+I(c2)*c2*a2*a2+I(c3)*c3*a3*a3;
                require(I(q)*q*word*word == I(d)*d*sphere, "candidate original equation");
                throw std::runtime_error("exact solution found");
            };
            for (int n3 = high.first_tail; n3 <= high.tail_cap; ++n3) {
                const u64 y = ten(n3);
                for (int n2 = 1; n2 <= high.second_cap; ++n2) {
                    const u64 x = ten(n2);
                    const u64 cap = strict_cap(d*b1*y, b3*(x*b1*y-d));
                    for (u64 a1 = 1; a1 <= cap; ++a1) {
                        if (std::gcd(a1, u64(b1)) != 1) continue;
                        for (u64 a2 = x/10; a2 < x; ++a2) {
                            if (std::gcd(a2, u64(b2)) != 1) continue;
                            ++rows;
                            const u64 known = (a1*x+a2)*y;
                            for (const I& z : roots(q,d,c3,1,known,I(c1)*c1*a1*a1+I(c2)*c2*a2*a2,standard)) {
                                if (z < y/10 || z >= y) continue;
                                const u64 a3 = z.convert_to<u64>();
                                if (std::gcd(a3,u64(b3)) == 1) accept(a1,a2,a3,x,y);
                            }
                        }
                    }
                }
            }
            for (int n3 = 2; n3 < high.first_tail; ++n3) {
                const u64 y = ten(n3);
                const auto [uniform, second_cap] = low_plan(b1,b2,b3,y);
                for (int n2 = 1; n2 <= second_cap; ++n2) {
                    const u64 x = ten(n2);
                    const u64 cap = strict_cap(d*b1*(x*b3+(y-1)*b2), b2*b3*(x*y*b1-d));
                    require(cap <= uniform, "low tightening");
                    for (u64 a1 = 1; a1 <= cap; ++a1) {
                        if (std::gcd(a1,u64(b1)) != 1) continue;
                        for (u64 a3 = y/10; a3 < y; ++a3) {
                            if (std::gcd(a3,u64(b3)) != 1) continue;
                            ++rows;
                            const u64 known = a1*x*y+a3;
                            for (const I& z : roots(q,d,c2,y,known,I(c1)*c1*a1*a1+I(c3)*c3*a3*a3,standard)) {
                                if (z < x/10 || z >= x) continue;
                                const u64 a2 = z.convert_to<u64>();
                                if (std::gcd(a2,u64(b2)) == 1) accept(a1,a2,a3,x,y);
                            }
                        }
                    }
                }
            }
            total += rows;
            std::cout << '(' << b1 << ',' << b2 << ',' << b3 << "): " << rows << " rows, hits=0\n";
        }
        require(total == (tail_one ? 45015 : 3759479), "quadratic coverage differs");
        std::cout << "PASS: " << total << " rows, exact hits=0; reader="
                  << (standard ? "standard" : "factored")
                  << (tail_one ? "; n3=1 suffix-one slice\n" : "; general DD remains open\n");
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "FAIL: " << error.what() << '\n';
        return 1;
    }
}
