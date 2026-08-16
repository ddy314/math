# `A_1`-only 分支

本文件对应原总稿 §§28–31。它包含薄环约束、尾商斜率锁、saturated `L = 1` 支、denominator-only 尾长界和 saturated 支的奇素数约束。

> 迁移说明：以下 §§28–31 由原始总稿机械拆分；§§32–33 记录 2026-08-16 的 A1 独立重建与新证明树。

# 28. \(A_1\)-only 分支

\(A_1\)-only 满足

\[
s_3\le0,
\qquad
s_2+s_3>0.
\]

统一记

\[
\boxed{g=-s_3\ge0,}
\qquad
\boxed{k_{12}=s_2+s_3\ge1.}
\]

有效第三尾长为

\[
\boxed{\ell=m_3-g.}
\]

定义

\[
U=H-y_3,
\qquad
\mathcal S_{12}=y_1^2+y_2^2.
\]

经过第三块正规化，同样有

\[
\boxed{U=La,\qquad La\mid\mathcal S_{12}.}
\]

并且

\[
H=\frac12\left(La+\frac{\mathcal S_{12}}{La}\right),
\qquad
y_3=\frac12\left(\frac{\mathcal S_{12}}{La}-La\right).
\]

---

## 28.1 薄环约束

由第一坐标 carrier 及球面条件可得到 \(La\) 必须处在一个很薄的实数区间：

\[
\boxed{
10^{k_{12}}y_1-
\sqrt{(10^{2k_{12}}-1)y_1^2-y_2^2}
<La<\sqrt{\mathcal S_{12}}.
}
\]

---

## 28.2 尾商斜率锁

第三分母正规化进一步给出

\[
\boxed{10^{g-1}\le\frac{\tau}{L}<10^g.}
\]

---

# 29. \(A_1\) 的 saturated 支 \(L=1\)

真正特殊的是

\[
\boxed{L=1.}
\]

旧思路曾希望在这里继续 Gaussian descent，但严格检查发现：

\[
\boxed{L=1\text{ 时 Gaussian flip 只是 projective identity}.}
\]

所以 saturated 支必须采用独立机制。

---

# 30. \(A_1\) saturated 的 denominator-only 尾长界

旧基线给出

\[
\boxed{
\ell\le\left\lfloor\log_5((10Q+2)G)\right\rfloor
}
\]

以及粗化

\[
\boxed{\ell\le3(m_1+m_2)+1.}
\]

---

# 31. \(A_1\) saturated 的奇素数约束

令

\[
d_*=\gcd(\tau,10^gQ),
\qquad
h=\frac{\tau}{d_*}.
\]

旧基线记录

\[
\boxed{\gcd(U,h)=1,\qquad h\mid G,}
\]

并进一步限制 `h` 的奇素因子及其来源。

这些旧结论保留为迁移基线；涉及第三分子正规化的推导必须按 §33 的审计边界重新核验。

---

# 32. 2026-08-16 A1 独立重建入口

A1 现已增加一套直接从原始拼接恒等式重建、且不依赖 Gaussian flip 的证明链：

1. [`a1-rational-contact-framework-2026-08-16.md`](a1-rational-contact-framework-2026-08-16.md)
   - 严格证明 \(\ell=n_3\)；
   - 得到 \(0\le g\le\min(s_2-1,s_1+1)\)；
   - 建立
     \[
     R=\frac{P+\theta r_3}{1+\theta},
     \qquad
     \frac1{10Q}\le\theta<\frac1Q;
     \]
   - 推出 A1 universal rational-contact quadratic 与判别平方；
   - 对 saturated 支给出新的整数平方与 denominator certificate。

2. [`a1-denominator-funnel-2026-08-16.md`](a1-denominator-funnel-2026-08-16.md)
   - 推出整个 A1 的整数平方证书
     \[
     W^2=T^2K-2Tb_3DN;
     \]
   - 推出
     \[
     b_3\mid10^{2m_3}Q^2G;
     \]
   - 因而若
     \[
     b_3=h2^u5^v,\qquad\gcd(h,10)=1,
     \]
     则
     \[
     h\mid Q^2G.
     \]

