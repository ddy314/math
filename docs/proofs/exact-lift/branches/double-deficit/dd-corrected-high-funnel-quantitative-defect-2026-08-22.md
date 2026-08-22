# DD corrected high-funnel 的 quantitative defect inequality

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-high-funnel-schmidt-2026-08-22.md`](dd-corrected-high-funnel-schmidt-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` high funnel 的渐近 quantitative stability）。**
> 本文不添加新的 global slope；它把原来“达到 `6.308883...` 等号时各 defect 必须趋零”加强为一个显式线性 defect lower bound。

## 1. 记号

令

\[
a:=\log_{10}2,
\qquad
b:=1-a=\log_{10}5,
\]

\[
A:=\frac{2(1+2a)}3,
\qquad
\lambda:=\frac{2+a}{1+2a}.
\]

则

\[
\lambda A=\frac{2(2+a)}3.
\]

corrected frontier constant 为

\[
\boxed{
c_*:=2+3\lambda
=\frac{8+7a}{1+2a}
=6.308883577618031\ldots.}
\tag{1.1}
\]

沿任意 high-funnel subsequence，使用 normalized variables

\[
\mathcal N:=\frac nS,
\quad M:=\frac mS,
\quad Q_2,N_2,Q_5,G_5,N_5,R\ge0.
\]

## 2. 两个 corrected 输入

`dd-corrected-high-funnel-schmidt-2026-08-22.md` 给出 stability：

\[
\boxed{
\mathcal N
\le
2+\frac{2(2+a)}3M
-\frac{2b}{3}Q_5
+\frac{2b}{3}G_5
-\frac b3N_5
+R+o(1).
}
\tag{2.1}
\]

以及 safe Schmidt budget：

\[
\boxed{
AM+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R
\le3+o(1).
}
\tag{2.2}
\]

定义 normalized Schmidt slack

\[
\boxed{
\sigma_S
:=
3-\left[
AM+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R
\right].
}
\tag{2.3}
\]

在渐近意义下 `sigma_S>=-o(1)`；若把 `(2.2)` 的 `o(1)` 吸收进 slack，则可取非负版本。

## 3. 直接消去 `M`

由 `(2.3)`：

\[
3\lambda-\lambda AM
=
\lambda\sigma_S
+2a\lambda Q_2+a\lambda N_2
+\frac{2b\lambda}{3}Q_5
+\frac{4b\lambda}{3}G_5
+\frac{b\lambda}{3}N_5
+2\lambda R.
\tag{3.1}
\]

而

\[
\lambda A=\frac{2(2+a)}3.
\]

从 `(2.1)`：

\[
\begin{aligned}
c_*-\mathcal N
\ge{}&
3\lambda-\lambda AM
+\frac{2b}{3}Q_5
-\frac{2b}{3}G_5
+\frac b3N_5-R-o(1).
\end{aligned}
\]

代入 `(3.1)` 得到：

\[
\boxed{
\begin{aligned}
c_*-\mathcal N
\ge{}&
\lambda\sigma_S
+2a\lambda Q_2
+a\lambda N_2\\
&+\frac{2b(\lambda+1)}3Q_5
+\frac{2b(2\lambda-1)}3G_5\\
&+\frac{b(\lambda+1)}3N_5
+(2\lambda-1)R
-o(1).
\end{aligned}}
\tag{Quantitative-defect}
\]

所有显示 coefficient 都严格为正。

## 4. 数值 coefficient

\[
\lambda=1.436294525872677\ldots,
\]

因此 `(Quantitative-defect)` 中：

\[
\boxed{
\begin{array}{c|c}
\text{defect}&\text{coefficient}\\ \hline
Q_2&0.864735469791304\ldots\\
N_2&0.432367734895652\ldots\\
Q_5&1.135264530208696\ldots\\
G_5&0.872589051745354\ldots\\
N_5&0.567632265104348\ldots\\
R&1.872589051745354\ldots\\
\sigma_S&1.436294525872677\ldots
\end{array}}
\tag{4.1}
\]

## 5. `epsilon`-neighborhood rigidity

若某一 subsequence 满足

\[
\mathcal N\ge c_*-\varepsilon+o(1),
\]

则由 `(Quantitative-defect)`，逐项有

\[
Q_2\le\frac{\varepsilon}{0.864735469791\ldots}+o(1),
\]

\[
N_2\le\frac{\varepsilon}{0.432367734896\ldots}+o(1),
\]

\[
Q_5\le\frac{\varepsilon}{1.135264530209\ldots}+o(1),
\]

\[
G_5\le\frac{\varepsilon}{0.872589051745\ldots}+o(1),
\]

\[
N_5\le\frac{\varepsilon}{0.567632265104\ldots}+o(1),
\]

\[
R\le\frac{\varepsilon}{1.872589051745\ldots}+o(1),
\]

并且 Schmidt budget slack 本身也只有

\[
\sigma_S\le\frac{\varepsilon}{1.436294525873\ldots}+o(1).
\]

因此 corrected terminal geometry 不只是 equality-ray rigidity；它有显式线性 stability：

\[
\boxed{
\mathcal N\to c_*
\Longrightarrow
Q_2,N_2,Q_5,G_5,N_5,R,\sigma_S\to0
}
\]

且收敛速度由 `c_*-mathcal N` 线性控制。

## 6. 用途与边界

这条式子的作用是把未来任何新的 positive payer 立即转换成显式 slope gap：

- 若可证明某个 defect `X>=eta>0`，则立刻有 `mathcal N<=c_*-c_X eta+o(1)`；
- 若某个 global theorem 只在 `epsilon`-terminal neighborhood成立，`(Quantitative-defect)` 可把所有 2/5-adic 与 rough-overlap参数统一限制为 `O(epsilon)`；
- 因此后续不必重新解整个 linear program。

本文本身没有证明任何 defect 有 uniform positive lower bound，所以没有把 `<=c_*` 升级为显式 `<c_*-epsilon_0`。

## 7. 状态摘要

- **已严格完成：** `(Quantitative-defect)` 与所有正 coefficient。
- **新接口：** corrected terminal 的显式 `epsilon`-neighborhood rigidity。
- **仍待证：** 在该薄邻域中找一个不由旧 normalization / hidden-square / exact-lift identities重复支付的 uniform positive defect；DD strict gap、空性与有效绝对高度界。
