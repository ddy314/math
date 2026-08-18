# A2 angle sign-pair common gcd 的 `Q_0` depth law

> **依赖：** `spontaneous-sign-companion-parity.md`、`spontaneous-angle-parity.md`、`spontaneous-denominator-depth-matrix.md`。
>
> **严格状态：**本文进一步压缩 actual/conjugate angle pair
> \(\widehat{\mathcal O}_+,\widehat{\mathcal O}_-\) 的共同 odd-inert support。先证明 non-`3,5` prime dividing `A=a_2` 不可能进入 angle carrier；因此 sign-pair common inert support从旧的 `A Q_0 c_Q` 精确缩到 `Q_0=c_Qq`。随后给出 `U_Omega` 的二阶 `Q`-adic identity，得到 pair-gcd 的完整 prime-power depth law：若 `e=v_p(Q_0)`、`c=v_p(c_Q)`，则共同 depth 恰为 `min(v_p(N^2 Delta_0),e+c)`。特别地 first layer 统一落在 `x=-2, Delta_0=0`，且所有 non-`3` inert roots均 simple。本文不证明该 common gcd 的总 mod-4 parity为偶，因此不关闭 A2。

---

## 1. 记号

固定 reflection endpoint：

\[
N=10^M,\qquad T=10^m,\qquad A=a_2,\qquad B=b_2,
\]

\[
Q=B+2N=2^{M+1}Q_0,
\qquad Q_0=c_Qq,
\]

\[
\mathcal U_\Omega=(45B^2-2AN)^2-A^2B(99B-4N),
\]

\[
\mathcal O_\pm=T\mathcal U_\Omega\pm2A^2Qb_3.
\]

primitive angle carriers are

\[
\widehat{\mathcal O}_\pm=\frac{\mathcal O_\pm}{2^{2M+m+2}},
\qquad
\widehat{\mathcal O}_\pm>0,
\qquad
\widehat{\mathcal O}_\pm\equiv3\pmod4.
\]

Define the integral prefix defect

\[
\boxed{
D_Q:=2025B^2-180AN-100A^2.
}
\tag{1.1}
\]

With

\[
x=B/N,\qquad y=10A/N,
\]
we have

\[
\boxed{D_Q=N^2\Delta_0,\qquad
\Delta_0=2025x^2-18y-y^2.}
\tag{1.2}
\]

---

## 2. `A=a_2` content cannot enter the genuine angle pair

Let `p` be an odd prime with

\[
p\mid A,\qquad p\notin\{3,5\}.
\]

Because `(A,B)=1`, one has `p\nmid B`. Modulo `p`,

\[
\mathcal U_\Omega\equiv(45B^2)^2\not\equiv0.
\]

Also the second term of `O_\pm` contains `A^2`, hence vanishes. Since `p\nmid T`,

\[
\boxed{
\mathcal O_\pm\equiv T(45B^2)^2\not\equiv0\pmod p.}
\tag{2.1}
\]

Therefore

\[
\boxed{
 p\mid A,\ p\notin\{3,5\}
 \Longrightarrow
 p\nmid\widehat{\mathcal O}_\pm.}
\tag{2.2}
\]

`spontaneous-sign-companion-parity.md` had already shown that any common odd prime of the two angle sheets divides

\[
A Q_0 5c_Qc_u.
\]

The angle-content lemma removes `c_u`, (2.2) removes `A`, and `c_Q\mid Q_0`. Thus for any genuine non-`3` inert common prime,

\[
\boxed{
 p\mid\gcd(\widehat{\mathcal O}_+,\widehat{\mathcal O}_-)
 \Longrightarrow p\mid Q_0.}
\tag{2.3}
\]

So the common sign-pair support is entirely `Q_0=c_Qq`-supported.

---

## 3. `U_Omega` 的 exact second-order `Q` bridge

A direct expansion gives the stronger identity

\[
\boxed{
\begin{aligned}
\mathcal U_\Omega
={}&-4N(B+N)D_Q\\
&-9Q^2(11A^2+20AN-225B^2).
\end{aligned}}
\tag{3.1}
\]

Hence

\[
\boxed{
\begin{aligned}
\mathcal O_\pm
={}&-4TN(B+N)D_Q\\
&+Q\Bigl[
-9TQ(11A^2+20AN-225B^2)
\pm2A^2b_3
\Bigr].
\end{aligned}}
\tag{3.2}
\]

This is the natural sign-pair analogue of the denominator depth bridges: the first term reads the pure prefix defect, while every sign-dependent term is pushed into a higher `Q/b_3` depth.

---

## 4. complete prime-power depth law

Fix a genuine odd inert prime `p` with

\[
p\mid Q_0.
\]

Write

\[
e:=v_p(Q_0)>0,
\qquad
c:=v_p(c_Q)\ge0.
\tag{4.1}
\]

Since

\[
Q=2^{M+1}Q_0,
\qquad
b_3=2^{M+m+1}5^dc_Qc_u,
\]
and `p\nmid2\cdot5\cdot c_u`,

\[
\boxed{v_p(Q)=e,\qquad v_p(b_3)=c.}
\tag{4.2}
\]

