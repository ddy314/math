// A2-F02: complete fixed-tail labels, without an exponent cutoff.
// All unreduced polynomial arithmetic uses signed __int128 (< 2^100 under
// the explicit bounds). Residue arithmetic is reduced before products.
// The Python reader independently checks all stage-one residuals.

#include "periodic_recovery.hpp"

struct Counts {
  Long tags = 0, geometry = 0, integral = 0, single = 0, joint = 0,
       residual = 0, refined = 0, binary = 0;
};
int main(int argc, char **argv) {
  bool stage_one = false, expanded = false;
  std::string selection = "all";
  for (int i = 1; i < argc; ++i) {
    const std::string argument = argv[i];
    if (argument == "--stage-one")
      stage_one = true;
    else if (argument == "--expanded")
      expanded = true;
    else if (argument == "--odd")
      selection = "odd";
    else if (argument == "--even")
      selection = "even";
    else
      return 2;
  }
  for (int i = 2; i <= 100000; ++i)
    if (!spf[i]) {
      for (int j = i; j <= 100000; j += i)
        if (!spf[j])
          spf[j] = i;
    }
  for (int p = 3; p <= 397; ++p)
    if (p != 5 && spf[p] == p) {
      primes.push_back(p);
      powers[p] = orbit(p);
      squares[p] = std::vector<bool>(p);
      for (int n = 0; n < p; ++n)
        squares[p][n * n % p] = true;
    }
  audit_group_kernel();
  for (int group = 0; group < 3; ++group) {
    if ((selection == "odd" && group != 0) ||
        (selection == "even" && group == 0))
      continue;
    const int B = group == 2 ? 2 : 1;
    std::vector<int> tails;
    if (group == 0)
      for (int b = 51; b < 100; b += 2)
        tails.push_back(b);
    else if (group == 1)
      for (int b = 54; b < 100; b += 4)
        tails.push_back(b);
    else
      tails = {84, 92};
    Counts count;
    for (int b : tails) {
      int nondecimal = b;
      while (nondecimal % 2 == 0)
        nondecimal /= 2;
      while (nondecimal % 5 == 0)
        nondecimal /= 5;
      const int J = valuation(b, 5);
      std::unordered_map<int, Gate> integral_cache;
      for (int c = 1; c <= b; ++c) {
        if (b % c || (J && valuation(c, 5) >= J))
          continue;
        if ((group == 1 && c % 2 == 0) || (group == 2 && valuation(c, 2) != 1))
          continue;
        const int increment = group == 0 ? 2 : group == 1 ? 4 : 8;
        const int offset = group == 0 ? 1 : group == 1 ? 2 : 4;
        for (int k = B * U * c + offset; k < (100 * B + 1) * U * c / 10;
             k += increment) {
          if (valuation(k, 5) != J || std::gcd(k, nondecimal) != 1)
            continue;
          auto found = integral_cache.find(k);
          if (found == integral_cache.end())
            found = integral_cache.emplace(k, integral_gate(B, b, k)).first;
          const std::vector<int> firsts =
              group == 0   ? std::vector<int>{2, 4, 6, 8}
              : group == 1 ? std::vector<int>{1, 2, 3, 4, 5, 6, 7, 8}
                           : std::vector<int>{5, 7, 9, 11, 13};
          for (int A : firsts)
            for (int a = 100; a < 2 * b; ++a) {
              if (std::gcd(a, b) != 1)
                continue;
              if (group == 0 && valuation(a, 2) != (A == 4   ? 1
                                                    : A == 8 ? 2
                                                             : 0))
                continue;
              if (group != 0 && a % 2 == 0)
                continue;
              if (group == 2 && 5 * a >= 6 * b)
                continue;
              const Tag tag{A, B, a, b, c, k};
              ++count.tags;
              if (geometry_empty(tag)) {
                ++count.geometry;
                continue;
              }
              if (found->second.allowed.empty()) {
                ++count.integral;
                continue;
              }
              const int reason =
                  periodic_reason(tag, found->second, 241, false, expanded);
              if (reason == 1) {
                ++count.single;
                continue;
              }
              if (reason == 2) {
                ++count.joint;
                continue;
              }
              ++count.residual;
              if (stage_one) {
                std::cout << "RESIDUAL " << B << ' ' << A << ' ' << b << ' '
                          << a << ' ' << c << ' ' << k << '\n';
              } else if (periodic_reason(tag, found->second, 397, true,
                                         expanded)) {
                ++count.refined;
              } else if (binary_fallback(tag)) {
                ++count.binary;
                std::cout << "BINARY " << B << ' ' << A << ' ' << b << ' ' << a
                          << ' ' << c << ' ' << k << '\n';
              } else {
                std::cerr << "uncovered tag " << B << ' ' << A << ' ' << b
                          << ' ' << a << ' ' << c << ' ' << k << '\n';
                return 1;
              }
            }
        }
      }
    }
    const std::array<Long, 3> expected{33683610, 13541128, 207750};
    assert(count.tags == expected[group]);
    assert(count.geometry + count.integral + count.single + count.joint +
               count.residual ==
           count.tags);
    assert(stage_one || count.refined + count.binary == count.residual);
    std::cout << "SUMMARY " << group << ' ' << count.tags << ' '
              << count.geometry << ' ' << count.integral << ' ' << count.single
              << ' ' << count.joint << ' ' << count.residual << ' '
              << count.refined << ' ' << count.binary << '\n';
    std::cerr << "completed periodic group " << group << ": " << count.tags
              << " labels\n";
  }
  std::cout << (stage_one ? "STAGE_ONE" : "PASS_PERIODIC")
            << " arbitrary m2>=2; no exponent cutoff\n";
}
