// Exact finite certificate for S_12=5, n_3=39, m_3=15.
//
// Build and run:
//   g++ -O3 -DNDEBUG -std=c++20 -fopenmp -Wall -Wextra -Wconversion
//       -Wshadow scripts/exact-lift/double-deficit/check_dd_2732.cpp -o /tmp/check_dd_2732_cpp
//   /tmp/check_dd_2732_cpp --self-check --threads 12 --expect-baseline
//
// The strict digit kernel has three shapes.  This program exhausts the
// complete primitive denominator-tail kernel for each shape.  It applies the
// exact corner-gap, valuation-height, L_F, and denominator-unit necessary
// filters before passing every survivor to the audited S=5 u128 residue tree
// and cpp_int discriminant engine from check_dd_2730.cpp.  All powers entering
// the d_3=24 gap test are formed in u128 (never u64).

#define CHECK_DD_2730_NO_MAIN
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-function"
#include "check_dd_2730.cpp"
#pragma GCC diagnostic pop
#undef CHECK_DD_2730_NO_MAIN

namespace {

constexpr int M3_15 = 15;
constexpr int D3_15 = 24;
constexpr std::array<Shape5, 3> SHAPES_15{{
    {1, 4, 6, 1},
    {4, 1, 1, 5},
    {4, 1, 1, 6},
}};

int maximum_valuation_below128_15(u128 bound, u64 prime) {
    int exponent = 0;
    u128 power = 1;
    while (power * prime < bound) {
        power *= prime;
        ++exponent;
    }
    return exponent;
}

bool value_in_interval15(int value, int lower, int upper) {
    return lower <= value && value <= upper;
}

bool condition_intersects_box15(
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
    return value_in_interval15(condition.resonance, n_lower, n_upper) ||
           value_in_interval15(
               condition.plus_gap,
               n_lower - a_upper,
               n_upper - a_lower
           ) ||
           value_in_interval15(condition.minus_a, a_lower, a_upper);
}

u128 gcd128_15(u128 left, u128 right) {
    while (right != 0) {
        const u128 remainder = left % right;
        left = right;
        right = remainder;
    }
    return left;
}

bool same_shape15(const Shape5& left, const Shape5& right) {
    return left.m1 == right.m1 && left.m2 == right.m2 &&
           left.n1 == right.n1 && left.n2 == right.n2;
}

std::string shape_name15(const Shape5& shape) {
    return "(" + std::to_string(shape.m1) + "," +
           std::to_string(shape.m2) + ";" +
           std::to_string(shape.n1) + "," +
           std::to_string(shape.n2) + ")";
}

u128 numerator_bound15(const Shape5& shape) {
    return pow_u128(10, shape.n1 + shape.n2);
}

u128 norm_bound15(const Shape5& shape) {
    return pow_u128(10, 2 * (shape.n1 + shape.m2)) +
           pow_u128(10, 2 * (shape.n2 + shape.m1));
}

u128 f_minus_upper15(const Shape5& shape) {
    const int s1 = shape.n1 - shape.m1;
    const int s2 = shape.n2 - shape.m2;
    const int exponent = 2 * S5 + s1 + s2 + std::abs(s1 - s2) +
                         2 * M3_15 - N3_5 + 4;
    if (exponent < 0) throw std::logic_error("negative F_- exponent");
    return u128(2) * pow_u128(10, exponent);
}

bool signature_fits_height_box15(
    const Shape5& shape,
    const Signature& signature
) {
    const u128 a_bound = numerator_bound15(shape);
    const u128 n_bound = norm_bound15(shape);
    const int max_a_2 = maximum_valuation_below128_15(a_bound, 2);
    const int max_a_5 = maximum_valuation_below128_15(a_bound, 5);
    const int max_n_2 = maximum_valuation_below128_15(n_bound, 2);
    const int max_n_5 = maximum_valuation_below128_15(n_bound, 5);
    return condition_intersects_box15(signature.two, 0, max_n_2, 0, max_a_2) &&
           condition_intersects_box15(signature.five, 0, max_n_5, 0, max_a_5);
}

bool corner_gap_possible15(const Shape5& shape, u64 b1, u64 b2) {
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
            const u128 left = pow_u128(10, D3_15) * u128(A);
            const u128 right = u128(40) * Q * Q * N;
            if (left < right) return true;
        }
    }
    return false;
}