Because `p|Q`,

\[
B\equiv-2N\pmod p,
\]
so

\[
B+N\equiv-N\not\equiv0\pmod p.
\]
Thus the coefficient

\[
-4TN(B+N)
\]
is a `p`-adic unit.

The bracketed correction in (3.2) has valuation at least `c`, since its first term has depth `e>=c` and its second term has depth exactly `c`. Therefore the whole correction term is divisible by

\[
p^{e+c}.
\]
Consequently

\[
\boxed{
\mathcal O_\pm
\equiv
-4TN(B+N)D_Q
\pmod{p^{e+c}}.}
\tag{4.3}
\]

Moreover

\[
\mathcal O_+-\mathcal O_-=4A^2Qb_3,
\]
and (2.2) gives `p\nmid A`; hence

\[
\boxed{
v_p(\mathcal O_+-\mathcal O_-)=e+c.}
\tag{4.4}
\]

Let

\[
d_O(p):=\min\{v_p(\mathcal O_+),v_p(\mathcal O_-)\}.
\]
If `v_p(D_Q)<e+c`, (4.3) makes both angle valuations exactly `v_p(D_Q)`. If `v_p(D_Q)>=e+c`, (4.3) makes both at least `e+c`, while (4.4) prevents both from exceeding `e+c`. Therefore

\[
\boxed{
 d_O(p)=\min\{v_p(D_Q),e+c\}.}
\tag{4.5}
\]

Since primitive normalization removes only a power of `2`, the same formula holds for the primitive pair gcd:

\[
\boxed{
 v_p\!\left(
 \gcd(\widehat{\mathcal O}_+,\widehat{\mathcal O}_-)
 \right)
 =
 \min\{v_p(N^2\Delta_0),\ v_p(Q_0)+v_p(c_Q)\}.}
\tag{4.6}
\]

Because `p\nmid N`, this can be written simply as

\[
\boxed{
 v_p(D_O)
 =
 \min\{v_p(\Delta_0),\ v_p(q)+2v_p(c_Q)\}.}
\tag{4.7}
\]

Here `D_O=gcd(widehat(O)_+,widehat(O)_-)`.

Two useful special cases are immediate:

### q-supported prime, `p\nmid c_Q`

If `p^e||q`, then `c=0` and

\[
\boxed{v_p(D_O)=\min\{v_p(\Delta_0),e\}.}
\tag{4.8q}
\]

This exactly matches the existing q-denominator angle depth law.

### pure `c_Q`-supported prime, `p\nmid q`

If `p^c||c_Q`, then `e=c`, hence

\[
\boxed{v_p(D_O)=\min\{v_p(\Delta_0),2c\}.}
\tag{4.8c}
\]

Thus a fully saturated pure-`c_Q` sign-pair contribution has even depth `2c`; odd parity from `c_Q` can only occur in an **unsaturated** prefix contact `v_p(Delta_0)<2c`.

---

## 5. first-layer geometry is a single simple conic

From `p|Q_0` one has

\[
Q=N(x+2)\equiv0\pmod p,
\]
so

\[
\boxed{x\equiv-2\pmod p.}
\tag{5.1}
\]

If the prime also divides the angle sign-pair gcd, then (4.6) gives

\[
\Delta_0\equiv0\pmod p.
\]
At `x=-2`,

\[
\Delta_0(-2,y)
=8100-18y-y^2,
\]
so equivalently

\[
\boxed{(y+9)^2=8181=3^4\cdot101.}
\tag{5.2}
\]

The discriminant of the quadratic in `y` is

\[
18^2+4\cdot8100
=324\cdot101.
\tag{5.3}
\]

The only odd ramified prime apart from `3` is

\[
101\equiv1\pmod4.
\]
Therefore

\[
\boxed{
\text{every genuine non-`3` inert angle-sign common first-layer root is simple.}}
\tag{5.4}
\]

In particular the sign-pair gcd has no new inert singular Hensel tree. Its only remaining freedom is the simple prime-power depth in (4.7).

---

## 6. update to the global parity ledger

The old support statement

\[
\operatorname{Supp}_{3\bmod4}(D_O)
\subseteq\operatorname{Supp}(A Q_0c_Q)
\]
can now be replaced by the strictly sharper valuation statement

\[
\boxed{
\operatorname{Supp}_{3\bmod4}(D_O)
\subseteq\operatorname{Supp}(Q_0),
}
\]

\[
\boxed{
 v_p(D_O)
 =
 \min\{v_p(\Delta_0),v_p(q)+2v_p(c_Q)\}.
}
\tag{6.1}
\]

So the actual/conjugate angle pair can share inert parity only through the same q-type prefix conic `x=-2, Delta_0=0`. The `a_2` content source disappears completely, and pure `c_Q` contribution is parity-even once it reaches its full square depth `2v_p(c_Q)`.

This still does not prove `D_O=1 mod4`: an unsaturated simple `Delta_0` contact may stop at odd depth. The remaining task is therefore no longer a content classification problem; it is a **simple unsaturated depth synchronization problem on a single conic**.
