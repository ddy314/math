// Exact finite certificate for the high denominator-tail layers at
//
//     S_12 = 5,  n_3 = 39,  22 <= m_3 <= 32.
//
// The complete numerator/discriminant certificate covers m_3=22,...,26.
// The exact primitive denominator-tail kernel is empty for m_3=27,...,32.
// This is only a bounded slice of the DD branch.
//
// Build and run the fixed regression certificate:
//
//   g++ -O3 -DNDEBUG -std=c++20 -fopenmp scripts/check_dd_2730.cpp -o /tmp/check_dd_2730_cpp
//   /tmp/check_dd_2730_cpp --self-check --expect-baseline --threads 12
//
// Short audit runs:
//
//   /tmp/check_dd_2730_cpp --m3 26 --expect-baseline --threads 12
//   /tmp/check_dd_2730_cpp --empty-high-only --expect-baseline --threads 12
//
// check_dd_2729.cpp is included as an implementation component so this file
// reuses its already audited divisor tree, exact quadratic interval solver,
// modular-square table, cpp_int square root, signature structures, and exact
// counters.  S=5 needs a wider N_12: it is represented by unsigned __int128
// through the p-adic and squarefree-gap stages, then converted exactly to
// cpp_int before the unified discriminant.  Every residue-tree candidate is
// rechecked against the original valuation disjunction, gcd conditions,
// strict squarefree gap, modular-square sieve, and exact discriminant.

#define main check_dd_2729_embedded_main
#include "check_dd_2729.cpp"
#undef main

