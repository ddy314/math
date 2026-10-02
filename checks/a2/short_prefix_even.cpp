// Exact bounded original A2 quadratics. cpp_int uses arbitrary precision.
// The Python driver proves/enumerates the denominator bounds and checks row
// counts. Q(a) differs from the original discriminant by the square
// (2*beta*b2)^2. Composite/prime square filters are necessary only; all
// survivors use exact sqrt.
#include <array>
#include <boost/multiprecision/cpp_int.hpp>
#include <cassert>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using Big = boost::multiprecision::cpp_int;
using Long = unsigned long long;
int rem(const Big &n, int p) {
  int r = (n % p).convert_to<int>();
  return r < 0 ? r + p : r;
}
int main(int argc, char **argv) {
  assert(argc == 2);
  std::ifstream in(argv[1]);
  assert(in);
  int A, B, b, U, upper, prefix;
  Long T, M, expected, rows = 0, pre = 0, squares = 0, active = 0;
  while (in >> A >> B >> T >> M >> b >> U >> upper >> prefix >> expected) {
    ++active;
    Big beta = (Big(B) * T + M) * U + b, prod = Big(B) * M * b, D = prod * prod;
    Big c2 = beta * beta * B * B * b * b - Big(10) * U * 10 * U * D;
    assert(c2 != 0);
    Big base = Big(A) * T * U, b4 = Big(B) * B * B * B * b * b * b * b;
    Big q2 = b4 - c2 * B * B, q1 = 2 * b4 * base,
        q0 = b4 * base * base - c2 * A * A * b * b;
    std::array<int, 8> moduli{64, 63, 11, 13, 17, 19, 23, 31};
    std::vector<std::vector<bool>> good;
    for (int p : moduli) {
      int r2 = rem(q2, p), r1 = rem(q1, p), r0 = rem(q0, p);
      std::vector<bool> s(p), allowed(p);
      for (int n = 0; n < p; ++n)
        s[n * n % p] = true;
      for (int n = 0; n < p; ++n)
        allowed[n] = s[((r2 * n + r1) * n + r0) % p];
      good.push_back(allowed);
    }
    Long local = 0;
    for (int a = U + 1; a <= upper; a += 2) {
      if (std::gcd(a, b) != 1)
        continue;
      ++local;
      bool possible = true;
      for (int i = 0; i < 8; ++i)
        if (!good[i][a % moduli[i]]) {
          possible = false;
          break;
        }
      if (!possible)
        continue;
      Big Q = (q2 * a + q1) * a + q0;
      if (Q < 0)
        continue;
      Big root = sqrt(Q);
      if (root * root != Q)
        continue;
      ++squares;
      Big L = base + a, c1 = -2 * L * 10 * U * D, den = 2 * c2;
      std::cout << "SQUARE " << A << ' ' << B << ' ' << T << ' ' << M << ' '
                << a << ' ' << b;
      for (int sign : {-1, 1}) {
        Big num = -c1 + sign * 2 * beta * M * root;
        std::cout << ' ' << num << '/' << den;
        if (num % den == 0) {
          Big N = num / den;
          if (N >= T / 100 && N < T / 10 &&
              std::gcd(N.convert_to<Long>(), M) == 1) {
            std::cerr << "LEGAL ROOT\n";
            return 1;
          }
        }
      }
      std::cout << '\n';
    }
    assert(local == expected);
    rows += local;
    pre += prefix * local;
  }
  std::cout << "SUMMARY " << active << ' ' << rows << ' ' << pre << ' '
            << rows - pre << ' ' << squares << " legal=0\n";
}
