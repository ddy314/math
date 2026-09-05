# Backward exact-recovery canonical dependency skeleton (curated import)

Source: `dongxuelian2/three-term-decimal-concatenation-square-sum`, master `2cfa389f1d4ced90653101e6c92ee8dfe85b5535`, original `research/exact-lift/backward/backward-canonical-dependency-skeleton.md`.

Source status: **canonicalization / structural formalism; no new death region**.

The main organizational theorem is that the apparent Exact-Lift recovery state is heavily over-parameterized. Using the audited common-denominator reconstruction, a complete candidate can be placed on the canonical spine
\[
\boxed{(x_1,x_2,x_3,\Lambda)},
\]
where
\[
\Lambda=\operatorname{lcm}(b_1,b_2,b_3),\qquad
x_i=\Lambda a_i/b_i,
\]
and
\[
d_i=\gcd(x_i,\Lambda),\qquad
a_i=x_i/d_i,\qquad b_i=\Lambda/d_i.
\]
Once the four integers are fixed and the sphere-square gate passes, the positive radius `t`, all six reduced blocks, digit lengths, valuations, Exact-Lift prefix quantities, tail normalization and coefficient data are deterministic functions of this spine.

Accordingly, gap roots, tail roots, discriminant square-root signs, Hensel branches, Gaussian allocation labels and enumeration indices should not be counted as independent original-candidate coordinates merely because a projected search formulation branches on them. They are finite search branches or proof artifacts unless a future theorem proves they encode distinct completion fibres.

The note reduces the raw recovery inventory to
\[
\boxed{\mathcal V_{\rm red}=\{x_1,x_2,x_3,\Lambda\}}.
\]
This is a count of canonical unbounded integer coordinates, not an algebraic-geometric dimension and not a finite assignment bound.

It proposes a presentation-resistant complexity notion, the **canonical synchronization width** `kappa_rec`: the smallest possible maximum number of canonical unbounded coordinates that must be shared across separators in a legitimate recovery-factorization tree. The current T3 presentation has gates
\[
G_{\rm sph}:\{x_1,x_2,x_3\},
\]
\[
G_{\rm can},G_{\rm bal}:\{x_1,x_2,x_3,\Lambda\},
\]
so
\[
\boxed{\kappa_{\rm rec}\le4}.
\]
No proof is given that the intrinsic minimum equals 4. Reducing the synchronization width to 3 or 2 by finding a genuine low-support recovery separator is explicitly left open.

A general separator lemma is also recorded: for two compiled recovery blocks meeting on separator `S`, their natural join is empty iff one side is empty or their feasible projections to `S` are disjoint. Thus future “small obstruction certificates” should be formulated as incompatibility of canonical block projections on a small separator, not as an arbitrary count of raw scalar relations.

The reusable methodological conclusion is:

> Exact-Lift currently looks like **few shared unbounded canonical coordinates + many deterministic projections**, rather than many independent witness variables.