bool large_divisor_fits15(const Shape5& shape, const Tail& tail) {
    const u128 numerator = u128(tail.kappa) * (tail.kappa + 2 * tail.G);
    const u128 primitive = numerator /
        gcd128_15(numerator, u128(tail.kappa) + tail.G);
    const u128 large_divisor = primitive / gcd128_15(primitive, tail.Q);
    return large_divisor < f_minus_upper15(shape);
}

bool denominator_unit_possible15(
    const Shape5& shape,
    const PCondition& condition,
    u64 prime,
    u64 b1,
    u64 b2
) {
    const int e1 = valuation(b1, prime);
    const int e2 = valuation(b2, prime);
    if (e1 == 0 && e2 == 0) return true;

    const int max_a = maximum_valuation_below128_15(
        numerator_bound15(shape), prime
    );
    const int max_n = maximum_valuation_below128_15(norm_bound15(shape), prime);
    int n_lower = 0;
    int n_upper = 0;
    int a_lower = 0;
    int a_upper = 0;

    if (e1 > 0 && e2 == 0) {
        a_upper = max_a;
    } else if (e1 == 0 && e2 > 0) {
        // Both N and A are units because a_2 is a denominator unit.
    } else if (e1 != e2) {
        n_lower = n_upper = 2 * std::min(e1, e2);
    } else if (prime == 2) {
        n_lower = n_upper = 2 * e1 + 1;
    } else {
        n_lower = 2 * e1;
        n_upper = max_n;
    }
    return condition_intersects_box15(
        condition, n_lower, n_upper, a_lower, a_upper
    );
}

struct FilterCounts15 {
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

