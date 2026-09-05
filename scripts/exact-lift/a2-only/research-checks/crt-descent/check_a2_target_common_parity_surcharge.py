#!/usr/bin/env python3
"""Certificate for target-common-parity-surcharge.md.

This checker verifies the elementary congruence/parity component of the
surcharge theorem.  The structural inputs are canonical proved facts:

* a genuine equal-depth target has v_p(W_q)=v_p(P)=h;
* W_q^prim := W_q/3^delta is 1 mod 4 and is not divisible by 3;
* target/descent common support is squarefree and contained in {31,179}.

The new observation is the odd/even h dichotomy: odd h forces another inert
prime in W_q^prim, while even h leaves P/(5 p^h) = 3 mod 4 and hence forces
another inert prefix prime.
"""


def P(K: int) -> int:
    return 6 * K * K - 36 * K + 55


# K=10*r with r odd.  P/5 is always 11 mod 24, and P is 1 mod 3.
for r in range(1, 2 * 24 + 1, 2):
    K = 10 * r
    value = P(K)
    assert value % 5 == 0
    assert (value // 5) % 24 == 11
    assert value % 3 == 1

# The two fixed target/descent labels are inert and their product is neutral.
assert 31 % 4 == 3
assert 179 % 4 == 3
assert (31 * 179) % 4 == 1

# If exactly one fixed target label p supplies the target/descent common parity,
# every baseline depth h has a complementary parity source.
for p in (31, 179):
    for h in range(1, 40):
        if h % 2:
            # W_q^prim == 1 mod4.  Removing the exact p^h contribution
            # leaves 3 mod4, so the remaining factor must carry odd inert parity.
            residual_w_mod4 = (1 * pow(pow(p, h, 4), -1, 4)) % 4
            assert residual_w_mod4 == 3
        else:
            # P/5 == 11 mod24, hence 3 mod4.  Exact p^h is 1 mod4,
            # so P/(5 p^h) remains 3 mod4.  Also 3 cannot divide it because
            # P itself is 1 mod3.
            residual_p_mod4 = (3 * pow(pow(p, h, 4), -1, 4)) % 4
            assert residual_p_mod4 == 3

print("OK: a lone fixed 31/179 target-common label always forces an additional non-3 inert supplier")
