// Exact C++ accelerator for the S_12=4, n_3=31 DD boundary slices.
//
// Build:
//   g++ -O3 -DNDEBUG -std=c++20 -fopenmp scripts/check_dd_2729.cpp -o /tmp/check_dd_2729_cpp
//
// Audit the optimizations, then cross-check the two short Python slices:
//   /tmp/check_dd_2729_cpp --self-check --m3 21 --expect-baseline
//   /tmp/check_dd_2729_cpp --m3 21 --expect-baseline
//   uv run python scripts/check_dd_2729.py --m3 21
//   /tmp/check_dd_2729_cpp --m3 20 --expect-baseline
//   uv run python scripts/check_dd_2729.py --m3 20
//
// Run the complete nonempty range assigned to this accelerator:
//   /tmp/check_dd_2729_cpp --m3-min 15 --m3-max 21
//
// This program deliberately mirrors check_dd_2726.py/check_dd_2729.py:
// denominator tails, ordered digit shapes, the exhaustive 2/5-adic state
// disjunction, the strict squarefree-gap inequality, the modular-square sieve,
// and the unified discriminant are unchanged.  cpp_int is used for the final
// discriminant.  This implementation intentionally omits the optional Python
// corner-gap, valuation-height-box, and general-L_F prefilters, so its recorded
// counters are the stable unfiltered baselines.  Its exact p-adic residue tree
// finds numerator rows accepted by at least one signature without materializing
// every digit pair.  --self-check compares that tree and the quadratic interval
// solver with direct exhaustive evaluation.

#include <algorithm>
#include <array>
#include <atomic>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <exception>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <optional>
#include <random>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

#ifdef _OPENMP
#include <omp.h>
#endif

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = unsigned __int128;
using i128 = __int128;

namespace {

constexpr int S = 4;
constexpr int N3 = 31;
constexpr u64 SQUARE_MODULUS = 64ULL * 9ULL * 5ULL * 7ULL * 11ULL * 13ULL;

u64 pow_u64(u64 base, int exponent) {
    u64 result = 1;
    for (int i = 0; i < exponent; ++i) {
        if (result > std::numeric_limits<u64>::max() / base) {
            throw std::overflow_error("u64 power overflow");
        }
        result *= base;
    }
    return result;
}

cpp_int pow_cpp(u64 base, int exponent) {
    cpp_int result = 1;
    for (int i = 0; i < exponent; ++i) result *= base;
    return result;
}

int valuation(u64 value, u64 prime) {
    if (value == 0) throw std::invalid_argument("valuation(0)");
    int exponent = 0;
    while (value % prime == 0) {
        value /= prime;
        ++exponent;
    }
    return exponent;
}

u64 mul_mod(u64 left, u64 right, u64 modulus) {
    return static_cast<u64>((static_cast<u128>(left) * right) % modulus);
}

u64 pow_mod(u64 base, int exponent, u64 modulus) {
    u64 result = 1 % modulus;
    base %= modulus;
    while (exponent > 0) {
        if (exponent & 1) result = mul_mod(result, base, modulus);
        base = mul_mod(base, base, modulus);
        exponent >>= 1;
    }
    return result;
}

cpp_int integer_sqrt(const cpp_int& value) {
    if (value < 0) throw std::invalid_argument("sqrt of negative cpp_int");
    if (value < 2) return value;
    const std::size_t bit_count = boost::multiprecision::msb(value) + 1;
    cpp_int current = cpp_int(1) << ((bit_count + 1) / 2);
    while (true) {
        cpp_int next = (current + value / current) >> 1;
        if (next >= current) break;
        current = std::move(next);
    }
    while ((current + 1) * (current + 1) <= value) ++current;
    while (current * current > value) --current;
    return current;
}

struct Interval {
    u64 lower;
    u64 upper;
};

i128 quadratic_value(i128 quadratic, i128 linear, i128 constant, u64 x) {
    const i128 xx = static_cast<i128>(x);
    return quadratic * xx * xx - linear * xx + constant;
}

std::vector<Interval> positive_quadratic_ranges(
    i128 quadratic,
    i128 linear,
    i128 constant,
    u64 lower,
    u64 upper
) {
    if (quadratic <= 0 || lower > upper || linear < 0) {
        throw std::invalid_argument("invalid positive-quadratic range input");
    }
    const u64 vertex_floor = static_cast<u64>(linear / (2 * quadratic));
    const u64 left_end = std::min(upper, std::max(lower, vertex_floor));
    const u64 right_start = std::max(lower, std::min(upper, vertex_floor + 1));
    std::vector<Interval> ranges;

    if (quadratic_value(quadratic, linear, constant, lower) > 0) {
        if (quadratic_value(quadratic, linear, constant, left_end) > 0) {
            ranges.push_back({lower, left_end});
        } else {
            u64 lo = lower;
            u64 hi = left_end;
            while (lo < hi) {
                const u64 middle = lo + (hi - lo + 1) / 2;
                if (quadratic_value(quadratic, linear, constant, middle) > 0) {
                    lo = middle;
                } else {
                    hi = middle - 1;
                }
            }
            ranges.push_back({lower, lo});
        }
    }

    if (quadratic_value(quadratic, linear, constant, upper) > 0) {
        Interval candidate{};
        if (quadratic_value(quadratic, linear, constant, right_start) > 0) {
            candidate = {right_start, upper};
        } else {
            u64 lo = right_start;
            u64 hi = upper;
            while (lo < hi) {
                const u64 middle = lo + (hi - lo) / 2;
                if (quadratic_value(quadratic, linear, constant, middle) > 0) {
                    hi = middle;
                } else {
                    lo = middle + 1;
                }
            }
            candidate = {lo, upper};
        }
        if (!ranges.empty() && candidate.lower <= ranges.back().upper + 1) {
            ranges.back().upper = candidate.upper;
        } else {
            ranges.push_back(candidate);
        }
    }
    return ranges;
}

std::vector<u64> primes_up_to(u64 bound) {
    std::vector<bool> composite(bound + 1, false);
    std::vector<u64> primes;
    for (u64 value = 2; value <= bound; ++value) {
        if (composite[value]) continue;
        primes.push_back(value);
        if (value <= bound / value) {
            for (u64 multiple = value * value; multiple <= bound; multiple += value) {
                composite[multiple] = true;
            }
        }
    }
    return primes;
}

const std::vector<u64>& factor_primes() {
    static const std::vector<u64> primes = primes_up_to(100000);
    return primes;
}

std::vector<std::pair<u64, int>> factorize(u64 value) {
    std::vector<std::pair<u64, int>> factors;
    for (u64 prime : factor_primes()) {
        if (prime > value / prime) break;
        if (value % prime) continue;
        int exponent = 0;
        do {
            value /= prime;
            ++exponent;
        } while (value % prime == 0);
        factors.emplace_back(prime, exponent);
    }
    if (value > 1) factors.emplace_back(value, 1);
    return factors;
}

std::vector<u64> distinct_prime_factors(u64 value) {
    std::vector<u64> result;
    for (const auto& [prime, exponent] : factorize(value)) {
        (void)exponent;
        result.push_back(prime);
    }
    return result;
}

u64 coprime_count(u64 lower, u64 upper, const std::vector<u64>& primes) {
    if (lower > upper) return 0;
    i128 total = static_cast<i128>(upper - lower + 1);
    const std::size_t combinations = std::size_t(1) << primes.size();
    for (std::size_t mask = 1; mask < combinations; ++mask) {
        u64 divisor = 1;
        int bits = 0;
        for (std::size_t index = 0; index < primes.size(); ++index) {
            if (!(mask & (std::size_t(1) << index))) continue;
            divisor *= primes[index];
            ++bits;
        }
        const u64 multiples = upper / divisor - (lower - 1) / divisor;
        total += (bits & 1) ? -static_cast<i128>(multiples)
                            : static_cast<i128>(multiples);
    }
    if (total < 0) throw std::logic_error("negative coprime count");
    return static_cast<u64>(total);
}

std::vector<u64> bounded_divisors(u64 value, int extra_2_5, u64 cap) {
    auto factors = factorize(value);
    bool saw_two = false;
    bool saw_five = false;
    for (auto& [prime, exponent] : factors) {
        if (prime == 2) {
            exponent += extra_2_5;
            saw_two = true;
        } else if (prime == 5) {
            exponent += extra_2_5;
            saw_five = true;
        }
    }
    if (!saw_two) factors.emplace_back(2, extra_2_5);
    if (!saw_five) factors.emplace_back(5, extra_2_5);
    std::sort(factors.begin(), factors.end());

    std::vector<u64> divisors;
    std::function<void(std::size_t, u64)> visit = [&](std::size_t index, u64 current) {
        if (index == factors.size()) {
            divisors.push_back(current);
            return;
        }
        const auto [prime, exponent] = factors[index];
        u64 power = 1;
        for (int e = 0; e <= exponent; ++e) {
            if (current <= cap / power) visit(index + 1, current * power);
            if (e == exponent || power > cap / prime) break;
            power *= prime;
        }
    };
    visit(0, 1);
    return divisors;
}

enum class Position { B3Unique, AllOdd, PrefixOrTie };
enum class PConditionKind { Disjunction, AtLeast, Unit };

struct PCondition {
    PConditionKind kind = PConditionKind::Unit;
    int resonance = 0;
    int plus_gap = 0;
    int minus_a = 0;
    int threshold = 0;

