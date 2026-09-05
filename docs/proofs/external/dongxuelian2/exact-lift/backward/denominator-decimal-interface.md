# Backward denominator-decimal recovery interface (curated import)

Source: master `2cfa389f1d4ced90653101e6c92ee8dfe85b5535`, original `research/exact-lift/backward/backward-denominator-decimal-interface.md`.

Source status: **explicit lossless pairwise interface theorem** between cleaned denominator recovery and decimal completion; it does not close the strict layer.

Let
\[
\Lambda=\operatorname{lcm}(b_1,b_2,b_3),\qquad M_i=10^{m_i},\qquad S=10^\ell,
\]
and let the denominator word be
\[
B=b_1M_2M_3+b_2M_3+b_3.
\]
The source proves that the denominator-decimal shared trace has two equivalent forms:
\[
\boxed{T_{\rm blk}=(b_1,b_2,b_3,S)},
\]
\[
\boxed{T_{\rm word}=(B,M_2,M_3,S)}.
\]
The word form decodes the three denominator blocks uniquely by decimal cuts, while the block form reconstructs the word and cuts from the actual digit lengths. Neither form retains numerator/sphere information.

The third-tail tuple is deterministic from `(b3,S)`:
\[
\eta_3=\gcd(S,b_3),\qquad
\mathcal L=S/\eta_3,\qquad
\tau=b_3/\eta_3.
\]
Similarly, the trace determines
\[
\Lambda,\quad d_i=\Lambda/b_i,\quad
Q=b_1M_2+b_2,\quad G=b_1b_2,
\]
and every denominator-only valuation/gcd/prime-support view.

A particularly useful branch-free identity unifies the old DD and A1 tail-weight formulas:
\[
\boxed{\kappa=\frac{M_3QG}{b_3}}.
\]
Therefore the denominator-tail certificate
\[
\boxed{S\mid\kappa^2(\kappa+2G)}
\]
is a pure predicate of the denominator-decimal trace; it does not require numerator coordinates, a gap root, `C,D,N12`, or a tail numerator.

After removing algebraic/root data that had previously been mixed into the denominator block, the source proves a lossless fibre-product statement: the joint denominator/decimal compatibility set is exactly the fibre product of the two semantic blocks over the common trace. In words, all genuine cross-synchronization between denominator recovery and decimal completion factors through
\[
\boxed{\text{same segmented denominator word} + \text{same effective tail scale}.}
\]

The interface is genuinely proper. The source gives an infinite family of distinct canonical sphere states with the same denominator trace, so this is not merely a repackaging of all canonical data into four other fields. It also supplies explicit canonical collisions showing that dropping any of `B`, `M2`, `M3`, or (uniformly across DD+A1) `S` loses necessary information.

For DD alone, `S=M3`, so the chamber-specific interface reduces further to the denominator triple. For A1, `S=10^{n3}` carries one projected numerator-side scale across the interface. This distinction is useful after the later SGR-9 result closes DD and leaves strict A1-only as the active strict chamber.
