// A2-F08: all coprime-denominator odd three-digit tails, arbitrary m2.
// c=1,k<10100,a<2000,b<1000,A<=8; signed 128-bit intermediates <2^100.
#define A2_TAIL_U 1000
#define A2_MAX_KEY 11000
#include "periodic_recovery.hpp"
int main(int argc, char **argv) {
  bool expanded = argc > 1 && std::string(argv[1]) == "--expanded";
  const int maximum = 11000;
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
  Long tags = 0, geo = 0, integer = 0, periodic = 0, residual = 0;
  for (int b = 501; b < 1000; b += 2) {
    if (b % 5 == 0)
      continue;
    std::map<int, std::vector<int>> tails;
    for (int A : {4, 8})
      for (int a = 1000; a < 2 * b; ++a)
        if (std::gcd(a, b) == 1 && (A == 4 ? a % 2 == 1 : a % 4 != 0))
          tails[A].push_back(a);
    std::unordered_map<int, Gate> integral_cache;
    const int c = 1, b0 = b;
    int initial = U * c + 1;
    initial += ((-c * U - initial) % b0 + b0) % b0;
    if (initial % 2 == 0)
      initial += b0;
    for (int k = initial; k * 10 < 101 * U * c; k += 2 * b0) {
      if (std::gcd(k, 10 * b) != 1)
        continue;
      for (int A : {4, 8}) {
        const auto &values = tails[A];
        tags += values.size();
        // The proven geometry condition is a strict upper bound on a^2.
        auto stop =
            std::partition_point(values.begin(), values.end(), [&](int a) {
              return !geometry_empty({A, 1, a, b, c, k});
            });
        Long admitted = stop - values.begin();
        geo += values.size() - admitted;
        if (admitted == 0)
          continue;
        auto found = integral_cache.find(k);
        if (found == integral_cache.end())
          found = integral_cache.emplace(k, integral_gate(1, b, k)).first;
        if (found->second.allowed.empty()) {
          integer += admitted;
          continue;
        }
        for (auto it = values.begin(); it != stop; ++it) {
          Tag tag{A, 1, *it, b, c, k};
          if (periodic_reason(tag, found->second, 397, true, expanded)) {
            ++periodic;
            continue;
          }
          ++residual;
          std::cout << "RESIDUAL 1 " << A << ' ' << b << ' ' << *it << ' ' << c
                    << ' ' << k << std::endl;
        }
      }
    }
  }
  assert(tags == 476207LL);
  assert(geo + integer + periodic + residual == tags);
  std::cout << "SUMMARY 1 " << tags << ' ' << geo << ' ' << integer << ' '
            << periodic << ' ' << residual << "\n";
}