    auto key() const {
        return std::tuple(kind, resonance, plus_gap, minus_a, threshold);
    }
    bool operator<(const PCondition& other) const { return key() < other.key(); }
    bool operator==(const PCondition& other) const { return key() == other.key(); }
};

struct Signature {
    Position position = Position::PrefixOrTie;
    PCondition two;
    PCondition five;

    auto key() const { return std::tuple(position, two.key(), five.key()); }
    bool operator<(const Signature& other) const { return key() < other.key(); }
    bool operator==(const Signature& other) const { return key() == other.key(); }
};

bool p_condition_accepts(const PCondition& condition, int n_value, int a_value) {
    switch (condition.kind) {
        case PConditionKind::Unit:
            return true;
        case PConditionKind::AtLeast:
            return n_value >= condition.threshold;
        case PConditionKind::Disjunction:
            return n_value == condition.resonance ||
                   n_value - a_value == condition.plus_gap ||
                   a_value == condition.minus_a;
    }
    throw std::logic_error("unknown p-condition");
}

struct Tail {
    int m1 = 0;
    int m2 = 0;
    u64 b1 = 0;
    u64 b2 = 0;
    int m3 = 0;
    u64 kappa = 0;
    u64 Q = 0;
    u64 G = 0;
    Signature signature;
    u64 leading_mod = 0;
    u64 norm_mod = 0;
    cpp_int leading;
    cpp_int norm_coefficient;
};

Position tail_position(int m3, u64 Q, u64 G, u64 kappa, u64 b1, u64 b2) {
    const int b3_two = m3 + valuation(Q, 2) + valuation(G, 2) - valuation(kappa, 2);
    const int prefix_max = std::max(valuation(b1, 2), valuation(b2, 2));
    if (b3_two == 0 && prefix_max == 0) return Position::AllOdd;
    if (b3_two > prefix_max) return Position::B3Unique;
    return Position::PrefixOrTie;
}

std::optional<Signature> state_signature(
    int m1,
    int m2,
    u64 b1,
    u64 b2,
    int m3,
    u64 kappa
) {
    (void)m1;
    const u64 Q = b1 * pow_u64(10, m2) + b2;
    const u64 G = b1 * b2;
    const Position position = tail_position(m3, Q, G, kappa, b1, b2);
    Signature signature;
    signature.position = position;

    if (position == Position::B3Unique) {
        const int k = valuation(kappa, 2);
        const int q = valuation(Q, 2);
        const int g = valuation(G, 2);
        if (k <= g) return std::nullopt;
        const int h = valuation(kappa + G, 2);
        const int f = valuation(kappa + 2 * G, 2);
        const int b3_two = m3 + q + g - k;
        if (N3 - m3 + b3_two <= q) {
            throw std::logic_error("2-adic gap lock failed");
        }
        signature.two = {
            PConditionKind::Disjunction,
            3 * k + f - 2 * m3 - 2 * q - 2 * h,
            N3 - 2 * m3 - 2 * q - h + 2 * k + g + 1,
            f + k - h - g - 1 - N3,
            0,
        };
    } else if (position == Position::AllOdd) {
        signature.two = {PConditionKind::AtLeast, 0, 0, 0, m3 + 1};
    } else {
        return std::nullopt;
    }

    const int k5 = valuation(kappa, 5);
    const int q5 = valuation(Q, 5);
    const int g5 = valuation(G, 5);
    const int b3_five = m3 + q5 + g5 - k5;
    if (b3_five == 0) {
        signature.five = {PConditionKind::Unit, 0, 0, 0, 0};
    } else {
        if (N3 - m3 + b3_five <= q5) {
            throw std::logic_error("5-adic gap lock failed");
        }
        const int h5 = valuation(kappa + G, 5);
        const int f5 = valuation(kappa + 2 * G, 5);
        signature.five = {
            PConditionKind::Disjunction,
            3 * k5 + f5 - 2 * m3 - 2 * q5 - 2 * h5,
            N3 - 2 * m3 - 2 * q5 - h5 + 2 * k5 + g5,
            f5 + k5 - h5 - g5 - N3,
            0,
        };
    }
    return signature;
}

struct PositionCounts {
    u64 b3_unique = 0;
    u64 all_odd = 0;
    u64 prefix_or_tie = 0;

