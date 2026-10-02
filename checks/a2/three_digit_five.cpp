// A2-F04/F07 periodic parts: complete m3=3 labels with v5(b2)>0.
// Explicit bounds: U=1000,A<=13,B<=2,b<1000,a<2000,c<200,k<2010000.
// All signed 128-bit intermediates are <2^124; no exponent cutoff.
#define A2_TAIL_U 1000
#define A2_MAX_KEY 2200000
#include "periodic_recovery.hpp"

int main(int argc, char **argv) {
  bool stage_one = false, expanded = false, tail_unit_prefix = false;
  for (int i = 1; i < argc; ++i) {
    const std::string argument = argv[i];
    if (argument == "--stage-one")
      stage_one = true;
    else if (argument == "--expanded")
      expanded = true;
    else if (argument == "--tail-five-unit-prefix")
      tail_unit_prefix = true;
    else
      return 2;
  }
  const int maximum = 2200000;
  for (int i = 2; i <= maximum; ++i)
    if (!spf[i])
      for (int j = i; j <= maximum; j += i)
        if (!spf[j])
          spf[j] = i;
  for (int p = 3; p <= 601; ++p)
    if (p != 5 && spf[p] == p) {
      primes.push_back(p);
      powers[p] = orbit(p);
      squares[p] = std::vector<bool>(p);
      for (int n = 0; n < p; ++n)
        squares[p][n * n % p] = true;
    }
  audit_group_kernel();
  for (int B : {1, 2}) {
    Long tags = 0, geo = 0, integer = 0, periodic = 0, residual = 0,
         refined = 0;
    for (int b = 501; b < 1000; ++b) {
      if (B == 2 && (b % 2 || 6 * b <= 5000))
        continue;
      int J = valuation(b, 5);
      if (tail_unit_prefix ? (J != 1 && J != 3) : J < 2)
        continue;
      int g = valuation(b, 2), nondecimal = b;
      while (nondecimal % 2 == 0)
        nondecimal /= 2;
      while (nondecimal % 5 == 0)
        nondecimal /= 5;
      std::unordered_map<int, Gate> integral_cache;
      for (int c = 1; c <= b; ++c) {
        if (b % c)
          continue;
        int F = valuation(c, 5);
        if (tail_unit_prefix ? F != 0 : (F == 0 || F >= J))
          continue;
        int f = valuation(c, 2);
        if (b % 2 == 0) {
          if (B == 1 &&
              !((f == 0 && (g == 1 || g == 2)) || (f > 0 && g == f + 2)))
            continue;
          if (B == 2 && !((f == 1 && (g == 2 || g == 3)) ||
                          (tail_unit_prefix && f > 1 && g == f + 2)))
            continue;
        }
        // J-F=2 only has the finite prefix m2<=F; handled separately.
        if (J - F != 1 && J - F != 3)
          continue;
        const int increment =
            (1 << g) * static_cast<int>(modpower(5, J, maximum));
        for (int k = (B * U * c / increment + 1) * increment;
             k * 10 < (100 * B + 1) * U * c; k += increment) {
          if (valuation(k, 2) != g || valuation(k, 5) != J ||
              std::gcd(k, nondecimal) != 1)
            continue;
          auto found = integral_cache.find(k);
          if (found == integral_cache.end())
            found = integral_cache.emplace(k, integral_gate(B, b, k)).first;
          for (int A :
               (B == 1 ? (b % 2 ? std::vector<int>{4, 8}
                                : std::vector<int>{1, 2, 3, 4, 5, 6, 7, 8})
                       : std::vector<int>{5, 7, 9, 11, 13}))
            for (int a = 1000; a < 2 * b; ++a) {
              if (std::gcd(a, b) != 1)
                continue;
              if (b % 2 &&
                  (A == 4 ? valuation(a, 2) != 0 : valuation(a, 2) > 1))
                continue;
              if (!(b % 2) && a % 2 == 0)
                continue;
              if (B == 2 && 5 * a >= 6 * b)
                continue;
              const Tag tag{A, B, a, b, c, k};
              ++tags;
              if (geometry_empty(tag)) {
                ++geo;
                continue;
              }
              if (found->second.allowed.empty()) {
                ++integer;
                continue;
              }
              if (periodic_reason(tag, found->second, 397, true, expanded)) {
                ++periodic;
                continue;
              }
              ++residual;
              if (!stage_one) {
                assert(periodic_reason(tag, found->second,
                                       tail_unit_prefix ? 601 : 499, true,
                                       expanded));
                ++refined;
                continue;
              }
              std::cout << "RESIDUAL " << B << ' ' << A << ' ' << b << ' ' << a
                        << ' ' << c << ' ' << k << '\n';
            }
        }
      }
    }
    assert(tags == (tail_unit_prefix ? (B == 1 ? 2966809178LL : 23500070LL)
                                     : (B == 1 ? 119936428LL : 690140LL)));
    assert(geo + integer + periodic + residual == tags);
    assert(stage_one || refined == residual);
    std::cout << "SUMMARY " << B << ' ' << tags << ' ' << geo << ' ' << integer
              << ' ' << periodic << ' ' << residual << ' ' << refined << '\n';
    std::cerr << "completed B=" << B << ", tags=" << tags
              << ", residual=" << residual << ' ' << refined << '\n';
  }
  std::cout
      << (stage_one ? "STAGE_ONE" : "PASS_PERIODIC")
      << " complete three-digit five-positive labels; no exponent cutoff\n";
}
