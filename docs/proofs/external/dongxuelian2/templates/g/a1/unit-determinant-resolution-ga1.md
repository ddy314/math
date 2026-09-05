# Critical G A1 unit-determinant closure: GA1-1 (curated import)

Source: master `2cfa389f1d4ced90653101e6c92ee8dfe85b5535`, original `research/templates/g/a1/unit-determinant-resolution.md`.

Source status: **GA1-1 — `G_prim`, `gamma=1`, A1 is fully closed**.

The previous reduction splits this intersection into a finite low-E certificate and a high layer with even
\[
E\in\{6,8,10,\ldots\}.
\]
The source independently reconstructs the complete low-E certificate and finds exactly two residue-state rows; each row represents a full infinite arithmetic progression of decimal exponents, not a finite sample.

For the high layer, let
\[
A=5^E,\qquad B\in\{1,5\},\qquad r=k-2A,
\]
with the exact terminal relation
\[
qr=1+4B10^m.
\]
The frozen congruences give
\[
r\equiv15\pmod{16},
\]
so the Jacobi symbols satisfy
\[
\left(\frac{-1}{r}\right)=-1,
\qquad
\left(\frac2r\right)=1.
\]
The 5-adic gate gives `r≡±1 mod 5`, hence
\[
\left(\frac5r\right)=1,
\quad
\left(\frac{10}{r}\right)=1,
\quad
\left(\frac Br\right)=1.
\]
Taking Jacobi symbols in
\[
4B10^m\equiv-1\pmod r
\]
then gives `1=-1`, closing all high states at once. This argument is valid for composite odd `r`; it uses the Jacobi symbol, not a primality assumption.

For the two low-E state progressions, exact sphere/recovery gives a quadratic in the middle numerator whose discriminant is a square only if
\[
z^2=R^2-C
\]
with `R` of size at least `5*10^556`, whereas a uniform digit-window estimate gives `C<6*10^15`. Any integer square difference would require `R<=C`, a contradiction. This closes every exponent in both progressions simultaneously.

Hence
\[
\boxed{G_{\rm prim},\ \gamma=1,\ \mathrm{A1}\Longrightarrow\text{no candidate}.}
\]
The theorem does not extend to A2, B, C, `gamma>1`, nonprimitive C2/C5, Q, or the strict layer.
