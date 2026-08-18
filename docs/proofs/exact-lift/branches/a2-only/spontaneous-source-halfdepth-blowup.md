# A2 source odd-extra 在 half-depth saturation 后的 two-orientation blow-up

> **依赖：** `spontaneous-source-primary-bridge.md`、`spontaneous-source-depth-transfer.md`、`spontaneous-source-equal-depth-nogo.md`、`spontaneous-source-common-gate.md`。
>
> **严格状态：**source base primary `p^{2h}` 对 angle parity为偶；真正可能贡献 odd angle residual 的只有 equal-depth shell `v_p(d)=h` 加 normalized angle cancellation。本文把这个唯一危险 shell 与 source→additive-common 的 half-depth saturation `v_p(C_src)>=h` 联立，在 source double-sphere center做 blow-up。结论是：angle extra condition一旦成立，normalized sphere discriminant自动成为非零平方，产生两个严格不同的 simple orientations；超过 half-depth 的 additive lift分别落在两条互斥的 affine gate上，每条对 normalized `C_src` 都有 unit slope。因此 source odd-extra + common saturation不会产生新的 singular Hensel tree。simple affine decimal synchronization仍可能存在，故 A2 仍未全局关闭。

---

## 1. equal-depth source 坐标

固定 genuine non-`3` inert source prime

\[
p^{2h}\Vert\sigma,
\qquad h\ge1.
\]

真正可能产生 angle-over-source extra depth的唯一 shell为

\[
\boxed{v_p(d)=h,}
\qquad
 d:=225x^2-y,
\tag{1.1}
\]

同时

\[
\boxed{v_p(\Phi_s)=2h.}
\tag{1.2}
\]

令

\[
\boxed{d=p^hD,\qquad D\in\mathbf Z_p^\times,}
\tag{1.3}
\]

\[
\boxed{\Phi_s=p^{2h}\phi.}
\tag{1.4}
\]

写

\[
A_s:=99x-4,
\qquad
r_0:=\frac{2(x+2)}{A_s},
\]
则

\[
r_s=r_0+\frac{p^{2h}\phi}{A_s}.
\tag{1.5}
\]

source double-sphere center由 `spontaneous-source-depth-transfer.md` 给出：

\[
\boxed{
\bar\zeta_s
=\frac{x^2(297x-12)^2}{16(x+2)^2}.}
\tag{1.6}
\]

令真实 third-numerator phase写成

\[
\boxed{
\bar\zeta=\bar\zeta_s+p^h Z.}
\tag{1.7}
\]

---

## 2. `已严格完成`：sphere 的 normalized blow-up quadratic

把

\[
y=225x^2-p^hD,
\]

\[
r_s=r_0+p^{2h}\phi/A_s,
\qquad
\bar w=x/r_s,
\]
以及 (1.7) 代入 exact sphere。前 `p^0` 与 `p^h` coefficient均精确消失；除以 `p^{2h}` 再模 `p` 得

\[
\boxed{
\mathcal B_{\rm sph}(Z;D,\phi)
=a_ZZ^2+b_ZDZ+c_DD^2+c_\phi\phi=0,}
\tag{2.1}
\]

其中

\[
\boxed{a_Z=-4x^2(25x^2+1),}
\tag{2.2}
\]

\[
\boxed{
b_Z=-\frac{x^4(99x-4)^2}{2(x+2)^2},}
\tag{2.3}
\]

\[
\boxed{
 c_D=-\frac{x^2(99x-4)^2
(81x^2-36x+8)(121x^2+44x+8)}
{1600(x+2)^4},}
\tag{2.4}
\]

\[
\boxed{
 c_\phi=
\frac{81x^5(99x-4)^3(101x^2+4x+8)^2}
{512(x+2)^5}.}
\tag{2.5}
\]

所有 denominator在 genuine source channel中为 units。`a_Z` 是 source-slice sphere 的 unit quadratic coefficient。

---

## 3. sphere branch collision 的一般 discriminant

对 (2.1) 视为 `Z` 的 quadratic，直接因式分解：

\[
\boxed{
\begin{aligned}
\operatorname{Disc}_Z(\mathcal B_{\rm sph})
={}&
\frac{x^4(99x-4)^2(101x^2+4x+8)^2}
{800(x+2)^5}\\
&\cdot\left[
-8(x+2)D^2
+2025x^3(99x-4)(25x^2+1)\phi
\right].
\end{aligned}}
\tag{3.1}
\]

所以一般 source half-depth sphere collision对应最后方括号为零。本文真正关心的是它能否与 **odd angle-extra** 同时发生。

---

## 4. `已严格完成`：odd angle-extra 自动把 sphere discriminant变成非零平方

`spontaneous-source-primary-bridge.md` / `...equal-depth-nogo.md` 的 normalized angle extra condition在本文坐标中为

\[
\boxed{
\phi
=
\frac{8(x+2)}{50625(99x-4)x^5}D^2
\pmod p.}
\tag{4.1}
\]

把 (4.1) 代入 (3.1)，全部高次项塌掉：

\[
\boxed{
\operatorname{Disc}_Z
=
\frac{
D^2x^2(99x-4)^2(101x^2+4x+8)^2
}{2500(x+2)^4}.}
\tag{4.2}
\]

在 genuine pure source channel：

\[
p\nmid D\,x(x+2)(99x-4),
\]
且 source slice 上

\[
\boxed{
A_-ig|_{y=225x^2}
=-50625x^4(101x^2+4x+8).}
\tag{4.3}
\]

旧 `A_-=0` 已归入 common-`alpha` boundary，不属于 pure spontaneous/source channel。因此