namespace {

constexpr int S5 = 5;
constexpr int N3_5 = 39;
constexpr int FINITE_MIN_M3 = 22;
constexpr int FINITE_MAX_M3 = 26;
constexpr int EMPTY_MIN_M3 = 27;
constexpr int EMPTY_MAX_M3 = 32;

u128 pow_u128(u128 base, int exponent) {
    u128 result = 1;
    for (int index = 0; index < exponent; ++index) result *= base;
    return result;
}

int valuation128(u128 value, u64 prime) {
    if (value == 0) throw std::invalid_argument("valuation128(0)");
    int exponent = 0;
    while (value % prime == 0) {
        value /= prime;
        ++exponent;
    }
    return exponent;
}

cpp_int cpp_from_u128(u128 value) {
    constexpr u128 mask = (u128(1) << 64) - 1;
    cpp_int result = static_cast<u64>(value >> 64);
    result <<= 64;
    result += static_cast<u64>(value & mask);
    return result;
}

std::optional<Signature> state_signature_s5(
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
        if (N3_5 - m3 + b3_two <= q) {
            throw std::logic_error("S=5 two-adic gap lock failed");
        }
        signature.two = {
            PConditionKind::Disjunction,
            3 * k + f - 2 * m3 - 2 * q - 2 * h,
            N3_5 - 2 * m3 - 2 * q - h + 2 * k + g + 1,
            f + k - h - g - 1 - N3_5,
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
        if (N3_5 - m3 + b3_five <= q5) {
            throw std::logic_error("S=5 five-adic gap lock failed");
        }
        const int h5 = valuation(kappa + G, 5);
        const int f5 = valuation(kappa + 2 * G, 5);
        signature.five = {
            PConditionKind::Disjunction,
            3 * k5 + f5 - 2 * m3 - 2 * q5 - 2 * h5,
            N3_5 - 2 * m3 - 2 * q5 - h5 + 2 * k5 + g5,
            f5 + k5 - h5 - g5 - N3_5,
            0,
        };
    }
    return signature;
}

TailGroups build_tail_groups_s5(
    int m1,
    int m2,
    u64 b1,
    u64 b2,
    int m3
) {
    TailGroups result;
    const u64 Q = b1 * pow_u64(10, m2) + b2;
    const u64 G = b1 * b2;
    const u64 QG = Q * G;
    for (u64 kappa : bounded_divisors(QG, m3, 10 * QG)) {
        if (kappa <= QG) continue;
        if (2 * valuation(kappa, 2) + valuation(kappa + 2 * G, 2) < m3) continue;
        if (2 * valuation(kappa, 5) + valuation(kappa + 2 * G, 5) < m3) continue;
        ++result.total;
        result.positions.add(tail_position(m3, Q, G, kappa, b1, b2));
        const auto signature = state_signature_s5(m1, m2, b1, b2, m3, kappa);
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
        const int d3 = N3_5 - m3;
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

struct Polynomial128 {
    u64 a_linear;
    u64 a_constant;
    u64 n_quadratic;
    u128 n_constant;

    u64 A(u64 value) const {
        const u128 result = static_cast<u128>(a_linear) * value + a_constant;
        if (result > std::numeric_limits<u64>::max()) {
            throw std::overflow_error("S=5 A_12 overflow");
        }
        return static_cast<u64>(result);
    }

    u128 N(u64 value) const {
        return static_cast<u128>(n_quadratic) * value * value + n_constant;
    }
};

struct Residue128 {
    u64 residue;
    u128 modulus;
};

bool intersects128(const Residue128& row, u64 lower, u64 upper) {
    if (row.residue > upper) return false;
    if (row.residue >= lower) return true;
    const u128 distance = lower - row.residue;
    const u128 steps = (distance + row.modulus - 1) / row.modulus;
    return static_cast<u128>(row.residue) + steps * row.modulus <= upper;
}

std::vector<Residue128> accepted_classes128(
    u64 prime,
    const PCondition& condition,
    const Polynomial128& polynomial,
    u64 lower,
    u64 upper
) {
    if (condition.kind == PConditionKind::Unit) return {{0, 1}};
    std::vector<Residue128> result;
    const auto visit = [&] (
        auto&& self,
        int exponent,
        u128 modulus,
        u64 residue
    ) -> void {
        const Residue128 current{residue, modulus};
        if (!intersects128(current, lower, upper)) return;
        const u64 A = polynomial.A(residue);
        const u128 N = polynomial.N(residue);
        std::optional<int> a_valuation;
        std::optional<int> n_valuation;
        if (modulus != 1 && static_cast<u128>(A) % modulus != 0) {
            a_valuation = valuation(A, prime);
        }
        if (modulus != 1 && N % modulus != 0) {
            n_valuation = valuation128(N, prime);
        }
        const Decision decision = partial_decision(
            condition, n_valuation, a_valuation, exponent
        );
        if (decision == Decision::Accept) {
            result.push_back(current);
            return;
        }
        if (decision == Decision::Reject) return;
        constexpr u128 maximum = ~u128(0);
        if (modulus > maximum / prime) {
            throw std::overflow_error("S=5 p-adic modulus overflow");
        }
        const u128 next_modulus = modulus * prime;
        for (u64 digit = 0; digit < prime; ++digit) {
            const u128 next_residue = static_cast<u128>(residue) + digit * modulus;
            if (next_residue <= upper) {
                self(self,
                     exponent + 1,
                     next_modulus,
                     static_cast<u64>(next_residue));
            }
        }
    };
    visit(visit, 0, 1, 0);
    return result;
}

u64 first128(const Residue128& row, u64 lower, u64 upper) {
    if (!intersects128(row, lower, upper)) return upper + 1;
    if (row.residue >= lower) return row.residue;
    const u128 steps = (static_cast<u128>(lower - row.residue) + row.modulus - 1) /
                       row.modulus;
    return static_cast<u64>(static_cast<u128>(row.residue) + steps * row.modulus);
}

void combine128(
    const std::vector<Residue128>& two_classes,
    const std::vector<Residue128>& five_classes,
    u64 lower,
    u64 upper,
    CandidateMarker& marker
) {
    for (const Residue128& two : two_classes) {
        for (const Residue128& five : five_classes) {
            const Residue128* base = &two;
            const Residue128* other = &five;
            if (five.modulus > two.modulus) {
                base = &five;
                other = &two;
            }
            u64 value = first128(*base, lower, upper);
            while (value <= upper) {
                if (static_cast<u128>(value) % other->modulus == other->residue) {
                    marker.mark(value, lower);
                }
                if (base->modulus > upper - value) break;
                value += static_cast<u64>(base->modulus);
            }
        }
    }
}

struct Shape5 {
    int m1;
    int m2;
    int n1;
    int n2;
};

bool size_killed_s5(const Shape5& shape, int d3) {
    const int exponent_one = shape.n1 + 2 * shape.m2 - shape.n2;
    const int exponent_two = shape.n2 + 2 * shape.m1;
    const int shift = std::max({0, -exponent_one, -exponent_two});
    const cpp_int ratio = pow_cpp(10, exponent_one + shift) +
                          pow_cpp(10, exponent_two + shift);
    return cpp_int(40) * pow_cpp(10, 2 * S5) * ratio < pow_cpp(10, d3 + shift);
}

std::vector<Shape5> digit_shapes_s5(
    int m3,
    int* coarse_count,
    int* killed_count
) {
    const int d3 = N3_5 - m3;
    std::vector<Shape5> result;
    *coarse_count = 0;
    *killed_count = 0;
    for (int m1 = 1; m1 < S5; ++m1) {
        const int m2 = S5 - m1;
        for (int n1 = 1; n1 <= S5 + 1; ++n1) {
            for (int n2 = 1; n2 <= S5 + 2 - n1; ++n2) {
                const int s1 = n1 - m1;
                const int s2 = n2 - m2;
                if (d3 > 3 * S5 + std::abs(s1 - s2) + 2) continue;
                ++*coarse_count;
                const Shape5 shape{m1, m2, n1, n2};
                if (size_killed_s5(shape, d3)) {
                    ++*killed_count;
                    continue;
                }
                result.push_back(shape);
            }
        }
    }
    return result;
}

struct Context5 {
    Shape5 shape;
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

Context5 make_context5(const Shape5& shape, u64 b1, u64 b2, int d3) {
    const auto [a1_lower, a1_upper] = digit_interval(shape.n1);
    const auto [a2_lower, a2_upper] = digit_interval(shape.n2);
    Context5 context;
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

Polynomial128 polynomial5(const Context5& context, u64 fixed) {
    const u64 scale = pow_u64(10, context.shape.n2);
    if (context.long_is_a2) {
        const u128 norm = static_cast<u128>(fixed) * context.b2;
        return {1, fixed * scale, context.b1 * context.b1, norm * norm};
    }
    const u128 norm = static_cast<u128>(fixed) * context.b1;
    return {scale, fixed, context.b2 * context.b2, norm * norm};
}

std::vector<Interval> gap_ranges5(const Context5& context, u64 fixed) {
    const i128 forty_q_squared = static_cast<i128>(40) * context.Q * context.Q;
    const i128 ten_d = static_cast<i128>(pow_u128(10, context.d3));
    const u64 scale = pow_u64(10, context.shape.n2);
    if (context.long_is_a2) {
        const i128 norm = static_cast<i128>(fixed) * context.b2;
        return positive_quadratic_ranges(
            forty_q_squared * context.b1 * context.b1,
            ten_d,
            forty_q_squared * norm * norm - ten_d * scale * fixed,
            context.long_lower,
            context.long_upper
        );
    }
    const i128 norm = static_cast<i128>(fixed) * context.b1;
    return positive_quadratic_ranges(
        forty_q_squared * context.b2 * context.b2,
        ten_d * scale,
        forty_q_squared * norm * norm - ten_d * fixed,
        context.long_lower,
        context.long_upper
    );
}

bool signature_accepts_s5(const Signature& signature, u64 A, u128 N) {
    const int a2 = valuation(A, 2);
    const int n2 = valuation128(N, 2);
    if (!p_condition_accepts(signature.two, n2, a2)) return false;
    return p_condition_accepts(
        signature.five,
        valuation128(N, 5),
        valuation(A, 5)
    );
}

void test_discriminant_s5(const Tail& tail, u64 A, u128 N, Counts& counts) {
    const u64 leading_square = mul_mod(
        tail.leading_mod, tail.leading_mod, SQUARE_MODULUS
    );
    const u64 a_square = mul_mod(A % SQUARE_MODULUS,
                                 A % SQUARE_MODULUS,
                                 SQUARE_MODULUS);
    const u64 positive = mul_mod(leading_square, a_square, SQUARE_MODULUS);
    const u64 n_mod = static_cast<u64>(N % SQUARE_MODULUS);
    const u64 negative = mul_mod(tail.norm_mod, n_mod, SQUARE_MODULUS);
    const u64 residue = (positive + SQUARE_MODULUS - negative) % SQUARE_MODULUS;
    if (!square_residues()[residue]) return;
    ++counts.modular_square_pairs;
    const cpp_int leading_a = tail.leading * A;
    const cpp_int discriminant =
        leading_a * leading_a - tail.norm_coefficient * cpp_from_u128(N);
    if (discriminant < 0) return;
    ++counts.nonnegative_discriminants;
    const cpp_int root = integer_sqrt(discriminant);
    if (root * root == discriminant) ++counts.square_discriminants;
}

void process_shape_s5(
    const Shape5& shape,
    u64 b1,
    u64 b2,
    int m3,
    const std::map<Signature, std::vector<Tail>>& groups,
    CandidateMarker& marker,
    Counts& counts
) {
    const Context5 context = make_context5(shape, b1, b2, N3_5 - m3);
    const u64 fixed_width = context.fixed_upper - context.fixed_lower + 1;
    const u64 long_width = context.long_upper - context.long_lower + 1;
    counts.digit_pairs += fixed_width * long_width;
    counts.coprime_pairs +=
        coprime_count(context.fixed_lower,
                      context.fixed_upper,
                      context.fixed_primes) *
        coprime_count(context.long_lower,
                      context.long_upper,
                      context.long_primes);

    for (u64 fixed = context.fixed_lower; fixed <= context.fixed_upper; ++fixed) {
        if (std::gcd(fixed, context.fixed_denominator) != 1) continue;
        const auto ranges = gap_ranges5(context, fixed);
        for (const Interval& range : ranges) {
            counts.squarefree_pairs += coprime_count(
                range.lower, range.upper, context.long_primes
            );
        }
        if (ranges.empty()) continue;

        const Polynomial128 polynomial = polynomial5(context, fixed);
        marker.begin();
        for (const auto& [signature, tails] : groups) {
            (void)tails;
            const auto two_classes = accepted_classes128(
                2,
                signature.two,
                polynomial,
                context.long_lower,
                context.long_upper
            );
            if (two_classes.empty()) continue;
            const auto five_classes = accepted_classes128(
                5,
                signature.five,
                polynomial,
                context.long_lower,
                context.long_upper
            );
            if (five_classes.empty()) continue;
            combine128(two_classes,
                       five_classes,
                       context.long_lower,
                       context.long_upper,
                       marker);
        }

        for (u64 long_value : marker.candidates) {
            if (std::gcd(long_value, context.long_denominator) != 1) continue;
            const u64 a1 = context.long_is_a2 ? fixed : long_value;
            const u64 a2 = context.long_is_a2 ? long_value : fixed;
            const u64 A = a1 * pow_u64(10, shape.n2) + a2;
            const u128 first_norm = static_cast<u128>(a1) * b2;
            const u128 second_norm = static_cast<u128>(a2) * b1;
            const u128 N = first_norm * first_norm + second_norm * second_norm;
            const u128 gap_left = pow_u128(10, N3_5 - m3) * A;
            const u128 gap_right =
                static_cast<u128>(40) * context.Q * context.Q * N;
            if (gap_left >= gap_right) continue;
            for (const auto& [signature, tails] : groups) {
                if (!signature_accepts_s5(signature, A, N)) continue;
                counts.valuation_tail_pairs += tails.size();
                for (const Tail& tail : tails) {
                    test_discriminant_s5(tail, A, N, counts);
                }
            }
        }
    }
}

std::vector<DenominatorJob> denominator_jobs_s5() {
    std::vector<DenominatorJob> result;
    for (int m1 = 1; m1 < S5; ++m1) {
        const int m2 = S5 - m1;
        const auto [b1_lower, b1_upper] = digit_interval(m1);
        const auto [b2_lower, b2_upper] = digit_interval(m2);
        for (u64 b1 = b1_lower; b1 <= b1_upper; ++b1) {
            for (u64 b2 = b2_lower; b2 <= b2_upper; ++b2) {
                result.push_back({m1, m2, b1, b2});
            }
        }
    }
    return result;
}

SliceResult check_slice_s5(int m3, int thread_count, bool progress) {
    SliceResult result;
    result.m3 = m3;
    const auto shapes = digit_shapes_s5(
        m3, &result.coarse_shapes, &result.killed_shapes
    );
    result.surviving_shapes = static_cast<int>(shapes.size());
    std::map<std::pair<int, int>, std::vector<Shape5>> shapes_by_split;
    for (const Shape5& shape : shapes) {
        shapes_by_split[{shape.m1, shape.m2}].push_back(shape);
    }
    const auto jobs = denominator_jobs_s5();
    std::atomic<std::size_t> completed{0};
    const auto started = std::chrono::steady_clock::now();
    if (thread_count > 0) omp_set_num_threads(thread_count);

#pragma omp parallel
    {
        Counts local_counts;
        PositionCounts local_positions;
        CandidateMarker marker(900000);
#pragma omp for schedule(dynamic, 1)
        for (std::int64_t raw_index = 0;
             raw_index < static_cast<std::int64_t>(jobs.size());
             ++raw_index) {
            const DenominatorJob& job = jobs[static_cast<std::size_t>(raw_index)];
            TailGroups tails = build_tail_groups_s5(
                job.m1, job.m2, job.b1, job.b2, m3
            );
            local_counts.tail_rows += tails.total;
            local_positions += tails.positions;
            u64 eligible = 0;
            for (const auto& [signature, rows] : tails.groups) {
                (void)signature;
                eligible += rows.size();
            }
            local_counts.eligible_tail_rows += eligible;
            if (!tails.groups.empty()) {
                ++local_counts.denominator_pairs;
                const auto found = shapes_by_split.find({job.m1, job.m2});
                if (found != shapes_by_split.end()) {
                    for (const Shape5& shape : found->second) {
                        ++local_counts.shape_denominator_pairs;
                        process_shape_s5(shape,
                                         job.b1,
                                         job.b2,
                                         m3,
                                         tails.groups,
                                         marker,
                                         local_counts);
                    }
                }
            }
            const std::size_t done = ++completed;
            if (progress && done % 10000 == 0) {
#pragma omp critical(s5_progress_output)
                std::cerr << "  m_3=" << m3 << ": checked " << done << "/"
                          << jobs.size() << " denominator jobs\n";
            }
        }
#pragma omp critical(s5_result_merge)
        {
            result.counts += local_counts;
            result.positions += local_positions;
        }
    }
    result.seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started
    ).count();
    return result;
}

std::optional<ExpectedSlice> expected_s5(int m3) {
    if (m3 == 22) {
        return ExpectedSlice{
            Counts{136692, 132546, 62213, 1306473, 3297289062213,
                   909237470148, 724662728226, 14434, 3022, 3022, 0},
            PositionCounts{136692, 0, 0},
            84, 0, 84,
        };
    }
    if (m3 == 23) {
        return ExpectedSlice{
            Counts{23052, 21862, 12626, 265146, 669178012626,
                   157204132194, 149533255023, 9653, 2354, 2354, 0},
            PositionCounts{23052, 0, 0},
            84, 0, 84,
        };
    }
    if (m3 == 24) {
        return ExpectedSlice{
            Counts{3742, 3349, 2594, 54474, 137482002594,
                   30699617734, 30667990956, 464987, 40494, 40494, 0},
            PositionCounts{3742, 0, 0},
            84, 0, 84,
        };
    }
    if (m3 == 25) {
        return ExpectedSlice{
            Counts{401, 397, 344, 7224, 18232000344,
                   3588054173, 3588054173, 0, 0, 0, 0},
            PositionCounts{401, 0, 0},
            84, 0, 84,
        };
    }
    if (m3 == 26) {
        return ExpectedSlice{
            Counts{35, 35, 35, 735, 1855000035,
                   371671617, 371671617, 84, 21, 21, 0},
            PositionCounts{35, 0, 0},
            84, 0, 84,
        };
    }
    return std::nullopt;
}

std::array<u64, EMPTY_MAX_M3 - EMPTY_MIN_M3 + 1> high_tail_counts_s5(
    int thread_count,
    bool progress
) {
    std::array<u64, EMPTY_MAX_M3 - EMPTY_MIN_M3 + 1> result{};
    const auto jobs = denominator_jobs_s5();
    std::atomic<std::size_t> completed{0};
    if (thread_count > 0) omp_set_num_threads(thread_count);
#pragma omp parallel
    {
        std::array<u64, EMPTY_MAX_M3 - EMPTY_MIN_M3 + 1> local{};
#pragma omp for schedule(dynamic, 4)
        for (std::int64_t raw_index = 0;
             raw_index < static_cast<std::int64_t>(jobs.size());
             ++raw_index) {
            const DenominatorJob& job = jobs[static_cast<std::size_t>(raw_index)];
            const u64 Q = job.b1 * pow_u64(10, job.m2) + job.b2;
            const u64 G = job.b1 * job.b2;
            const u64 QG = Q * G;
            const int qg2 = valuation(QG, 2);
            const int qg5 = valuation(QG, 5);
            for (u64 kappa : bounded_divisors(QG, EMPTY_MAX_M3, 10 * QG)) {
                if (kappa <= QG) continue;
                const int k2 = valuation(kappa, 2);
                const int k5 = valuation(kappa, 5);
                const int lower = std::max({EMPTY_MIN_M3, k2 - qg2, k5 - qg5});
                const int upper = std::min({
                    EMPTY_MAX_M3,
                    2 * k2 + valuation(kappa + 2 * G, 2),
                    2 * k5 + valuation(kappa + 2 * G, 5),
                });
                for (int m3 = lower; m3 <= upper; ++m3) {
                    ++local[static_cast<std::size_t>(m3 - EMPTY_MIN_M3)];
                }
            }
            const std::size_t done = ++completed;
            if (progress && done % 20000 == 0) {
#pragma omp critical(s5_high_progress_output)
                std::cerr << "  high-tail check: " << done << "/" << jobs.size()
                          << " denominator jobs\n";
            }
        }
#pragma omp critical(s5_high_result_merge)
        for (std::size_t index = 0; index < result.size(); ++index) {
            result[index] += local[index];
        }
    }
    return result;
}

void check_residue_solver128() {
    std::mt19937_64 random(2730001);
    for (u64 prime : {2ULL, 5ULL}) {
        for (int trial = 0; trial < 3000; ++trial) {
            const u64 lower = 1 + random() % 40;
            const u64 upper = lower + random() % 160;
            const u128 high_constant =
                (static_cast<u128>(1 + random() % 32) << 64) + random();
            const Polynomial128 polynomial{
                1 + random() % 50,
                1 + random() % 100,
                1 + random() % 70,
                high_constant,
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
                    PConditionKind::AtLeast,
                    0,
                    0,
                    0,
                    static_cast<int>(random() % 12),
                };
            } else {
                condition = {PConditionKind::Unit, 0, 0, 0, 0};
            }
            const auto classes = accepted_classes128(
                prime, condition, polynomial, lower, upper
            );
            for (u64 value = lower; value <= upper; ++value) {
                bool found = false;
                for (const Residue128& row : classes) {
                    if (static_cast<u128>(value) % row.modulus == row.residue) {
                        found = true;
                        break;
                    }
                }
                const bool expected = p_condition_accepts(
                    condition,
                    valuation128(polynomial.N(value), prime),
                    valuation(polynomial.A(value), prime)
                );
                if (found != expected) {
                    throw std::logic_error("S=5 u128 residue-tree mismatch");
                }
            }
        }
    }
}

void check_cpp_conversion128() {
    std::mt19937_64 random(2730002);
    for (int trial = 0; trial < 3000; ++trial) {
        const u64 high = random();
        const u64 low = random();
        const u128 value = (static_cast<u128>(high) << 64) + low;
        const cpp_int expected = (cpp_int(high) << 64) + low;
        if (cpp_from_u128(value) != expected) {
            throw std::logic_error("u128 to cpp_int conversion mismatch");
        }
    }
}

void self_check_s5() {
    check_residue_solver128();
    std::cout << "S=5 u128 p-adic residue tree vs direct enumeration: OK\n";
    check_cpp_conversion128();
    std::cout << "exact u128 to cpp_int conversion: OK\n";
}

struct Options5 {
    int m3_min = FINITE_MIN_M3;
    int m3_max = FINITE_MAX_M3;
    int threads = 0;
    bool progress = false;
    bool run_self_check = false;
    bool expect_baseline = false;
    bool empty_high_only = false;
    bool selected_one_m3 = false;
};

Options5 parse_options_s5(int argc, char** argv) {
    Options5 options;
    for (int index = 1; index < argc; ++index) {
        const std::string option = argv[index];
        auto require_value = [&]() -> const char* {
            if (++index >= argc) {
                throw std::invalid_argument("missing value for " + option);
            }
            return argv[index];
        };
        if (option == "--m3") {
            options.m3_min = options.m3_max = parse_int(require_value(), option);
            options.selected_one_m3 = true;
        } else if (option == "--threads") {
            options.threads = parse_int(require_value(), option);
        } else if (option == "--progress") {
            options.progress = true;
        } else if (option == "--self-check") {
            options.run_self_check = true;
        } else if (option == "--expect-baseline") {
            options.expect_baseline = true;
        } else if (option == "--empty-high-only") {
            options.empty_high_only = true;
        } else if (option == "--help" || option == "-h") {
            std::cout
                << "usage: check_dd_2730_cpp [--m3 N] [--threads N] [--progress]\n"
                << "       [--self-check] [--expect-baseline] [--empty-high-only]\n";
            std::exit(0);
        } else {
            throw std::invalid_argument("unknown option: " + option);
        }
    }
    if (options.m3_min < FINITE_MIN_M3 ||
        options.m3_max > FINITE_MAX_M3 ||
        options.m3_min > options.m3_max) {
        throw std::invalid_argument("finite certificate covers 22 <= m_3 <= 26");
    }
    if (options.threads < 0) throw std::invalid_argument("negative thread count");
    if (options.empty_high_only && options.selected_one_m3) {
        throw std::invalid_argument("--m3 and --empty-high-only are incompatible");
    }
    return options;
}

}  // namespace

#ifndef CHECK_DD_2730_NO_MAIN
int main(int argc, char** argv) {
    try {
        const Options5 options = parse_options_s5(argc, argv);
        if (options.run_self_check) {
            self_check();
            self_check_s5();
        }

        if (!options.empty_high_only) {
            for (int m3 = options.m3_min; m3 <= options.m3_max; ++m3) {
                SliceResult result = check_slice_s5(
                    m3, options.threads, options.progress
                );
                print_result(result);
                if (result.counts.square_discriminants != 0) {
                    throw std::logic_error("S=5 square discriminant found");
                }
                if (options.expect_baseline) {
                    const auto expected = expected_s5(m3);
                    if (!expected ||
                        result.coarse_shapes != expected->coarse_shapes ||
                        result.killed_shapes != expected->killed_shapes ||
                        result.surviving_shapes != expected->surviving_shapes ||
                        !(result.counts == expected->counts) ||
                        !same_positions(result.positions, expected->positions)) {
                        throw std::logic_error("S=5 recorded exact-counter mismatch");
                    }
                    std::cout << "  S=5 recorded exact counters: OK\n";
                }
            }
        }

        if (options.empty_high_only || !options.selected_one_m3) {
            const auto high_counts = high_tail_counts_s5(
                options.threads, options.progress
            );
            if (std::any_of(high_counts.begin(), high_counts.end(),
                            [](u64 count) { return count != 0; })) {
                throw std::logic_error("S=5 high-tail kernel is not empty");
            }
            std::cout << "m_3=27,...,32 primitive denominator-tail rows =";
            for (u64 count : high_counts) std::cout << ' ' << count;
            std::cout << '\n';
            if (options.expect_baseline) {
                std::cout << "  S=5 recorded high-tail counters: OK\n";
            }
        }

        std::cout << "DD S=5 high-tail finite certificate: OK\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 1;
    }
}
#endif