    void add(Position position) {
        if (position == Position::B3Unique) ++b3_unique;
        else if (position == Position::AllOdd) ++all_odd;
        else ++prefix_or_tie;
    }
    PositionCounts& operator+=(const PositionCounts& other) {
        b3_unique += other.b3_unique;
        all_odd += other.all_odd;
        prefix_or_tie += other.prefix_or_tie;
        return *this;
    }
};

struct Counts {
    u64 tail_rows = 0;
    u64 eligible_tail_rows = 0;
    u64 denominator_pairs = 0;
    u64 shape_denominator_pairs = 0;
    u64 digit_pairs = 0;
    u64 coprime_pairs = 0;
    u64 squarefree_pairs = 0;
    u64 valuation_tail_pairs = 0;
    u64 modular_square_pairs = 0;
    u64 nonnegative_discriminants = 0;
    u64 square_discriminants = 0;

    Counts& operator+=(const Counts& other) {
        tail_rows += other.tail_rows;
        eligible_tail_rows += other.eligible_tail_rows;
        denominator_pairs += other.denominator_pairs;
        shape_denominator_pairs += other.shape_denominator_pairs;
        digit_pairs += other.digit_pairs;
        coprime_pairs += other.coprime_pairs;
        squarefree_pairs += other.squarefree_pairs;
        valuation_tail_pairs += other.valuation_tail_pairs;
        modular_square_pairs += other.modular_square_pairs;
        nonnegative_discriminants += other.nonnegative_discriminants;
        square_discriminants += other.square_discriminants;
        return *this;
    }
    bool operator==(const Counts&) const = default;
};

struct TailGroups {
    u64 total = 0;
    PositionCounts positions;
    std::map<Signature, std::vector<Tail>> groups;
};

const std::vector<bool>& square_residues() {
    static const std::vector<bool> table = [] {
        std::vector<bool> values(SQUARE_MODULUS, false);
        for (u64 value = 0; value < SQUARE_MODULUS; ++value) {
            values[mul_mod(value, value, SQUARE_MODULUS)] = true;
        }
        return values;
    }();
    return table;
}

TailGroups build_tail_groups(int m1, int m2, u64 b1, u64 b2, int m3) {
    TailGroups result;
    const u64 Q = b1 * pow_u64(10, m2) + b2;
    const u64 G = b1 * b2;
    const u64 QG = Q * G;
    for (u64 kappa : bounded_divisors(QG, m3, 10 * QG)) {
        if (kappa <= QG) continue;
        if (2 * valuation(kappa, 2) + valuation(kappa + 2 * G, 2) < m3) continue;
        if (2 * valuation(kappa, 5) + valuation(kappa + 2 * G, 5) < m3) continue;
        ++result.total;
        const Position position = tail_position(m3, Q, G, kappa, b1, b2);
        result.positions.add(position);
        auto signature = state_signature(m1, m2, b1, b2, m3, kappa);
        if (!signature) continue;

        Tail tail;
        tail.m1 = m1;
        tail.m2 = m2;
        tail.b1 = b1;
        tail.b2 = b2;
        tail.m3 = m3;
        tail.kappa = kappa;
        tail.Q = Q;
        tail.G = G;
        tail.signature = *signature;
        const int d3 = N3 - m3;
        tail.leading_mod = mul_mod(
            mul_mod(kappa % SQUARE_MODULUS, G % SQUARE_MODULUS, SQUARE_MODULUS),
            pow_mod(10, d3, SQUARE_MODULUS),
            SQUARE_MODULUS
        );
        tail.norm_mod = mul_mod(kappa % SQUARE_MODULUS,
                                (kappa + 2 * G) % SQUARE_MODULUS,
                                SQUARE_MODULUS);
        tail.norm_mod = mul_mod(tail.norm_mod, Q % SQUARE_MODULUS, SQUARE_MODULUS);
        tail.norm_mod = mul_mod(tail.norm_mod, Q % SQUARE_MODULUS, SQUARE_MODULUS);
        tail.leading = cpp_int(kappa) * G * pow_cpp(10, d3);
        tail.norm_coefficient = cpp_int(kappa) * (kappa + 2 * G) * Q * Q;
        result.groups[*signature].push_back(std::move(tail));
    }
    return result;
}

struct Shape {
    int m1;
    int m2;
    int n1;
    int n2;
};

bool size_killed(const Shape& shape, int d3) {
    const int exponent_one = shape.n1 + 2 * shape.m2 - shape.n2;
    const int exponent_two = shape.n2 + 2 * shape.m1;
    const int shift = std::max({0, -exponent_one, -exponent_two});
    const cpp_int ratio_scaled = pow_cpp(10, exponent_one + shift) +
                                 pow_cpp(10, exponent_two + shift);
    const cpp_int left = cpp_int(40) * pow_cpp(10, 2 * S) * ratio_scaled;
    const cpp_int right = pow_cpp(10, d3 + shift);
    return left < right;
}

std::vector<Shape> digit_shapes(int m3, int* coarse_count, int* killed_count) {
    const int d3 = N3 - m3;
    std::vector<Shape> survivors;
    *coarse_count = 0;
    *killed_count = 0;
    for (int m1 = 1; m1 < S; ++m1) {
        const int m2 = S - m1;
        for (int n1 = 1; n1 < S + 2; ++n1) {
            for (int n2 = 1; n2 < S + 3 - n1; ++n2) {
                const int s1 = n1 - m1;
                const int s2 = n2 - m2;
                if (d3 > 3 * S + std::abs(s1 - s2) + 2) continue;
                ++*coarse_count;
                Shape shape{m1, m2, n1, n2};
                if (size_killed(shape, d3)) {
                    ++*killed_count;
                    continue;
                }
                survivors.push_back(shape);
            }
        }
    }
    return survivors;
}

struct PolynomialPair {
    u64 a_linear;
    u64 a_constant;
    u64 n_quadratic;
    u64 n_constant;