3. [`a1-resonance-collapse-2026-08-16.md`](a1-resonance-collapse-2026-08-16.md)
   - 以
     \[
     x=u-\ell,\qquad y=v-\ell
     \]
     为偏移坐标；
   - 证明任意至少含一个 `2/5` resonance 的状态固定前缀下只剩有限 offset；
   - 每个固定 offset 与根号符号至多对应一个 \(\ell\)。

4. [`a1-cross-corridor-reduction-2026-08-16.md`](a1-cross-corridor-reduction-2026-08-16.md)
   - 双非 resonance 的四象限中 `++`、`--` 自动有限；
   - 唯一看似无界的形状只剩两条交叉走廊；
   - 建立 universal factor-pair identity
     \[
     (TGC-W)(TGC+W)=TDN(TD+2b_3).
     \]

5. [`a1-cross-corridor-primitive-collapse-2026-08-16.md`](a1-cross-corridor-primitive-collapse-2026-08-16.md)
   - 使用原问题的 \(\gcd(a_3,b_3)=1\)；
   - 在 `2+5-` 走廊用二进归一化分子赋值给出显式 `x` 上界；
   - 在 `2-5+` 走廊用五进赋值给出显式 `y` 上界；
   - 因而两个交叉走廊也 fixed-prefix finite；
   - 得到完整的 **A1 fixed-prefix finite theorem**。

6. [`a1-safe-integer-gap-recovery-2026-08-16.md`](a1-safe-integer-gap-recovery-2026-08-16.md)
   - 重新接回整数球面；
   - 定义
     \[
     E=Cq-DH,\qquad U=H-y_3;
     \]
   - 严格推出
     \[
     10^\ell E=b_3U;
     \]
   - 若
     \[
     \delta=\gcd(10^\ell,b_3),\quad
     L=10^\ell/\delta,\quad
     \tau=b_3/\delta,
     \]
     则存在正整数 gap 参数 `A` 满足
     \[
     \boxed{U=LA,\qquad E=\tau A};
     \]
   - 从而安全恢复
     \[
     LA(H+y_3)=y_1^2+y_2^2.
     \]

---

# 33. 当前严格状态与审计边界

## 33.1 已严格完成

当前新框架已经证明：

\[
\boxed{
\text{对任意固定前两块 }(a_1,b_1,a_2,b_2),
\text{ A1 第三块候选集合有限。}
}
\]

更具体地，第三分母的非 `2,5` 部分由 `Q^2G` 控制，所有 `2/5` resonance、同向非 resonance、两条交叉非 resonance 都不能承载固定前缀下的无界尾族。

因此 A1 的研究核心已经从“第三尾是否无界”转移到“移动前缀本身是否可能”。

## 33.2 仍待证明

上面的 fixed-prefix finite theorem **不能**推出所有前缀的并集有限，也不能推出 A1 已全局为空。

剩余目标是：利用前缀对象

\[
C=a_1 10^{n_2}+a_2,
\quad
D=10^gQ,
\quad
G=b_1b_2,
\quad
N=(a_1b_2)^2+(a_2b_1)^2,
\]

以及

\[
K=G^2C^2-D^2N
\]

的 contact 必要条件，继续限制移动前缀，直到得到全局矛盾或真正 prefix-uniform 的有限盒。

## 33.3 旧统一正规化的审计警告

旧公共框架曾定义

\[
\delta=\gcd(10^\ell,b_3)
\]

后又使用类似 `a_3/\delta` 的第三分子整数化。由于原问题有

\[
\gcd(a_3,b_3)=1,
\]

而 `\delta\mid b_3`，故除 `\delta=1` 外不能无条件有 `\delta\mid a_3`。

因此当前 A1 主线只使用 §32 第 6 项中的安全 gap parameter `A`，不使用 `a_3/\delta` 作为整数 primitive numerator。
