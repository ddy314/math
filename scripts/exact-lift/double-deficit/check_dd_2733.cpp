// Exact finite certificate for S_12=5, n_3=39, m_3=16.
//
// Build and run:
//   g++ -O3 -DNDEBUG -std=c++20 -fopenmp -Wall -Wextra -Wconversion
//       -Wshadow scripts/exact-lift/double-deficit/check_dd_2733.cpp -o /tmp/check_dd_2733_cpp
//   /tmp/check_dd_2733_cpp --self-check --threads 12 --expect-baseline
//
// Every strict digit shape is treated separately.  The complete primitive
// denominator-tail kernel is reduced by exact corner-gap, valuation-height,
// L_F, and denominator-unit necessary filters.  Every survivor then enters
// the audited u128 prefix residue tree and cpp_int discriminant engine.  The
// d_3=23 gap power is constructed in u128.

#define CHECK_DD_2730_NO_MAIN
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-function"
#include "check_dd_2730.cpp"
#pragma GCC diagnostic pop
#undef CHECK_DD_2730_NO_MAIN

namespace {

constexpr int M3_16 = 16;
constexpr int D3_16 = 23;
constexpr std::array<Shape5, 7> SHAPES_16{{
    {1, 4, 5, 1},
    {1, 4, 6, 1},
    {3, 2, 1, 6},
    {4, 1, 1, 4},
    {4, 1, 1, 5},
    {4, 1, 1, 6},
    {4, 1, 2, 5},
}};

bool same_shape16(const Shape5& left, const Shape5& right) {
    return left.m1 == right.m1 && left.m2 == right.m2 &&
           left.n1 == right.n1 && left.n2 == right.n2;
}

std::string shape_name16(const Shape5& shape) {
    return "(" + std::to_string(shape.m1) + "," +
           std::to_string(shape.m2) + ";" +
           std::to_string(shape.n1) + "," +
           std::to_string(shape.n2) + ")";
}

u128 numerator_bound16(const Shape5& shape) {
    return pow_u128(10, shape.n1 + shape.n2);
}

u128 norm_bound16(const Shape5& shape) {
    return pow_u128(10, 2 * (shape.n1 + shape.m2)) +
           pow_u128(10, 2 * (shape.n2 + shape.m1));
}

int maximum_valuation_below128_16(u128 bound, u64 prime) {
    int exponent = 0;
    u128 power = 1;
    while (power * prime < bound) {
        power *= prime;
        ++exponent;
    }
    return exponent;
}

bool condition_intersects_box16(
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
    auto inside = [](int value, int lower, int upper) {
        return lower <= value && value <= upper;
    };
    return inside(condition.resonance, n_lower, n_upper) ||
           inside(
               condition.plus_gap,
               n_lower - a_upper,
               n_upper - a_lower
           ) ||
           inside(condition.minus_a, a_lower, a_upper);
}

u128 gcd128_16(u128 left, u128 right) {
    while (right != 0) {
        const u128 remainder = left % right;
        left = right;
        right = remainder;
    }
    return left;
}

bool signature_fits_height_box16(
    const Shape5& shape,
    const Signature& signature
) {
    const u128 a_bound = numerator_bound16(shape);
    const u128 n_bound = norm_bound16(shape);
    const int max_a_2 = maximum_valuation_below128_16(a_bound, 2);
    const int max_a_5 = maximum_valuation_below128_16(a_bound, 5);
    const int max_n_2 = maximum_valuation_below128_16(n_bound, 2);
    const int max_n_5 = maximum_valuation_below128_16(n_bound, 5);
    return condition_intersects_box16(signature.two, 0, max_n_2, 0, max_a_2) &&
           condition_intersects_box16(signature.five, 0, max_n_5, 0, max_a_5);
}

bool denominator_unit_possible16(
    const Shape5& shape,
    const PCondition& condition,
    u64 prime,
    u64 b1,
    u64 b2
) {
    const int e1 = valuation(b1, prime);
    const int e2 = valuation(b2, prime);
    if (e1 == 0 && e2 == 0) return true;

    const int max_a = maximum_valuation_below128_16(
        numerator_bound16(shape), prime
    );
    const int max_n = maximum_valuation_below128_16(norm_bound16(shape), prime);
    int n_lower = 0;
    int n_upper = 0;
    int a_lower = 0;
    int a_upper = 0;
    if (e1 > 0 && e2 == 0) {
        a_upper = max_a;
    } else if (e1 == 0 && e2 > 0) {
        // Both N and A are units.
    } else if (e1 != e2) {
        n_lower = n_upper = 2 * std::min(e1, e2);
    } else if (prime == 2) {
        n_lower = n_upper = 2 * e1 + 1;
    } else {
        n_lower = 2 * e1;
        n_upper = max_n;
    }
    return condition_intersects_box16(
        condition, n_lower, n_upper, a_lower, a_upper
    );
}

struct FilterCounts16 {
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