    u64 A(u64 x) const {
        const u128 value = static_cast<u128>(a_linear) * x + a_constant;
        if (value > std::numeric_limits<u64>::max()) throw std::overflow_error("A overflow");
        return static_cast<u64>(value);
    }
    u64 N(u64 x) const {
        const u128 value = static_cast<u128>(n_quadratic) * x * x + n_constant;
        if (value > std::numeric_limits<u64>::max()) throw std::overflow_error("N overflow");
        return static_cast<u64>(value);
    }
};

enum class Decision { Accept, Reject, Unknown };

Decision partial_decision(
    const PCondition& condition,
    const std::optional<int>& n_value,
    const std::optional<int>& a_value,
    int known_modulus_exponent
) {
    if (condition.kind == PConditionKind::Unit) return Decision::Accept;
    if (condition.kind == PConditionKind::AtLeast) {
        if (n_value) {
            return *n_value >= condition.threshold ? Decision::Accept : Decision::Reject;
        }
        if (known_modulus_exponent >= condition.threshold) return Decision::Accept;
        return Decision::Unknown;
    }
    if (n_value && *n_value == condition.resonance) return Decision::Accept;
    if (a_value && *a_value == condition.minus_a) return Decision::Accept;
    if (n_value && a_value) {
        return *n_value - *a_value == condition.plus_gap
                   ? Decision::Accept
                   : Decision::Reject;
    }
    return Decision::Unknown;
}

struct ResidueClass {
    u64 residue;
    u64 modulus;
};

bool class_intersects(const ResidueClass& residue_class, u64 lower, u64 upper) {
    if (residue_class.residue > upper) return false;
    u64 first = residue_class.residue;
    if (first < lower) {
        const u64 steps = (lower - first + residue_class.modulus - 1) /
                          residue_class.modulus;
        if (steps > (upper - first) / residue_class.modulus) return false;
        first += steps * residue_class.modulus;
    }
    return first <= upper;
}

std::optional<int> fixed_valuation(u64 value, u64 prime, u64 modulus) {
    if (modulus == 1 || value % modulus == 0) return std::nullopt;
    return valuation(value, prime);
}

std::vector<ResidueClass> accepted_residue_classes(
    u64 prime,
    const PCondition& condition,
    const PolynomialPair& polynomial,
    u64 lower,
    u64 upper
) {
    if (condition.kind == PConditionKind::Unit) return {{0, 1}};
    std::vector<ResidueClass> result;
    std::function<void(int, u64, u64)> visit = [&](int exponent, u64 modulus, u64 residue) {
        const ResidueClass current{residue, modulus};
        if (!class_intersects(current, lower, upper)) return;
        const u64 a_value = polynomial.A(residue);
        const u64 n_value = polynomial.N(residue);
        const auto a_valuation = fixed_valuation(a_value, prime, modulus);
        const auto n_valuation = fixed_valuation(n_value, prime, modulus);
        const Decision decision = partial_decision(
            condition, n_valuation, a_valuation, exponent
        );
        if (decision == Decision::Accept) {
            result.push_back(current);
            return;
        }
        if (decision == Decision::Reject) return;
        if (modulus > std::numeric_limits<u64>::max() / prime) {
            throw std::overflow_error("p-adic residue modulus overflow");
        }
        const u64 new_modulus = modulus * prime;
        for (u64 digit = 0; digit < prime; ++digit) {
            visit(exponent + 1, new_modulus, residue + digit * modulus);
        }
    };
    visit(0, 1, 0);
    return result;
}

u64 first_in_class(const ResidueClass& residue_class, u64 lower, u64 upper) {
    if (!class_intersects(residue_class, lower, upper)) return upper + 1;
    if (residue_class.residue >= lower) return residue_class.residue;
    const u64 steps = (lower - residue_class.residue + residue_class.modulus - 1) /
                      residue_class.modulus;
    return residue_class.residue + steps * residue_class.modulus;
}

struct CandidateMarker {
    std::vector<std::uint32_t> stamps;
    std::uint32_t generation = 0;
    std::vector<u64> candidates;

    explicit CandidateMarker(std::size_t maximum_width) : stamps(maximum_width, 0) {}

    void begin() {
        ++generation;
        if (generation == 0) {
            std::fill(stamps.begin(), stamps.end(), 0);
            generation = 1;
        }
        candidates.clear();
    }

