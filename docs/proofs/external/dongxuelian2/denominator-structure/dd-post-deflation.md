# DD post-deflation structural reduction (curated import)

Source: `dongxuelian2/three-term-decimal-concatenation-square-sum`, master `2cfa389f1d4ced90653101e6c92ee8dfe85b5535`, original file `strict_layer_DD_post_deflation_campaign.md`.

Evidence level in source: **SGR-5D — STRUCTURAL REDUCTION**. This is an intermediate DD result; later SGR-9 closes DD.

Starting from
\[
\varepsilon M^2-E=\varepsilon Y^2,\qquad J=M-Y\ge1,
\]
with top-DD double resonance
\[
v_p(M-Y)=v_p(M+Y)=j_p\quad(p=2,5),
\]
define
\[
D_0=2^{j_2}5^{j_5},\qquad J^\sharp=(M-Y)/D_0,\qquad K^\sharp=(M+Y)/D_0.
\]
Then
\[
\gcd(J^\sharp K^\sharp,10)=1,
\]
\[
H^\sharp=J^\sharp+K^\sharp=2M/D_0,
\]
\[
N^\sharp=J^\sharp K^\sharp=E/(\varepsilon D_0^2),
\]
and hence
\[
\boxed{(J^\sharp)^2-H^\sharp J^\sharp+N^\sharp=0.}
\]

Writing `n^{<10>}` for the prime-to-10 part, introduce the residual supply
\[
\boxed{\Omega_{DD}=(Q_{12}\mathcal N_{12}\mathscr T)^{\langle10\rangle}},
\qquad
\mathscr T=\kappa^2(\kappa+2G)/10^{m_3}.
\]
The key divisor result is
\[
\boxed{J^\sharp\mid \Omega_{DD}^2.}
\]
Thus every residual odd prime power of the deflated small factor is supplied by the prefix objects `Q12`, `N12`, or the tail residual `T-script`.

The residual local phase can be written
\[
(J^\sharp)^2\equiv-N^\sharp\pmod{p^{R_p^\sharp}},\qquad R_p^\sharp=v_p(H^\sharp),\quad p=2,5.
\]
The exact Archimedean formula is
\[
J^\sharp=\frac{M\rho}{D_0(1+\sqrt{1-\rho})},\qquad \rho=E/(\varepsilon M^2),
\]
so
\[
\frac{M\rho}{2D_0}\le J^\sharp\le\frac{M\rho}{D_0}.
\]
Using the frozen top-DD inequalities gives the explicit, but height-dependent, bound
\[
\boxed{J^\sharp<14443\cdot10^{3S_{12}-10}.}
\]

At this stage no height-independent bound on `J^sharp` was known; the remaining supply bottleneck was the moving prefix contribution `(Q12 N12)^{<10>}`. Later SGR-6 shows that the projected phase is endogenous, SGR-8 recovers the source orientation, and SGR-9 closes DD.
