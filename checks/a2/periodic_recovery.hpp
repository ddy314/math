// Shared exact periodic-recovery kernel for A2-F02/F04.
// Callers declare their finite bounds and signed 128-bit width in PROOF.md.
// This file is registered as a hashed dependency of every using check.
#pragma once
#ifndef A2_TAIL_U
#define A2_TAIL_U 100
#endif
#ifndef A2_MAX_KEY
#define A2_MAX_KEY 100000
#endif

#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>

using Wide = __int128_t;
using Long = long long;
struct Tag {
  int A, B, a, b, c, k;
};
struct Gate {
  int period;
  std::vector<int> allowed;
};
constexpr int U = A2_TAIL_U;
std::vector<int> spf(A2_MAX_KEY + 1);
std::vector<int> primes;
std::map<int, std::vector<int>> powers;
std::map<int, std::vector<bool>> squares;

int valuation(int n, int p) {
  int depth = 0;
  while (n % p == 0) {
    n /= p;
    ++depth;
  }
  return depth;
}
Long modpower(Long a, int n, int modulus) {
  Long result = 1 % modulus;
  while (n) {
    if (n & 1)
      result = result * a % modulus;
    a = a * a % modulus;
    n >>= 1;
  }
  return result;
}
Long inverse(Long a, int modulus) {
  Long b = modulus, x = 1, y = 0;
  while (b) {
    const Long quotient = a / b;
    const Long next = a - quotient * b;
    a = b;
    b = next;
    const Long coefficient = x - quotient * y;
    x = y;
    y = coefficient;
  }
  assert(a == 1);
  return (x % modulus + modulus) % modulus;
}
int order10(int modulus) {
  if (modulus == 1)
    return 1;
  int phi = modulus, value = modulus;
  while (value > 1) {
    const int p = spf[value];
    phi = phi / p * (p - 1);
    while (value % p == 0)
      value /= p;
  }
  int order = phi;
  value = phi;
  while (value > 1) {
    const int p = spf[value];
    while (order % p == 0 && modpower(10, order / p, modulus) == 1)
      order /= p;
    while (value % p == 0)
      value /= p;
  }
  assert(modpower(10, order, modulus) == 1);
  return order;
}
Gate integral_gate(int B, int b, int k) {
  // The 2/5 part is already paid by c(BUT+b), by the proved tag shapes.
  int modulus = k;
  while (modulus % 2 == 0)
    modulus /= 2;
  while (modulus % 5 == 0)
    modulus /= 5;
  if (modulus == 1)
    return {1, {0}};
  const int order = order10(modulus);
  const Long target =
      (modulus - Long(b) * inverse(B * U * 100 % modulus, modulus) % modulus) %
      modulus;
  int step = 1;
  while (step * step < order)
    ++step;
  std::unordered_map<int, int> baby;
  Long value = 1;
  for (int j = 0; j < step; ++j) {
    baby.emplace(static_cast<int>(value), j);
    value = value * 10 % modulus;
  }
  const Long factor = inverse(modpower(10, step, modulus), modulus);
  Long giant = target;
  for (int i = 0; i <= step; ++i) {
    const auto found = baby.find(static_cast<int>(giant));
    if (found != baby.end()) {
      const int n = i * step + found->second;
      if (n < order) {
        assert(modpower(10, n, modulus) == target);
        return {order, {n}};
      }
    }
    giant = giant * factor % modulus;
  }
  return {order, {}};
}
std::vector<int> orbit(int modulus) {
  const int first = 100 % modulus;
  std::vector<int> result{first};
  int value = first * 10 % modulus;
  while (value != first) {
    result.push_back(value);
    value = value * 10 % modulus;
  }
  return result;
}
bool propagate(std::vector<Gate> gates) {
  bool changed = true;
  while (changed) {
    changed = false;
    for (auto &current : gates)
      for (const auto &other : gates) {
        const int common = std::gcd(current.period, other.period);
        std::vector<bool> possible(common);
        for (int r : other.allowed)
          possible[r % common] = true;
        const auto before = current.allowed.size();
        std::erase_if(current.allowed,
                      [&](int r) { return !possible[r % common]; });
        if (current.allowed.empty())
          return true;
        changed |= current.allowed.size() != before;
      }
  }
  return false;
}
bool geometry_empty(const Tag &t) {
  const int A = t.A, B = t.B, a = t.a, b = t.b, c = t.c, k = t.k;
  if (B == 2) {
    if (A == 5)
      return 8 * a * a >= 9 * b * b;
    if (A == 7)
      return 3 * a * a >= 4 * b * b;
    return Wide(a) * a * 1764 >=
           Wide(b) * b * (400 * (A + 1) * (A + 1) - 441 * A * A - 1764);
  }
  const bool decreasing =
      A >= 3 || (A == 2 && 3 * k <= 25 * U * c) || (A == 1 && k <= 5 * U * c);
  if (!decreasing)
    return A == 2 ? 2 * a * a >= 5 * b * b : 5 * a * a >= 8 * b * b;
  if (k >= 10 * U * c)
    return Wide(a) * a * 121 >= Wide(b) * b * (-21 * A * A + 200 * A - 21);
  const Wide scale = Wide(100) * c * c * U * U;
  const Wide prefix = Wide(k + c * U) * (k + c * U);
  const Wide denominator = scale * prefix;
  const Wide numerator = scale * (A + 1) * (A + 1) * k * k -
                         (Wide(A) * A * scale + Wide(k) * k) * prefix;
  return Wide(a) * a * denominator >= Wide(b) * b * numerator;
}
int residue(Wide value, int modulus) {
  const int r = static_cast<int>(value % modulus);
  return r < 0 ? r + modulus : r;
}
int periodic_reason(const Tag &t, const Gate &integral, int maximum,
                    bool coprime, bool expanded) {
  std::vector<Gate> gates{integral};
  const Wide h = Wide(t.k + t.c * U) * (t.k + t.c * U) -
                 Wide(10 * t.c * U) * (10 * t.c * U);
  const Wide C = t.A * t.A * t.b * t.b + t.B * t.B * t.a * t.a;
  const Wide p2 =
      Wide(U) * U *
      (Wide(t.k) * t.k * t.B * t.B * t.b * t.b * t.A * t.A - h * C * t.B * t.B);
  const Wide p1 =
      2 * U *
      (Wide(t.k) * t.k * t.B * t.B * t.b * t.b * t.A * t.a - h * C * t.B * t.b);
  const Wide p0 =
      Wide(t.k) * t.k * t.B * t.B * t.b * t.b * t.a * t.a - h * C * t.b * t.b;
  for (int p : primes) {
    if (p > maximum)
      break;
    const Long km = t.k % p, cm = t.c % p, um = U % p, bm = t.b % p,
               am = t.a % p;
    const Long lambda = (km + cm * um) % p, u = 10 * cm * um % p;
    const Long hm = (lambda * lambda - u * u) % p;
    const Long cc = (t.A * t.A * bm * bm + t.B * t.B * am * am) % p;
    const Long hc = hm * cc % p, kb = t.B * t.B * km * km % p * bm * bm % p;
    const bool primitive = coprime && (t.B * t.a - t.A * t.b) % p == 0 &&
                           hm != 0 && km != 0 && bm != 0;
    const auto &values = powers[p];
    Gate gate{static_cast<int>(values.size()), {}};
    for (int i = 0; i < gate.period; ++i) {
      const Long T = values[i], L = (t.A * um * T + am) % p,
                 s = (t.B * um * T + bm) % p;
      const int value = expanded ? residue((p2 * T + p1) * T + p0, p)
                                 : residue(kb * L * L - hc * s * s, p);
      if (squares[p][value] && !(primitive && s == 0))
        gate.allowed.push_back(i);
    }
    if (gate.allowed.empty())
      return 1;
    gates.push_back(std::move(gate));
  }
  return propagate(std::move(gates)) ? 2 : 0;
}
Wide wide_gcd(Wide a, Wide b) {
  if (a < 0)
    a = -a;
  if (b < 0)
    b = -b;
  while (b) {
    const Wide next = a % b;
    a = b;
    b = next;
  }
  return a;
}
bool binary_fallback(const Tag &t) {
  // N^2, NT, N, T^2, T, 1: clear original recovery and remove its content.
  const Wide A = t.A, B = t.B, a = t.a, b = t.b, c = t.c, k = t.k;
  const Wide lambda = k + c * U, h = lambda * lambda - 100 * c * c * U * U;
  const Wide C = A * A * b * b + B * B * a * a;
  std::array<Wide, 6> coefficients{
      B * B * k * k * b * b * h,
      -20 * k * k * b * b * c * c * B * B * A * U * U,
      -20 * k * k * b * b * c * c * B * B * U * a,
      c * c * B * B * U * U * (lambda * lambda * C - k * k * b * b * A * A),
      2 * lambda * lambda * C * c * c * B * U * b -
          2 * k * k * b * b * c * c * B * B * A * U * a,
      lambda * lambda * C * c * c * b * b -
          k * k * b * b * c * c * B * B * a * a};
  Wide content = 0;
  for (Wide coefficient : coefficients)
    content = wide_gcd(content, coefficient);
  assert(content != 0);
  for (auto &coefficient : coefficients)
    coefficient /= content;
  Long T = 100;
  for (int m2 = 2; m2 < 6; ++m2, T *= 10) {
    if (Long(t.c) * (t.B * U * T + t.b) % t.k == 0)
      return false;
  }
  // For m2 >= 6, T is zero modulo 64. No numerator residue may survive.
  for (int n = 0; n < 64; ++n) {
    if (residue(coefficients[0] * n * n + coefficients[2] * n + coefficients[5],
                64) == 0)
      return false;
  }
  return true;
}
void audit_group_kernel() {
  // Independent direct cyclic orbit vs baby-step/giant-step, all targets
  // on every unit modulus <= 500. This is a kernel audit, not a cutoff.
  for (int m = 1; m <= 500; ++m) {
    if (std::gcd(m, 10) != 1)
      continue;
    const auto values = orbit(m);
    assert(static_cast<int>(values.size()) == order10(m));
    for (int b = 1; b <= m; ++b) {
      if (std::gcd(b, m) != 1)
        continue;
      const auto gate = integral_gate(1, b, m);
      int actual = -1;
      for (int i = 0; i < static_cast<int>(values.size()); ++i) {
        if ((U * values[i] + b) % m == 0)
          actual = i;
      }
      assert(gate.allowed.empty() == (actual == -1));
      if (actual >= 0)
        assert(gate.allowed[0] == actual);
    }
  }
}