    void mark(u64 value, u64 lower) {
        const std::size_t index = static_cast<std::size_t>(value - lower);
        if (index >= stamps.size()) throw std::out_of_range("candidate marker");
        if (stamps[index] == generation) return;
        stamps[index] = generation;
        candidates.push_back(value);
    }
};

void combine_classes_and_mark(
    const std::vector<ResidueClass>& two_classes,
    const std::vector<ResidueClass>& five_classes,
    u64 lower,
    u64 upper,
    CandidateMarker& marker
) {
    for (const ResidueClass& two : two_classes) {
        for (const ResidueClass& five : five_classes) {
            const ResidueClass* base = &two;
            const ResidueClass* other = &five;
            if (five.modulus > two.modulus) {
                base = &five;
                other = &two;
            }
            u64 value = first_in_class(*base, lower, upper);
            while (value <= upper) {
                if (value % other->modulus == other->residue) marker.mark(value, lower);
                if (base->modulus > upper - value) break;
                value += base->modulus;
            }
        }
    }
}

std::pair<u64, u64> digit_interval(int digits) {
    return {pow_u64(10, digits - 1), pow_u64(10, digits) - 1};
}

struct ShapeContext {
    Shape shape;
    u64 b1;
    u64 b2;
    u64 Q;
    int d3;
    bool long_is_a2;
    u64 fixed_lower;
    u64 fixed_upper;
    u64 long_lower;
    u64 long_upper;
    u64 fixed_denominator;
    u64 long_denominator;
    std::vector<u64> fixed_primes;
    std::vector<u64> long_primes;
};

ShapeContext make_shape_context(const Shape& shape, u64 b1, u64 b2, int d3) {
    const auto [a1_lower, a1_upper] = digit_interval(shape.n1);
    const auto [a2_lower, a2_upper] = digit_interval(shape.n2);
    ShapeContext context;
    context.shape = shape;
    context.b1 = b1;
    context.b2 = b2;
    context.Q = b1 * pow_u64(10, shape.m2) + b2;
    context.d3 = d3;
    context.long_is_a2 = shape.n1 <= shape.n2;
    if (context.long_is_a2) {
        context.fixed_lower = a1_lower;
        context.fixed_upper = a1_upper;
        context.long_lower = a2_lower;
        context.long_upper = a2_upper;
        context.fixed_denominator = b1;
        context.long_denominator = b2;
    } else {
        context.fixed_lower = a2_lower;
        context.fixed_upper = a2_upper;
        context.long_lower = a1_lower;
        context.long_upper = a1_upper;
        context.fixed_denominator = b2;
        context.long_denominator = b1;
    }
    context.fixed_primes = distinct_prime_factors(context.fixed_denominator);
    context.long_primes = distinct_prime_factors(context.long_denominator);
    return context;
}

PolynomialPair polynomial_for_fixed(const ShapeContext& context, u64 fixed) {
    const u64 scale = pow_u64(10, context.shape.n2);
    if (context.long_is_a2) {
        const u64 a1 = fixed;
        return {
            1,
            a1 * scale,
            context.b1 * context.b1,
            (a1 * context.b2) * (a1 * context.b2),
        };
    }
    const u64 a2 = fixed;
    return {
        scale,
        a2,
        context.b2 * context.b2,
        (a2 * context.b1) * (a2 * context.b1),
    };
}

std::vector<Interval> squarefree_ranges(const ShapeContext& context, u64 fixed) {
    const i128 forty_q_squared = static_cast<i128>(40) * context.Q * context.Q;
    const i128 ten_d = static_cast<i128>(pow_u64(10, context.d3));
    const u64 scale = pow_u64(10, context.shape.n2);
    if (context.long_is_a2) {
        const i128 quadratic = forty_q_squared * context.b1 * context.b1;
        const i128 linear = ten_d;
        const i128 first_norm = static_cast<i128>(fixed) * context.b2;
        const i128 constant = forty_q_squared * first_norm * first_norm -
                              ten_d * scale * fixed;
        return positive_quadratic_ranges(
            quadratic, linear, constant, context.long_lower, context.long_upper
        );
    }
    const i128 quadratic = forty_q_squared * context.b2 * context.b2;
    const i128 linear = ten_d * scale;
    const i128 second_norm = static_cast<i128>(fixed) * context.b1;
    const i128 constant = forty_q_squared * second_norm * second_norm - ten_d * fixed;
    return positive_quadratic_ranges(
        quadratic, linear, constant, context.long_lower, context.long_upper
    );
}

bool squarefree_gap(const ShapeContext& context, u64 a1, u64 a2, u64 A, u64 N) {
    (void)a1;
    (void)a2;
    const u128 left = static_cast<u128>(pow_u64(10, context.d3)) * A;
    const u128 right = static_cast<u128>(40) * context.Q * context.Q * N;
    return left < right;
}

bool signature_accepts(const Signature& signature, u64 A, u64 N) {
    const int a2 = valuation(A, 2);
    const int n2 = valuation(N, 2);
    if (!p_condition_accepts(signature.two, n2, a2)) return false;
    const int a5 = valuation(A, 5);
    const int n5 = valuation(N, 5);
    return p_condition_accepts(signature.five, n5, a5);
}

void test_discriminant(const Tail& tail, u64 A, u64 N, Counts& counts) {
    const u64 leading_square = mul_mod(tail.leading_mod, tail.leading_mod, SQUARE_MODULUS);
    const u64 a_square = mul_mod(A % SQUARE_MODULUS, A % SQUARE_MODULUS, SQUARE_MODULUS);
    const u64 positive = mul_mod(leading_square, a_square, SQUARE_MODULUS);
    const u64 negative = mul_mod(tail.norm_mod, N % SQUARE_MODULUS, SQUARE_MODULUS);
    const u64 residue = (positive + SQUARE_MODULUS - negative) % SQUARE_MODULUS;
    if (!square_residues()[residue]) return;
    ++counts.modular_square_pairs;
    const cpp_int leading_a = tail.leading * A;
    const cpp_int discriminant = leading_a * leading_a - tail.norm_coefficient * N;
    if (discriminant < 0) return;
    ++counts.nonnegative_discriminants;
    const cpp_int root = integer_sqrt(discriminant);
    if (root * root == discriminant) ++counts.square_discriminants;
}

void process_shape(
    const Shape& shape,
    u64 b1,
    u64 b2,
    int m3,
    const std::map<Signature, std::vector<Tail>>& groups,
    CandidateMarker& marker,
    Counts& counts
) {
    const int d3 = N3 - m3;
    const ShapeContext context = make_shape_context(shape, b1, b2, d3);
    const u64 fixed_width = context.fixed_upper - context.fixed_lower + 1;
    const u64 long_width = context.long_upper - context.long_lower + 1;
    counts.digit_pairs += fixed_width * long_width;
    const u64 fixed_coprime = coprime_count(
        context.fixed_lower, context.fixed_upper, context.fixed_primes
    );
    const u64 long_coprime = coprime_count(
        context.long_lower, context.long_upper, context.long_primes
    );
    counts.coprime_pairs += fixed_coprime * long_coprime;

    for (u64 fixed = context.fixed_lower; fixed <= context.fixed_upper; ++fixed) {
        if (std::gcd(fixed, context.fixed_denominator) != 1) continue;
        const auto ranges = squarefree_ranges(context, fixed);
        for (const Interval& range : ranges) {
            counts.squarefree_pairs += coprime_count(
                range.lower, range.upper, context.long_primes
            );
        }
        if (ranges.empty()) continue;

        const PolynomialPair polynomial = polynomial_for_fixed(context, fixed);
        marker.begin();
        for (const auto& [signature, tails] : groups) {
            (void)tails;
            const auto two_classes = accepted_residue_classes(
                2, signature.two, polynomial, context.long_lower, context.long_upper
            );
            if (two_classes.empty()) continue;
            const auto five_classes = accepted_residue_classes(
                5, signature.five, polynomial, context.long_lower, context.long_upper
            );
            if (five_classes.empty()) continue;
            combine_classes_and_mark(
                two_classes,
                five_classes,
                context.long_lower,
                context.long_upper,
                marker
            );
        }

        for (u64 long_value : marker.candidates) {
            if (std::gcd(long_value, context.long_denominator) != 1) continue;
            u64 a1;
            u64 a2;
            if (context.long_is_a2) {
                a1 = fixed;
                a2 = long_value;
            } else {
                a1 = long_value;
                a2 = fixed;
            }
            const u64 A = a1 * pow_u64(10, shape.n2) + a2;
            const u64 first_norm = a1 * b2;
            const u64 second_norm = a2 * b1;
            const u64 N = static_cast<u64>(
                static_cast<u128>(first_norm) * first_norm +
                static_cast<u128>(second_norm) * second_norm
            );
            if (!squarefree_gap(context, a1, a2, A, N)) continue;
            for (const auto& [signature, tails] : groups) {
                if (!signature_accepts(signature, A, N)) continue;
                counts.valuation_tail_pairs += tails.size();
                for (const Tail& tail : tails) test_discriminant(tail, A, N, counts);
            }
        }
    }
}

struct DenominatorJob {
    int m1;
    int m2;
    u64 b1;
    u64 b2;
};

std::vector<DenominatorJob> denominator_jobs() {
    std::vector<DenominatorJob> jobs;
    for (int m1 = 1; m1 < S; ++m1) {
        const int m2 = S - m1;
        const auto [b1_lower, b1_upper] = digit_interval(m1);
        const auto [b2_lower, b2_upper] = digit_interval(m2);
        for (u64 b1 = b1_lower; b1 <= b1_upper; ++b1) {
            for (u64 b2 = b2_lower; b2 <= b2_upper; ++b2) {
                jobs.push_back({m1, m2, b1, b2});
            }
        }
    }
    return jobs;
}

struct SliceResult {
    int m3 = 0;
    int coarse_shapes = 0;
    int killed_shapes = 0;
    int surviving_shapes = 0;
    Counts counts;
    PositionCounts positions;
    double seconds = 0;
};

SliceResult check_slice(
    int m3,
    int thread_count,
    std::size_t job_start,
    std::size_t job_count,
    bool progress
) {
    SliceResult result;
    result.m3 = m3;
    const auto shapes = digit_shapes(m3, &result.coarse_shapes, &result.killed_shapes);
    result.surviving_shapes = static_cast<int>(shapes.size());
    std::map<std::pair<int, int>, std::vector<Shape>> shapes_by_split;
    for (const Shape& shape : shapes) {
        shapes_by_split[{shape.m1, shape.m2}].push_back(shape);
    }
    auto jobs = denominator_jobs();
    job_start = std::min(job_start, jobs.size());
    const std::size_t remaining_jobs = jobs.size() - job_start;
    const std::size_t end = job_count >= remaining_jobs
                                ? jobs.size()
                                : job_start + job_count;
    std::atomic<std::size_t> completed{0};
    const auto started = std::chrono::steady_clock::now();

#ifdef _OPENMP
    if (thread_count > 0) omp_set_num_threads(thread_count);
#else
    (void)thread_count;
#endif

#pragma omp parallel
    {
        Counts local_counts;
        PositionCounts local_positions;
        CandidateMarker marker(90000);
#pragma omp for schedule(dynamic, 1)
        for (std::int64_t raw_index = static_cast<std::int64_t>(job_start);
             raw_index < static_cast<std::int64_t>(end);
             ++raw_index) {
            const DenominatorJob& job = jobs[static_cast<std::size_t>(raw_index)];
            TailGroups tails = build_tail_groups(
                job.m1, job.m2, job.b1, job.b2, m3
            );
            local_counts.tail_rows += tails.total;
            local_positions += tails.positions;
            u64 eligible = 0;
            for (const auto& [signature, values] : tails.groups) {
                (void)signature;
                eligible += values.size();
            }
            local_counts.eligible_tail_rows += eligible;
            if (!tails.groups.empty()) {
                ++local_counts.denominator_pairs;
                const auto found = shapes_by_split.find({job.m1, job.m2});
                if (found != shapes_by_split.end()) {
                    for (const Shape& shape : found->second) {
                        ++local_counts.shape_denominator_pairs;
                        process_shape(
                            shape,
                            job.b1,
                            job.b2,
                            m3,
                            tails.groups,
                            marker,
                            local_counts
                        );
                    }
                }
            }
            const std::size_t done = ++completed;
            if (progress && done % 1000 == 0) {
#pragma omp critical(progress_output)
                std::cerr << "  m_3=" << m3 << ": checked " << done << "/"
                          << (end - job_start) << " denominator jobs\n";
            }
        }
#pragma omp critical(result_merge)
        {
            result.counts += local_counts;
            result.positions += local_positions;
        }
    }
    const auto finished = std::chrono::steady_clock::now();
    result.seconds = std::chrono::duration<double>(finished - started).count();
    return result;
}

void print_result(const SliceResult& result) {
    std::cout << "m_3=" << result.m3
              << ": coarse-shapes=" << result.coarse_shapes
              << ", size-killed=" << result.killed_shapes
              << ", surviving-shapes=" << result.surviving_shapes << '\n';
    std::cout << "  tail positions = {'b3-unique': " << result.positions.b3_unique
              << ", 'all-odd': " << result.positions.all_odd
              << ", 'prefix-or-tie': " << result.positions.prefix_or_tie << "}\n";
    const Counts& c = result.counts;
    std::cout << "  Counts(tail_rows=" << c.tail_rows
              << ", eligible_tail_rows=" << c.eligible_tail_rows
              << ", denominator_pairs=" << c.denominator_pairs
              << ", shape_denominator_pairs=" << c.shape_denominator_pairs
              << ", digit_pairs=" << c.digit_pairs
              << ", coprime_pairs=" << c.coprime_pairs
              << ", squarefree_pairs=" << c.squarefree_pairs
              << ", valuation_tail_pairs=" << c.valuation_tail_pairs
              << ", modular_square_pairs=" << c.modular_square_pairs
              << ", nonnegative_discriminants=" << c.nonnegative_discriminants
              << ", square_discriminants=" << c.square_discriminants << ")\n";
    std::cout << "  elapsed_seconds=" << std::fixed << std::setprecision(3)
              << result.seconds << '\n';
}

struct ExpectedSlice {
    Counts counts;
    PositionCounts positions;
    int coarse_shapes;
    int killed_shapes;
    int surviving_shapes;
};

std::optional<ExpectedSlice> recorded_expected(int m3) {
    if (m3 == 15) {
        return ExpectedSlice{
            Counts{171086, 159257, 19964, 152597, 57299353506,
                   21911817780, 10139813772, 14150484, 1614629, 1614629, 0},
            PositionCounts{171075, 9, 2},
            28, 5, 23,
        };
    }
    if (m3 == 16) {
        return ExpectedSlice{
            Counts{94053, 90486, 17354, 202178, 61689364533,
                   22512218443, 13048746205, 9828, 1122, 1122, 0},
            PositionCounts{94053, 0, 0},
            38, 3, 35,
        };
    }
    if (m3 == 17) {
        return ExpectedSlice{
            Counts{27472, 25791, 8998, 134970, 39591208998,
                   13577745617, 9937601615, 8792, 784, 784, 0},
            PositionCounts{27472, 0, 0},
            45, 0, 45,
        };
    }
    if (m3 == 18) {
        return ExpectedSlice{
            Counts{9078, 7935, 4348, 65220, 19131204348,
                   5443009377, 5107596510, 112243, 30504, 30504, 0},
            PositionCounts{9078, 0, 0},
            45, 0, 45,
        };
    }
    if (m3 == 19) {
        return ExpectedSlice{
            Counts{1336, 1283, 821, 12315, 3612400821,
                   884434500, 882724160, 70, 0, 0, 0},
            PositionCounts{1336, 0, 0},
            45, 0, 45,
        };
    }
    if (m3 == 20) {
        return ExpectedSlice{
            Counts{188, 179, 150, 2250, 660000150, 158999184, 158999184,
                   1887, 34, 34, 0},
            PositionCounts{188, 0, 0},
            45, 0, 45,
        };
    }
    if (m3 == 21) {
        return ExpectedSlice{
            Counts{9, 9, 9, 135, 39600009, 10813386, 10813386, 0, 0, 0, 0},
            PositionCounts{9, 0, 0},
            45, 0, 45,
        };
    }
    return std::nullopt;
}

bool same_positions(const PositionCounts& left, const PositionCounts& right) {
    return left.b3_unique == right.b3_unique &&
           left.all_odd == right.all_odd &&
           left.prefix_or_tie == right.prefix_or_tie;
}

void check_quadratic_solver() {
    std::mt19937_64 random(2725);
    for (int trial = 0; trial < 2000; ++trial) {
        const i128 quadratic = 1 + random() % 1000;
        const i128 linear = random() % 10000;
        const i128 constant = static_cast<i128>(random() % 200001) - 100000;
        const u64 lower = random() % 101;
        const u64 upper = lower + random() % 300;
        std::set<u64> actual;
        for (const Interval& interval : positive_quadratic_ranges(
                 quadratic, linear, constant, lower, upper)) {
            for (u64 value = interval.lower; value <= interval.upper; ++value) {
                actual.insert(value);
            }
        }
        std::set<u64> expected;
        for (u64 value = lower; value <= upper; ++value) {
            if (quadratic_value(quadratic, linear, constant, value) > 0) {
                expected.insert(value);
            }
        }
        if (actual != expected) throw std::logic_error("quadratic solver mismatch");
    }
}

void check_residue_solver() {
    std::mt19937_64 random(2729001);
    for (u64 prime : {2ULL, 5ULL}) {
        for (int trial = 0; trial < 3000; ++trial) {
            const u64 lower = 1 + random() % 40;
            const u64 upper = lower + random() % 160;
            const PolynomialPair polynomial{
                1 + random() % 50,
                1 + random() % 100,
                1 + random() % 70,
                1 + random() % 200,
            };
            PCondition condition;
            const int kind = static_cast<int>(random() % 3);
            if (kind == 0) {
                condition = {
                    PConditionKind::Disjunction,
                    static_cast<int>(random() % 12) - 3,
                    static_cast<int>(random() % 14) - 4,
                    static_cast<int>(random() % 12) - 3,
                    0,
                };
            } else if (kind == 1) {
                condition = {
                    PConditionKind::AtLeast, 0, 0, 0,
                    static_cast<int>(random() % 12),
                };
            } else {
                condition = {PConditionKind::Unit, 0, 0, 0, 0};
            }
            const auto classes = accepted_residue_classes(
                prime, condition, polynomial, lower, upper
            );
            for (u64 value = lower; value <= upper; ++value) {
                bool found = false;
                for (const ResidueClass& residue_class : classes) {
                    if (value % residue_class.modulus == residue_class.residue) {
                        found = true;
                        break;
                    }
                }
                const bool expected = p_condition_accepts(
                    condition,
                    valuation(polynomial.N(value), prime),
                    valuation(polynomial.A(value), prime)
                );
                if (found != expected) {
                    throw std::logic_error("p-adic residue solver mismatch");
                }
            }
        }
    }
}

void check_sqrt() {
    std::mt19937_64 random(2729002);
    for (int trial = 0; trial < 2000; ++trial) {
        cpp_int root = cpp_int(random()) * random() + random();
        cpp_int square = root * root;
        if (integer_sqrt(square) != root) throw std::logic_error("sqrt square mismatch");
        if (integer_sqrt(square + root) != root) throw std::logic_error("sqrt interval mismatch");
    }
}

void self_check() {
    check_quadratic_solver();
    std::cout << "exact positive-quadratic interval solver: OK\n";
    check_residue_solver();
    std::cout << "p-adic residue-tree solver vs direct enumeration: OK\n";
    check_sqrt();
    std::cout << "cpp_int integer square root: OK\n";
}

struct Options {
    int m3_min = 15;
    int m3_max = 21;
    int threads = 0;
    std::size_t job_start = 0;
    std::size_t job_count = std::numeric_limits<std::size_t>::max();
    bool progress = false;
    bool run_self_check = false;
    bool expect_baseline = false;
};

int parse_int(const char* text, const std::string& option) {
    char* end = nullptr;
    const long value = std::strtol(text, &end, 10);
    if (!end || *end != '\0') throw std::invalid_argument("invalid " + option);
    return static_cast<int>(value);
}

std::size_t parse_size(const char* text, const std::string& option) {
    char* end = nullptr;
    const unsigned long long value = std::strtoull(text, &end, 10);
    if (!end || *end != '\0') throw std::invalid_argument("invalid " + option);
    return static_cast<std::size_t>(value);
}

Options parse_options(int argc, char** argv) {
    Options options;
    for (int index = 1; index < argc; ++index) {
        const std::string option = argv[index];
        auto require_value = [&]() -> const char* {
            if (++index >= argc) throw std::invalid_argument("missing value for " + option);
            return argv[index];
        };
        if (option == "--m3") {
            options.m3_min = options.m3_max = parse_int(require_value(), option);
        } else if (option == "--m3-min") {
            options.m3_min = parse_int(require_value(), option);
        } else if (option == "--m3-max") {
            options.m3_max = parse_int(require_value(), option);
        } else if (option == "--threads") {
            options.threads = parse_int(require_value(), option);
        } else if (option == "--job-start") {
            options.job_start = parse_size(require_value(), option);
        } else if (option == "--job-count") {
            options.job_count = parse_size(require_value(), option);
        } else if (option == "--progress") {
            options.progress = true;
        } else if (option == "--self-check") {
            options.run_self_check = true;
        } else if (option == "--expect-baseline") {
            options.expect_baseline = true;
        } else if (option == "--help" || option == "-h") {
            std::cout
                << "usage: check_dd_2729_cpp [--m3 N | --m3-min N --m3-max N]\n"
                << "       [--threads N] [--job-start N --job-count N] [--progress]\n"
                << "       [--self-check] [--expect-baseline]\n";
            std::exit(0);
        } else {
            throw std::invalid_argument("unknown option: " + option);
        }
    }
    if (options.m3_min < 15 || options.m3_max > 21 || options.m3_min > options.m3_max) {
        throw std::invalid_argument("this accelerator covers 15 <= m_3 <= 21");
    }
    if (options.threads < 0) throw std::invalid_argument("negative thread count");
    return options;
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_options(argc, argv);
        if (options.run_self_check) self_check();
        for (int m3 = options.m3_min; m3 <= options.m3_max; ++m3) {
            SliceResult result = check_slice(
                m3,
                options.threads,
                options.job_start,
                options.job_count,
                options.progress
            );
            print_result(result);
            if (result.counts.square_discriminants != 0) {
                throw std::logic_error("square discriminant found");
            }
            if (options.expect_baseline) {
                const auto expected = recorded_expected(m3);
                if (!expected) {
                    throw std::invalid_argument(
                        "--expect-baseline has no recorded baseline for this m_3"
                    );
                }
                if (options.job_start != 0 ||
                    options.job_count != std::numeric_limits<std::size_t>::max()) {
                    throw std::invalid_argument(
                        "--expect-baseline requires the complete denominator range"
                    );
                }
                if (!(result.counts == expected->counts) ||
                    !same_positions(result.positions, expected->positions) ||
                    result.coarse_shapes != expected->coarse_shapes ||
                    result.killed_shapes != expected->killed_shapes ||
                    result.surviving_shapes != expected->surviving_shapes) {
                    throw std::logic_error("recorded exact-counter mismatch");
                }
                std::cout << "  recorded exact counters: OK\n";
            }
        }
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 1;
    }
}
