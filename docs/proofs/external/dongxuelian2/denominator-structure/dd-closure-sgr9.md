# DD closure: oriented 5-adic quotient overload (curated import)

Source master: `2cfa389f1d4ced90653101e6c92ee8dfe85b5535`; original `strict_layer_DD_oriented_tail_window_campaign.md`.

Source status: **SGR-9A — DD CLOSED**, relative to the frozen pre-SGR-9 DD reduction chain. This later result supersedes older imported notes that still mark DD open.

The final open DD core had
\[
10S+11\le n_3\le11S+3,\qquad d_3\le5S,
\quad S=m_1+m_2,
\]
so, with `m=m3=n3-d3`,
\[
\boxed{m\ge5S+11.}
\]
It also satisfies the top 5-adic double resonance
\[
v_5(F_-)=v_5(F_+).
\]

Use the SGR-8 source orientation and define
\[
h=\gcd(\kappa,G),\quad A_\kappa=\kappa/h,\quad D=G/h,
\quad B_\kappa=(\kappa+2G)/h,
\]
\[
c=10^mQ/A_\kappa,\qquad b_3=cD,
\]
\[
u=F_-/B_\kappa,\qquad v=F_+/A_\kappa.
\]
Then
\[
\boxed{uv=Nc^2,\qquad v-u=2ha_3,\qquad \gcd(a_3,cD)=1.}
\]
The exact third-block reducedness implies
\[
\gcd(v-u,cD)=\gcd(2h,cD),
\]
and in particular, for every prime `p|cD`,
\[
v_p(v-u)=v_p(2h).
\]

The top-size bounds give
\[
\kappa\le10QG<10^{2S+1},\qquad \kappa+2G<11\cdot10^{2S},
\]
so
\[
v_5(\kappa),v_5(\kappa+2G)\le3S+3.
\]
Since
\[
c=10^mQ/A_\kappa,
\]
one obtains
\[
\boxed{v_5(c)\ge2S+8>0.}
\]
Thus `5|b3`, and reducedness forces
\[
\boxed{v_5(a_3)=0.}
\]
Hence, if `H=v_5(h)`,
\[
\boxed{v_5(v-u)=H.}
\]

Write
\[
a=v_5(A_\kappa),\quad b=v_5(B_\kappa),\quad
x=v_5(u),\quad y=v_5(v).
\]
Because `gcd(A_kappa,B_kappa)∈{1,2}`,
\[
\min(a,b)=0.
\]
The resonance `v5(F_-)=v5(F_+)` implies
\[
|x-y|=a+b,
\]
while the product gives
\[
x+y=v_5(N)+2v_5(c).
\]
Using `v5(v-u)=H`, one gets uniformly
\[
x+y\le2H+a+b.
\]
Substituting `v5(c)=m+v5(Q)-a`, together with
\[
v_5(\kappa)=H+a,\qquad v_5(\kappa+2G)=H+b,
\]
yields
\[
\boxed{v_5(N)+2m+2v_5(Q)\le9S+9.}
\]
Dropping nonnegative terms:
\[
\boxed{2m\le9S+9.}
\]
But the top-DD lower bound gives
\[
\boxed{2m\ge10S+22.}
\]
Contradiction.

Therefore the last top-DD state is empty. Since the earlier proof chain had already reduced all DD candidates to this top state,
\[
\boxed{DD=\varnothing.}
\]

The decisive mechanism is source orientation + source-labelled division + individual reducedness + 5-adic double resonance. The older near-square, near-S-unit, projected Hensel and post-deflation routes become historical internal nodes rather than active DD frontiers.
