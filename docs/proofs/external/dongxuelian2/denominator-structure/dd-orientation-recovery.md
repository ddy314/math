# DD source orientation recovery (curated import)

Source master: `2cfa389f1d4ced90653101e6c92ee8dfe85b5535`; original `strict_layer_DD_orientation_recovery_campaign.md`.

Source status: **SGR-8B — ORIENTATION RECOVERY GATE**. This is a direct prerequisite of the later DD closure.

For the frozen top-DD chamber, write
\[
Q=b_1 10^{m_2}+b_2,\quad G=b_1b_2,\quad
N=(a_1b_2)^2+(a_2b_1)^2,
\]
\[
A=a_1 10^{n_2}+a_2,\quad C=10^{d_3}A,\quad T=10^{m_3},
\]
\[
\kappa=TQG/b_3,\qquad QG<\kappa\le10QG.
\]
The original six-variable equation becomes a quadratic in `a=a3`:
\[
\kappa^3(\kappa+2G)a^2-2CG^2T\kappa^2a
+T^2[NQ^2(\kappa+G)^2-C^2G^2\kappa^2]=0.
\]
If `t=G(R-r3)` is the gap root, then third-numerator recovery is affine and strictly decreasing:
\[
\boxed{a(t)=\frac{TCG}{\kappa}-\frac{TQ(\kappa+G)}{\kappa^2}t},
\qquad da/dt<0.
\]
The Vieta involution on the gap quadratic exactly exchanges the two roots of this tail quadratic.

For the top DD range, if `a3` is the legal `n3`-digit root, the sum of the two tail roots satisfies
\[
\Sigma_a/a_3<2\cdot10^{-3},
\]
so the conjugate root obeys
\[
\boxed{a_3^\vee<0.}
\]
Hence the original positive-decimal problem selects a unique algebraic orientation: the legal gap root is the smaller Vieta root. In the source-factor notation this yields
\[
\boxed{F_-<F_+},
\]
and with the post-deflation ordered roots `J^sharp<K^sharp`,
\[
\boxed{F_-=\Lambda D_0J^\sharp,\qquad F_+=\Lambda D_0K^\sharp.}
\]
Thus the orientation bit is a theorem, not a gauge choice.

Let
\[
h=\gcd(\kappa,G),\quad A_\kappa=\kappa/h,\quad D=G/h,\quad
B_\kappa=(\kappa+2G)/h=A_\kappa+2D.
\]
Then
\[
\boxed{B_\kappa\mid F_-,\qquad A_\kappa\mid F_+},
\]
\[
\gcd(A_\kappa,B_\kappa)\in\{1,2\},
\]
and denominator normalization gives `A_kappa|TQ`. Define
\[
c=TQ/A_\kappa,\qquad b_3=cD,
\]
\[
u=F_-/B_\kappa,\qquad v=F_+/A_\kappa.
\]
Then the source-oriented quotient system is
\[
\boxed{uv=Nc^2,\qquad v-u=2ha_3,\qquad b_3=cD.}
\]
Equivalently,
\[
\boxed{a_3=(v-u)/(2h).}
\]
This system, together with third-block reducedness and top-DD 5-adic resonance, is the input used by SGR-9 to close DD.
