# `A_1`-only 分支

本文件对应原总稿 §§28–31。它包含薄环约束、尾商斜率锁、saturated `L = 1` 支、denominator-only 尾长界和 saturated 支的奇素数约束。

> 迁移说明：以下正文由原始总稿机械拆分，公式和证明状态不作数学改写。
# 28. \(A_1\)-only 分支

\(A_1\)-only 满足

\[
s_3\le0,
\qquad
s_2+s_3>0.
\]

统一记

\[
\boxed{
g=-s_3\ge0,
}
\]

\[
\boxed{
k_{12}=s_2+s_3\ge1.
}
\]

有效第三尾长为

\[
\boxed{
\ell=m_3-g.
}
\]

定义

\[
U=H-y_3,
\qquad
\mathcal S_{12}=y_1^2+y_2^2.
\]

经过第三块正规化，同样有

\[
\boxed{
U=La,
\qquad
La\mid\mathcal S_{12}.
}
\]

并且

\[
H
=
\frac12
\left(
La+\frac{\mathcal S_{12}}{La}
\right),
\]

\[
y_3
=
\frac12
\left(
\frac{\mathcal S_{12}}{La}
-La
\right).
\]

---

## 28.1 薄环约束

由第一坐标 carrier 及球面条件可得到 \(La\) 必须处在一个很薄的实数区间：

\[
\boxed{
10^{k_{12}}y_1
-
\sqrt{
(10^{2k_{12}}-1)y_1^2-y_2^2
}
<
La
<
\sqrt{\mathcal S_{12}}.
}
\]

这说明 tail gap 并非可以任意选取二平方和的除数，并且必须同时处在一个很窄的几何环带中。

---

## 28.2 尾商斜率锁

第三分母正规化进一步给出

\[
\boxed{
10^{g-1}
\le
\frac{\tau}{L}
<
10^g.
}
\]

因此 \(g\) 直接锁定 normalized denominator quotient 的数量级。

---

# 29. \(A_1\) 的 saturated 支 \(L=1\)

当

\[
L>1
\]

时，高斯因子转移至少存在严格尺度变化。

真正特殊的是

\[
\boxed{
L=1.
}
\]

这等价于有效尾幂

\[
10^\ell
\]

已经全部被第三分母吸收。

旧思路曾希望在这里继续 Gaussian descent，但后来严格检查发现：

\[
\boxed{
L=1
\text{ 时 Gaussian flip 只是 projective identity}.
}
\]

约掉整体尺度后，球面点与线性平面都回到原对象，没有任何严格变小的高度。

所以 saturated 支必须采用独立于 Gaussian descent 的机制。

---

# 30. \(A_1\) saturated 的 denominator-only 尾长界

对整个 saturated 支，可以不再分别处理旧稿中的若干高侧二进/五进子分支，而直接得到

\[
\boxed{
\ell
\le
\left\lfloor
\log_5((10Q+2)G)
\right\rfloor.
\]

粗化为

\[
\boxed{
\ell
\le
3(m_1+m_2)+1.
}
\]

这是一个重要进展：saturated 支原本看似可以任意增长的“有效第三尾长”已经被前两分母位数线性控制。

因此 \(A_1\) 中真正还可能独立无界的量主要变成了 decimal shift

\[
\boxed{
g.
}
\]

---

# 31. \(A_1\) saturated 的奇素数约束

令

\[
d_*=\gcd(\tau,10^gQ),
\]

\[
h=\frac{\tau}{d_*}.
\]

可证明

\[
\boxed{
\gcd(U,h)=1,
}
\]

并且

\[
\boxed{
h\mid G.
}
\]

更强地，\(h\) 的所有奇素因子满足

\[
\boxed{
p\equiv1\pmod4.
}
\]

还有

\[
\boxed{
h
\mid
\frac{
b_1b_2
}{
\gcd(b_1,b_2)^2
}.
}
\]

所以 saturated 第三分母中所有非十进制“新奇素数”都必须来自前两分母的不共享部分，而且只能是 \(1\bmod4\) 素数。

这大幅限制了 denominator prime supply，却仍没有直接给出 \(g\) 的统一上界。

---

# 32. 2026-08-16 A1 独立重建入口

A1 现已增加两份直接从原始拼接恒等式重建的新文件：

- [`a1-rational-contact-framework-2026-08-16.md`](a1-rational-contact-framework-2026-08-16.md)：证明 \(\ell=n_3\)，建立前缀 rational contact 坐标 \((P,\theta)\)，推出 universal 判别平方，并把 saturated 支化为整数平方与整除系统；
- [`a1-denominator-funnel-2026-08-16.md`](a1-denominator-funnel-2026-08-16.md)：推出整个 A1 的整数平方证书
  \[
  W^2=T^2K-2Tb_3D\mathcal N_{12}
  \]
  以及 universal denominator certificate
  \[
  b_3\mid10^{2m_3}Q^2G,
  \]
  从而把第三分母压入固定前缀因子乘 \(2^u5^v\) 的 near-\(S\)-unit funnel。

这两份新文件不依赖 Gaussian flip，并对旧公共框架中的 `z_3=a_3/\delta_3` 整数化步骤提出审计警告。当前 A1 后续应以这套 rational-contact / denominator-funnel 结构为主入口，旧 §§28–31 保留为历史基线，相关旧正规化结论在审计完成前不应自动向新框架迁移。
