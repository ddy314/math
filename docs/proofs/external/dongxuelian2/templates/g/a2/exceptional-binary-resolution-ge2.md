# Critical G A2 exceptional binary chamber: GE2-1 (curated import)

Source: master `2cfa389f1d4ced90653101e6c92ee8dfe85b5535`, original `research/templates/g/a2/exceptional-binary-resolution.md`.

Source status: **GE2-1 — the exceptional 2-adic recovery chamber is closed by a pure symbolic argument**.

For the `G_prim`, `gamma=1`, A2 full discriminant/recovery system, set
\[
\mathcal A=2ZH_1,\qquad R=(5^ea_1)^2+(2a_2)^2,\qquad K=k^2-1,
\]
\[
w_0^2=\mathcal A^2-KR,
\]
\[
L_\varepsilon=\mathcal A+\varepsilon k w_0.
\]
Exact recovery requires, for one sign,
\[
2^a5^\varphi=\frac{K}{\gcd(K,L_\varepsilon)}.
\]
Let
\[
\alpha=v_2(K),\qquad A_2=v_2(\mathcal A)=2a+v_2(H_1)>a.
\]
For the recovery sign, the gcd equality forces the exact valuation
\[
\boxed{v_2(L_\varepsilon)=\alpha-a}.
\]
The exceptional chamber is
\[
\alpha\ge2A_2.
\]
There both `A-script` and `w0` are divisible by `2^{A2}`, so
\[
v_2(L_+),v_2(L_-)\ge A_2.
\]
But the exact conjugate product is
\[
L_+L_-=K(k^2R-\mathcal A^2),
\]
and the parenthesized factor is odd. Hence
\[
\boxed{v_2(L_+)+v_2(L_-)=\alpha}.
\]
Subtracting the recovery-sign valuation gives
\[
v_2(L_{-\varepsilon})=a,
\]
contradicting the simultaneous lower bound `>=A2>a`.

Therefore
\[
\boxed{\mathrm E_2\Longrightarrow\text{no complete candidate}.}
\]
Together with the preceding A2 dichotomy this upgrades every complete A2 candidate to the exact necessary condition
\[
\boxed{v_2(k^2-1)=2a.}
\]
No finite computation, terminal J/m case split, or 5-adic lifting is used. The result does not close the remaining A2 `F_{P-}` / low-phi moving-modulus systems.