    FilterCounts15& operator+=(const FilterCounts15& other) {
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

struct Result15 {
    FilterCounts15 filters;
    Counts prefixes;
};

Result15 check_shape15(
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
    Result15 result;
    if (thread_count > 0) omp_set_num_threads(thread_count);
#pragma omp parallel
    {
        FilterCounts15 local_filters;
        Counts local_prefixes;
        CandidateMarker marker(900000);
#pragma omp for schedule(dynamic, 1)
        for (std::int64_t raw_index = 0;
             raw_index < static_cast<std::int64_t>(jobs.size());
             ++raw_index) {
            const DenominatorJob& job = jobs[static_cast<std::size_t>(raw_index)];
            TailGroups groups = build_tail_groups_s5(
                shape.m1, shape.m2, job.b1, job.b2, M3_15
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
            if (!corner_gap_possible15(shape, job.b1, job.b2)) continue;
            local_filters.corner_rows += eligible;

            std::map<Signature, std::vector<Tail>> survivors;
            for (const auto& [signature, tails] : groups.groups) {
                if (!signature_fits_height_box15(shape, signature)) continue;
                local_filters.valuation_box_rows += tails.size();
                for (const Tail& tail : tails) {
                    if (!large_divisor_fits15(shape, tail)) continue;
                    ++local_filters.large_divisor_rows;
                    if (!denominator_unit_possible15(
                            shape, signature.two, 2, job.b1, job.b2)) continue;
                    ++local_filters.two_unit_rows;
                    if (!denominator_unit_possible15(
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
                    M3_15,
                    survivors,
                    marker,
                    local_prefixes
                );
            }
            const std::size_t done = ++completed;
            if (progress && done % 5000 == 0) {
#pragma omp critical(m15_progress)
                std::cerr << "  m_3=15 shape " << shape_name15(shape)
                          << ": checked " << done << "/" << jobs.size()
                          << " denominator jobs\n";
            }
        }
#pragma omp critical(m15_merge)
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

void check_digit_kernel15() {
    int coarse = 0;
    int killed = 0;
    const std::vector<Shape5> actual = digit_shapes_s5(
        M3_15, &coarse, &killed
    );
    if (coarse != 4 || killed != 1 || actual.size() != SHAPES_15.size()) {
        throw std::logic_error("m_3=15 digit-kernel count mismatch");
    }
    for (std::size_t index = 0; index < SHAPES_15.size(); ++index) {
        if (!same_shape15(actual[index], SHAPES_15[index])) {
            throw std::logic_error("m_3=15 digit-kernel shape mismatch");
        }
    }
    std::cout << "m_3=15 digit kernel: coarse=4, size-killed=1, surviving=3\n";
}

void check_unit_filter_samples15() {
    std::mt19937_64 random(2732001);
    for (const Shape5& shape : SHAPES_15) {
        const auto [a1_lower, a1_upper] = digit_interval(shape.n1);
        const auto [a2_lower, a2_upper] = digit_interval(shape.n2);
        const auto [b1_lower, b1_upper] = digit_interval(shape.m1);
        const auto [b2_lower, b2_upper] = digit_interval(shape.m2);
        for (u64 prime : {2ULL, 5ULL}) {
            for (int trial = 0; trial < 4000; ++trial) {
                const u64 b1 = b1_lower + random() % (b1_upper - b1_lower + 1);
                const u64 b2 = b2_lower + random() % (b2_upper - b2_lower + 1);
                u64 a1 = a1_lower + random() % (a1_upper - a1_lower + 1);
                u64 a2 = a2_lower + random() % (a2_upper - a2_lower + 1);
                if (std::gcd(a1, b1) != 1 || std::gcd(a2, b2) != 1) continue;
                const u64 A = a1 * pow_u64(10, shape.n2) + a2;
                const u128 x = u128(a1) * b2;
                const u128 y = u128(a2) * b1;
                const u128 N = x * x + y * y;
                const int n = valuation128(N, prime);
                const int a = valuation(A, prime);
                PCondition condition;
                const u64 mode = random() % 4;
                if (mode == 0) {
                    condition = {PConditionKind::AtLeast, 0, 0, 0, n};
                } else if (mode == 1) {
                    condition = {PConditionKind::Disjunction, n, -100, -100, 0};
                } else if (mode == 2) {
                    condition = {PConditionKind::Disjunction, -100, n - a, -100, 0};
                } else {
                    condition = {PConditionKind::Disjunction, -100, -100, a, 0};
                }
                if (!p_condition_accepts(condition, n, a) ||
                    !denominator_unit_possible15(
                        shape, condition, prime, b1, b2)) {
                    throw std::logic_error(
                        "m_3=15 denominator-unit sample implication failed"
                    );
                }
            }
        }
    }
    std::cout << "m_3=15 denominator-unit sampled implications: OK\n";
}

void print_result15(const Shape5& shape, const Result15& result) {
    const FilterCounts15& f = result.filters;
    const Counts& c = result.prefixes;
    std::cout << "m_3=15 shape " << shape_name15(shape)
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

struct Options15 {
    int threads = 0;
    bool progress = false;
    bool self_check = false;
    bool expect_baseline = false;
};

Options15 parse_options15(int argc, char** argv) {
    Options15 options;
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
            std::cout << "usage: check_dd_2732_cpp [--threads N] [--progress] "
                         "[--self-check] [--expect-baseline]\n";
            std::exit(0);
        } else {
            throw std::invalid_argument("unknown option: " + option);
        }
    }
    if (options.threads < 0) throw std::invalid_argument("negative threads");
    return options;
}

void expect_shape_baseline15(
    std::size_t index,
    const Result15& result
) {
    struct Expected15 {
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
    constexpr std::array<Expected15, 3> expected{{
        {4143226, 3970657, 1294195, 1284602, 145896, 15971, 1404,
         80983, 224, 4064152, 28860, 50214,
         1814400000, 1055554100, 332164802, 18036040, 4270550, 4270550},
        {4037587, 3858105, 967130, 700622, 3977, 436, 17,
         80979, 12, 3950433, 26234, 60920,
         9720000, 4689000, 167566, 0, 0, 0},
        {4037587, 3858105, 2808958, 2728920, 259926, 34418, 5499,
         80979, 1035, 3950433, 26234, 60920,
         8383500000, 4589789640, 1571805173, 16890624, 3861540, 3861540},
    }};
    if (index >= expected.size()) {
        throw std::logic_error("m_3=15 baseline index out of range");
    }
    const Expected15& e = expected[index];
    const FilterCounts15& f = result.filters;
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
            "m_3=15 structural baseline mismatch for shape " +
            shape_name15(SHAPES_15[index])
        );
    }
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options15 options = parse_options15(argc, argv);
        if (options.self_check) {
            self_check();
            self_check_s5();
            check_digit_kernel15();
            check_unit_filter_samples15();
        }
        if (options.expect_baseline && !options.self_check) check_digit_kernel15();

        u64 square_discriminants = 0;
        for (std::size_t index = 0; index < SHAPES_15.size(); ++index) {
            const Result15 result = check_shape15(
                SHAPES_15[index], options.threads, options.progress
            );
            print_result15(SHAPES_15[index], result);
            if (options.expect_baseline) expect_shape_baseline15(index, result);
            square_discriminants += result.prefixes.square_discriminants;
        }
        if (square_discriminants != 0) {
            throw std::logic_error("m_3=15 square discriminant found");
        }
        std::cout << "DD S=5, m_3=15 finite certificate: OK\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 1;
    }
}
