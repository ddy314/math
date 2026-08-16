# A1 second-repunit lower-resonance slope — 2026-08-16

本文继续 `a1-repunit-5adic-newton-funnel-2026-08-16.md`，处理唯一尚未被 Newton uniqueness 排除的 lower resonance wall

\[
\boxed{3q=5k+s-3,}
\qquad
q=v_5(f),
\qquad
s=\ell-2k.
\]

结合 second-repunit edge 已证明的 `2^k\mid f` 与第三 endpoint 上界，得到一个新的线性尾长斜率。

本文结论为 **已严格完成**。

---

## 1. Resonance 给出 `v_5(f)` 的精确值

lower resonance 为

\[
3q=5k+s-3.
\]

所以

\[
\boxed{q=\frac{5k+s-3}{3}.}
\tag{1}
\]

因为 `q` 是整数，这还隐含同余条件

\[
\boxed{5k+s\equiv0\pmod3.}
\tag{2}
\]

---

## 2. 同时存在二进深度

second-repunit edge 已经严格证明

\[
\boxed{2^k\mid f.}
\tag{3}
\]

而当前 `v_5(f)=q`，所以由 `2,5` 互素：

\[
\boxed{f\ge2^k5^q.}
\tag{4}
\]

另一方面第三坐标 endpoint 几何给出

\[
\boxed{f<\frac18\,10^s.}
\tag{5}
\]

因此

\[
2^k5^q<\frac18\,10^s.
\tag{6}
\]

---

## 3. 消去 `q`

将 (1) 代入 (6)，取自然对数：

\[
k\log2+rac{5k+s-3}{3}\log5
<s\log10-3\log2.
\]

乘以 `3` 并整理：

\[
s(3\log10-\log5)
>
k(3\log2+5\log5)
+9\log2-3\log5.
\]

因此

\[
\boxed{
 s>
\frac{3\log2+5\log5}{3\log10-\log5}\,k
+
\frac{9\log2-3\log5}{3\log10-\log5}.
}
\tag{7}

数值上

\[
\boxed{
 s>1.911291907084842\ldots\,k
+0.266124278745472\ldots.
}
\tag{8}

因为

\[
\ell=2k+s,
\]

得到

\[
\boxed{
\ell>3.911291907084842\ldots\,k
+0.266124278745472\ldots.
}
\tag{9}

---

## 4. 当前 Newton 图的斜率解释

5-unsaturated second-repunit edge 现在分成：

### strict lower

\[
3q<5k+s-3,
\]

仍可能处在 moderate tail，但必须满足

\[
v_5(10^{m_1}-b_1)=k-1,
\qquad
v_5(e)=0,
\]

以及 prefix phase lock

\[
d_0^2+(-1)^{k+1}e^2\equiv0\pmod5;
\]

### lower resonance

\[
3q=5k+s-3,
\]

现已强迫

\[
\boxed{\ell>3.91129\ldots\,k+0.26612\ldots;}
\]

### upper resonance / 5-saturated

已经强迫更强的

\[
\ell>6.643856\ldots\,k+0.678071\ldots.
\]

因此所有第三尾斜率低于约 `3.91` 的 second-repunit 候选都只能进入 strict-lower Newton side。