\[
p\nmid101x^2+4x+8.
\tag{4.4}
\]

于是 (4.2) 是严格非零平方：

\[
\boxed{
\text{odd source angle-extra}
\Longrightarrow
\text{half-depth sphere 有两个不同 roots}.}
\tag{4.5}
\]

尤其 angle extra 与 sphere blow-up collision **不能同时发生**。

也可直接比较两种 `phi`：sphere collision要求

\[
\phi=\frac{8(x+2)}{2025x^3(99x-4)(25x^2+1)}D^2,
\]
而 angle extra要求 (4.1)。二者相等会强迫

\[
25x^2+1=25x^2,
\]
即 `1=0`，在任何 prime上都不可能。

---

## 5. `已严格完成`：两个 normalized sphere orientations 显式线性化

在 angle-extra condition (4.1) 下，(2.1) 的两个 roots精确为

\[
\boxed{Z_1=c_1D,\qquad Z_2=c_2D,}
\tag{5.1}
\]

其中

\[
\boxed{
 c_1=
-\frac{(99x-4)(99x^2-4x-8)}
{400x(x+2)^2},}
\tag{5.2}
\]

\[
\boxed{
 c_2=
-\frac{(99x-4)(2475x^4-100x^3+101x^2+4x+8)}
{400x(x+2)^2(25x^2+1)}.}
\tag{5.3}
\]

其差完全因子化：

\[
\boxed{
 c_2-c_1
=-\frac{(99x-4)(101x^2+4x+8)}
{200x(x+2)^2(25x^2+1)}.}
\tag{5.4}
\]

由 genuine units与 (4.4)：

\[
\boxed{c_2-c_1\in\mathbf Z_p^\times.}
\tag{5.5}
\]

所以两个 source-sphere orientations在 blow-up 后不是“同一个 root 的两种写法”，而是严格分离的两个 simple directions。

---

## 6. additive root在 half-depth 的 affine 坐标

source→common half-depth saturation定义为

\[
\boxed{v_p(\mathcal C_{\rm src})\ge h.}
\tag{6.1}
\]

令

\[
\boxed{C^\sharp:=\mathcal C_{\rm src}/p^h\pmod p.}
\tag{6.2}
\]

若实际 depth `>h`，则 `C^sharp=0`。

由 source-slice exact distance identity：

\[
\bar\zeta_\Theta(x,y_0,\tau)-\bar\zeta_s
=
\frac{\mathcal C_{\rm src}}
{144(x+2)^2(50x^2+2-\tau)},
\]
定义 unit

\[
\boxed{
 u_C:=\frac1{144(x+2)^2(50x^2+2-\tau)}.}
\tag{6.3}
\]

另一方面 `y=y_0-p^hD`。additive affine root对 `d=y_0-y` 的一阶 coefficient为

\[
\boxed{
 c_\Theta
=-\frac{
104\tau^2-8019\tau x^2+324\tau x
+200475x^4-8100x^3+8019x^2-324x
}
{324(50x^2+2-\tau)^2}.}
\tag{6.4}
\]

因此

\[
\boxed{
\frac{\bar\zeta_\Theta-\bar\zeta_s}{p^h}
\equiv
u_CC^\sharp+c_\Theta D
\pmod p.}
\tag{6.5}
\]

---

## 7. 超过 half-depth 的 additive/common lift只有两条 simple affine gate

在 angle-extra source branch上，真实 sphere orientation必须是 (5.1) 的其中之一。若 additive depth要从 baseline `h` 再提升至少一层，就必须使 normalized additive root与该 sphere root一致：

\[
\boxed{
\mathcal F_i(C^\sharp,D)
:=u_CC^\sharp+(c_\Theta-c_i)D
=0,
\qquad i=1,2.}
\tag{7.1}
\]

因为 `u_C` 为 unit：

\[
\boxed{
\frac{\partial\mathcal F_i}{\partial C^\sharp}=u_C\ne0.}
\tag{7.2}
\]

所以每条 orientation gate 对 normalized `C_src` 都是 simple linear Hensel equation。

而两条 gate的差为

\[
\boxed{
\mathcal F_1-\mathcal F_2
=(c_2-c_1)D.}
\tag{7.3}
\]

由 `D` unit及 (5.5)：

\[
\boxed{
\mathcal F_1=\mathcal F_2=0
\quad\text{不可能}.}
\tag{7.4}
\]

因此超过 source half-depth的 additive lift最多选择一个 sphere orientation；不存在 branch collision。

---

## 8. source odd residual + common saturation 的最终局部分类

对真正会影响 angle mod-4 parity 的 source residual，局部结构现在是：

1. source base primary：`2h`，严格偶深；
2. equal-depth angle-extra：由 (4.1) 唯一固定 normalized `phi`；
3. 若 `C_src` 未达 `h`，`spontaneous-source-depth-transfer.md` 已精确读取 common depth；
4. 若 `C_src` 达到 `h`，sphere blow-up自动分裂成两个不同 orientations；
5. additive/common 若继续超过 `h`，只能命中两条互斥且 unit-slope 的 affine gate (7.1)。

所以

\[
\boxed{
\text{source odd angle residual}
+\text{half-depth common saturation}
\text{ 不会产生新的 singular Hensel tree}.}
\tag{8.1}

剩余困难完全变成 simple branch 与真实 decimal/natural representative的同步，而不是 source local singularity。

这使 source pool与 denominator pool的最终形态高度一致：两者的 singular mechanisms都已剥掉，只剩 simple depth/orbit allocation。