# Critical G zero-middle-remainder closure: GD1 (curated import)

Source: master `2cfa389f1d4ced90653101e6c92ee8dfe85b5535`, original `research/templates/g/core/exact-divisor-states.md`.

Source status: **GD1 — the entire normal-state sublayer `T-Jb2=0` is closed**.

In the critical `G` template, let
\[
r=T-Jb_2.
\]
The exact remainder identity is
\[
qu\rho=Yr+gu.
\]
When `r=0`, coprimality immediately yields
\[
\boxed{q=1,\qquad \rho=g}.
\]
Then `T=Jb2`; because `1<=J<=9` and `J|10^m`, only
\[
J\in\{1,2,4,5,8\}
\]
can occur, and `J=1` violates the strict upper digit window `b2<T`. The remaining cases are split by `(b1,v)=(2,2),(1,1),(2,1)`.

The source derives a J-dependent 5-adic slope from the full sphere+concatenation system:
\[
\boxed{n=3v_5(g)-v_5(Jb_1+1)}.
\]
It also derives exact 2-adic factor-allocation conditions, then combines them with E4 and the true denominator windows. All but two parameter families become finitely many denominator points; the two surviving unbounded families are closed uniformly by the full discriminant, either because it is negative or because a required square would imply an impossible square root of `-1 mod 4`.

For the finitely reduced remainder, the full discriminant is
\[
\boxed{\mathcal D=Y^2H^2-(k^2-1)\mathcal S},
\]
with
\[
\mathcal S=g^2((ua_1)^2+(va_2)^2),\qquad H=a_1T+10a_2,
\]
and any original candidate must also satisfy
\[
\boxed{a_3=\frac{YH\pm k\sqrt{\mathcal D}}{k^2-1}}
\]
with the true digit and reducedness constraints. After theoretical finite reduction, exactly 13 fixed denominator states remain. They are all excluded by exact integer nonsquare certificates (negative discriminant or a quadratic-nonresidue witness); the finite computation occurs only after the unbounded parameters have been rigorously eliminated.

Therefore
\[
\boxed{G_{\rm div}:\ T-Jb_2=0\Longrightarrow\text{no candidate}.}
\]
The next `G` system must have `1<=T-Jb2<b2`; this theorem does not close that positive-remainder system.
