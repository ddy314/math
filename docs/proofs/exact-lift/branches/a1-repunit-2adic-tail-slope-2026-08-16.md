# A1 second-repunit 2-adic tail slope — 2026-08-16

本文继续 second-repunit edge，并把安全二进 tail-gap 定理与第三分母 endpoint excess 联立。

当前写

\[
\boxed{
 s=\ell-2k>0,
\qquad
 b_3=10^{\ell-1}+f,
\qquad f>0.
}
\]

前文有

\[
\boxed{0<f<\frac18\,10^s.}
\tag{1}
\]

本文证明统一的更强第三尾斜率：

\[
\boxed{
 s>\frac{4k+7}{3\log_2 10-1},
}
\]

所以

\[
\boxed{
\ell>
\left(2+\frac4{3\log_2 10-1}\right)k
+
\frac7{3\log_2 10-1}.
}
\]

数值上第三尾斜率已经大于约 `2.4461`。

本文结论均为 **已严格完成**。

---

## 1. 记二进 excess

令

\[
\boxed{p=v_2(f).}
\]

基项

\[
10^{\ell-1}
\]

的二进赋值为

\[
\ell-1.
\]

分两种情况。

---

# 2. 情形 A：`p<\ell-1`

若

\[
p<\ell-1,
\]

则两项赋值不同，所以

\[
\boxed{v_2(b_3)=p.}
\tag{2}
\]

特别地

\[
p<\ell,
\]

当前处于安全二进 unsaturated side。

因此第三块必须取得唯一二进最大，并且前文 tail-gap 上界给出

\[
\ell\le
\begin{cases}
3p-2M-1,&e_1\ne e_2,\\
3p-2M,&e_1=e_2,
\end{cases}
\tag{3}
\]

其中

\[
M=\max(v_2(b_1),v_2(b_2)).
\]

second-repunit edge 有

\[
b_2=10^{k-1},
\]

所以

\[
\boxed{M\ge k-1.}
\tag{4}
\]

用较弱但统一的第二行粗化 (3)：

\[
\ell\le3p-2(k-1).
\]

代入

\[
\ell=2k+s
\]

得到

\[
2k+s\le3p-2k+2,
\]

即

\[
\boxed{
p\ge\frac{4k+s-2}{3}.}
\tag{5}
\]

---

## 3. 用十进制 endpoint 上界消去 `p`

由 `p=v_2(f)` 与 `f>0`：

\[
f\ge2^p.
\]

结合 (1)：

\[
2^p<\frac18 10^s.
\]

取以 `2` 为底的对数：

\[
p<s\log_2 10-3.
\tag{6}
\]

把 (5) 代入 (6)：

\[
\frac{4k+s-2}{3}
<s\log_2 10-3.
\]

乘以 `3` 并整理：

\[
4k+7
<s(3\log_2 10-1).
\]

所以

\[
\boxed{
 s>\frac{4k+7}{3\log_2 10-1}.
}
\tag{7}
\]

---

# 4. 情形 B：`p\ge\ell-1`

若

\[
p\ge\ell-1,
\]

则直接有

\[
f\ge2^{\ell-1}.
\]

和 (1) 联立：

\[
2^{\ell-1}<\frac18 10^s.
\]

取 `\log_2`：

\[
\ell-1<s\log_2 10-3.
\]

代入

\[
\ell=2k+s
\]

得到

\[
2k+2<s(\log_2 10-1).
\]

因此

\[
\boxed{
 s>\frac{2k+2}{\log_2 10-1}.
}
\tag{8}

这比 (7) 更强，因为

\[
\frac2{\log_2 10-1}
>
\frac4{3\log_2 10-1}.
\]

所以 (7) 无条件覆盖两种情况。

---

# 5. 统一第三尾斜率

因此 second-repunit edge 的全部剩余候选满足

\[
\boxed{
 s>\frac{4k+7}{3\log_2 10-1}.
}
\tag{9}

即

\[
\boxed{
\ell>
\left(2+\frac4{3\log_2 10-1}\right)k
+
\frac7{3\log_2 10-1}.
}
\tag{10}

数值上

\[
\frac4{3\log_2 10-1}\approx0.4461,
\]

所以

\[
\boxed{
\ell>2.4461\ldots\,k+0.7807\ldots.
}
\]

这严格强化了此前只由 `2^k\mid f` 得到的 slope `2.3010...`。

---

## 6. Unsaturated 子区的额外 `v_2(f)` 锁

在情形 A 中还保留

\[
\boxed{
\frac{4k+s-2}{3}
\le v_2(f)
<\ell-1.
}
\tag{11}

所以 moderate `2`-unsaturated tail 不只要求 `f` 含 `2^k`，其二进深度实际上至少接近 `\frac43k+\frac13s`。

这可与 5-adic Newton funnel 对 `v_5(f)` 的两条 resonance wall 联立，继续压缩第三 excess 的 prime-power 形状。