    FilterCounts16& operator+=(const FilterCounts16& other) {
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

struct Result16 {
    FilterCounts16 filters;
    Counts prefixes;
};

u128 f_minus_upper16(const Shape5& shape) {
    const int s1 = shape.n1 - shape.m1;
    const int s2 = shape.n2 - shape.m2;
    const int exponent = 2 * S5 + s1 + s2 + std::abs(s1 - s2) +
                         2 * M3_16 - N3_5 + 4;
    if (exponent < 0) throw std::logic_error("negative m_3=16 F_- exponent");
    return u128(2) * pow_u128(10, exponent);
}

bool corner_gap_possible16(const Shape5& shape, u64 b1, u64 b2) {
    const auto [a1_lower, a1_upper] = digit_interval(shape.n1);
    const auto [a2_lower, a2_upper] = digit_interval(shape.n2);
    const u64 Q = b1 * pow_u64(10, shape.m2) + b2;
    const std::array<u64, 2> a1_corners{a1_lower, a1_upper};
    const std::array<u64, 2> a2_corners{a2_lower, a2_upper};
    for (u64 a1 : a1_corners) {
        for (u64 a2 : a2_corners) {
            const u64 A = a1 * pow_u64(10, shape.n2) + a2;
            const u128 x = u128(a1) * b2;
            const u128 y = u128(a2) * b1;
            const u128 N = x * x + y * y;
            const u128 left = pow_u128(10, D3_16) * u128(A);
            const u128 right = u128(40) * Q * Q * N;
            if (left < right) return true;
        }
    }
    return false;
}

bool large_divisor_fits16(const Shape5& shape, const Tail& tail) {
    const u128 numerator = u128(tail.kappa) * (tail.kappa + 2 * tail.G);
    const u128 primitive = numerator /
        gcd128_16(numerator, u128(tail.kappa) + tail.G);
    const u128 large_divisor = primitive / gcd128_16(primitive, tail.Q);
    return large_divisor < f_minus_upper16(shape);
}

Result16 check_shape16(
    const Shape5& shape,
    int thread_count,
    bool progress
) {
    const auto [b1_lower, b1_upper] = digit_interval(shape.m1);
    const auto [b2_lower, b2_upper] = digit_interval(shape.m2);
    std::vector<DenominatorJob> jobs;
    for (u64 b1 = b1_lower; b1 <= b1_upper; ++b1) {
        for (u64 b2 = b2_lower; b2 <= b2_upper; ++b2) {
            jobs.push_back({shape.m1, shape.m2, b1, b2});
        }
    }

    std::atomic<std::size_t> completed{0};
    Result16 result;
    if (thread_count > 0) omp_set_num_threads(thread_count);
#pragma omp parallel
    {
        FilterCounts16 local_filters;
        Counts local_prefixes;
        CandidateMarker marker(900000);
#pragma omp for schedule(dynamic, 1)
        for (std::int64_t raw_index = 0;
             raw_index < static_cast<std::int64_t>(jobs.size());
             ++raw_index) {
            const DenominatorJob& job = jobs[static_cast<std::size_t>(raw_index)];
            TailGroups groups = build_tail_groups_s5(
                shape.m1, shape.m2, job.b1, job.b2, M3_16
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
            if (!corner_gap_possible16(shape, job.b1, job.b2)) continue;
            local_filters.corner_rows += eligible;

            std::map<Signature, std::vector<Tail>> survivors;
            for (const auto& [signature, tails] : groups.groups) {
                if (!signature_fits_height_box16(shape, signature)) continue;
                local_filters.valuation_box_rows += tails.size();
                for (const Tail& tail : tails) {
                    if (!large_divisor_fits16(shape, tail)) continue;
                    ++local_filters.large_divisor_rows;
                    if (!denominator_unit_possible16(
                            shape, signature.two, 2, job.b1, job.b2)) continue;
                    ++local_filters.two_unit_rows;
                    if (!denominator_unit_possible16(
                            shape, signature.five, 5, job.b1, job.b2)) continue;
                    ++local_filters.five_unit_rows;
                    survivors[signature].push_back(tail);
                }
            }
            if (!survivors.empty()) {
                ++local_filters.surviving_denominator_pairs;
                ++local_prefixes.shape_denominator_pairs;
                process_shape_s5(
                    shape,
                    job.b1,
                    job.b2,
                    M3_16,
                    survivors,
                    marker,
                    local_prefixes
                );
            }
            const std::size_t done = ++completed;
            if (progress && done % 5000 == 0) {
#pragma omp critical(m16_progress)
                std::cerr << "  m_3=16 shape " << shape_name16(shape)
                          << ": checked " << done << "/" << jobs.size()
                          << " denominator jobs\n";
            }
        }
#pragma omp critical(m16_merge)
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

void check_digit_kernel16() {
    int coarse = 0;
    int killed = 0;
    const std::vector<Shape5> actual = digit_shapes_s5(
        M3_16, &coarse, &killed
    );
    if (coarse != 10 || killed != 3 || actual.size() != SHAPES_16.size()) {
        throw std::logic_error("m_3=16 digit-kernel count mismatch");
    }
    for (std::size_t index = 0; index < SHAPES_16.size(); ++index) {
        if (!same_shape16(actual[index], SHAPES_16[index])) {
            throw std::logic_error("m_3=16 digit-kernel shape mismatch");
        }
    }
    std::cout << "m_3=16 digit kernel: coarse=10, size-killed=3, surviving=7\n";
}

void check_unit_filter_samples16() {
    std::mt19937_64 random(2733001);
    for (const Shape5& shape : SHAPES_16) {
        const auto [a1_lower, a1_upper] = digit_interval(shape.n1);
        const auto [a2_lower, a2_upper] = digit_interval(shape.n2);
        const auto [b1_lower, b1_upper] = digit_interval(shape.m1);
        const auto [b2_lower, b2_upper] = digit_interval(shape.m2);
        for (u64 prime : {2ULL, 5ULL}) {
            for (int trial = 0; trial < 2500; ++trial) {
                const u64 b1 = b1_lower + random() % (b1_upper - b1_lower + 1);
                const u64 b2 = b2_lower + random() % (b2_upper - b2_lower + 1);
                const u64 a1 = a1_lower + random() % (a1_upper - a1_lower + 1);
                const u64 a2 = a2_lower + random() % (a2_upper - a2_lower + 1);
                if (std::gcd(a1, b1) != 1 || std::gcd(a2, b2) != 1) continue;
                const u64 A = a1 * pow_u64(10, shape.n2) + a2;
                const u128 x = u128(a1) * b2;
                const u128 y = u128(a2) * b1;
                const u128 N = x * x + y * y;
                const int n = valuation128(N, prime);
                const int a = valuation(A, prime);
                std::array<PCondition, 4> conditions{{
                    {PConditionKind::AtLeast, 0, 0, 0, n},
                    {PConditionKind::Disjunction, n, -100, -100, 0},
                    {PConditionKind::Disjunction, -100, n - a, -100, 0},
                    {PConditionKind::Disjunction, -100, -100, a, 0},
                }};
                for (const PCondition& condition : conditions) {
                    if (!p_condition_accepts(condition, n, a) ||
                        !denominator_unit_possible16(
                            shape, condition, prime, b1, b2)) {
                        throw std::logic_error(
                            "m_3=16 denominator-unit sample implication failed"
                        );
                    }
                }
            }
        }
    }
    std::cout << "m_3=16 denominator-unit sampled implications: OK\n";
}

void print_result16(const Shape5& shape, const Result16& result) {
    const FilterCounts16& f = result.filters;
    const Counts& c = result.prefixes;
    std::cout << "m_3=16 shape " << shape_name16(shape)
              << " filter counts: tail=" << f.tail_rows
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
    std::cout << "  Counts(shape_denominator_pairs="
              << c.shape_denominator_pairs
              << ", digit_pairs=" << c.digit_pairs
              << ", coprime_pairs=" << c.coprime_pairs
              << ", squarefree_pairs=" << c.squarefree_pairs
              << ", valuation_tail_pairs=" << c.valuation_tail_pairs
              << ", modular_square_pairs=" << c.modular_square_pairs
              << ", nonnegative_discriminants="
              << c.nonnegative_discriminants
              << ", square_discriminants=" << c.square_discriminants
              << ")\n";
}

struct Options16 {
    int threads = 0;
    bool progress = false;
    bool self_check = false;
    bool expect_baseline = false;
};

Options16 parse_options16(int argc, char** argv) {
    Options16 options;
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
            std::cout << "usage: check_dd_2733_cpp [--threads N] [--progress] "
                         "[--self-check] [--expect-baseline]\n";
            std::exit(0);
        } else {
            throw std::invalid_argument("unknown option: " + option);
        }
    }
    if (options.threads < 0) throw std::invalid_argument("negative threads");
    return options;
}

void expect_shape_baseline16(std::size_t index, const Result16& result) {
    struct Expected16 {
        u64 tail;
        u64 eligible;
        u64 corner;
        u64 valuation_box;
        u64 large_divisor;
        u64 two_unit;
        u64 five_unit;
        u64 denominator_pairs;
        u64 surviving_denominators;
        u64 b3_unique;
        u64 all_odd;
        u64 prefix_or_tie;
        u64 digit_pairs;
        u64 coprime_pairs;
        u64 squarefree_pairs;
        u64 valuation_tail_pairs;
        u64 modular_square_pairs;
        u64 nonnegative_discriminants;
    };
    constexpr std::array<Expected16, 7> expected{{
        {3204978, 3144514, 1080702, 919334, 92629, 7726, 832,
         80980, 162, 3184969, 9419, 10590,
         131220000, 72564454, 20659196, 649641, 140824, 140824},
        {3204978, 3144514, 2674736, 2674736, 1226788, 130183, 45745,
         80980, 8423, 3184969, 9419, 10590,
         68226300000, 40312186920, 28606011556, 78800336, 11796342,
         11796342},
        {3779969, 3678398, 972341, 835902, 93771, 7083, 1262,
         80976, 191, 3754364, 9036, 16569,
         1547100000, 655610788, 26157576, 552354, 96627, 96627},
        {3117668, 3055605, 795593, 130736, 1280, 148, 3,
         80974, 3, 3095302, 8453, 13913,
         243000, 129600, 7126, 0, 0, 0},
        {3117668, 3055605, 2273319, 1922656, 142863, 10920, 3145,
         80974, 672, 3095302, 8453, 13913,
         544320000, 281530324, 100812497, 504802, 36993, 36993},
        {3117668, 3055605, 2820978, 2814558, 1299092, 157396, 60659,
         80974, 13880, 3095302, 8453, 13913,
         112428000000, 65834745916, 40926887605, 61262465, 10462987,
         10462987},
        {3117668, 3055605, 1323922, 1112913, 65168, 4883, 1356,
         80974, 325, 3095302, 8453, 13913,
         2632500000, 1232406148, 32153659, 56614, 2200, 2200},
    }};
    if (index >= expected.size()) {
        throw std::logic_error("m_3=16 baseline index out of range");
    }
    const Expected16& e = expected[index];
    const FilterCounts16& f = result.filters;
    const Counts& c = result.prefixes;
    if (f.tail_rows != e.tail || f.eligible_rows != e.eligible ||
        f.corner_rows != e.corner ||
        f.valuation_box_rows != e.valuation_box ||
        f.large_divisor_rows != e.large_divisor ||
        f.two_unit_rows != e.two_unit || f.five_unit_rows != e.five_unit ||
        f.denominator_pairs != e.denominator_pairs ||
        f.surviving_denominator_pairs != e.surviving_denominators ||
        f.positions.b3_unique != e.b3_unique ||
        f.positions.all_odd != e.all_odd ||
        f.positions.prefix_or_tie != e.prefix_or_tie ||
        c.shape_denominator_pairs != e.surviving_denominators ||
        c.digit_pairs != e.digit_pairs ||
        c.coprime_pairs != e.coprime_pairs ||
        c.squarefree_pairs != e.squarefree_pairs ||
        c.valuation_tail_pairs != e.valuation_tail_pairs ||
        c.modular_square_pairs != e.modular_square_pairs ||
        c.nonnegative_discriminants != e.nonnegative_discriminants ||
        c.square_discriminants != 0) {
        throw std::logic_error(
            "m_3=16 structural baseline mismatch for shape " +
            shape_name16(SHAPES_16[index])
        );
    }
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options16 options = parse_options16(argc, argv);
        if (options.self_check) {
            self_check();
            self_check_s5();
            check_digit_kernel16();
            check_unit_filter_samples16();
        }
        if (options.expect_baseline && !options.self_check) check_digit_kernel16();

        u64 square_discriminants = 0;
        for (std::size_t index = 0; index < SHAPES_16.size(); ++index) {
            const Result16 result = check_shape16(
                SHAPES_16[index], options.threads, options.progress
            );
            print_result16(SHAPES_16[index], result);
            if (options.expect_baseline) expect_shape_baseline16(index, result);
            square_discriminants += result.prefixes.square_discriminants;
        }
        if (square_discriminants != 0) {
            throw std::logic_error("m_3=16 square discriminant found");
        }
        std::cout << "DD S=5, m_3=16 finite certificate: OK\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 1;
    }
}
