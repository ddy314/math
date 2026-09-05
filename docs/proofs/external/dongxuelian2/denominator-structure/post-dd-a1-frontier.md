# Post-DD consolidation and the A1-only frontier (curated import)

Source master: `2cfa389f1d4ced90653101e6c92ee8dfe85b5535`; original `strict_layer_post_DD_consolidation_A1_frontier.md`.

Source status: **SGR-10B — CONSOLIDATION + A1 REDUCTION**.

After auditing the SGR-9 dependency chain, the source records
\[
\boxed{DD=\varnothing.}
\]
The strict-layer carrier decomposition has three chambers:
\[
A_2:\ s_3>0,\ s_2+s_3\le0,
\]
\[
DD:\ s_3>0,\ s_2+s_3>0,
\]
\[
A_1:\ s_3\le0,\ s_2+s_3>0.
\]
Since the strict layer requires `s2+s3>=1`, A2 is incompatible with strictness, and SGR-9 removes DD. Hence
\[
\boxed{\text{Strict candidate}\Longrightarrow A_1\text{-only}.}
\]

For A1 define
\[
g=-s_3=m_3-n_3\ge0,\qquad k_{12}=s_2+s_3\ge1,
\]
so the effective third-tail length is
\[
\ell=m_3-g=n_3.
\]
The old unified coefficient pair simplifies to the actual prefix words:
\[
\boxed{C=A_{12}},\qquad \boxed{D=10^gQ_{12}}.
\]

A sufficient denominator-decimal trace is
\[
\boxed{T=(b_1,b_2,b_3,S),\qquad S=10^{n_3}.}
\]
Fixed `T` determines `m_i`, `Q`, `G`, `n3`, `g`, and the tail normalization `L,tau,kappa,D`. In particular, `g` is not a free variable inside a fixed trace fibre.

A later backward-recovery audit shows that the old gap quadratic and primitive-tail quadratic become identities once exact reconstruction is imposed. Discriminant and resultant conditions are therefore certificates/elimination shadows rather than independent terminal gates.

Define the full denominator and numerator words
\[
\mathbf B=b_1 10^{m_2+m_3}+b_2 10^{m_3}+b_3,
\]
\[
\mathbf A=A_{12}10^{n_3}+a_3.
\]
For A1, fixed `(T, A-word)` recovers all residual algebraic semantics. Let
\[
P=\lfloor\mathbf A/S\rfloor=A_{12},\qquad a_3=\mathbf A\bmod S.
\]
For a decimal cut at length `n`, set
\[
a_1=\lfloor P/10^n\rfloor,\qquad a_2=P\bmod10^n.
\]
Then define the weighted prefix norm
\[
F_n=b_2^2a_1^2+b_1^2a_2^2.
\]
The exact A1 word-recovery equation is
\[
\boxed{
F_n=G^2\left[\left(\frac{\mathbf A}{\mathbf B}\right)^2-\left(\frac{a_3}{b_3}\right)^2\right].
}
\tag{A1-WR}
\]
Together with positive digit windows, `g>=0`, `k12=n-m2-g>=1`, and
\[
\gcd(a_i,b_i)=1,
\]
this is equivalent to an original A1 candidate.

The decimal split functional `F_n` is strictly discretely convex along legal cuts, hence any horizontal level is hit at most twice. Consequently
\[
\boxed{\text{fixed }(T,\mathbf A)\Longrightarrow\text{at most two A1 prefix realizations}.}
\]
Thus the remaining cut multiplicity is only a binary finite choice, not another unbounded direction.

The fixed-primitive-core finite-fibre theorem further implies that any infinite A1 candidate sequence must have primitive-core height
\[
\boxed{Q_0\to\infty.}
\]
This does not mean every coordinate is a function of `Q0`; it means moving primitive-core height is the only top-level infinity source.

The resulting single open terminal target is the **A1 Moving-Core Word-Realization Theorem**: prove that no admissible `(T, A-word, n)` satisfies A1-WR + the legal digit cell + individual reducedness + the necessary tail admissibility conditions.

After this consolidation, DD-specific near-square/Hensel/orientation machinery is historical, and the A1 gap/tail quadratics, discriminant, resultant and square-spacing should not be treated as parallel frontier obligations.
