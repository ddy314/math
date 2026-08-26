# A1 minimal diagonal: normalized complement shell for the full 2-high master

> 日期：2026-08-26。依赖 `deep-double-2high-master.md`、`deep-complement-height.md`、`deep-contact-sign-window.md` 与 `deep-hl-one-exponent-divisor-family.md`。当前统一 frontier 为 `k>=32`。
>
> 本文适用于全部 surviving double-deep 2-high / 5-low master states：既包括 moderate `HL` (`eta<=0`)，也包括原 2-extreme `E_2` (`eta>0`)。

本文把 stripped complement equation

\[
2\beta u-\alpha v=5^d
\]

进一步改写成一个单整数 `R` 的固定尺度问题。核心结论是：虽然 `d` 仍然无界，但

\[
\frac{R}{5^d}
\]

始终落在一个绝对固定区间；对 moderate HL，六类型还能得到显式有限 leading-slot 区间。同时，`R` 只允许一个由 `(alpha,beta)` 决定的 CRT residue class，并自动产生两个此前未单独记录的 cross-coprimality 条件。

状态：**归一化、CRT lock 与 cross-coprimality 严格完成；本结果不关闭 full 2-high master。**

---

## 1. master 输入

沿用

\[
T=10^k,
\qquad
D=2^{2k+3+\eta}5^B,
\qquad
Y=B+\nu_5<k+1,
\]

\[
\boxed{d:=k+1-Y>0,}
\]

以及

\[
\boxed{\alpha\beta=r_{10},}
\qquad
\boxed{\gcd(\alpha,\beta)=1,}
\qquad
(\alpha\beta,10)=1.
\]

complementary divisors 为

\[
su=b_1,
\qquad
qv=Q,
\]

其中

\[
b_1=10^{2k+1}-w,
\qquad
Q=10^{2k+2}-(10w-1).
\]

完整 2-high master 的 stripped complement equation 是

\[
\boxed{2\beta u-\alpha v=5^d.}
\tag{1}
\]

再记 bounded renormalized factor parameter

\[
\boxed{\xi:=\frac tD
=2^{-\eta}5^{B+2\nu_5}r_{10}.}
\tag{2}
\]

已有

\[
196000<\xi<15214000,
\]

而 contact-sign window 给更强的 typewise lower bounds。

complement height 记为

\[
\boxed{\mu:=\frac{MD}{T^2},}
\qquad
M:=uv,
\]

并有

