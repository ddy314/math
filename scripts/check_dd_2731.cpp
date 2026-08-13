// Exact finite certificate for S_12=5, n_3=39, m_3=14.
//
// Build and run:
//   g++ -O3 -DNDEBUG -std=c++20 -fopenmp scripts/check_dd_2731.cpp
//       -o /tmp/check_dd_2731_cpp
//   /tmp/check_dd_2731_cpp --self-check --threads 12 --expect-baseline
//
// Section 27.29 leaves 14 <= m_3 <= 21.  At m_3=14 the strict digit
// kernel contains only (m_1,m_2;n_1,n_2)=(4,1;1,6).  This certificate
// applies four numerator-free necessary filters to its complete primitive
// tail kernel, then reuses the audited S=5 u128 residue tree and cpp_int
// discriminant from check_dd_2730.cpp on every surviving prefix.

#define CHECK_DD_2730_NO_MAIN
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-function"
#include "check_dd_2730.cpp"
#pragma GCC diagnostic pop
#undef CHECK_DD_2730_NO_MAIN

namespace {

constexpr int M3_14 = 14;
constexpr int D3_14 = 25;
constexpr Shape5 SHAPE_14{4, 1, 1, 6};
constexpr u128 F_MINUS_UPPER_14 = u128(2) * 10000000000000ULL;

struct FilterCounts14 {
    u64 tail_rows = 0;
    u64 eligible_rows = 0;
    u64 corner_rows = 0;
    u64 valuation_box_rows = 0;
    u64 large_divisor_rows = 0;
    u64 two_unit_rows = 0;
    u64 five_unit_rows = 0;
    u64 denominator_pairs = 0;
    u64 surviving_denominator_pairs = 0;
    PositionCounts positions;

