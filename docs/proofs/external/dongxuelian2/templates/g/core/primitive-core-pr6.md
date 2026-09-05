# Critical G primitive core: PR6 reduction (curated import)

Source: `dongxuelian2/three-term-decimal-concatenation-square-sum`, master `2cfa389f1d4ced90653101e6c92ee8dfe85b5535`, original `research/templates/g/core/primitive-core.md`.

Source status: **PR6 — structural reduction, not a full G closure**.

This note records the strongest reusable normal form for the primitive positive-remainder part of the critical `G` template (`h=1`). Starting from
\[
J\in\{1,\dots,9\},\quad T=\tau N,\quad b_2=\tau q,
\]
\[
N=Jq+s,\quad1\le s<q,\quad\gcd(s,q)=1,
\]
\[
q\rho-Es=g,\quad\gcd(q,E)=\gcd(q,g)=\gcd(q,10)=1,
\]
define
\[
d=\gcd(g,E),\qquad \rho=d\rho_0,\qquad E=dE_0,\qquad \gamma=g/d.
\]
The correct reduced determinant is
\[
\boxed{q\rho_0-E_0s=\gamma},
\]
with
\[
\gcd(q,E_0)=\gcd(\rho_0,E_0)=1,
\quad \gcd(\gamma,E_0)=\gcd(\gamma,q)=1.
\]
A key audit correction is that the prime-to-10 odd core of `g` need not equal `gamma`; even when that odd core is 1, unabsorbed 2/5-adic overflow may leave `gamma>1`.

Introducing
\[
Z=Y/(vd),\qquad E_0=b_1Z,\qquad M_0=JE_0+\rho_0=\gamma k-Z,
\]
gives the shifted determinant
\[
qM_0-E_0N=\gamma
\]
and the terminal factorization
\[
\boxed{\gamma(qk-1)=Z(q+b_1N)}.
\]
Consequently
\[
\boxed{\gamma\mid q+b_1N,\qquad Z\mid qk-1,\qquad \gamma<21q.}
\]
For `gamma=1` the two reduced fractions are Farey-adjacent, but the source constructs unbounded auxiliary families satisfying all denominator/K5/E4 front gates, so Farey adjacency alone does not close the branch. For `gamma>1`, any reduced fraction strictly between the endpoints has denominator at least
\[
\left\lceil\frac{q+E_0}{\gamma}\right\rceil,
\]
but the moving factor `q+b1 N` still prevents uniform finite reduction.

The full discriminant factors as
\[
\mathcal D=d^2\Delta,
\]
\[
\boxed{\Delta=v^2Z^2H_1^2-(k^2-1)\gamma^2((ua_1)^2+(va_2)^2)}.
\]
If `Delta=w0^2`, exact third-block recovery plus `gcd(a3,b3)=1` forces, for one sign,
\[
\boxed{d=\frac{k^2-1}{\gcd(k^2-1,vZH_1\pm kw_0)}},
\]
\[
\boxed{a_3=\frac{vZH_1\pm kw_0}{\gcd(k^2-1,vZH_1\pm kw_0)}}.
\]
Thus each fixed reduced state and sign admits at most one original scale `d`. Two explicit unbounded auxiliary rays are then closed by the reduced discriminant, proving this gate is genuinely stronger than the earlier Farey-only structure.

For the primitive `h=1` E4 support, A and B remain with `e<=m`; C survives only at `b1=1,c=m,e<m`; D is empty. The remaining moving parameters `(q,N,gamma,Z,k,u,v,...)` are not uniformly bounded, hence the classification remains PR6 rather than a full template theorem.