\[
\boxed{1000<\mu<10001.}
\tag{3}

---

## 2. 引入单一 complement coordinate `R`

定义

\[
\boxed{R:=2\beta u+\alpha v.}
\tag{4}
\]

由 (1)：

\[
\boxed{R-5^d=2\alpha v,}
\tag{5}
\]

\[
\boxed{R+5^d=4\beta u.}
\tag{6}
\]

所以 `(u,v)` 可由 `(d,R)` 唯一恢复：

\[
\boxed{u=\frac{R+5^d}{4\beta},}
\tag{7}
\]

\[
\boxed{v=\frac{R-5^d}{2\alpha}.}
\tag{8}
\]

这已经把 one-exponent family 的两个 complementary divisors 换成一个整数 `R`。

两式相乘还给出

\[
\boxed{R^2-5^{2d}=8\alpha\beta uv=8r_{10}M.}
\tag{9}
\]

---

## 3. `eta` 完全消失的 normalized shell identity

由

\[
T^2=2^{2k}5^{2k},
\qquad
D=2^{2k+3+\eta}5^B,
\]

以及

\[
2d=2k+2-2B-2\nu_5,
\]

直接计算：

\[
\frac{T^2}{D5^{2d}}
=2^{-3-\eta}5^{B+2\nu_5-2}.
\tag{10}
\]

另一方面 (2) 给

\[
\xi=2^{-\eta}5^{B+2\nu_5}r_{10}.
\]

因此

\[
\boxed{
r_{10}\frac{T^2}{D5^{2d}}
=\frac{\xi}{200}.}
\tag{11}
\]

再用 `M=mu*T^2/D`：

\[
\boxed{
\frac{r_{10}M}{5^{2d}}
=\frac{\mu\xi}{200}.}
\tag{12}
\]

把 (12) 代入 (9)，得到主恒等式

\[
\boxed{
\left(\frac{R}{5^d}\right)^2
=1+\frac{\mu\xi}{25}.}
\tag{13}
\]

关键点是：右侧完全没有 `k,eta,A,B,nu_5` 的独立大尺度因子。moderate HL 与原 `E_2` 在这个坐标中真正共享同一固定 shell。

---

## 4. full master 的绝对固定 shell

六类型 contact-sign lower 中最弱的是 `(z,w)=(1,4)`：

\[
\boxed{\xi>357209.975.}
\]

结合 `mu>1000`：

\[
1+\frac{\mu\xi}{25}
>
1+40\cdot357209.975
=14288400
=3780^2.
\]

因此

\[
\boxed{\frac{R}{5^d}>3780.}
\tag{14}
\]

上侧使用

\[
\mu<10001,
\qquad
\xi<15214000.
\]

于是

\[
\left(\frac{R}{5^d}\right)^2
<1+\frac{10001\cdot15214000}{25}
=6086208561.
\]

而

\[
6086208561<78015^2=6086340225.
\]

所以

\[
\boxed{3780<\frac{R}{5^d}<78015.}
\tag{15}
\]

这对 **全部** surviving double-deep 2-high master 成立。

定义 leading slot

\[
\boxed{m:=\left\lfloor\frac{R}{5^d}\right\rfloor.}
\]

则无论 `k` 与 `eta` 多大：

\[
\boxed{3780\le m\le78014.}
\tag{16}
\]

所以 leading quotient 只有

\[
\boxed{74235}
\]

个绝对有限槽位。

---

## 5. moderate HL 的 typewise leading-slot 区间

moderate 中

\[
\eta=-v_2(r),
\qquad
\xi=r\in\mathbf Z.
\]

使用 contact-sign sharpened lower bounds 与 moderate typewise `r` upper windows：

\[
\boxed{
\begin{array}{c|c|c|c}
(z,w)&\xi_{\min}\text{ strict}&r_{\max}&m\text{ 必须位于}\\ \hline
(1,1)&973439.975&10885221&6240\le m\le65988\\
(1,2)&734409.975&8400003&5420\le m\le57968\\
(1,3)&528999.975&6236387&4600\le m\le49948\\
(1,4)&357209.975&4394372&3780\le m\le41927\\
(3,1)&519839.975&15204352&4560\le m\le77989\\
(3,2)&428489.975&13677244&4140\le m\le73969
\end{array}}
\tag{17}
\]

lower endpoints 恰好来自 perfect squares：

\[
1+40\xi_{\min}
=
6240^2,5420^2,4600^2,3780^2,4560^2,4140^2
\]

按表中顺序。

upper endpoints 则来自

\[
\left(\frac R{5^d}\right)^2
<1+\frac{10001r_{\max}}{25}.
\]

六类型 slot 数分别为

\[
59749,52549,45349,38148,73430,69830.
\]

这仍然没有关闭 `d`，但把旧的 unbounded lattice coefficient 换成了一个 absolute finite leading slot。

---

## 6. exact CRT lock

(5)-(6) 立即给

\[
\boxed{R\equiv5^d\pmod{2\alpha},}
\tag{18}
\]

\[
\boxed{R\equiv-5^d\pmod{4\beta}.}
\tag{19}
\]

由于

\[
\gcd(2\alpha,4\beta)=2
\]

且两个右端模 2 一致，CRT compatibility 自动成立；模

\[
\operatorname{lcm}(2\alpha,4\beta)=4\alpha\beta=4r_{10}
\]

只有唯一 residue class。

因为 `5` 与 `4r_10` 互素，可把 `5^d` 除掉。定义唯一 residue

\[
\boxed{x_{\alpha,\beta}\pmod{4r_{10}}}
\]

满足

\[
\boxed{x_{\alpha,\beta}\equiv1\pmod{2\alpha},}
\tag{20}
\]

\[
\boxed{x_{\alpha,\beta}\equiv-1\pmod{4\beta}.}
\tag{21}
\]

则任何 candidate 必须满足固定 CRT ray

\[
\boxed{
R\equiv x_{\alpha,\beta}5^d
\pmod{4r_{10}}.}
\tag{22}
\]

因此对 fixed `(alpha,beta)`，`R` 的 residue dependence on `d` 只剩 `5^d mod 4r_10` 的有限周期。

---

## 7. cross-coprimality

由 (1)：

\[
2\beta u-\alpha v=5^d.
\]

注意

\[
5\nmid\alpha\beta uv.
\]

若某个素数同时整除 `alpha*v` 与 `2*beta*u`，它也整除两者之差 `5^d`；但该公共因子不含 5，因此只能为 1。于是

\[
\boxed{\gcd(\alpha v,2\beta u)=1.}
\tag{23}
\]

这立即给出此前未单独记录的两条 cross locks：

\[
\boxed{\gcd(\alpha,u)=1,}
\tag{24}
\]

\[
\boxed{\gcd(\beta,v)=1.}
\tag{25}
\]

并重新包含已有的

\[
\gcd(\alpha,\beta)=1,
\qquad
\gcd(u,v)=1.
\]

从 (5)-(6) 还可写成 exact near-factor gcd：

\[
\boxed{
\gcd(R-5^d,R+5^d)=2.}
\tag{26}
\]

---

## 8. 2-adic signature of `R`

`alpha,beta,v` 都是奇数，所以 (5) 给

\[
\boxed{v_2(R-5^d)=1.}
\tag{27}
\]

whole-block selector `s` 为奇数，因此

\[
v_2(u)=v_2(b_1)=v_2(w)=:e.
\]

由 (6)：

\[
\boxed{v_2(R+5^d)=2+e.}
\tag{28}
\]

特别地，由 `5^d=1 mod4`：

\[
\boxed{R\equiv3\pmod4.}
\tag{29}
\]

而六类型按 `w` 还精确知道 `R+5^d` 的 2-adic valuation：

- `w=1,3`: `v_2(R+5^d)=2`；
- `w=2`: `v_2(R+5^d)=3`；
- `w=4`: `v_2(R+5^d)=4`。

---

## 9. prime-source 的直接新过滤

`u=b_1/s` 中，selector `s` 只能使用 `b_1` 的 `1 mod4` whole prime-power blocks。因此若

\[
p\equiv3\pmod4,
\qquad p\mid b_1,
\]

则整个 `p`-primary block 必留在 `u`。

结合 (24)：

\[
\boxed{
p\equiv3\pmod4,\ p\mid\alpha
\Longrightarrow p\nmid b_1.}
\tag{30}
\]

在 moderate one-exponent coordinates 中

\[
b_1(d)=10^{2d+2Y-1}-w,
\]

所以对 fixed `p|alpha`，(30) 是 `d mod ord_p(10)` 的一个 **finite periodic exclusion**。

一个立即可用的固定推论是：`w=1,4` 时 `3|b_1` 恒成立，因此

\[
\boxed{w\in\{1,4\}\Longrightarrow3\nmid\alpha.}
\tag{31}
\]

若此时 `3|r_10`，whole 3-primary block 只能分给 `beta`。

Q-side 同理，由 (25)：

\[
\boxed{p\mid\beta,\ p\mid Q\Longrightarrow p\nmid v.}
\tag{32}
\]

因为 `qv=Q`，这意味着该 `p`-primary block 在 Q 中必须全部进入 selected factor `q`。于是 fixed `beta` 与 periodic condition `p|Q(d)` 可以直接标出 contact-square 的 selected Q-block，而无需先 factor 整个 `Q`。

例如 `w=2` 时

\[
Q=10^{2k+2}-19\equiv0\pmod9,
\]

所以若 `3|beta`，则 Q 的整个 3-primary block 必进入 `q`。

---

## 10. one-exponent family 的新接口

moderate HL 原来写成

\[
\boxed{
\begin{aligned}
&u\mid10^{2d+2Y-1}-w,\\
&v\mid10^{2d+2Y}-(10w-1),\\
&2\beta u-\alpha v=5^d.
\end{aligned}}
\]

现在可等价地从单整数 `R` 出发：

\[
\boxed{
\begin{aligned}
&3780\cdot5^d<R<78015\cdot5^d,\\
&R\equiv x_{\alpha,\beta}5^d\pmod{4r_{10}},\\
&u=(R+5^d)/(4\beta),\\
&v=(R-5^d)/(2\alpha),\\
&u\mid10^{2d+2Y-1}-w,\\
&v\mid10^{2d+2Y}-(10w-1),\\
&\gcd(\alpha,u)=\gcd(\beta,v)=1.
\end{aligned}}
\tag{33}
\]

moderate 时第一行应替换成 (17) 的 typewise slot interval。

因此 unbounded arithmetic 可以重新组织成：

\[
\boxed{
\text{fixed finite signature}
+(d,R),
}
\]

其中 `R/5^d` 只有 absolute finite leading slots，且 `R` 处于一个固定 CRT ray。下一步最自然的 certificate 应按 `(w,Y,alpha,beta,m)` 组织，再对 `d` 的 periodic prime-source exclusions 做 cover，而不再扫描 arbitrary divisor pairs `(u,v)`。

---

## 11. 依赖审计

(13) 与 four-factor complement square 是同一个结构的归一化版本；因此它**不能**被当作独立于 four-factor frame 的第二个平方条件重复计数。

本文真正新增的价值是：

1. 把 full master 的 complement scale 精确压到 `R~5^d`，并消掉 `eta`；
2. 把 one-exponent lattice 的 leading quotient 压成绝对有限 slots；
3. 提取 fixed CRT ray (22)；
4. 显式提取 cross-coprimality (24)-(25)，从而得到 periodic prime-source filter (30)-(32)。

这些都是 full four-factor skeleton 的严格后果，适合作为下一阶段 modular / primitive-block certificate 的输入；它们本身不宣称关闭 A1 或 full 2-high master。