    FilterCounts14& operator+=(const FilterCounts14& other) {
        tail_rows += other.tail_rows;
        eligible_rows += other.eligible_rows;
        corner_rows += other.corner_rows;
        valuation_box_rows += other.valuation_box_rows;
        large_divisor_rows += other.large_divisor_rows;
        two_unit_rows += other.two_unit_rows;
        five_unit_rows += other.five_unit_rows;
        denominator_pairs += other.denominator_pairs;
        surviving_denominator_pairs += other.surviving_denominator_pairs;
        positions += other.positions;
        return *this;
    }
};

int maximum_valuation_below128(u128 bound, u64 prime) {
    int exponent = 0;
    u128 power = 1;
    while (power * prime < bound) {
        power *= prime;
        ++exponent;
    }
    return exponent;
}

bool value_in_interval(int value, int lower, int upper) {
    return lower <= value && value <= upper;
}

bool condition_intersects_box(
    const PCondition& condition,
    int n_lower,
    int n_upper,
    int a_lower,
    int a_upper
) {
    if (n_lower > n_upper || a_lower > a_upper) return false;
    if (condition.kind == PConditionKind::Unit) return true;
    if (condition.kind == PConditionKind::AtLeast) {
        return n_upper >= condition.threshold;
    }
    return value_in_interval(condition.resonance, n_lower, n_upper) ||
           value_in_interval(
               condition.plus_gap,
               n_lower - a_upper,
               n_upper - a_lower
           ) ||
           value_in_interval(condition.minus_a, a_lower, a_upper);
}

bool signature_fits_height_box14(const Signature& signature) {
    constexpr u128 A_BOUND = u128(10000000);
    constexpr u128 N_BOUND = u128(10000) +
                             u128(10000000000ULL) * 10000000000ULL;
    const int max_a_2 = maximum_valuation_below128(A_BOUND, 2);
    const int max_a_5 = maximum_valuation_below128(A_BOUND, 5);
    const int max_n_2 = maximum_valuation_below128(N_BOUND, 2);
    const int max_n_5 = maximum_valuation_below128(N_BOUND, 5);
    return condition_intersects_box(signature.two, 0, max_n_2, 0, max_a_2) &&
           condition_intersects_box(signature.five, 0, max_n_5, 0, max_a_5);
}

bool corner_gap_possible14(u64 b1, u64 b2) {
    const u64 Q = b1 * 10 + b2;
    constexpr std::array<u64, 2> A1{1, 9};
    constexpr std::array<u64, 2> A2{100000, 999999};
    for (u64 a1 : A1) {
        for (u64 a2 : A2) {
            const u64 A = a1 * 1000000 + a2;
            const u128 x = u128(a1) * b2;
            const u128 y = u128(a2) * b1;
            const u128 N = x * x + y * y;
            const u128 left = pow_u128(10, D3_14) * u128(A);
            const u128 right = u128(40) * Q * Q * N;
            if (left < right) return true;
        }
    }
    return false;
}

u128 gcd128(u128 left, u128 right) {
    while (right != 0) {
        const u128 remainder = left % right;
        left = right;
        right = remainder;
    }
    return left;
}

bool large_divisor_fits14(const Tail& tail) {
    const u128 numerator = u128(tail.kappa) * (tail.kappa + 2 * tail.G);
    const u128 primitive = numerator /
        gcd128(numerator, u128(tail.kappa) + tail.G);
    const u128 large_divisor = primitive / gcd128(primitive, tail.Q);
    return large_divisor < F_MINUS_UPPER_14;
}

bool denominator_unit_possible14(
    const PCondition& condition,
    u64 prime,
    u64 b1,
    u64 b2
) {
    const int e1 = valuation(b1, prime);
    const int e2 = valuation(b2, prime);
    if (e1 == 0 && e2 == 0) return true;

    constexpr u128 A_BOUND = u128(10000000);
    constexpr u128 N_BOUND = u128(10000) +
                             u128(10000000000ULL) * 10000000000ULL;
    const int max_a = maximum_valuation_below128(A_BOUND, prime);
    const int max_n = maximum_valuation_below128(N_BOUND, prime);
    int n_lower = 0;
    int n_upper = 0;
    int a_lower = 0;
    int a_upper = 0;

    if (e1 > 0 && e2 == 0) {
        // gcd(a_1,b_1)=1 makes a_1 b_2 a unit; A may have any height.
        a_upper = max_a;
    } else if (e1 == 0 && e2 > 0) {
        // gcd(a_2,b_2)=1 makes both N and A units.
    } else if (e1 != e2) {
        // Both numerators are units; the two norm terms have unequal depth.
        n_lower = n_upper = 2 * std::min(e1, e2);
    } else if (prime == 2) {
        // Odd squares sum to 2 mod 8 after removing the common 2^e factor.
        n_lower = n_upper = 2 * e1 + 1;
    } else {
        // For p=5 equal denominator depths may cancel to any larger depth.
        n_lower = 2 * e1;
        n_upper = max_n;
    }
    return condition_intersects_box(
        condition, n_lower, n_upper, a_lower, a_upper
    );
}

bool direct_prefix_exists_in_small_box(
    const PCondition& condition,
    u64 prime,
    u64 b1,
    u64 b2,
    u64 a1_upper,
    u64 a2_upper
) {
    for (u64 a1 = 1; a1 <= a1_upper; ++a1) {
        if (std::gcd(a1, b1) != 1) continue;
        for (u64 a2 = 1; a2 <= a2_upper; ++a2) {
            if (std::gcd(a2, b2) != 1) continue;
            const u64 A = a1 * 1000000 + a2;
            const u128 x = u128(a1) * b2;
            const u128 y = u128(a2) * b1;
            const u128 N = x * x + y * y;
            if (p_condition_accepts(
                    condition, valuation128(N, prime), valuation(A, prime))) {
                return true;
            }
        }
    }
    return false;
}

void check_unit_filter_small_boxes() {
    std::mt19937_64 random(2731001);
    for (u64 prime : {2ULL, 5ULL}) {
        for (int trial = 0; trial < 3000; ++trial) {
            const u64 b1 = 1 + random() % 40;
            const u64 b2 = 1 + random() % 20;
            PCondition condition;
            if (random() % 4 == 0) {
                condition = {
                    PConditionKind::AtLeast, 0, 0, 0,
                    static_cast<int>(random() % 16),
                };
            } else {
                condition = {
                    PConditionKind::Disjunction,
                    static_cast<int>(random() % 24) - 6,
                    static_cast<int>(random() % 30) - 8,
                    static_cast<int>(random() % 24) - 6,
                    0,
                };
            }
            const bool possible = denominator_unit_possible14(
                condition, prime, b1, b2
            );
            const bool actual = direct_prefix_exists_in_small_box(
                condition, prime, b1, b2, 9, 120
            );
            if (actual && !possible) {
                throw std::logic_error("denominator-unit filter removed a direct row");
            }
        }
    }
    std::cout << "denominator-unit height filter vs direct small boxes: OK\n";
}

void check_digit_kernel14() {
    int coarse = 0;
    int killed = 0;
    const std::vector<Shape5> shapes = digit_shapes_s5(
        M3_14, &coarse, &killed
    );
    if (coarse != 2 || killed != 1 || shapes.size() != 1 ||
        shapes.front().m1 != SHAPE_14.m1 ||
        shapes.front().m2 != SHAPE_14.m2 ||
        shapes.front().n1 != SHAPE_14.n1 ||
        shapes.front().n2 != SHAPE_14.n2) {
        throw std::logic_error("m_3=14 digit-kernel mismatch");
    }
    std::cout << "m_3=14 digit kernel: coarse=2, size-killed=1, surviving=1\n";
}

struct Result14 {
    FilterCounts14 filters;
    Counts prefixes;
};

Result14 check_m14(int thread_count, bool progress) {
    const auto [b1_lower, b1_upper] = digit_interval(4);
    const auto [b2_lower, b2_upper] = digit_interval(1);
    std::vector<DenominatorJob> jobs;
    for (u64 b1 = b1_lower; b1 <= b1_upper; ++b1) {
        for (u64 b2 = b2_lower; b2 <= b2_upper; ++b2) {
            jobs.push_back({4, 1, b1, b2});
        }
    }
    std::atomic<std::size_t> completed{0};
    Result14 result;
    if (thread_count > 0) omp_set_num_threads(thread_count);
#pragma omp parallel
    {
        FilterCounts14 local_filters;
        Counts local_prefixes;
        CandidateMarker marker(900000);
#pragma omp for schedule(dynamic, 1)
        for (std::int64_t raw_index = 0;
             raw_index < static_cast<std::int64_t>(jobs.size());
             ++raw_index) {
            const DenominatorJob& job = jobs[static_cast<std::size_t>(raw_index)];
            TailGroups groups = build_tail_groups_s5(
                4, 1, job.b1, job.b2, M3_14
            );
            local_filters.tail_rows += groups.total;
            local_filters.positions += groups.positions;
            u64 eligible = 0;
            for (const auto& [signature, tails] : groups.groups) {
                (void)signature;
                eligible += tails.size();
            }
            local_filters.eligible_rows += eligible;
            if (eligible == 0) continue;
            ++local_filters.denominator_pairs;
            if (!corner_gap_possible14(job.b1, job.b2)) continue;
            local_filters.corner_rows += eligible;

            std::map<Signature, std::vector<Tail>> survivors;
            for (const auto& [signature, tails] : groups.groups) {
                if (!signature_fits_height_box14(signature)) continue;
                local_filters.valuation_box_rows += tails.size();
                for (const Tail& tail : tails) {
                    if (!large_divisor_fits14(tail)) continue;
                    ++local_filters.large_divisor_rows;
                    if (!denominator_unit_possible14(
                            signature.two, 2, job.b1, job.b2)) continue;
                    ++local_filters.two_unit_rows;
                    if (!denominator_unit_possible14(
                            signature.five, 5, job.b1, job.b2)) continue;
                    ++local_filters.five_unit_rows;
                    survivors[signature].push_back(tail);
                }
            }
            if (!survivors.empty()) {
                ++local_filters.surviving_denominator_pairs;
                ++local_prefixes.shape_denominator_pairs;
                process_shape_s5(
                    SHAPE_14,
                    job.b1,
                    job.b2,
                    M3_14,
                    survivors,
                    marker,
                    local_prefixes
                );
            }
            const std::size_t done = ++completed;
            if (progress && done % 5000 == 0) {
#pragma omp critical(m14_progress)
                std::cerr << "  m_3=14: checked " << done << "/" << jobs.size()
                          << " denominator jobs\n";
            }
        }
#pragma omp critical(m14_merge)
        {
            result.filters += local_filters;
            result.prefixes += local_prefixes;
        }
    }
    result.prefixes.tail_rows = result.filters.tail_rows;
    result.prefixes.eligible_tail_rows = result.filters.eligible_rows;
    result.prefixes.denominator_pairs = result.filters.denominator_pairs;
    return result;
}

struct Options14 {
    int threads = 0;
    bool progress = false;
    bool self_check = false;
    bool expect_baseline = false;
};

Options14 parse_options14(int argc, char** argv) {
    Options14 options;
    for (int index = 1; index < argc; ++index) {
        const std::string option = argv[index];
        auto require_value = [&]() -> const char* {
            if (++index >= argc) throw std::invalid_argument("missing " + option);
            return argv[index];
        };
        if (option == "--threads") {
            options.threads = parse_int(require_value(), option);
        } else if (option == "--progress") {
            options.progress = true;
        } else if (option == "--self-check") {
            options.self_check = true;
        } else if (option == "--expect-baseline") {
            options.expect_baseline = true;
        } else if (option == "--help" || option == "-h") {
            std::cout << "usage: check_dd_2731_cpp [--threads N] [--progress] "
                         "[--self-check] [--expect-baseline]\n";
            std::exit(0);
        } else {
            throw std::invalid_argument("unknown option: " + option);
        }
    }
    if (options.threads < 0) throw std::invalid_argument("negative threads");
    return options;
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options14 options = parse_options14(argc, argv);
        if (options.self_check) {
            self_check();
            self_check_s5();
            check_digit_kernel14();
            check_unit_filter_small_boxes();
        }
        if (options.expect_baseline && !options.self_check) check_digit_kernel14();
        const Result14 result = check_m14(options.threads, options.progress);
        const FilterCounts14& f = result.filters;
        const Counts& c = result.prefixes;
        std::cout << "m_3=14 filter counts: tail=" << f.tail_rows
                  << ", eligible=" << f.eligible_rows
                  << ", corner=" << f.corner_rows
                  << ", valuation-box=" << f.valuation_box_rows
                  << ", L_F=" << f.large_divisor_rows
                  << ", two-unit=" << f.two_unit_rows
                  << ", five-unit=" << f.five_unit_rows
                  << ", denominator-pairs=" << f.denominator_pairs
                  << ", surviving-denominators="
                  << f.surviving_denominator_pairs << '\n';
        std::cout << "  tail positions = {'b3-unique': "
                  << f.positions.b3_unique << ", 'all-odd': "
                  << f.positions.all_odd << ", 'prefix-or-tie': "
                  << f.positions.prefix_or_tie << "}\n";
        std::cout << "  Counts(digit_pairs=" << c.digit_pairs
                  << ", coprime_pairs=" << c.coprime_pairs
                  << ", squarefree_pairs=" << c.squarefree_pairs
                  << ", valuation_tail_pairs=" << c.valuation_tail_pairs
                  << ", modular_square_pairs=" << c.modular_square_pairs
                  << ", nonnegative_discriminants="
                  << c.nonnegative_discriminants
                  << ", square_discriminants=" << c.square_discriminants
                  << ")\n";
        if (options.expect_baseline) {
            if (f.tail_rows != 6207930 || f.eligible_rows != 5828153 ||
                f.corner_rows != 1378380 || f.valuation_box_rows != 1123254 ||
                f.large_divisor_rows != 8495 || f.two_unit_rows != 611 ||
                f.five_unit_rows != 75 || f.denominator_pairs != 80991 ||
                f.surviving_denominator_pairs != 49 ||
                f.positions.b3_unique != 5904517 ||
                f.positions.all_odd != 72157 ||
                f.positions.prefix_or_tie != 231256 ||
                c.shape_denominator_pairs != 49 ||
                c.digit_pairs != 396900000 ||
                c.coprime_pairs != 222531424 ||
                c.squarefree_pairs != 7930779 ||
                c.valuation_tail_pairs != 0 ||
                c.modular_square_pairs != 0 ||
                c.nonnegative_discriminants != 0 ||
                c.square_discriminants != 0) {
                throw std::logic_error("m_3=14 structural baseline mismatch");
            }
        }
        if (c.square_discriminants != 0) {
            throw std::logic_error("m_3=14 square discriminant found");
        }
        std::cout << "DD S=5, m_3=14 finite certificate: OK\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 1;
    }
}
