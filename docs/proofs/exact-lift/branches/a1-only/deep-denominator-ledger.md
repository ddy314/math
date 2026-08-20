# A1-only Deep Denominator Ledger

> 本文件是细粒度研究记录的机械归并账本。各来源的标题、正文和证明状态原样保留；账本中的局部闭合、有限证书或降级路线均不表示该分支或主不存在性命题已经关闭。

## 来源索引

- [`deep-2high-denominator-cap.md`](#source-deep-2high-denominator-cap)
- [`deep-2high-endpoint-collapse.md`](#source-deep-2high-endpoint-collapse)
- [`deep-2high-mod5-lock.md`](#source-deep-2high-mod5-lock)
- [`deep-2high-mod8-lock.md`](#source-deep-2high-mod8-lock)
- [`deep-2high-q-superlinear.md`](#source-deep-2high-q-superlinear)
- [`deep-b1-block-loss.md`](#source-deep-b1-block-loss)
- [`deep-b1-sharp-mandatory-blocks.md`](#source-deep-b1-sharp-mandatory-blocks)
- [`deep-balanced-collapse.md`](#source-deep-balanced-collapse)
- [`deep-complement-divisor-system.md`](#source-deep-complement-divisor-system)
- [`deep-complement-height.md`](#source-deep-complement-height)
- [`deep-contact-mandatory3-lock.md`](#source-deep-contact-mandatory3-lock)
- [`deep-contact-q-resultant-loss.md`](#source-deep-contact-q-resultant-loss)
- [`deep-contact-q-square-blocks-universal.md`](#source-deep-contact-q-square-blocks-universal)
- [`deep-contact-q-square-blocks.md`](#source-deep-contact-q-square-blocks)
- [`deep-contact-sign-window.md`](#source-deep-contact-sign-window)
- [`deep-double-2high-master.md`](#source-deep-double-2high-master)
- [`deep-double-5high-collapse.md`](#source-deep-double-5high-collapse)
- [`deep-extreme-classification.md`](#source-deep-extreme-classification)
- [`deep-extreme-height-collapse.md`](#source-deep-extreme-height-collapse)
- [`deep-first-complement-remainder.md`](#source-deep-first-complement-remainder)
- [`deep-four-factor-frame.md`](#source-deep-four-factor-frame)
- [`deep-gap-unit-square.md`](#source-deep-gap-unit-square)
- [`deep-gap-valuation-normal-form.md`](#source-deep-gap-valuation-normal-form)
- [`deep-global-factorization.md`](#source-deep-global-factorization)
- [`deep-hl-5adic-hensel-lock.md`](#source-deep-hl-5adic-hensel-lock)
- [`deep-hl-forced-contact-lift.md`](#source-deep-hl-forced-contact-lift)
- [`deep-hl-hensel-dependency-audit.md`](#source-deep-hl-hensel-dependency-audit)
- [`deep-hl-local-signature-count.md`](#source-deep-hl-local-signature-count)
- [`deep-hl-mod4-orientation.md`](#source-deep-hl-mod4-orientation)
- [`deep-hl-one-exponent-divisor-family.md`](#source-deep-hl-one-exponent-divisor-family)
- [`deep-hl-q-superlinear.md`](#source-deep-hl-q-superlinear)
- [`deep-hl-tiny-complements.md`](#source-deep-hl-tiny-complements)
- [`deep-ll-modular-exhaustion.md`](#source-deep-ll-modular-exhaustion)
- [`deep-ll-pell-normal-form.md`](#source-deep-ll-pell-normal-form)
- [`deep-ll-w4-modular-exhaustion.md`](#source-deep-ll-w4-modular-exhaustion)
- [`deep-moderate-adjugate-gcd-lock.md`](#source-deep-moderate-adjugate-gcd-lock)
- [`deep-moderate-block-partition.md`](#source-deep-moderate-block-partition)
- [`deep-moderate-factor-quotients.md`](#source-deep-moderate-factor-quotients)
- [`deep-moderate-factorization.md`](#source-deep-moderate-factorization)
- [`deep-moderate-root-normal-form.md`](#source-deep-moderate-root-normal-form)
- [`deep-moderate-three-pattern.md`](#source-deep-moderate-three-pattern)
- [`deep-q-side-proper-divisor.md`](#source-deep-q-side-proper-divisor)
- [`deep-root-factor-splitting.md`](#source-deep-root-factor-splitting)
- [`deep-single5-contact-dichotomy.md`](#source-deep-single5-contact-dichotomy)
- [`deep-single5-first-remainder-height.md`](#source-deep-single5-first-remainder-height)
- [`deep-typewise-r-window.md`](#source-deep-typewise-r-window)
- [`deep-universal-factorization.md`](#source-deep-universal-factorization)
- [`deep-w1-joint-complement-minimum.md`](#source-deep-w1-joint-complement-minimum)

<a id="source-deep-2high-denominator-cap"></a>

> 整合来源：`deep-2high-denominator-cap.md`

# A1 minimal diagonal: full 2-high denominator cap

> 日期：2026-08-20。依赖 `deep-q-side-proper-divisor.md`、`deep-b1-sharp-mandatory-blocks.md`、`deep-w1-joint-complement-minimum.md`、`deep-complement-height.md` 与 `deep-double-2high-master.md`。当前 `k>=32`。

本文给全部 surviving double-deep 2-high master 的 denominator cap。`w=1` 还使用 u/v 周期不能同时取独立最小值的 joint refinement。

最终：

\[
\boxed{
D<
\begin{cases}
17T^2,&w=1,\\
88T^2,&w=2,\\
1429T^2,&w=3,\\
120T^2,&w=4.
\end{cases}}
\]

状态：**已严格完成。**

---

## 1. independent complement minima

写

\[
u=b_1/s,
\qquad v=Q/q.
\]

Q-side proper-divisor orientation：

\[
\boxed{(v_{\min})=(7,3,7,7).}
\]

`deep-b1-sharp-mandatory-blocks.md`：

\[
\boxed{(u_{\min})=(27,38,1,12).}
\]

所以 independent product minima 为

\[
\boxed{uv\ge(189,114,7,84).}
\tag{1}

---

## 2. w=1 joint improvement

`deep-w1-joint-complement-minimum.md` 利用：

- `v3(b1)=2+v3(2k+1)`；
- `7|Q iff k=0 mod3`；
- `19|Q iff k=4 mod9`；
- `3,11 not|Q`；

证明独立 minima `u=27`,`v=7` 不能同时出现，并最终得到

\[
\boxed{w=1:\quad M=uv\ge621.}
\tag{2}

其余三型暂保留 independent minima：

\[
\boxed{
M\ge
\begin{cases}
114,&w=2,\\
7,&w=3,\\
84,&w=4.
\end{cases}}
\tag{3}

---

## 3. complement-height 转成 D cap

在 double-deep：

\[
\mu:=MD/T^2<10001.
\]

因此

\[
D<\frac{10001}{M}T^2.
\]

由 (2)-(3)：

\[
\boxed{
D<
\begin{cases}
17T^2,&w=1,\\
88T^2,&w=2,\\
1429T^2,&w=3,\\
120T^2,&w=4.
\end{cases}}
\tag{4}

其中 w=1 的精确 ratio 是

\[
10001/621<16.11,
\]

所以 `17T^2` 是整洁 safe cap。

---

## 4. master offset `eta` slope

master：

\[
D=2^{2k+3+\eta}5^B,
\qquad T^2=2^{2k}5^{2k}.
\]

若 `C_w=(17,88,1429,120)`：

\[
2^{3+\eta}5^B<C_w5^{2k}.
\]

所以

\[
\boxed{
\eta<\log_2C_w-3+(2k-B)\log_25.}
\tag{5}

`w=1` 现在尤其强：

\[
\boxed{2^{3+\eta}5^B<17\,5^{2k}.}
\]

---

## 5. complement size endpoint

仍有

\[
M<10001T^2/D.
\]

所以任何更强的 joint lower bound on M 都会立即转成 D/T^2 cap。`w=1` 展示了这种“period-coupled complement minimum”比单独 u/v minima 强得多；后续可对 w=2,3,4继续寻找类似 coupling。

---

<a id="source-deep-2high-endpoint-collapse"></a>

> 整合来源：`deep-2high-endpoint-collapse.md`

# A1 minimal diagonal: top 2-high endpoint collapse

> 日期：2026-08-20。依赖 `deep-b1-sharp-mandatory-blocks.md`、`deep-2high-denominator-cap.md` 与 `deep-double-2high-master.md`。当前 `k>=32`。

当

\[
\delta:=D/T^2
\]

靠近 typewise denominator cap 时，complement product

\[
M=uv<10001/\delta
\]

变成很小的整数。结合 sharpened mandatory blocks、`v` orientation 与 `gcd(u,v)=1`，top endpoint 的 complementary divisors 被唯一锁死。

状态：**已严格完成。**

---

## 1. sharp structural minima

因为

\[
u\mid b_1,
\qquad v\mid Q,
\qquad\gcd(b_1,Q)=1,
\]

有

\[
\boxed{\gcd(u,v)=1.}
\tag{1}

sharpened minima：

\[
\boxed{
\begin{array}{c|c|c|c}
w&u_{\min}&v_{\min}&M_{\min}\\ \hline
1&9&7&63\\
2&38&3&114\\
3&1&7&7\\
4&12&7&84
\end{array}}
\tag{2}

其中 `w=1` 的 `u>=9` 来自 `v3(b1)>=2`；`w=2` 的 `u>=38` 来自 mandatory `3 mod4` odd prime至少 19。

---

## 2. next possible complement product

可安全取：

\[
\boxed{
\begin{array}{c|c}
w&M_{\rm next}\\ \hline
1&99\\
2&186\\
3&11\\
4&132
\end{array}}
\tag{3}

说明：

### w=1

`u` 是 odd multiple of完整 `3^e` block，至少 9；`v>=7`, `v=3 mod4`, 且 `3 not|Q`。

minimum：

\[
9\cdot7=63.
\]

若不取 `(9,7)`，最小下一可能是

\[
9\cdot11=99
\]

（而下一 3-power `27*7=189` 更大）。

### w=2

`u` 必含 fixed 2 与一个至少 19 的 `3 mod4` odd block，所以 minimum `u=38`; `v>=3`。

minimum：

\[
38\cdot3=114.
\]

若 mandatory odd block不是 19，则下一个可能至少 31，故 `u>=62`, 与 `v=3` 给

\[
62\cdot3=186.
\]

另一方面保留 `u=38` 而把 `v` 提到下一个 `3 mod4` unit至少 7，得到 266，更大。所以 next product可取 186。

### w=3

保留 `M_next=11`。

### w=4

保留 `M_next=132`。

---

## 3. sharpened endpoint thresholds

若

\[
\delta>10001/M_{\rm next},
\]

则

\[
M<M_{\rm next}.
\]

结合 `M>=M_min`，只能取 minimum pair。

取整洁 safe thresholds：

\[
\boxed{
\frac D{T^2}>
\begin{cases}
102,&w=1,\\
54,&w=2,\\
910,&w=3,\\
76,&w=4
\end{cases}}
\Longrightarrow
(u,v)=
\begin{cases}
(9,7),&w=1,\\
(38,3),&w=2,\\
(1,7),&w=3,\\
(12,7),&w=4.
\end{cases}}
\tag{4}

注意 `w=2` 的 top endpoint 已从旧 threshold 152 大幅降到 54，而其整个 denominator cap 只有 88。

---

## 4. fixed-coefficient S-unit equations

master complement：

\[
2\beta u-\alpha v=5^d.
\]

代入 (4)：

\[
\boxed{
\begin{array}{c|c}
w&\text{endpoint equation}\\ \hline
1&18\beta-7\alpha=5^d\\
2&76\beta-3\alpha=5^d\\
3&2\beta-7\alpha=5^d\\
4&24\beta-7\alpha=5^d
\end{array}}
\tag{5}

并仍有

\[
\alpha\beta=r_{10},
\qquad\gcd(\alpha,\beta)=1.
\]

---

## 5. supply equation 统一简化

endpoint 中

\[
q=Q/v,
\qquad s=b_1/u,
\qquad M=uv.
\]

master supply

\[
\beta q-5\alpha s=2^cn_0
\]

乘 `uv`：

\[
\beta uQ-5\alpha vb_1=M2^cn_0.
\]

利用

\[
Q=10b_1+1,
\qquad2\beta u-\alpha v=5^d,
\]

得到统一恒等式

\[
\boxed{
5^{d+1}b_1+\beta u
=M2^cn_0.}
\tag{6}

其中 `u,v,M` 现在只依赖 w。

---

## 6. periodic divisibility入口

固定 pairs 还要求：

\[
u\mid b_1,
\qquad v\mid Q.
\]

例如：

- `w=1`: `u=9` 自动整除 `b_1`; `v=7` 强迫 `k mod3` 的一个固定 class；
- `w=2`: `u=38` 强迫 `19|b_1`，因此 k 落在 mod9 的固定 class；`v=3` 自动可行；
- `w=3`: `v=7` 给一个 mod3 class；
- `w=4`: `u=12` 自动，`v=7` 给一个 mod3 class。

所以 top endpoint 已是 fixed coefficient + short-period k classes，适合下一步对 (5)-(6) 做 2-adic/periodic exhaustion。

---

<a id="source-deep-2high-mod5-lock"></a>

> 整合来源：`deep-2high-mod5-lock.md`

# A1 minimal diagonal: unified 2-high mod-5 Legendre lock

> 日期：2026-08-20。依赖 `deep-double-2high-master.md`、`deep-gap-unit-square.md`。本文提取 strict-5 contact square 在 surviving double-deep master branch 中真正独立的局部信息。

状态：**已严格完成。**

---

## 1. master stripped equations mod 5

剩余 double-deep 全部处于 2-high / 5-low。沿用

\[
\alpha\beta=r_{10},
\qquad
2\beta u-\alpha v=5^d,
\]

\[
\beta q-5\alpha s=2^c n_0,
\]

以及

\[
qv=Q,
\qquad su=b_1.
\]

其中所有 `alpha,beta,q,s,u,v,n0` 都与 5 互素。

模 5：

\[
\boxed{\beta q\equiv2^c n_0,}
\tag{1}
\]

\[
\boxed{2\beta u\equiv\alpha v.}
\tag{2}

又

\[
Q\equiv1\pmod5,
\qquad b_1\equiv-w\pmod5,
\]

所以

\[
\boxed{qv\equiv1,}
\qquad
\boxed{su\equiv-w}
\pmod5.
\tag{3}

---

## 2. 消去 four-factor variables

由 (1)：

\[
q\equiv2^c n_0\beta^{-1}.
\]

于是由 `qv=1 mod 5`：

\[
v\equiv\beta 2^{-c}n_0^{-1}.
\]

代入 (2)：

\[
u\equiv\alpha 2^{-c-1}n_0^{-1}.
\]

再由 `su=-w mod 5`：

\[
s\equiv-w\,2^{c+1}n_0\alpha^{-1}.
\]

所以

\[
\begin{aligned}
h=qs
&\equiv
-w\,2^{2c+1}n_0^2(\alpha\beta)^{-1}\\
&=-w\,2^{2c+1}n_0^2r_{10}^{-1}
\pmod5.
\end{aligned}
\tag{4}

取 Legendre symbol。因为

\[
\left(\frac{-1}{5}\right)=1,
\qquad
\left(\frac2{5}\right)=-1,
\]

且 `2c+1` 为奇数：

\[
\boxed{
\left(\frac h5\right)
=-\left(\frac w5\right)
\left(\frac{r_{10}}5\right).}
\tag{5}

这里逆元与原数具有相同 Legendre symbol。

---

## 3. 与原 contact square 的 strict-5 unit lock 联立

`deep-gap-unit-square.md` 在 double-deep `lambda_2=0` 中给

\[
\boxed{
\left(\frac{hN_5}{5}\right)
=(-1)^{1-A},}
\tag{6}

其中

\[
N_5=N/5^{v_5(N)}
\]

是 prefix square norm 的 5-adic unit part。

把 (5) 代入 (6)：

\[
-\left(\frac{wr_{10}N_5}{5}\right)
=(-1)^{1-A}.
\]

因此

\[
\boxed{
\left(\frac{w\,r_{10}\,N_5}{5}\right)
=(-1)^A.}
\tag{7}

这是主结论。

---

## 4. 用 master offset `eta` 表示

master branch 有

\[
A=2k+3+\eta.
\]

由于 `2k+3` 为奇数：

\[
(-1)^A=-(-1)^\eta.
\]

故也可写为

\[
\boxed{
\left(\frac{w\,r_{10}\,N_5}{5}\right)
=-(-1)^\eta.}
\tag{8}

所以 RHS 完全不依赖 `k`，只依赖 `eta mod 2`。

再结合 `deep-double-2high-master.md`：

- even `w=2,4` 时 `eta` 必为偶数，因此
  \[
  \boxed{\left(\frac{w r_{10}N_5}{5}\right)=-1;}
  \]
- odd `w=1,3` 时 `eta mod2=v_2(N) mod2`，所以 (8) 与 prefix 2-adic branch直接联动。

---

## 5. prefix `N_5` 可稳定局部化

对当前 `k>=32`，任意固定小 `m<=31` 有

\[
\boxed{
N\equiv(N_0-1)^2+(zw)^2\pmod{5^m}.}
\tag{9}

因此 `v_5(N)` 与 `N_5 mod5` 可完全由 `N_0 mod 5^{m}` 的有限 Hensel branch决定。

特别地若 `v_5(N_0)>=2`，则 `N_0=0 mod25`，直接得到：

\[
\boxed{
\begin{array}{c|c|c}
(z,w)&v_5(N)&N_5\bmod5\\ \hline
(1,1)&0&2\\
(1,2)&1&1\\
(1,3)&1&2\\
(1,4)&0&2\\
(3,1)&1&2\\
(3,2)&0&2
\end{array}}
\tag{10}

所以在这些 prefix cells 上，(7) 立即变成只含 `w,r_10,eta` 的显式 Legendre filter。

---

## 6. 审计边界

(7) 是 contact square 的独立局部信息；它不应与 `deep-hl-hensel-dependency-audit.md` 中已证明为 four-factor推论的 growing-depth Hensel lock混淆。

当前 surviving 2-high master branch 的安全独立局部组合可以取：

1. 2-adic mod-8 block lock；
2. 本文 mod-5 Legendre lock；
3. contact Q-side square-block lifting；
4. contact continuous sign window；
5. four-factor prime-source skeleton。

---

<a id="source-deep-2high-mod8-lock"></a>

> 整合来源：`deep-2high-mod8-lock.md`

# A1 minimal diagonal: unified 2-high mod-8 block lock

> 日期：2026-08-20。依赖 `deep-double-2high-master.md` 与 `deep-gap-unit-square.md`。

本文把此前 HL 的 mod-4 orientation 提升成一个对**全部剩余 double-deep 2-high / 5-low branch** 都成立的 mod-8 公式。它同时覆盖 moderate HL 与 2-extreme `E_2`。

状态：**已严格完成。**

---

## 1. 输入

沿用 master branch：

\[
a=2^{k+1}5^Y\alpha,
\qquad
b=2^{k+2}5^Y\beta,
\qquad
\alpha\beta=r_{10},
\]

且

\[
\beta q-5\alpha s=2^c n_0.
\]

当前 `k>=32`，而所有 surviving 2-high branch 都有 `c>=3`，所以模 8：

\[
\boxed{\beta q\equiv5\alpha s\pmod8.}
\tag{1}

whole-block selector `s` 只含 `1 mod 4` prime-power blocks，因此

\[
s\equiv1\text{ or }5\pmod8,
\qquad s^2\equiv1\pmod8.
\tag{2}

---

## 2. strict-2 unit square

`deep-gap-unit-square.md` 给

\[
\gamma QN_2 5^B\equiv1\pmod8,
\qquad N_2=N/2^{v_2(N)}.
\]

在 double-deep 中

\[
\gamma\equiv-h\pmod8,
\qquad h=qs.
\]

所以

\[
\boxed{hQN_2 5^B\equiv-1\pmod8.}
\tag{3}

另一方面由 (1)：

\[
q\equiv5\alpha s\beta^{-1}\pmod8.
\]

乘以 `s` 并用 `s^2=1 mod 8`：

\[
\boxed{h=qs\equiv5\alpha\beta^{-1}\pmod8.}
\tag{4}

把 (4) 代入 (3)：

\[
5^{B+1}\alpha QN_2\beta^{-1}\equiv-1\pmod8.
\]

因此

\[
\boxed{
\beta
\equiv
-5^{B+1}QN_2\,\alpha
\pmod8.}
\tag{5}

由于任意 odd `alpha` 都满足 `alpha^2=1 mod 8`，再乘 `alpha`：

\[
\boxed{
r_{10}
\equiv
-5^{B+1}QN_2
\pmod8.}
\tag{6}

这是主结论。

---

## 3. even `w` 的显式版本

已有：

- `w=2`：`QN_2=1 mod 8`；
- `w=4`：`QN_2=1 mod 8`。

所以统一：

\[
\boxed{
r_{10}\equiv-5^{B+1}\pmod8
\qquad(w=2,4).}
\tag{7}

等价于

\[
\boxed{
B\text{ even}\Longrightarrow r_{10}\equiv3\pmod8,}
\]

\[
\boxed{
B\text{ odd}\Longrightarrow r_{10}\equiv7\pmod8.}
\tag{8}

在 moderate HL 中 `B+2nu_5=v_5(r)`，所以 `B` parity 就是 `v_5(r)` parity。故对 fixed `r`，(8) 是立即可检查的 local filter。

它比旧的

\[
r_{10}\equiv3\pmod4
\]

严格强一位。

---

## 4. odd `w` 的显式版本

对 `w=1,3`，`QN_2 mod 8` 由 prefix `N_0 mod 16` 决定，但始终只取 `3` 或 `7`。

因此 (6) 说明：

\[
\boxed{r_{10}\equiv1\text{ or }5\pmod8,}
\tag{9}

与旧 `r_10=1 mod 4` 一致，但现在具体的 `1/5 mod 8` 类会反向锁定 `QN_2`，从而锁定 `N_0 mod 16` 的一半 classes。

例如当 `QN_2=7 mod 8`：

\[
B\text{ even}\Rightarrow r_{10}\equiv5\pmod8,
\qquad
B\text{ odd}\Rightarrow r_{10}\equiv1\pmod8;
\]

当 `QN_2=3 mod 8` 时两者交换。

---

## 5. 与 `eta` parity 联立

`deep-double-2high-master.md` 已给：

- even `w`：`eta` 必为偶数；
- odd `w`：`eta mod 2=v_2(N) mod 2`，等价地锁定 `N_0` parity。

所以 (6) 与 `eta` parity 合并后，剩余 2-high branch 的 2-adic局部数据不再只有 `q mod 4`：

\[
\boxed{
(\eta\bmod2,\ B\bmod2,\ r_{10}\bmod8,\ N_0\bmod16)
}
\]

之间存在显式有限兼容表。

这套表可直接用于后续 finite modular exhaustion；尤其 even-`w` moderate HL 的 `r` 候选在 `v_2(r)` parity 与 (8) 两层过滤后会显著减少。

---

<a id="source-deep-2high-q-superlinear"></a>

> 整合来源：`deep-2high-q-superlinear.md`

# A1 minimal diagonal: Q-side superlinear bound on the full 2-high master

> 日期：2026-08-20。依赖 `deep-double-2high-master.md`、`deep-complement-height.md`、`deep-contact-q-resultant-loss.md`。本文 supersede `deep-hl-q-superlinear.md` 中“仅 moderate”这一范围限制。

核心结论：对**全部** surviving double-deep 2-high / 5-low master states（包括 `eta<=0` moderate 与 `eta>0` former E2），当前 `k>=32` 都有

\[
\boxed{q>10,900,000T,}
\qquad
\boxed{v<10^{-5}T.}
\]

并且 contact exceptional loss `g=gcd(q,C)` 满足

\[
\boxed{q/g>6800\cdot2^{k-32}.}
\]

状态：**已严格完成。**

---

## 1. complement equation 的通用 q bound

master stripped complement equation始终为

\[
2\beta u-\alpha v=5^d>0,
\qquad M=uv.
\]

所以

\[
\alpha v<2\beta u,
\]

\[
v^2<\frac{2\beta}{\alpha}M.
\]

而 complement height 给

\[
M<10001\frac{T^2}{D}.
\]

因此

\[
v<T\sqrt{\frac{20002\beta}{\alpha D}}.
\]

使用 `Q>99T^2`：

\[
\boxed{
\frac qT
>99\sqrt{\frac{\alpha D}{20002\beta}}.}
\tag{1}

又

\[
\alpha\beta=r_{10},
\]

故

\[
\frac{\alpha D}{\beta}
=\frac{D\alpha^2}{r_{10}}
\ge\frac D{r_{10}}.
\tag{2}

---

## 2. master identity 消去 `eta`

完整 2-high master：

\[
D=2^{2k+3+\eta}5^B,
\]

\[
\xi:=\frac tD
=2^{-\eta}5^{B+2\nu_5}r_{10}.
\]

所以

\[
r_{10}=\xi\,2^\eta5^{-B-2\nu_5}.
\]

代回：

\[
\boxed{
\frac D{r_{10}}
=
\frac{2^{2k+3}5^{2B+2\nu_5}}\xi
=
\frac{2^{2k+3}5^{2Y}}\xi,}
\tag{3}

其中

\[
Y:=B+\nu_5\ge1.
\]

关键是 `eta` 完全消失；因此 moderate / extreme 在 q-scale 上没有区别。

---

## 3. uniform 数值

universal factor window：

\[
\xi<15,214,000.
\]

而 `Y>=1`，故

\[
\boxed{
\frac D{r_{10}}
>
\frac{25\cdot2^{2k+3}}{15,214,000}.}
\tag{4}

结合 (1)-(2)：

\[
\frac qT
>99\sqrt{
\frac{25\cdot2^{2k+3}}
{20002\cdot15,214,000}
}.
\]

最弱层 `k=32` 已大于 `10,900,000`，以后每增加一层精确多一个 factor 2。因此

\[
\boxed{q>10,900,000T.}
\tag{5}

---

## 4. `v` 与 contact exceptional part

由

\[
v=Q/q,
\qquad Q<101T^2,
\]

得到

\[
\boxed{v<10^{-5}T.}
\tag{6}

另一方面 contact resultant：

\[
\boxed{g:=\gcd(q,C)<1599T.}
\]

所以

\[
\boxed{
\frac qg>6800
}
\]

在 `k=32` 已成立，而且 q/T lower 每层翻倍、`g/T` bound 不变：

\[
\boxed{
\frac qg>6800\cdot2^{k-32}.}
\tag{7}

---

## 5. forced contact lift 覆盖 entire master

`deep-contact-q-resultant-loss.md` 给 contact factors `L_-,L_+` 的 guaranteed Q-side block product

\[
Q_-Q_+=q^2/g.
\]

因为 `q/g>1`，必有至少一个 selected Q-primary block满足 `e>v_p(C)`，并在某个 contact factor 中出现严格 amplification

\[
p^{2e-v_p(C)},
\qquad2e-v_p(C)>e.
\]

所以该 forced lifted-block event 现在覆盖：

- moderate 2-high；
- `eta>0` pure-2 denominator side；
- 换言之全部 surviving double-deep。

后续 contact descent 不应再把 `E_2` 当例外分支。

---

<a id="source-deep-b1-block-loss"></a>

> 整合来源：`deep-b1-block-loss.md`

# A1 minimal diagonal: strict 2-deep `b_1` block loss

> 日期：2026-08-19。依赖 `deep-q-side-proper-divisor.md` 与 minimal-diagonal odd-prime supply theorem。

strict 2-adic low-side 已知

\[
h=qs,
\qquad q\mid Q,
\]

其中 `s` 只能选择 `b_1` 中 `1 mod 4` 的完整 odd prime-power blocks。

`deep-q-side-proper-divisor.md` 已证明 Q-side 永久损失：

\[
q\le Q/7\quad(w=1,3,4),
\qquad q\le Q/3\quad(w=2).
\]

本文补上 `b_1` 侧的 prefix-uniform block loss，并把两侧合并。

状态：**已严格完成。**

---

## 1. `B_+` 记号

写

\[
b_1=10^{2k+1}-w,
\]

并令

\[
B_+
=
\prod_{p\equiv1(4),\ p^e\Vert b_1}p^e.
\]

odd-prime supply 中

\[
s\le B_+.
\]

任何 `2` 次幂以及所有 `p=3 mod4` prime-power blocks 都不可能进入 `B_+`。

---

## 2. `w=1`：固定因子 `3` 永久丢失

因为

\[
10\equiv1\pmod3,
\]

有

\[
b_1=10^{2k+1}-1\equiv0\pmod3.
\]

而

\[
3\equiv3\pmod4,
\]

所以整个 `3`-power block 都不能进入 `B_+`。至少损失一个因子 `3`：

\[
\boxed{B_+\le b_1/3.}
\tag{1}
\]

---

## 3. `w=2`：`2` 加上至少一个 `>=7` 的 `3 mod 4` odd block

这里

\[
b_1=10^{2k+1}-2.
\]

由于高十进制幂被 `8` 整除，

\[
b_1\equiv6\pmod8,
\]

故

\[
\boxed{v_2(b_1)=1.}
\tag{2}
\]

写 odd part

\[
b_1=2m.
\]

则

\[
m\equiv3\pmod4.
\]

所以 `m` 的素因子分解中至少有一个 `p=3 mod4` 的 prime-power block 以奇次数贡献；否则所有 blocks 的乘积只能是 `1 mod4`。

另一方面

\[
b_1\equiv1-2\equiv2\pmod3,
\]

故 `3` 不整除 `b_1`。因此这个被迫存在的 `3 mod4` odd prime 至少为 `7`。

`B_+` 同时不能使用 factor `2` 与该 odd block，所以

\[
\boxed{B_+\le b_1/(2\cdot7)=b_1/14.}
\tag{3}
\]

---

## 4. `w=3`：本文不虚构额外 loss

此时 `b_1` 为奇数且

\[
b_1\equiv1\pmod4.
\]

这个 residue 本身允许所有 odd prime-power blocks 都来自 `1 mod4` primes，因此没有一个仅凭绝对小模即可强迫的 `3 mod4` block。

所以保留安全粗界

\[
\boxed{B_+\le b_1.}
\tag{4}
\]

---

## 5. `w=4`：固定 `2^2` 与 `3` block 同时丢失

现在

\[
b_1=10^{2k+1}-4.
\]

高十进制幂被 `16` 整除，所以

\[
b_1\equiv12\pmod{16},
\]

从而

\[
\boxed{v_2(b_1)=2.}
\tag{5}
\]

同时模 `3`：

\[
b_1\equiv1-4\equiv0\pmod3.
\]

因此 `B_+` 既不能使用 `2^2`，也不能使用 `3 mod4` 的 factor `3`：

\[
\boxed{B_+\le b_1/(4\cdot3)=b_1/12.}
\tag{6}
\]

---

## 6. 与 Q-side proper-divisor cap 合并

strict 2-deep 中

\[
h=qs,
\qquad s\le B_+.
\]

结合已有

\[
q\le
\begin{cases}
Q/7,&w=1,3,4,\\
Q/3,&w=2,
\end{cases}
\]

得到新的统一表：

\[
\boxed{
\begin{array}{c|c}
w&h\text{ upper bound in strict 2-deep}\\ \hline
1&Qb_1/21\\
2&Qb_1/42\\
3&Qb_1/7\\
4&Qb_1/84
\end{array}}
\tag{7}
\]

这些损失全部来自永久局部结构，与 `k`、具体 factorization、`ell` 无关。

---

## 7. 当前用途

(7) 仍只是常数因子收缩，单独不足以证明 deep sector 为空；但 fixed-layer exponent box 与任何统一 decade estimate 都不应再使用 `QB_+` 或 `Qb_1` 作为 strict 2-deep 的极值。

特别地 even-`w` 的供给损失已经很显著：

\[
w=2:\quad h\le Qb_1/42,
\]

\[
w=4:\quad h\le Qb_1/84.
\]

后续 deep 证明应把这些界与 `A` 的奇偶/resonance、Q-side orientation、5-adic Legendre lock 同时使用。

---

<a id="source-deep-b1-sharp-mandatory-blocks"></a>

> 整合来源：`deep-b1-sharp-mandatory-blocks.md`

# A1 minimal diagonal: sharpened mandatory `b_1` complement blocks

> 日期：2026-08-20。强化 `deep-b1-block-loss.md`。本文只研究 whole-block selector 本身，因此结论可用于所有需要 `s|b_1` supply 的 deep sectors。

最终 prefix-uniform minima：

\[
\boxed{u=b_1/s\ge(27,38,1,12)}
\]

按 `w=1,2,3,4`。

状态：**已严格完成。**

---

## 1. `w=1`：universal complement 至少 27

\[
b_1=10^{2k+1}-1.
\]

令

\[
n=2k+1
\]

为奇数。LTE 对 p=3：

\[
\boxed{
v_3(b_1)=v_3(10^n-1)=2+v_3(n).}
\tag{1}

整个 3-primary block 都是 `3 mod4` prime-power source，不能进入 selector s。

分 parity。

### `v_3(n)` 为奇数

则

\[
2+v_3(n)\ge3,
\]

所以

\[
\boxed{27\mid u.}
\tag{2}

### `v_3(n)` 为偶数

此时 3-primary exponent

\[
2+v_3(n)
\]

为偶数，所以整个 3-block本身

\[
3^{2+v_3(n)}\equiv1\pmod4.
\]

但

\[
b_1\equiv-1\equiv3\pmod4.
\]

因此 b1 中必须存在另一个 `p=3 mod4` prime-power block以 odd parity贡献。

排除所有小于 31 的候选：

\[
\operatorname{ord}_7(10)=6,
\quad
\operatorname{ord}_{11}(10)=2,
\quad
\operatorname{ord}_{19}(10)=18,
\quad
\operatorname{ord}_{23}(10)=22.
\]

这些 order 全为偶数，不可能整除 odd exponent n，因此

\[
7,11,19,23\nmid10^n-1.
\]

所以这个额外 `3 mod4` prime至少为 31。又 3-primary block 至少为 9：

\[
\boxed{u\ge9\cdot31=279}
\tag{3}

在该 parity branch。

综合 (2)-(3)：

\[
\boxed{w=1:\quad u\ge27.}
\tag{4}

因此

\[
\boxed{s\le b_1/27.}
\tag{5}

该界可达其数量级：例如 n=3 时 `10^3-1=3^3*37`，3-mod-4 complement 正好包含 27。

---

## 2. `w=2`：mandatory `3 mod4` odd prime 至少是 19

\[
b_1=10^{2k+1}-2.
\]

模 8：

\[
b_1\equiv6\pmod8,
\]

故

\[
\boxed{v_2(b_1)=1.}
\]

写

\[
b_1=2m.
\]

则

\[
\boxed{m\equiv3\pmod4.}
\]

所以 m 中至少有一个 `p=3 mod4` odd prime-power block以 odd parity贡献。

排除 3,7,11：

- `p=3`: `b_1=1-2=-1 mod3`；
- `p=7`: `10^(2k+1)=3*2^k mod7`，等于 2 会要求 `2^k=3 mod7`，不可能；
- `p=11`: odd exponent 给 `10^(2k+1)=-1 mod11`，所以 `b_1=-3 mod11`。

因此 mandatory odd prime至少 19，整个 block留在 u：

\[
\boxed{w=2:\quad u\ge2\cdot19=38.}
\tag{6}

所以

\[
\boxed{s\le b_1/38.}
\tag{7}

---

## 3. `w=3,4`

`w=3`：目前没有 prefix-uniform mandatory `3 mod4` odd block，安全保留

\[
\boxed{u\ge1.}
\]

`w=4`：

\[
v_2(b_1)=2,
\qquad v_3(b_1)=1,
\]

所以

\[
\boxed{u\ge12,}
\qquad
\boxed{s\le b_1/12.}
\]

---

## 4. final structural minima

\[
\boxed{
(c_1,c_2,c_3,c_4)=(27,38,1,12).}
\tag{8}

以后所有仅依赖 mandatory `b_1` complement 的 supply bounds 应使用 (8)，而不再使用历史粗值 `(3,14,1,12)` 或中间值 `(9,38,1,12)`。

---

<a id="source-deep-balanced-collapse"></a>

> 整合来源：`deep-balanced-collapse.md`

# A1 minimal diagonal: fully-balanced deep collapse

> 日期：2026-08-20。依赖 `deep-complement-height.md`。当前统一剩余范围为 `k=g>=31`，central 已关闭，因此只研究 deep denominator。

本文把原先的 balanced double-deep collapse 推广到**任意 deep sector**。

沿用

\[
T=10^k,
\qquad
\Gamma_k=\frac{\gamma}{D},
\qquad
D=2^A5^B,
\qquad
15.09<\Gamma_k<39.003,
\]

以及非 deep 一侧的 numerator powers

\[
\lambda=2^{\lambda_2}5^{\lambda_5}.
\]

记

\[
e=v_2(w),
\qquad
\nu_2=v_2(N_0),
\qquad
\nu_5=v_5(N_0).
\]

核心结论：若两侧 cancellation depth 足以把整个 `lambda*T^2` 吃掉，即

\[
\boxed{
A+e+\nu_2\ge k+\lambda_2,
\qquad
B+\nu_5\ge k+\lambda_5,
}
\tag{1}
\]

则不存在 candidate。

所以任何尚存 deep candidate 必须满足

\[
\boxed{
A+e+\nu_2<k+\lambda_2
\quad\text{或}\quad
B+\nu_5<k+\lambda_5.
}
\tag{2}
\]

特别地，double-deep `A,B>0` 时 `lambda_2=lambda_5=0`，恢复

\[
\boxed{
A+e+\nu_2<k
\quad\text{或}\quad
B+\nu_5<k.
}
\tag{3}
\]

状态：**已严格完成。**

---

## 1. general deep complement identity

`deep-complement-height.md` 给出

\[
DTN_0-\gamma=h\lambda,
\qquad
M:=\frac{Qb_1}{h}\in\mathbf Z_{>0}.
\]

记

\[
P:=Qb_1
=1000T^4+c_2T^2+C_0,
\]

其中

\[
\boxed{c_2:=10(1-20w),}
\qquad
\boxed{C_0:=w(10w-1).}
\]

乘以 `M`：

\[
\boxed{
M(DTN_0-\gamma)=P\lambda.
}
\tag{4}
\]

仍有

\[
v_2(M)=e,
\qquad
v_5(M)=0.
\tag{5}
\]

---

## 2. fully-balanced 条件产生 bounded integer `J`

由 (1)、(5)：

\[
v_2(MDTN_0)
=e+A+k+\nu_2
\ge2k+\lambda_2,
\]

\[
v_5(MDTN_0)
=B+k+\nu_5
\ge2k+\lambda_5.
\]

因此

\[
\boxed{
\lambda T^2\mid MDTN_0.
}
\tag{6}
\]

由 (4)：

\[
M\gamma=MDTN_0-P\lambda.
\]

而

\[
P\lambda\equiv C_0\lambda\pmod{\lambda T^2},
\]

所以

\[
\boxed{
\lambda T^2\mid M\gamma+C_0\lambda.
}
\]

定义整数

\[
\boxed{
J:=\frac{M\gamma+C_0\lambda}{\lambda T^2}.
}
\tag{7}
\]

另一方面 complement-height 定义

\[
\mu:=\frac{MD}{\lambda T^2},
\qquad
1000<\mu<10001.
\]

因为 `gamma=D Gamma_k`：

\[
J=\mu\Gamma_k+\frac{C_0}{T^2}.
\]

于是完全独立于 deep 类型：

\[
\boxed{15091\le J\le390069.}
\tag{8}
\]

---

## 3. `lambda` 完全消失

由 (7)：

\[
\boxed{
M\gamma=\lambda(JT^2-C_0).
}
\tag{9}
\]

代回 (4)：

\[
MDTN_0
=\lambda\left(1000T^4+(c_2+J)T^2\right).
\tag{10}
\]

将 (9)、(10) 相除。左侧比值为

\[
\frac{M\gamma}{MDTN_0}
=\frac{\Gamma_k}{TN_0},
\]

而右侧的 `lambda` 精确约掉，所以仍得到

\[
\boxed{
\Gamma_k
=
\frac{
N_0(JT^2-C_0)
}{
T(1000T^2+c_2+J)
}.
}
\tag{11}
\]

这是最关键的一点：**fully-balanced 后的有理正规形与 single/deep 类型、`lambda`、`A,B` 全部无关。**

---

## 4. denominator odd part 必须被分子完全吸收

记

\[
\boxed{C:=c_2+J,}
\qquad
\boxed{F:=1000T^2+C,}
\qquad
\boxed{G:=JT^2-C_0.}
\]

由 `w=1,2,3,4` 与 (8)：

\[
\boxed{14301\le C\le389879.}
\tag{12}
\]

又

\[
v_2(1000T^2)=v_5(1000T^2)=2k+3\ge65,
\]

远大于 `C` 的可能赋值，所以

\[
\boxed{v_2(F)=v_2(C),}
\qquad
\boxed{v_5(F)=v_5(C).}
\tag{13}
\]

定义去掉全部 `2,5` 因子的部分

\[
\boxed{
F_0:=\frac{F}{2^{v_2(C)}5^{v_5(C)}}.
}
\tag{14}
\]

则

\[
\boxed{
F_0>\frac{1000T^2}{389879}.
}
\tag{15}
\]

无论 single-deep 还是 double-deep，`Gamma_k=gamma/D` 的既约分母 `D=2^A5^B` 都只含 `2,5`。而 (11) 中 `T` 也只含 `2,5`。因此 `F` 的全部非 `2,5` 因子必须在分子 `N_0G` 中完全消失：

\[
\boxed{F_0\mid N_0G.}
\tag{16}
\]

---

## 5. `F,G` 的公共 odd part 只有绝对常数大小

计算

\[
JF-1000G
=J(c_2+J)+1000C_0.
\]

定义

\[
\boxed{
R_J:=J(c_2+J)+1000C_0.
}
\tag{17}
\]

所以

\[
\boxed{
\gcd(F,G)\mid R_J.
}
\tag{18}
\]

由 (8)、(12) 与 `C_0<=156`：

\[
\boxed{
0<R_J<152080000000.
}
\tag{19}
\]

令

\[
d:=\gcd(F_0,G).
\]

由 (16)：

\[
\frac{F_0}{d}\mid N_0.
\]

而 (18)-(19)、`N_0<T` 给出

\[
\boxed{
F_0<152080000000\,T.
}
\tag{20}
\]

与 (15) 联立：

\[
\frac{1000T^2}{389879}
<152080000000\,T,
\]

故

\[
T<6\times10^{13}.
\tag{21}
\]

当前 `T=10^k`、`k>=31`，矛盾。

因此 fully-balanced 条件 (1) 下不存在任何 deep candidate。

---

## 6. 对各 deep sector 的直接推论

### double-deep

`A,B>0` 时

\[
\lambda_2=\lambda_5=0,
\]

所以任何 candidate 必须满足

\[
\boxed{
A+e+\nu_2<k
\quad\text{或}\quad
B+\nu_5<k.
}
\]

### single 2-deep

若

\[
A>0,\qquad B=0,
\]

则 `lambda_2=0`，`lambda_5=k+y>=0`。fully-balanced 区域

\[
A+e+\nu_2\ge k,
\qquad
\nu_5\ge k+\lambda_5
\]

全部为空。

### single 5-deep

若

\[
A=0,\qquad B>0,
\]

则 `lambda_5=0`，`lambda_2=k+x>=0`。fully-balanced 区域

\[
e+\nu_2\ge k+\lambda_2,
\qquad
B+\nu_5\ge k
\]

全部为空。

---

## 7. 当前 deep 几何

`deep-complement-height.md` 给出了 logarithmic height strip；本文又删除了所有 fully-balanced 点。因此剩余 deep 状态必须贴着至少一个**相对于 `lambda*T^2` 的 shallow side**。

后续不应再把 deep 当成完整二维 lattice。应分成：

1. 2-shallow：
   \[
   A+e+\nu_2<k+\lambda_2;
   \]
2. 5-shallow：
   \[
   B+\nu_5<k+\lambda_5;
   \]
3. 两者同时 shallow。

再分别加入 resonance parity、mod-8 / mod-5 unit locks、Q-side orientation 与 proper-divisor / whole-block loss。

---

<a id="source-deep-complement-divisor-system"></a>

> 整合来源：`deep-complement-divisor-system.md`

# A1 minimal diagonal: complementary quadratic-divisor system

> 日期：2026-08-20。依赖 `deep-four-factor-frame.md`。当前范围 `k=g>=31`。

本文把 complementary linear relation

\[
\bar s b-\bar q a=10\lambda T
\]

与

\[
\bar s\mid b_1,
\qquad
\bar q\mid Q
\]

直接联立，得到一对互相嵌套的二次整除条件。

在 double-deep 中 `lambda=1`，它尤其适合 moderate LL：此时 `a,b` 来自绝对有限集合，因此问题变成 fixed-coefficient simultaneous quadratic-divisor system。

状态：**整除正规形严格完成；Vieta-jumping / descent 方向仍待证。**

---

## 1. 记号

令

\[
\boxed{u:=\bar s=b_1/s,}
\qquad
\boxed{v:=\bar q=Q/q.}
\]

four-factor frame 给

\[
\boxed{bu-av=10\lambda T.}
\tag{1}

又

\[
b_1=10T^2-w,
\qquad
Q=100T^2-(10w-1).
\tag{2}

---

## 2. `u` 侧二次整除

由 (1)：

\[
100\lambda^2T^2=(bu-av)^2.
\]

把 `10b_1=100T^2-10w` 乘上 `lambda^2`：

\[
10\lambda^2b_1
=(bu-av)^2-10w\lambda^2.
\]

因为

\[
u\mid b_1,
\]

左侧被 `u` 整除。右侧模 `u` 只剩

\[
a^2v^2-10w\lambda^2.
\]

因此

\[
\boxed{
u\mid a^2v^2-10w\lambda^2.}
\tag{3}

---

## 3. `v` 侧二次整除

由 (1)：

\[
100\lambda^2T^2=(bu-av)^2.
\]

而

\[
\lambda^2Q
=100\lambda^2T^2-(10w-1)\lambda^2.
\]

所以

\[
\lambda^2Q
=(bu-av)^2-(10w-1)\lambda^2.
\]

因为

\[
v\mid Q,
\]

模 `v` 得

\[
\boxed{
v\mid b^2u^2-(10w-1)\lambda^2.}
\tag{4}

---

## 4. double-deep 专门化

在 double-deep 中

\[
\lambda=1.
\]

于是 (1),(3),(4) 变成

\[
\boxed{bu-av=10T,}
\tag{5}

\[
\boxed{
u\mid a^2v^2-10w,}
\tag{6}

\[
\boxed{
v\mid b^2u^2-(10w-1).}
\tag{7}

这已经完全不含 `N_0,gamma,D`。

所以所有 double-deep candidate 都必须在 complementary divisor plane `(u,v)` 上满足一对固定形状的 quadratic divisibilities；`D,N_0,gamma` 只在其他方程中负责进一步筛选。

---

## 5. moderate LL 的 fixed-coefficient 版本

LL 中

\[
A\le23,
\qquad
B\le10,
\qquad
196000<r<15214000,
\]

而 `deep-moderate-factor-quotients.md` 给出

\[
\alpha\beta=r_{10}
\]

以及显式 `a,b`。因此对每个固定

\[
(w,r,A,B,\nu_2,\nu_5,\alpha,\beta)
\]

，`a,b` 都是固定正整数。

此时 LL 剩余的 unbounded `k` 必须产生正整数 `u,v` 满足

\[
\boxed{
\begin{aligned}
&bu-av=10^{k+1},\\
&u\mid a^2v^2-10w,\\
&v\mid b^2u^2-(10w-1).
\end{aligned}}
\tag{8}

这是一套 fixed-coefficient simultaneous quadratic-divisor system。

它已经与原来的 `Q,b_1` 完整 factorization 解耦：不需要先 factor `10^{2k+2}-(10w-1)` 或 `10^{2k+1}-w` 才能陈述必要条件。

---

## 6. quotient variables

可进一步定义整数

\[
\boxed{m:=\frac{a^2v^2-10w}{u},}
\]

\[
\boxed{n:=\frac{b^2u^2-(10w-1)}{v}.}
\]

由 (8)，`u,v,m,n` 全为正整数（当前 `u,v` 巨大，所以 numerator 为正）。

后续可能的 Vieta-jumping / descent 目标是研究 `(u,v)` 与 `(m,n)` 的 size direction 和 involution；本文暂不把该方向误写成已经证明的无限下降。

---

## 7. 当前用途

这套 system 对 LL 最直接，因为 `a,b` 固定；对 LH/HL 虽然 `a,b` 含显式 `2^k/5^k`，仍可先除去 `deep-moderate-factor-quotients.md` 中已知的大 prime powers，再得到相应的 scaled quadratic divisibility。

因此后续可以并行尝试：

1. LL：Vieta-jumping / minimal-solution descent；
2. LH/HL：先 strip 大 `2/5` powers，再做 periodic congruence；
3. 与 `deep-moderate-root-normal-form.md` 的 square-root branch 同时使用。

---

<a id="source-deep-complement-height"></a>

> 整合来源：`deep-complement-height.md`

# A1 minimal diagonal: deep complement-quotient height bound

> 日期：2026-08-19。依赖 `gap-denominator-normal-form.md`、minimal-diagonal odd-prime supply 与 `deep-gap-valuation-normal-form.md`。
> 当前真正需要统一处理的范围已经可取 `k=g>=31`，因为 `k<=30` 有 fixed-layer certificates，而 central denominator 在全部 `k>=26` 上已由 `central-modular-exhaustion.md` 关闭。

本文给 deep denominator sector 一个新的全局高度约束。核心不是继续枚举 `(A,B)`，而是研究 odd-prime supply 的**补因子**

\[
M:=\frac{Qb_1}{h}\in\mathbf Z_{>0}.
\]

最终得到一个非常强的 rational-approximation necessary condition。特别地，在 double-deep `A,B>0` 中：

\[
\boxed{
2^{\min(A+e+\nu_2,3k)}
5^{\min(B+\nu_5,3k)}
<390100\,10^k,
}
\]

其中

\[
e=v_2(w),
\qquad\nu_2=v_2(N_0),
\qquad\nu_5=v_5(N_0).
\]

这把原来的无界二维 deep lattice 压入一个显式线性高度带。

状态：**已严格完成。**

---

## 1. general deep numerator identity

沿用 reduced normalized gap

\[
\Gamma_k=10^k(N_0-\rho)
=\frac{\gamma}{2^A5^B},
\qquad
15.09<\Gamma_k<39.003.
\]

记

\[
T=10^k,
\qquad
D=2^A5^B.
\]

若某一素数侧不 deep，则该侧可能仍在 `rho=h2^x5^y` 的分子中。定义

\[
\lambda_2=
\begin{cases}
0,&A>0,\\
k+x,&A=0,
\end{cases}
\qquad
\lambda_5=
\begin{cases}
0,&B>0,\\
k+y,&B=0,
\end{cases}
\]

以及

\[
\boxed{\lambda=2^{\lambda_2}5^{\lambda_5}.}
\]

由定义直接有

\[
D T(N_0-\rho)=\gamma,
\]

而

\[
D T\rho=h\lambda.
\]

所以

\[
\boxed{
DTN_0-\gamma=h\lambda.}
\tag{1}
\]

这是 central decimal equation 在任意 deep sector 中的统一替代式。

---

## 2. 引入 supply complement `M`

minimal-diagonal odd supply 给

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\]

故至少有

\[
\boxed{h\mid Qb_1.}
\]

定义

\[
\boxed{M:=\frac{Qb_1}{h}\in\mathbf Z_{>0}.}
\tag{2}
\]

又

\[
Qb_1
=1000T^4+10(1-20w)T^2+C_0,
\qquad
C_0=w(10w-1).
\tag{3}
\]

由 (1)-(2)：

\[
MD(TN_0-\Gamma_k)
=M(DTN_0-\gamma)
=Mh\lambda
=Qb_1\lambda.
\]

所以定义

\[
\boxed{
\mu:=\frac{MD}{\lambda T^2}}
\tag{4}
\]

后，有精确恒等式

\[
\boxed{
\mu(TN_0-\Gamma_k)
=\frac{Qb_1}{T^2}.}
\tag{5}
\]

---

## 3. `mu` 永远落在固定区间 `(1000,10001)`

因为 `rho` 有 `k` 位且 `0<N_0-rho<1`，有

\[
\frac T{10}<N_0\le T.
\tag{6}
\]

首先证明下界。由 `N_0<=T`：

\[
1000T^2(TN_0-\Gamma_k)
\le1000T^2(T^2-\Gamma_k).
\]

而由 (3)：

\[
\begin{aligned}
Qb_1-1000T^2(T^2-\Gamma_k)
={}&\bigl(1000\Gamma_k+10(1-20w)\bigr)T^2+C_0.
\end{aligned}
\]

使用

\[
\Gamma_k>15.09,
\qquad w\le4,
\]

括号严格大于

\[
15090-790=14300.
\]

所以

\[
Qb_1>1000T^2(TN_0-\Gamma_k),
\]

结合 (5)：

\[
\boxed{\mu>1000.}
\tag{7}
\]

再证上界。由

\[
Qb_1<1000T^4
\]

以及

\[
TN_0-\Gamma_k>rac{T^2}{10}-39.003,
\]

得到

\[
\mu
<\frac{1000T^2}{T^2/10-39.003}
=\frac{10000}{1-390.03/T^2}.
\]

当前 `k>=31`，当然严格小于 `10001`；事实上 `k>=4` 已足够。因此

\[
\boxed{1000<\mu<10001.}
\tag{8}
\]

---

## 4. 得到 `O(T^-2)` 的超近有理逼近

把 (3) 代回 (5)：

\[
\mu TN_0-\mu\Gamma_k
=1000T^2+10(1-20w)+\frac{C_0}{T^2}.
\]

除以 `T^2`：

\[
\boxed{
\frac{MDN_0}{\lambda T^3}-1000
=
\frac{
\mu\Gamma_k+10(1-20w)+C_0/T^2
}{T^2}.}
\tag{9}
\]

由 (7) 与 `Gamma_k>15.09`，右侧分子严格为正：

\[
1000\cdot15.09-790>14300.
\]

另一方面由 (8)、`Gamma_k<39.003`：

\[
\mu\Gamma_k+10(1-20w)+C_0/T^2
<10001\cdot39.003+1
<390100.
\]

故

\[
\boxed{
0<
\frac{MDN_0}{\lambda T^3}-1000
<\frac{390100}{T^2}.}
\tag{10}
\]

---

## 5. reduced denominator 必须巨大

把左侧第一个有理数写成既约形式

\[
\frac{MDN_0}{\lambda T^3}=\frac ab,
\qquad\gcd(a,b)=1.
\]

因为它与整数 `1000` 的差非零，必有

\[
\left|\frac ab-1000\right|\ge\frac1b.
\]

结合 (10)：

\[
\boxed{
b>\frac{T^2}{390100}.}
\tag{11}
\]

现在计算这个 `b` 的 2/5 结构。

由于 `h` 与 `10` 互素，

\[
v_2(M)=v_2(Qb_1)=v_2(b_1)=e:=v_2(w),
\]

\[
v_5(M)=0.
\]

再记

\[
\nu_2=v_2(N_0),
\qquad
\nu_5=v_5(N_0).
\]

于是

\[
\boxed{
 b
=2^{(3k+\lambda_2-A-e-\nu_2)_+}
 5^{(3k+\lambda_5-B-\nu_5)_+}.}
\tag{12}
\]

因此 general deep sector 必须满足

\[
\boxed{
2^{(3k+\lambda_2-A-e-\nu_2)_+}
5^{(3k+\lambda_5-B-\nu_5)_+}
>
\frac{10^{2k}}{390100}.}
\tag{13}
\]

这是本文最通用的 complement-height inequality。

---

## 6. double-deep 的显式线性高度带

若

\[
A>0,
\qquad B>0,
\]

则

\[
\lambda_2=\lambda_5=0.
\]

把 (13) 等价地写成 cancellation 上界：

\[
\boxed{
2^{\min(A+e+\nu_2,3k)}
5^{\min(B+\nu_5,3k)}
<390100\,10^k.}
\tag{14}
\]

这已经改变了 `(A,B)` 可行区域的渐近斜率。

### 6.1 `5` 侧不可能达到 `3k`

若

\[
B+\nu_5\ge3k,
\]

则 (14) 左侧至少为 `5^(3k)`。但

\[
\frac{5^{3k}}{10^k}
=\left(\frac{125}{10}\right)^k
=12.5^k,
\]

对 `k>=31` 远大于 `390100`，矛盾。因此

\[
\boxed{B+\nu_5<3k.}
\tag{15}
\]

### 6.2 若 2 侧达到 `3k`，5 侧立刻变浅

若

\[
A+e+\nu_2\ge3k,
\]

由 (14)-(15)：

\[
2^{3k}5^{B+\nu_5}
<390100\,10^k.
\]

所以

\[
5^{B+\nu_5}
<390100\left(\frac54\right)^k.
\]

注意

\[
390100<5^8,
\qquad
\frac54<5^{0.139}.
\]

故得到简洁安全界

\[
\boxed{
B+\nu_5<8+0.139k.}
\tag{16}
\]

所以 extreme 2-deep 不可能同时伴随显著 5-deep。

### 6.3 未饱和区

若

\[
A+e+\nu_2<3k,
\]

则结合 (15)，(14) 直接变成

\[
\boxed{
2^{A+e+\nu_2}5^{B+\nu_5}
<390100\,10^k.}
\tag{17}
\]

这是一条真正的线性 logarithmic height bound，而不是此前 supply cap 的常数因子改进。

---

## 7. 当前意义

central denominator 已全部关闭，所以 minimal diagonal 的统一问题只剩 deep。

本文说明 deep 的 complement quotient 本身产生一个 `T^-2` 级别的 rational approximation；由于其分母只能来自 `2,5`，不能被任意深地约掉。

特别是 double-deep：

- `B+v_5(N_0)<3k`；
- 若 2 侧达到 `3k`，则 `B+v_5(N_0)<8+0.139k`；
- 其余区域满足 (17)。

下一步应把 (13)-(17) 与已有的 resonance parity、unit-square locks、Q-side orientation、primitive cross-corridor caps 联用。

---

<a id="source-deep-contact-mandatory3-lock"></a>

> 整合来源：`deep-contact-mandatory3-lock.md`

# A1 minimal diagonal: contact square + mandatory `3`-block lock

> 日期：2026-08-20。依赖 `deep-double-2high-master.md`、`deep-four-factor-frame.md` 与原 rational-contact square。本文适用于 `w=1,4`，因为这两型的 `b_1` 永远含有 mandatory `3 mod 4` block。

状态：**已严格完成。**

---

## 1. `3` 永远在 complementary `u` 侧

若 `w=1` 或 `w=4`，则

\[
b_1=10^{2k+1}-w\equiv1-w\equiv0\pmod3.
\]

而

\[
3\equiv3\pmod4,
\]

所以 odd-prime supply selector `s` 不能使用整个 3-primary block。

因此

\[
\boxed{3\mid u=b_1/s,}
\qquad
\boxed{3\nmid s.}
\tag{1}

同时

\[
Q=10b_1+1\equiv1\pmod3,
\]

故 `q,v` 都是 3-adic units，且

\[
\boxed{qv\equiv1\pmod3.}
\tag{2}

---

## 2. stripped equations mod 3

master branch：

\[
2\beta u-\alpha v=5^d,
\]

\[
\beta q-5\alpha s=2^c n_0.
\]

由 `3|u`，第一式给

\[
-\alpha v\equiv(-1)^d\pmod3.
\]

所以

\[
v\equiv-(-1)^d\alpha^{-1},
\]

再由 (2)：

\[
\boxed{q\equiv-(-1)^d\alpha\pmod3.}
\tag{3}

第二式模 3 为

\[
\beta q+\alpha s\equiv(-1)^c n_0.
\]

代入 (3) 与 `alpha beta=r_10`：

\[
\alpha s
\equiv(-1)^c n_0+(-1)^d r_{10}.
\]

所以

\[
\begin{aligned}
h=qs
&\equiv q\alpha^{-1}igl((-1)^c n_0+(-1)^d r_{10}\bigr)\\
&\equiv-r_{10}-(-1)^{c+d}n_0
\pmod3.
\end{aligned}
\tag{4}

---

## 3. 把 `n_0` 换回 `N_0`

写

\[
N_0=2^{\nu_2}5^{\nu_5}n_0.
\]

模 3 中 `2≡5≡-1`，因此

\[
n_0\equiv(-1)^{\nu_2+\nu_5}N_0\pmod3.
\]

而

\[
c=k+1+\eta+\nu_2,
\]

\[
d=k+1-B-\nu_5.
\]

所以

\[
(-1)^{c+d}n_0
\equiv(-1)^{\eta+B}N_0\pmod3.
\]

于是 (4) 化成

\[
\boxed{
h\equiv-r_{10}-(-1)^{\eta+B}N_0\pmod3.}
\tag{5}

---

## 4. contact square mod 3

因为 `3|b_1`、`Q≡T≡1 mod3`，prefix norm 满足

\[
N=a_1^2+(a_2b_1)^2\equiv a_1^2\pmod3.
\]

六型公式给在 `w=1,4,z=1`：

\[
a_1\equiv N_0+1\pmod3.
\]

原 contact square

\[
V^2=K-2\rho TQN
\]

而模 3：

\[
K\equiv-N,
\qquad
\rho=\frac h{DT}.
\]

所以

\[
\boxed{
V^2\equiv-(1+2hD^{-1})a_1^2\pmod3.}
\tag{6}

若

\[
N_0\not\equiv2\pmod3,
\]

则 `a_1` 是 unit。非零平方模 3 只能为 1，因此 (6) 强迫

\[
-(1+2hD^{-1})\equiv1\pmod3.
\]

即

\[
\boxed{h\equiv2D\pmod3.}
\tag{7}

master branch 中

\[
A=2k+3+\eta,
\]

所以

\[
D=2^A5^B\equiv(-1)^{A+B}
=-(-1)^{\eta+B}\pmod3.
\]

又 `2=-1 mod3`，故

\[
\boxed{2D\equiv(-1)^{\eta+B}\pmod3.}
\tag{8}

把 (5),(7),(8) 联立：

\[
-r_{10}-(-1)^{\eta+B}N_0
\equiv(-1)^{\eta+B}
\pmod3.
\]

最终得到

\[
\boxed{
r_{10}
\equiv-(-1)^{\eta+B}(N_0+1)
\pmod3,}
\tag{9}

只要 `N_0 !=2 mod3`。

---

## 5. 一个立即推论

若

\[
3\mid r_{10},
\]

而 `N_0 !=2 mod3`，(9) 右侧非零，矛盾。

因此

\[
\boxed{
3\mid r_{10}
\Longrightarrow
N_0\equiv2\pmod3
\qquad(w=1,4).}
\tag{10}

在 `N_0=2 mod3` 时 `a_1=0 mod3`，contact square (6) 本身退化为 `0`，所以本文不虚构额外条件。

---

## 6. 意义

这是第一条把：

- mandatory `b_1` prime block；
- four-factor stripped equations；
- 原 rational-contact square；

三者联立后反推出 prefix `N_0` residue 的显式公式。

后续可对其他周期性 mandatory primes 做同样处理：固定某个 `p=3 mod4` 与 `d mod ord_p(10)`，若该 p-primary block 被迫留在 `u`，则 contact square可产生相应 `(r_10,N_0)` residue lock。

---

<a id="source-deep-contact-q-resultant-loss"></a>

> 整合来源：`deep-contact-q-resultant-loss.md`

# A1 minimal diagonal: total resultant loss in contact Q-side lifting

> 日期：2026-08-20。依赖 `deep-contact-q-square-blocks.md`。

本文强化 contact Q-side block theorem：异常 prime contamination 的总损失不只在 support 上受控，而是其完整 `q`-primary gcd 因子本身被一个 `O(T)` resultant 控制。

状态：**已严格完成。**

---

## 1. `gcd(q,C)` 与线性 resultant 完全相同

`deep-contact-q-square-blocks.md` 已证明

\[
10C\equiv E_C\pmod Q,
\]

其中

\[
E_C=(10w-1)N_0+10(10w-1)(5-z)T-10z,
\]

且

\[
0<E_C<c_{z,w}T,
\qquad c_{z,w}\le1599.
\]

由于

\[
q\mid Q,
\qquad \gcd(10,q)=1,
\]

同余直接给出

\[
\boxed{
\gcd(q,C)=\gcd(q,E_C).}
\tag{1}

定义

\[
\boxed{g:=\gcd(q,C).}
\]

则

\[
\boxed{g<1599T.}
\tag{2}

按类型可用更小的 `369,779,1189,1599,189,399` 常数。

---

## 2. 每个 selected block 的 guaranteed exponent

仍记

\[
L_\pm=Db_1C\pm Z,
\]

以及

\[
L_-L_+=DNq^2v(DT^2v+2s).
\]

固定

\[
p^e\Vert q,
\qquad c=v_p(C).
\]

令

\[
x=v_p(L_-),
\qquad y=v_p(L_+).
\]

则

\[
x+y\ge2e.
\]

又

\[
\min(x,y)\le c
\]

因为 `gcd(L_-,L_+)|2Db1C`，而 `p` 与 `2Db1D` 互素。

同时当然

\[
\max(x,y)\ge e.
\]

所以若

\[
c_e:=\min(e,c)=v_p(g),
\]

则

\[
\boxed{
\max(x,y)\ge2e-c_e.}
\tag{3}

证明：

- 若 `c<e`，由 `x+y>=2e`、`min<=c` 得 `max>=2e-c`；
- 若 `c>=e`，则 `c_e=e`，而 `max>=e=2e-c_e`。

---

## 3. 全局 block partition

对每个 `p^e||q`，把 guaranteed block

\[
p^{2e-c_e}
\]

分配给实际承担较高 valuation 的 contact factor。

不同素数 blocks 两两互素，所以存在互素正整数 `Q_-`,`Q_+` 使

\[
\boxed{Q_-Q_+=\frac{q^2}{g},}
\tag{4}

并且

\[
\boxed{Q_-\mid L_-,
\qquad Q_+\mid L_+.}
\tag{5}

这里每个 `p` 的完整 guaranteed power `p^(2e-c_e)` whole-block 进入一边。

所以 contact square 对 Q-side supply 的统一结论可写成：

\[
\boxed{
\text{ideal }q^2\text{ square lifting}
\text{ 最多损失 }g=\gcd(q,C)<1599T.}
\tag{6}

---

## 4. regular / exceptional 情形作为特例

若 `g=1`，则

\[
Q_-Q_+=q^2,
\]

且每个 `p^e||q` 都以 `p^(2e)` 整块进入一边，恢复完全平方 whole-block partition。

一般情况下，所有异常损失的总乘积也只有 `g=O(T)`，而

\[
Q\asymp100T^2.
\]

因此在后续若能从 supply/four-factor 得到 `q` 的超线性下界，则 contact side 上必然出现一个显著的 lifted block；无需逐个追踪异常 prime support。

---

<a id="source-deep-contact-q-square-blocks-universal"></a>

> 整合来源：`deep-contact-q-square-blocks-universal.md`

# A1 minimal diagonal: universal deep contact Q-side lifting

> 日期：2026-08-20。推广 `deep-contact-q-square-blocks.md`，并吸收 `deep-b1-sharp-mandatory-blocks.md`。本文适用于任意 deep denominator state，包括 single-2、single-5 与 double-deep。

状态：**已严格完成。**

---

## 1. universal contact factorization

原 rational-contact square：

\[
V^2=K-2\rho TQN,
\]

其中

\[
K=b_1^2C^2-T^2Q^2N.
\]

所以

\[
(b_1C)^2-V^2=TQN(TQ+2\rho).
\tag{1}

任意 deep state 都有

\[
DT\rho=h\lambda,
\qquad h=qs,
\qquad Q=qv.
\]

若 `V=a/b` 既约，则 `V^2` 的分母 `b^2` 整除 D，故 `b|D`，所以

\[
\boxed{Z:=DV\in\mathbf Z.}
\tag{2}

乘以 `D^2` 并代入 supply：

\[
\boxed{
L_-L_+
=DNq^2v(DT^2v+2s\lambda),}
\tag{3}

其中

\[
\boxed{L_\pm:=Db_1C\pm Z.}
\]

因此 Q-side `q^2` lifting 不依赖 `lambda=1`。

---

## 2. q-primary lifting

对任意

\[
p^e\Vert q,
\]

有

\[
v_p(L_-)+v_p(L_+)\ge2e.
\]

且

\[
\gcd(L_-,L_+)\mid2Db_1C.
\]

因为 `p|Q` 与 `2Db_1D` 互素：

\[
\boxed{
\max(v_p(L_-),v_p(L_+))
\ge2e-\min(e,v_p(C)).}
\tag{4}

特别地

\[
p\nmid C
\Longrightarrow
\boxed{p^{2e}\mid L_-\text{ or }L_+.}
\tag{5}

---

## 3. resultant exceptional loss

minimal diagonal：

\[
10C\equiv E_C\pmod Q,
\]

\[
E_C=(10w-1)N_0+10(10w-1)(5-z)T-10z.
\]

所以对任意 `q|Q`：

\[
\boxed{\gcd(q,C)=\gcd(q,E_C).}
\]

令

\[
g:=\gcd(q,C).
\]

六类型：

\[
\boxed{
\begin{array}{c|c}
(z,w)&g<c_{z,w}T\\ \hline
(1,1)&369T\\
(1,2)&779T\\
(1,3)&1189T\\
(1,4)&1599T\\
(3,1)&189T\\
(3,2)&399T
\end{array}}
\tag{6}

并存在 coprime block products `Q_-,Q_+`：

\[
\boxed{Q_-Q_+=q^2/g,}
\]

\[
\boxed{Q_-\mid L_-,
\qquad Q_+\mid L_+.}
\tag{7}

---

## 4. universal selected-Q lower bound

\[
h=\frac{D(TN_0-\Gamma)}\lambda.
\]

当前 `N_0>=T/10`、`Gamma<39.003`，所以对 `k>=32`：

\[
TN_0-\Gamma>T^2/11.
\]

故

\[
\boxed{h>DT^2/(11\lambda).}
\tag{8}

sharpened mandatory `b_1` complements：

\[
\boxed{(c_1,c_2,c_3,c_4)=(9,38,1,12),}
\tag{9}

且

\[
s\le b_1/c_w<10T^2/c_w.
\]

所以

\[
\boxed{
q=h/s>
\frac{c_w}{110}\frac D\lambda.}
\tag{10}

---

## 5. sharpened forced-lift criterion

若

\[
\frac D\lambda>K_{z,w}T,
\]

其中

\[
K_{z,w}:=110c_{z,w}/c_w,
\]

则由 (6),(10)：

\[
q>c_{z,w}T>g,
\]

所以 contact exceptional resultant 不可能吞掉整个 q，必出现 strict exponent amplification。

sharpened constants：

\[
\boxed{
\begin{array}{c|c}
(z,w)&K_{z,w}\\ \hline
(1,1)&4510\\
(1,2)&2255\\
(1,3)&130790\\
(1,4)&14657.5\\
(3,1)&2310\\
(3,2)&1155
\end{array}}
\tag{11}

其中 `(1,1),(1,2),(3,1),(3,2)` 比旧值明显下降。

---

## 6. 当前用途

contact-square block mechanism 现在统一覆盖所有 deep：

- double-deep 2-high master 远超 criterion (11)；
- single-5 使用 `D/lambda=5^B/2^lambda2`；
- single-2 使用 `D/lambda=2^A/5^lambda5`。

所以 single-deep 也可自然分为：

1. typewise low-ratio strip；
2. forced contact-lift strip。

---

<a id="source-deep-contact-q-square-blocks"></a>

> 整合来源：`deep-contact-q-square-blocks.md`

# A1 minimal diagonal: contact-square Q-side block lifting

> 日期：2026-08-20。依赖 `rational-contact.md`、minimal diagonal odd-prime supply 与 `deep-double-2high-master.md`。本文只使用 double-deep `lambda=1`；当前 surviving double-deep 都属于 2-high/5-low master branch。

本文从**原 rational-contact square** 导出一条与 four-factor/Hensel skeleton 不同源的全局因子结构。核心现象是 Q-side supply divisor `q` 在 contact 差平方中以 `q^2` 出现，因此其 regular prime-power blocks 会平方提升并 whole-block 分配到两个 contact factors。

状态：**已严格完成。**

---

## 1. 原 contact square 的差平方

minimal diagonal 的 contact square 写成

\[
V^2=K-2\rho\,TQ\,N,
\]

其中

\[
K=b_1^2C^2-(TQ)^2N.
\]

因此

\[
\boxed{
(b_1C)^2-V^2
=TQN(TQ+2\rho).}
\tag{1}

在 double-deep 中

\[
\Gamma=\frac\gamma D,
\qquad
\rho=N_0-\frac\gamma{DT},
\]

且

\[
\gamma=DTN_0-h.
\]

因为 `V^2` 的 reduced denominator 整除 `D`，若 `V=a/b` 既约，则 `b^2|D`，故 `b|D`。所以

\[
\boxed{Z:=DV\in\mathbf Z.}
\tag{2}

把 (1) 乘以 `D^2`：

\[
(Db_1C-Z)(Db_1C+Z)
=DQN\bigl(DT(TQ+2N_0)-2\gamma\bigr).
\]

代入 `gamma=DTN_0-h`：

\[
\boxed{
(Db_1C-Z)(Db_1C+Z)
=DQN(DT^2Q+2h).}
\tag{3}

---

## 2. Q-side supply 产生 `q^2`

写完整 odd supply

\[
h=qs,
\qquad Q=qv.
\]

则

\[
DT^2Q+2h
=q(DT^2v+2s).
\]

所以 (3) 精确化为

\[
\boxed{
L_-L_+
=D\,N\,q^2v\,(DT^2v+2s),}
\tag{4}

其中

\[
\boxed{L_\pm:=Db_1C\pm Z.}
\]

这就是 contact Q-side square lifting 的来源。

---

## 3. 两个 contact factors 的公共奇因子

显然

\[
\gcd(L_-,L_+)\mid2Db_1C.
\tag{5}

另一方面

\[
\gcd(Q,Db_1)=1
\]

因为 `D` 只含 2、5，`Q` 与 10 互素，并且 `gcd(Q,b1)=1`。

所以若奇素数

\[
p\mid q\mid Q,
\]

则 `p` 能同时整除 `L_-`,`L_+` 的唯一来源是

\[
\boxed{p\mid C.}
\tag{6}

---

## 4. regular `q` blocks 平方 whole-block lifting

设

\[
p^e\Vert q.
\]

由 (4)：

\[
v_p(L_-)+v_p(L_+)\ge2e.
\tag{7}

若

\[
p\nmid C,
\]

则由 (5)-(6)：

\[
\min(v_p(L_-),v_p(L_+))=0.
\]

故另一边必须承担全部 `2e`：

\[
\boxed{
p^{2e}\mid L_-
\quad\text{or}\quad
p^{2e}\mid L_+.}
\tag{8}

所以每一个不碰 `C` 的 selected Q-side prime-power block 都会：

1. 不能拆到两个 contact factors；
2. exponent 从 `e` 提升到至少 `2e`。

定义

\[
q_{\rm reg}
:=\prod_{p^e\Vert q,\ p\nmid C}p^e.
\]

则存在互素分解

\[
\boxed{q_{\rm reg}=q_-q_+}
\]

使

\[
\boxed{q_-^2\mid L_-,
\qquad q_+^2\mid L_+.}
\tag{9}

这里每个 `p^e` block 整块进入一边。

---

## 5. 即使是 exceptional block，也至少 whole-block 进入一边

若 `p|C`，令

\[
c=v_p(C).
\]

由 (5)：

\[
\min(v_p(L_-),v_p(L_+))\le c.
\]

结合 (7)：

\[
\max(v_p(L_-),v_p(L_+))
\ge2e-c.
\]

同时仅由 `x+y>=2e` 已有

\[
\max(x,y)\ge e.
\]

因此

\[
\boxed{
\max(v_p(L_-),v_p(L_+))
\ge\max(e,2e-c).}
\tag{10}

特别地，哪怕 `p|C`，完整 selected block `p^e` 仍不能被迫拆碎：至少有一个 contact factor 含整个 `p^e`。

regular case `c=0` 正好恢复平方提升 `2e`。

---

## 6. exceptional prime support 只落在一个 `O(T)` resultant 上

现在精确控制

\[
\gcd(Q,C).
\]

minimal diagonal 中

\[
Q=100T^2-10w+1,
\]

\[
a_1=100T^3+(10(5-z-w)+1)T+N_0-1,
\]

\[
C=10T^2a_1+a_2,
\qquad a_2=10T^2-z.
\]

模 `Q`：

\[
100T^2\equiv10w-1,
\]

所以

\[
a_1\equiv10(5-z)T+N_0-1\pmod Q.
\]

乘 `C` 以 10，消去 `10^{-1}`：

\[
\boxed{
10C\equiv
(10w-1)N_0
+10(10w-1)(5-z)T
-10z
\pmod Q.}
\tag{11}

因为 `gcd(10,Q)=1`，令右侧为 `E_C`，则

\[
\boxed{\gcd(Q,C)\mid E_C.}
\tag{12}

使用 `0<N0<=T`，六类型分别有安全界：

\[
\boxed{
\begin{array}{c|c}
(z,w)&0<E_C<c_{z,w}T\\ \hline
(1,1)&c_{z,w}=369\\
(1,2)&779\\
(1,3)&1189\\
(1,4)&1599\\
(3,1)&189\\
(3,2)&399
\end{array}}
\tag{13}

因此统一：

\[
\boxed{\gcd(Q,C)<1599T.}
\tag{14}

所以能破坏平方 whole-block lifting 的 exceptional prime support 必须来自这个显式线性 resultant `E_C=O(T)`；它不可能在 `Q~100T^2` 中任意游走。

---

## 7. 当前意义

剩余 double-deep 2-high master branch 现在同时受两套真正独立的 prime-block skeleton 控制：

1. four-factor：`q,s,bar q,bar s` 与 `alpha,beta` 的 unimodular frame；
2. contact factor：Q-side `q` 的 regular prime-power blocks在 `L_-,L_+` 中平方 whole-block lifting。

尤其后续可以把 `q=q_reg*q_exc` 分开：

- `q_reg` 具有 (9) 的平方 block partition；
- `q_exc` 的 prime support 必须落在 `E_C` 上；
- strict-2 unit square 还固定 `q mod4` 与 `r_10 mod8`。

这为真正利用原 rational-contact square（而不是重复 root/Hensel 条件）提供了新的全局入口。

---

<a id="source-deep-contact-sign-window"></a>

> 整合来源：`deep-contact-sign-window.md`

# A1 minimal diagonal: continuous contact-sign window in deep sector

> 日期：2026-08-20。依赖 `central-gap-sign-collapse.md` 与 `sharp-positive-tail-window.md`。当前统一剩余范围可取 `k=g>=32`；本文估计实际从 `k>=31` 已足够。

`central-gap-sign-collapse.md` 的最高阶平方核并不依赖 `Gamma` 为整数。这里把同一个 leading-sign argument 直接用于 deep sector 的连续 normalized gap

\[
\Gamma=10^k(N_0-\rho).
\]

得到六类型新的 contact-sign 下沿，并把 double-deep 的 bounded renormalized 参数 `xi=t/D` 的下界同步抬高。

状态：**已严格完成。**

---

## 1. contact square leading term

令

\[
T=10^k,
\qquad s=N_0/T\in[0.1,1].
\]

原 rational-contact square kernel 写成

\[
R=10000F_{z,w,\Gamma}(s)T^{10}+E_9,
\]

其中 `central-gap-sign-collapse.md` 已严格给出

\[
|E_9|\le101834561T^9.
\]

六类型：

\[
F_{1,1}=s^2-280s+200\Gamma-5980,
\]

\[
F_{1,2}=s^2-280s+200\Gamma-5180,
\]

\[
F_{1,3}=s^2-280s+200\Gamma-4380,
\]

\[
F_{1,4}=s^2-280s+200\Gamma-3580,
\]

\[
F_{3,1}=s^2-240s+200\Gamma-4340,
\]

\[
F_{3,2}=s^2-240s+200\Gamma-3940.
\]

这些公式是关于 real/rational `Gamma` 的多项式恒等式；central 中取整数 gap 只是其特例。

---

## 2. deep candidate 必须有 `F` 非负到极小误差

任何 exact candidate 都要求

\[
R\ge0.
\]

故

\[
F_{z,w,\Gamma}(s)
\ge-rac{101834561}{10000T}.
\]

当前 `k>=31`：

\[
\frac{101834561}{10000T}<1.1\times10^{-27}.
\]

因此所有下面保留到 `10^-4` 的十进制下界都有巨大安全余量。

又每个 `F` 在 `s in[0.1,1]` 上严格递减，所以

\[
F(s)\le F(0.1).
\]

若 `F(s)` 能非负，则 `F(0.1)` 必须至少大于上述极小负误差。

由此得到：

\[
\boxed{
\begin{array}{c|c}
(z,w)&\Gamma\text{ 必须满足}\\ \hline
(1,1)&\Gamma>30.0399\\
(1,2)&\Gamma>26.0399\\
(1,3)&\Gamma>22.0399\\
(1,4)&\Gamma>18.0399\\
(3,1)&\Gamma>21.8199\\
(3,2)&\Gamma>19.8199
\end{array}}
\tag{1}

这比纯 positive-tail theorem 的类型下界再次提高约 `2--3` 个 gap units。

---

## 3. 与 sharpened upper window 合并

`sharp-positive-tail-window.md` 的类型上界可安全写成

\[
\boxed{
\begin{array}{c|c}
(z,w)&\Gamma\text{ window}\\ \hline
(1,1)&30.0399<\Gamma<33.003\\
(1,2)&26.0399<\Gamma<29.003\\
(1,3)&22.0399<\Gamma<25.003\\
(1,4)&18.0399<\Gamma<21.003\\
(3,1)&21.8199<\Gamma<39.003\\
(3,2)&19.8199<\Gamma<37.003
\end{array}}
\tag{2}

尤其四个 `z=1` 类型的 continuous gap 都被压到宽度不足 3 的窄带。

---

## 4. 对 renormalized factor 参数 `xi=t/D` 的影响

对任意 double-deep，universal factorization 给

\[
\boxed{
\xi:=\frac tD
=
\frac{
(10\Gamma T-wN_0)
(100\Gamma T-(10w-1)N_0)
}{TN_0-\Gamma}.}
\tag{3}

写 `s=N_0/T`：

\[
\xi
=
\frac{
(10\Gamma-ws)
(100\Gamma-(10w-1)s)
}{s-\Gamma/T^2}.
\tag{4}

在当前区域中，右侧对 `Gamma` 严格递增、对 `s` 严格递减。

另一方面 contact sign 本身给每个 `s` 的必要下界

\[
\Gamma
\gtrsim
\frac{C+a s-s^2}{200},
\]

其中 `(C,a)` 为对应 `F` 中常数与线性系数。把它代回 (4)，最小值发生在 `s=1`。忽略只会使 denominator 变小、从而使 `xi` 变大的 `Gamma/T^2` correction，得到严格安全整数下界：

\[
\boxed{
\begin{array}{c|c}
(z,w)&\xi\text{ 下界}\\ \hline
(1,1)&\xi>973439.975\\
(1,2)&\xi>734409.975\\
(1,3)&\xi>528999.975\\
(1,4)&\xi>357209.975\\
(3,1)&\xi>519839.975\\
(3,2)&\xi>428489.975
\end{array}}
\tag{5}

因此在 moderate branch `xi=r` 为整数时：

\[
\boxed{
\begin{array}{c|c}
(z,w)&r\ge\\ \hline
(1,1)&973440\\
(1,2)&734410\\
(1,3)&529000\\
(1,4)&357210\\
(3,1)&519840\\
(3,2)&428490
\end{array}}
\tag{6}

旧 typewise upper bounds 保持不变，所以新的 moderate `r` windows 为

\[
\boxed{
\begin{array}{c|c}
(z,w)&r\\ \hline
(1,1)&973440\le r\le10885221\\
(1,2)&734410\le r\le8400003\\
(1,3)&529000\le r\le6236387\\
(1,4)&357210\le r\le4394372\\
(3,1)&519840\le r\le15204352\\
(3,2)&428490\le r\le13677244
\end{array}}
\tag{7}

---

## 5. 当前用途

LL 已经关闭，所以 (7) 现在主要缩短 moderate 2-high master branch `eta<=0` 的 HL 参数窗。

对 `eta>0` 的 former `E_2`，(5) 同样适用于 bounded rational `xi`; 因此 extreme pure-2 denominator descent 也应使用新的 typewise lower bounds，而不再使用全局 `196000` 粗界。

更重要的是 (1)-(2) 是**原 rational-contact square 的独立全局输入**；它不属于 four-factor/Hensel skeleton，因此可以安全与后者联用。

---

<a id="source-deep-double-2high-master"></a>

> 整合来源：`deep-double-2high-master.md`

# A1 minimal diagonal: unified double-deep 2-high / 5-low master branch

> 日期：2026-08-20。依赖 `deep-moderate-three-pattern.md`、`deep-double-5high-collapse.md`、`deep-ll-modular-exhaustion.md`、`deep-extreme-height-collapse.md` 与 `deep-four-factor-frame.md`。

当前 double-deep 中：

- moderate LL 已全部关闭；
- moderate LH（5-high）已关闭；
- 5-extreme 已关闭；
- high-high 已由 balanced collapse 关闭。

所以所有尚存 double-deep candidate 实际都处于同一个方向：

\[
\boxed{2\text{-high}/5\text{-low}.}
\]

本文把此前分开的 moderate HL 与 2-extreme `E_2` 合并成一套单一正规形。

状态：**已严格完成。**

---

## 1. 统一偏移参数

写

\[
T=10^k,
\qquad D=2^A5^B,
\qquad N_0=2^{\nu_2}5^{\nu_5}n_0,
\]

其中 `(n_0,10)=1`。

在剩余 2-high branch 中定义

\[
\boxed{\eta:=A-(2k+3).}
\tag{1}

于是

\[
\boxed{A=2k+3+\eta.}
\tag{2}

- `eta<=0`：moderate HL；
- `eta=0`：moderate threshold；
- `eta>0`：原来的 2-extreme `E_2`。

所以 moderate / extreme 的区别只剩 `eta` 的符号。

---

## 2. 5-low 高度

记

\[
\boxed{Y:=B+\nu_5.}
\]

所有剩余 double-deep 都必须在 5-low：

\[
\boxed{Y<k+1.}
\tag{3}

定义

\[
\boxed{d:=k+1-Y>0.}
\tag{4}

---

## 3. `t` 的统一 valuation

universal factorization 给

\[
X_1=sa,
\qquad X_2=qb,
\qquad ab=t.
\]

2-high 时两项低 valuation 固定为

\[
v_2(X_1)=k+1,
\qquad
v_2(X_2)=k+2,
\]

而 5-low 给

\[
v_5(X_1)=v_5(X_2)=Y.
\]

所以

\[
\boxed{v_2(t)=2k+3,}
\qquad
\boxed{v_5(t)=2Y.}
\tag{5}

因此存在唯一正整数 `r_10`，满足

\[
\boxed{
t=2^{2k+3}5^{2Y}r_{10},
\qquad (r_{10},10)=1.}
\tag{6}

---

## 4. bounded renormalized gap 参数

令

\[
\boxed{\xi:=t/D.}
\]

由 (2)、(6)：

\[
\boxed{
\xi
=2^{-\eta}5^{B+2\nu_5}r_{10}.}
\tag{7}

universal real window 仍给

\[
\boxed{196000<\xi<15214000.}
\tag{8}

所以：

- `eta<=0` 时 `xi` 为整数，正是旧 moderate 参数 `r`；
- `eta>0` 时 `xi` 的 reduced denominator 是纯 `2^eta`，正是旧 `E_2` 的 pure-2 excess。

因此 moderate HL 与 2-extreme 在同一 `xi` 坐标中无缝连接。

---

## 5. factor quotients 统一

由 (5) 可写

\[
\boxed{
a=2^{k+1}5^Y\alpha,}
\]

\[
\boxed{
b=2^{k+2}5^Y\beta,}
\tag{9}

其中

\[
\boxed{\alpha\beta=r_{10},}
\qquad
\boxed{\gcd(\alpha,\beta)=1.}
\tag{10}

所以 `r_10` 的 prime-power blocks 仍必须 whole-block 分配给 `alpha` 或 `beta`。

---

## 6. stripped four-factor system

定义

\[
\boxed{c:=A+\nu_2-k-2
=k+1+\eta+\nu_2.}
\tag{11}

2-high 保证 `c>0`。

four-factor 两条线性式除去显式 2/5 powers 后统一变成

\[
\boxed{2\beta u-\alpha v=5^d,}
\tag{12}

\[
\boxed{\beta q-5\alpha s=2^c n_0.}
\tag{13}

其中

\[
su=b_1,
\qquad qv=Q,
\qquad qv-10su=1.
\]

取 adjugate：

\[
\boxed{2^{c+1}n_0u-5^dq=\alpha,}
\tag{14}

\[
\boxed{2^cn_0v-5^{d+1}s=\beta.}
\tag{15}

这四式对 moderate HL 与 `E_2` 完全相同；`eta` 只通过 `c` 出现。

---

## 7. 2-adic parity 也统一

因为

\[
A=2k+3+\eta,
\]

其 parity 只是 `1+eta mod 2`。

### even `w=2,4`

全部 2-deep strict-low 要求 `A` 为奇数，所以

\[
\boxed{\eta\equiv0\pmod2.}
\tag{16}

因此：

- moderate HL 的 `v_2(r)=-eta` 必为偶数；
- 2-extreme 的 excess `E=eta` 也必为偶数。

### odd `w=1,3`

若 `n_2=v_2(N)`，strict-low parity 为

\[
A\equiv1+n_2\pmod2.
\]

所以

\[
\boxed{\eta\equiv n_2\pmod2.}
\tag{17}

在 minimal diagonal 中 `n_2=0` 对应 `N_0` odd，`n_2=1` 对应 `N_0` even，因此 `eta` parity 同时锁定 prefix parity。

---

## 8. 当前意义

原来的分类

\[
HL_{\rm moderate}\cup E_2
\]

现在可直接替换成一个 master branch：

\[
\boxed{
\begin{gathered}
A=2k+3+\eta,\qquad Y=B+\nu_5<k+1,\\
t=2^{2k+3}5^{2Y}r_{10},\\
\xi=2^{-\eta}5^{B+2\nu_5}r_{10},\\
196000<\xi<15214000,\\
2\beta u-\alpha v=5^d,\\
\beta q-5\alpha s=2^c n_0,
\end{gathered}}
\]

其中

\[
c=k+1+\eta+\nu_2,
\qquad d=k+1-B-\nu_5.
\]

后续不再需要把 moderate HL 与 2-extreme 维护成两套算术证明；唯一差别只是 `eta<=0` 或 `eta>0`。

---

<a id="source-deep-double-5high-collapse"></a>

> 整合来源：`deep-double-5high-collapse.md`

# A1 minimal diagonal: double-deep 5-high collapse

> 日期：2026-08-20。依赖 `deep-first-complement-remainder.md`、`deep-moderate-three-pattern.md`、`deep-extreme-height-collapse.md`。当前范围 `k=g>=31`。

本文证明 double-deep 中所有 5-adic high branches 都为空。

`deep-extreme-height-collapse.md` 已经关闭 5-extreme；本文进一步关闭 moderate 5-high，也就是此前三模板中的 `LH`。

最终：

\[
\boxed{\text{double-deep 不存在任何 5-high candidate}.}
\]

因此 moderate double-deep 只剩 `LL` 与 `HL`，二者都在 5-low，并统一满足

\[
\boxed{B+2\nu_5=v_5(r)\le10.}
\]

状态：**已严格完成。**

---

## 1. moderate `LH` 的 5-adic depth

在 moderate double-deep 中有

\[
196000<r<15214000,
\qquad v_5(r)\le10.
\]

`LH` 模板由 `deep-moderate-three-pattern.md` 给出

\[
\boxed{B=2k+3-v_5(r).}
\tag{1}
\]

记

\[
Y:=B+\nu_5=v_5(MDN_0).
\]

则由 `v_5(r)<=10`：

\[
\boxed{Y\ge2k-7.}
\tag{2}
\]

另一方面 `deep-complement-height.md` 已证明所有 double-deep 都满足

\[
\boxed{B+\nu_5<3k,}
\]

所以

\[
\boxed{Y<3k.}
\tag{3}
\]

---

## 2. first remainder 必须承载全部 5-adic depth

在 double-deep 中 `lambda=1`。`deep-first-complement-remainder.md` 给出

\[
MDN_0=1000T^3+R_1,
\]

以及

\[
\boxed{14300T<R_1<390100T.}
\tag{4}
\]

第一项满足

\[
v_5(1000T^3)=3k+3.
\]

由 (3)：

\[
Y<3k<3k+3.
\]

所以 `MDN_0` 的较浅 5-adic valuation 不可能来自 `1000T^3`，而必须由 `R_1` 精确承担：

\[
\boxed{v_5(R_1)=Y.}
\tag{5}
\]

特别地

\[
\boxed{5^Y\mid R_1.}
\tag{6}
\]

---

## 3. real size 与 `5^Y` 矛盾

由 (2)：

\[
5^Y\ge5^{2k-7}.
\]

而

\[
\frac{5^{2k-7}}{T}
=
\frac{5^{2k-7}}{2^k5^k}
=
\frac1{5^7}\left(\frac52\right)^k.
\]

在 `k=31`：

\[
\frac1{5^7}\left(\frac52\right)^{31}
>27,000,000
>390100.
\]

该比值以后每增加一个 `k` 再乘 `5/2>1`。因此对所有 `k>=31`：

\[
\boxed{5^{2k-7}>390100T.}
\tag{7}
\]

结合 (4)、(6)：

\[
0<R_1<390100T<5^Y,
\qquad 5^Y\mid R_1,
\]

矛盾。

所以

\[
\boxed{\text{moderate LH 完全为空}.}
\tag{8}
\]

---

## 4. 所有 5-high double-deep 均为空

5-adic high branch 只有两种来源：

1. moderate `LH`；
2. 5-extreme。

本文关闭第一种；`deep-extreme-height-collapse.md` 已关闭第二种。因此

\[
\boxed{\text{double-deep 中所有 5-high states 为空}.}
\tag{9}
\]

于是 moderate double-deep 只剩

\[
\boxed{LL\cup HL.}
\]

两者都处于 5-low。由 `deep-moderate-three-pattern.md` 的 low formula：

\[
\boxed{B+2\nu_5=v_5(r)\le10.}
\tag{10}
\]

特别地

\[
\boxed{B\le10.}
\tag{11}
\]

所以整个 moderate double-deep 的 5-denominator 已被压入十层绝对有限带。

---

## 5. 当前 double-deep 核心

此前 double-deep 的五模板为

\[
LL,\ LH,\ HL,\ E_2,\ E_5.
\]

现在：

- `LH`：本文关闭；
- `E_5`：`deep-extreme-height-collapse.md` 关闭；
- high-high：`deep-balanced-collapse.md` 关闭。

因此只剩

\[
\boxed{LL\cup HL\cup E_2.}
\]

也就是说所有尚存 double-deep 都是 **5-low**；2-side 才是唯一还可能发生 high / extreme 的方向。

---

<a id="source-deep-extreme-classification"></a>

> 整合来源：`deep-extreme-classification.md`

# A1 minimal diagonal: extreme double-deep classification

> 日期：2026-08-20。依赖 `deep-global-factorization.md`、`deep-balanced-collapse.md`。当前范围 `k=g>=31`。

本文处理 double-deep 中超出 moderate threshold

\[
2k+3
\]

的 exponent。结论是：两侧不可能同时 extreme；任何 extreme candidate 只能是一侧 extreme-high、另一侧 shallow-low。

状态：**已严格完成。**

---

## 1. 两侧不能同时 extreme

已有粗 decade/supply 上界

\[
\boxed{D=2^A5^B<10000T^2.}
\tag{1}

若两侧同时 extreme，则整数指数至少满足

\[
A\ge2k+4,
\qquad
B\ge2k+4.
\]

于是

\[
D\ge2^{2k+4}5^{2k+4}
=10^{2k+4}
=10000T^2,
\]

与 (1) 矛盾。因此

\[
\boxed{
A>2k+3
\Longrightarrow B\le2k+3,
}
\tag{2}

\[
\boxed{
B>2k+3
\Longrightarrow A\le2k+3.
}
\tag{3}

所以 excess renormalization 的 reduced denominator永远只可能是纯 `2`-power 或纯 `5`-power，不会同时含两个 extreme prime sides。

---

## 2. 2-extreme 自动是 2-high

设

\[
A\ge2k+4.
\]

在 universal factor

\[
X_1=10\gamma T-wDN_0,
\]

两项的 2-adic valuations 为

\[
k+1,
\qquad A+e+\nu_2>k+1.
\]

因此

\[
\boxed{v_2(X_1)=k+1.}
\tag{4}

同理 `X_2` 两项赋值为

\[
k+2,
\qquad A+\nu_2>k+2,
\]

故

\[
\boxed{v_2(X_2)=k+2.}
\tag{5}

由于 `q,s` 与 2 互素且 `ab=t`：

\[
\boxed{v_2(t)=2k+3.}
\tag{6}

这也与 universal congruence

\[
t\equiv-1000\gamma T^2\pmod{2^A}
\]

完全一致。

定义 2-excess

\[
\boxed{E:=A-(2k+3)>0.}
\]

则

\[
\boxed{v_2(t/D)=-E.}
\tag{7}

---

## 3. fully-balanced collapse 强迫 5-shallow

2-extreme 下显然

\[
A+e+\nu_2>k.
\]

若再有

\[
B+\nu_5\ge k,
\]

则落入 `deep-balanced-collapse.md` 已排除的 double-deep balanced region。

所以任何 2-extreme candidate 必须满足

\[
\boxed{B+\nu_5<k.}
\tag{8}

特别地 5-side 一定处于 strict low branch，因为

\[
B+\nu_5<k<k+1.
\]

于是从 factor pair 的 5-adic valuation：

\[
\boxed{
v_5(X_1)=v_5(X_2)=B+\nu_5,}
\tag{9}

\[
\boxed{
v_5(t)=2B+2\nu_5.}
\tag{10}

所以 2-extreme 的唯一模板是

\[
\boxed{
2\text{-high extreme}/5\text{-low shallow}.}
\tag{11}

---

## 4. 5-extreme 完全对称

若

\[
B\ge2k+4,
\]

则

\[
\boxed{v_5(X_1)=k+1,}
\qquad
\boxed{v_5(X_2)=k+2,}
\]

所以

\[
\boxed{v_5(t)=2k+3.}
\tag{12}

定义

\[
\boxed{F:=B-(2k+3)>0,}
\]

则

\[
\boxed{v_5(t/D)=-F.}
\tag{13}

另一方面 balanced collapse 强迫

\[
\boxed{A+e+\nu_2<k.}
\tag{14}

因此 2-side 严格 low：

\[
\boxed{
v_2(X_1)=A+e+\nu_2,}
\]

\[
\boxed{
v_2(X_2)=A+\nu_2,}
\]

\[
\boxed{
v_2(t)=2A+2\nu_2+e.}
\tag{15}

所以 5-extreme 的唯一模板是

\[
\boxed{
2\text{-low shallow}/5\text{-high extreme}.}
\tag{16}

---

## 5. double-deep 的完整五模板分类

结合 `deep-moderate-three-pattern.md`：

### moderate

1. LL;
2. LH;
3. HL.

### extreme

4. 2-extreme HL：
   \[
   A\ge2k+4,
   \qquad B+\nu_5<k;
   \]
5. 5-extreme LH：
   \[
   B\ge2k+4,
   \qquad A+e+\nu_2<k.
   \]

不存在：

- transition strips；
- high-high；
- both-extreme。

因此

\[
\boxed{
\text{double-deep}
=LL\cup LH\cup HL\cup E_2\cup E_5.
}
\tag{17}

这已经把原始二维 `(A,B)` 平面替换成五条明确的 valuation templates。

---

## 6. extreme renormalized parameter

`deep-global-factorization.md` 定义

\[
r_*:=t/D,
\qquad
196000<r_*<15214000.
\]

在 2-extreme 中，由 (7)、而 5-side moderate：

\[
\boxed{
\operatorname{den}(r_*)=2^E.
}
\tag{18}

在 5-extreme 中：

\[
\boxed{
\operatorname{den}(r_*)=5^F.
}
\tag{19}

所以 extreme 分支各自只剩**单素数 denominator excess**。下一步可分别对 pure-2 与 pure-5 bounded rational `r_*` 做一维 denominator descent / local modular analysis。

---

<a id="source-deep-extreme-height-collapse"></a>

> 整合来源：`deep-extreme-height-collapse.md`

# A1 minimal diagonal: extreme height collapse

> 日期：2026-08-20。依赖 `deep-extreme-classification.md` 与 `deep-complement-height.md`。当前范围 `k=g>=31`。

`deep-extreme-classification.md` 已证明 extreme double-deep 只能是一侧 extreme、另一侧 shallow-low。本文把 complement-height inequality 代入，得到：

\[
\boxed{\text{5-extreme 完全为空}.}
\]

因此 double-deep 的 extreme 部分只剩 2-extreme；其 5-adic shallow height 还满足统一线性上界

\[
\boxed{B+\nu_5<7+0.570k.}
\]

状态：**已严格完成。**

---

## 1. 5-extreme 的结构

若 5-extreme，则

\[
B\ge2k+4.
\]

由 `deep-extreme-classification.md`，balanced collapse 强迫

\[
\boxed{A+e+\nu_2<k,}
\tag{1}

其中

\[
e=v_2(w),
\qquad\nu_2=v_2(N_0).
\]

同时 `deep-complement-height.md` 已证明

\[
B+\nu_5<3k,
\]

所以两个 cancellation exponents 都未达到 `3k`，可以直接使用未饱和 height inequality：

\[
\boxed{
2^{A+e+\nu_2}5^{B+\nu_5}
<390100\,10^k.
}
\tag{2}

---

## 2. 5-extreme 立即与 height inequality 矛盾

左侧最小也满足

\[
2^{A+e+\nu_2}5^{B+\nu_5}
\ge5^{2k+4}.
\]

因此 (2) 要求

\[
5^{2k+4}
<390100\,2^k5^k.
\]

约去 `5^k`：

\[
625\left(\frac52\right)^k<390100.
\tag{3}

但在 `k=31` 已有

\[
625(5/2)^{31}>10^{15}>390100,
\]

以后只会更大。矛盾。

故

\[
\boxed{
B\ge2k+4
\Longrightarrow\bot.
}
\tag{4}

所以 5-extreme double-deep 完全为空。

---

## 3. 2-extreme 的 5-side 统一高度界

现在唯一可能的 extreme branch 是

\[
A=2k+3+E,
\qquad E\ge1.
\]

balanced collapse 强迫

\[
\boxed{Y:=B+\nu_5<k.}
\tag{5}

### 3.1 若 2-side 未达到 `3k`

设

\[
A+e+\nu_2<3k.
\]

height inequality 为

\[
2^{2k+3+E+e+\nu_2}5^Y
<390100\,2^k5^k.
\]

所以

\[
5^Y
<390100\,
\frac{5^k}{2^{k+3+E+e+\nu_2}}.
\]

因为

\[
390100<5^8,
\qquad
2>5^{0.430},
\]

得到安全粗化

\[
Y
<k+8-0.430(k+3+E+e+\nu_2)
<7+0.570k.
\tag{6}

### 3.2 若 2-side 达到 `3k`

若

\[
A+e+\nu_2\ge3k,
\]

`deep-complement-height.md` 已给更强结论

\[
\boxed{Y<8+0.139k.}
\tag{7}

对 `k>=31`，(7) 显然蕴含更弱统一界 (6)。

所以全部 2-extreme candidate 都满足

\[
\boxed{
B+\nu_5<7+0.570k.
}
\tag{8}

---

## 4. 2-extreme 的 factor valuation

`deep-extreme-classification.md` 还给

\[
v_2(t)=2k+3,
\]

而 5-side shallow-low 给

\[
v_5(t)=2B+2\nu_5.
\]

因此可写

\[
\boxed{
t=
2^{2k+3}
5^{2B+2\nu_5}
r_{10},
\qquad\gcd(r_{10},10)=1.}
\tag{9}

又

\[
D=2^{2k+3+E}5^B,
\]

所以 renormalized bounded parameter 为

\[
\boxed{
\frac tD
=
\frac{5^{B+2\nu_5}r_{10}}{2^E},
}
\tag{10}

且始终满足

\[
\boxed{
196000
<\frac{5^{B+2\nu_5}r_{10}}{2^E}
<15214000.
}
\tag{11}

因此剩余 extreme branch 已严格变成一个 pure-2 denominator problem；5-side height 由 (8) 控制，而所有非 `2,5` 自由度集中在 odd integer `r_{10}`。

---

## 5. 当前 double-deep 分类进一步缩短

moderate three-pattern 仍为

\[
LL,\quad LH,\quad HL.
\]

extreme 原有 `E_2,E_5` 两支，现在 `E_5` 已由本文排除。因此

\[
\boxed{
\text{double-deep}
=LL\cup LH\cup HL\cup E_2,
}
\tag{12}

其中 `E_2` 是 one-sided 2-extreme / 5-low branch。

下一步对 extreme 只需研究 (10)-(11) 的 pure-2 denominator descent，不再需要 5-extreme 分支。

---

<a id="source-deep-first-complement-remainder"></a>

> 整合来源：`deep-first-complement-remainder.md`

# A1 minimal diagonal: universal first complement remainder

> 日期：2026-08-20。依赖 `deep-complement-height.md`。当前统一范围 `k=g>=31`。

本文保留 complement identity 的第一层十进制余数。这个对象对 single / double deep 都成立，并给出一个只有 `O(lambda*T)` 大小、但必须承载原 `MDN_0` 的局部深赋值的整数。

状态：**已严格完成。**

---

## 1. 定义 first remainder

沿用

\[
T=10^k,
\qquad
D=2^A5^B,
\qquad
DTN_0-\gamma=h\lambda,
\]

\[
M:=\frac{Qb_1}{h},
\qquad
\lambda=2^{\lambda_2}5^{\lambda_5}.
\]

又

\[
Qb_1=1000T^4+c_2T^2+C_0,
\]

其中

\[
c_2=10(1-20w),
\qquad
C_0=w(10w-1).
\]

乘以 `M`：

\[
M(DTN_0-\gamma)=\lambda Qb_1.
\]

模 `T` 看：

\[
-M\gamma\equiv C_0\lambda\pmod T.
\]

因此

\[
\boxed{
J_1:=\frac{M\gamma+C_0\lambda}{T}\in\mathbf Z.
}
\tag{1}
\]

把它代回原恒等式并除以 `T`：

\[
\boxed{
MDN_0
=1000\lambda T^3+c_2\lambda T+J_1.
}
\tag{2}
\]

---

## 2. `J_1/(lambda*T)` 落在固定区间

由 `deep-complement-height.md`：

\[
\mu:=\frac{MD}{\lambda T^2},
\qquad
1000<\mu<10001,
\]

以及

\[
\Gamma_k=\frac\gamma D,
\qquad
15.09<\Gamma_k<39.003.
\]

所以

\[
\frac{J_1}{\lambda T}
=
\frac{M\gamma}{\lambda T^2}
+
\frac{C_0}{T^2}
=
\mu\Gamma_k+\frac{C_0}{T^2}.
\]

因此

\[
\boxed{
15090<\frac{J_1}{\lambda T}<390070.
}
\tag{3}
\]

特别地 `J_1>0`。

---

## 3. 真正的小 remainder `R_1`

定义

\[
\boxed{R_1:=c_2\lambda T+J_1.}
\tag{4}
\]

由于

\[
-790\le c_2\le-190,
\]

由 (3) 得安全统一界

\[
\boxed{
14300\,\lambda T<R_1<390100\,\lambda T.
}
\tag{5}
\]

而 (2) 变成

\[
\boxed{
MDN_0=1000\lambda T^3+R_1.
}
\tag{6}
\]

所以任何落在 `MDN_0` 上、但比 `1000 lambda T^3` 更浅的 2/5-adic valuation，都必须完整落到这个只有 `O(lambda*T)` 大小的 `R_1` 上。

---

## 4. fully-balanced collapse 的解释

若两侧 cancellation depth 都达到

\[
A+e+\nu_2\ge k+\lambda_2,
\qquad
B+\nu_5\ge k+\lambda_5,
\]

则 `lambda*T^2 | MDTN_0`。由原 identity 进一步得到 `lambda*T | J_1`，于是可以写

\[
J_1=J\lambda T
\]

并得到 `deep-balanced-collapse.md` 中绝对有界的整数 `J`。

所以 `J_1` 是 balanced descent 与剩余 shallow branches 的公共第一层对象。

---

## 5. 当前用途

后续无需每次重新展开 `Qb_1`。任何 deep branch 若能证明某个素数 `p in {2,5}` 满足

\[
v_p(MDN_0)<v_p(1000\lambda T^3),
\]

就自动得到

\[
p^{v_p(MDN_0)}\mid R_1.
\]

再和 (5) 的实数尺寸比较即可产生 branch-specific contradiction 或高度上界。

`deep-double-5high-collapse.md` 将给出第一个整支应用。

---

<a id="source-deep-four-factor-frame"></a>

> 整合来源：`deep-four-factor-frame.md`

# A1 minimal diagonal: universal deep four-factor frame

> 日期：2026-08-20。依赖 `deep-universal-factorization.md`。当前范围 `k=g>=31`。

`deep-universal-factorization.md` 已证明，对任意 deep state 存在

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\]

以及正整数 `a,b,t`：

\[
X_1=sa,
\qquad
X_2=qb,
\qquad
ab=t,
\]

其中

\[
X_1=10\gamma T-wDN_0,
\]

\[
X_2=100\gamma T-(10w-1)DN_0.
\]

本文把 complementary divisors

\[
\bar q:=Q/q,
\qquad
\bar s:=b_1/s
\]

也接入同一组坐标，并得到第二个整数平方与两个精确乘法恒等式。

状态：**已严格完成。**

---

## 1. 两条线性关系

直接相减：

\[
X_2-10X_1=DN_0.
\]

代入 `X_1=sa,X_2=qb`：

\[
\boxed{
qb-10sa=DN_0.
}
\tag{1}

另一方面，由

\[
DTN_0-\gamma=h\lambda=qs\lambda
\]

有

\[
\begin{aligned}
X_1
&=10(DTN_0-h\lambda)T-wDN_0\\
&=DN_0(10T^2-w)-10qs\lambda T\\
&=s\left(\bar sDN_0-10q\lambda T\right).
\end{aligned}
\]

所以

\[
\boxed{a=\bar sDN_0-10q\lambda T.}
\tag{2}

同理

\[
X_2
=q\left(\bar qDN_0-100s\lambda T\right),
\]

故

\[
\boxed{b=\bar qDN_0-100s\lambda T.}
\tag{3}

由 (2)-(3)：

\[
\begin{aligned}
\bar q a-\bar s b
&=-10Q\lambda T+100b_1\lambda T\\
&=-10\lambda T,
\end{aligned}
\]

因为 `Q=10b_1+1`。因此

\[
\boxed{
\bar s b-\bar q a=10\lambda T.
}
\tag{4}

(1) 与 (4) 是 supply / complement 的完全对偶线性坐标。

---

## 2. supply-side square

由 (1) 与 `qs=h`，把 `s` 消掉：

\[
bq^2-DN_0q-10ah=0.
\]

因此判别式必须是整数平方。存在 `R>0`：

\[
\boxed{
R^2=D^2N_0^2+40abh
=D^2N_0^2+40th.
}
\tag{5}

实际上

\[
\boxed{
R=2bq-DN_0=DN_0+20as.
}
\tag{6}

---

## 3. complement-side square

由 (4) 与 `\bar q\bar s=M:=Qb_1/h`，消去 `\bar s`：

\[
a\bar q^2+10\lambda T\bar q-bM=0.
\]

故存在 `S>0`：

\[
\boxed{
S^2=100\lambda^2T^2+4abM
=100\lambda^2T^2+4tM.
}
\tag{7}

并且根公式精确给出

\[
\boxed{
S=10\lambda T+2a\bar q
=2b\bar s-10\lambda T.
}
\tag{8}

所以

\[
\boxed{
S-10\lambda T=2a\bar q,
}
\tag{9}

\[
\boxed{
S+10\lambda T=2b\bar s.
}
\tag{10}

这把 complementary Q-side / `b_1`-side divisors 全部显式化。

---

## 4. 两个 supply-free product identities

由 `X_2=qb` 与 (9)：

\[
X_2(S-10\lambda T)
=2ab\,q\bar q
=2tQ.
\]

因此

\[
\boxed{
X_2(S-10\lambda T)=2tQ.
}
\tag{11}

同理由 `X_1=sa` 与 (10)：

\[
\boxed{
X_1(S+10\lambda T)=2tb_1.
}
\tag{12}

这里 `q,s,\bar q,\bar s` 已完全消失。

于是 universal deep 可同时使用两层描述：

- prime-source frame：`X_1=sa,X_2=qb`；
- supply-free frame：(11)-(12)。

---

## 5. `S/(lambda T)` 也落在固定实区间

由 `deep-universal-factorization.md`：

\[
196000\lambda<\frac tD<15214000\lambda.
\]

由 `deep-complement-height.md`：

\[
1000<\mu:=\frac{MD}{\lambda T^2}<10001.
\]

因此

\[
\frac{tM}{\lambda^2T^2}
=\frac{t}{D\lambda}\mu
\]

严格落在

\[
196000000
<\frac{tM}{\lambda^2T^2}
<152155214000.
\]

从 (7)：

\[
\boxed{
28000<\frac S{\lambda T}<780142.
}
\tag{13}

所以 complement square 也产生一个与 `k`、single/double-deep 类型无关的固定实数窗。

这为后续在某个 prime side 出现 `\lambda T|S` 时再次引入 bounded integer 参数提供了入口。

---

## 6. 当前意义

任意 deep candidate 现在同时满足：

\[
\boxed{
\begin{aligned}
&X_1=sa,\qquad X_2=qb,\qquad ab=t,\\
&qb-10sa=DN_0,\\
&\bar s b-\bar q a=10\lambda T,\\
&R^2=D^2N_0^2+40th,\\
&S^2=100\lambda^2T^2+4tM.
\end{aligned}}
\]

并且 (11)-(12) 把 prime supply 本身消掉后仍保留两个精确 product identities。

这套 four-factor frame 将用于继续攻击 moderate LL/LH/HL 和 single-deep；尤其 high branches 中 `a,b` 的大 `2/5` 次幂已经显式已知，可以直接转成 `q,s,\bar q,\bar s` 的局部限制。

---

<a id="source-deep-gap-unit-square"></a>

> 整合来源：`deep-gap-unit-square.md`

# A1 minimal diagonal: deep-gap unit-square locks

> 日期：2026-08-19。依赖 `deep-gap-valuation-normal-form.md` 与 `diagonal.md` 的 odd-prime supply theorem。当前统一范围 `k=g>=26`。

已有 deep-gap 正规形

\[
\Gamma_k=\frac{\gamma}{2^A5^B},
\qquad
V^2=J+2\Gamma_kQN,
\]

其中

\[
v_2(J)=2v_2(w),
\qquad v_5(J)=0.
\]

上一层只使用了平方赋值必须为偶数。本文继续保留平方的**单位部分**，得到新的局部锁。

核心结论：

1. 在 strict 2-adic low-side，
   \[
   \boxed{\gamma QN_2 5^B\equiv1\pmod8,}
   \qquad N_2=N/2^{v_2(N)};
   \]
2. 于是所有 2-deep strict-low candidate 满足
   \[
   \boxed{
   w\in\{1,3\}\Longrightarrow h\equiv1\pmod4,
   }
   \]
   \[
   \boxed{
   w\in\{2,4\}\Longrightarrow h\equiv3\pmod4;
   }
   \]
3. 因为 `h=qs` 且 `s` 是 `1 mod 4` whole-block selector，故 Q-side 因子被定向为
   \[
   \boxed{
   w\text{ odd}\Longrightarrow q\equiv1\pmod4,
   \qquad
   w\text{ even}\Longrightarrow q\equiv3\pmod4.
   }
   \]
4. 在 strict 5-adic low-side 还得到显式 Legendre lock。

状态：**已严格完成。**

---

## 1. 2-adic strict-low 的单位平方条件

记

\[
n_2=v_2(N),
\qquad N_2=N/2^{n_2}.
\]

若 `A>0` 且位于 strict 2-adic low-side，则

\[
v_2(2\Gamma_kQN)=1+n_2-A
< v_2(J).
\]

已经证明该赋值必须为偶数。提出全部 2 次幂后，剩余 2-adic 单位为

\[
\gamma QN_2 5^{-B}.
\]

在模 8 中

\[
5^{-1}\equiv5\pmod8,
\]

所以 `5^{-B}≡5^B mod 8`。2-adic 单位平方必须同余 `1 mod 8`，于是

\[
\boxed{
\gamma QN_2 5^B\equiv1\pmod8.
}
\tag{1}
\]

这是 parity lock 之外真正新的 square-unit information。

---

## 2. even `w`：单位条件统一成 `gamma 5^B=1 mod 8`

### `w=2`

`b_1` 为偶数且 `gcd(a_1,b_1)=1`，故 `a_1` 为奇数，已有 `n_2=0`。

模 8：

\[
b_1\equiv6,
\]

而 `a_2` 为奇数，所以

\[
(a_2b_1)^2\equiv4\pmod8.
\]

因此

\[
N\equiv1+4=5\pmod8.
\]

同时

\[
Q=10b_1+1\equiv5\pmod8.
\]

故

\[
\boxed{QN_2\equiv5\cdot5\equiv1\pmod8.}
\tag{2}
\]

### `w=4`

同样 `a_1` 为奇数、`n_2=0`。此时

\[
b_1\equiv4\pmod8,
\]

所以

\[
(a_2b_1)^2\equiv0\pmod8,
\qquad N\equiv1\pmod8.
\]

并且

\[
Q\equiv1\pmod8.
\]

因此仍有

\[
\boxed{QN_2\equiv1\pmod8.}
\tag{3}
\]

由 (1)：

\[
\boxed{
\gamma5^B\equiv1\pmod8
\qquad(w=2,4).
}
\tag{4}
\]

---

## 3. even `w` 进一步强迫 `h=3 mod 4`

2-deep 意味着

\[
x=-k-A,
\qquad A>0.
\]

若 `B>0`，则同时 `y=-k-B`，从 gap 定义直接得到既约分子

\[
\gamma=2^A5^B10^kN_0-h.
\]

故

\[
\gamma\equiv-h\pmod8.
\tag{5}
\]

若 `B=0`，则 `y>=-k`。写

\[
e_5:=k+y\ge0.
\]

此时

\[
\gamma=2^A10^kN_0-h5^{e_5},
\]

所以

\[
\gamma\equiv-h5^{e_5}\pmod8.
\tag{6}
\]

结合 (4)：

- `B>0` 时
  \[
  h\equiv-5^B\pmod8;
  \]
- `B=0` 时
  \[
  h\equiv-5^{e_5}\pmod8.
  \]

而 `5^m mod 8` 只可能是 `1` 或 `5`，所以两种情况统一给出

\[
\boxed{
h\equiv3\text{ or }7\pmod8,}
\]

特别地

\[
\boxed{
h\equiv3\pmod4
\qquad(w=2,4).}
\tag{7}
\]

---

## 4. odd `w`：统一得到 `h=1 mod 4`

现在 `w=1,3`。模 4 有

\[
Q=10b_1+1\equiv3\pmod4.
\tag{8}
\]

还要证明

\[
\boxed{N_2\equiv1\pmod4.}
\tag{9}
\]

若 `n_2=0`，则 `a_1` 为偶数、`a_2b_1` 为奇数，所以

\[
N\equiv1\pmod4,
\]

即 (9)。

若 `n_2=1`，则 `a_1` 与 `a_2b_1` 都是奇数。两个奇平方均为 `1 mod 8`，故

\[
N\equiv2\pmod8,
\]

所以

\[
N_2=N/2\equiv1\pmod4.
\]

于是 (9) 对两种 `n_2` 都成立。

把 (1) 降模 4；`5^B≡1 mod 4`，故

\[
\gamma\cdot3\cdot1\equiv1\pmod4,
\]

从而

\[
\boxed{\gamma\equiv3\pmod4.}
\tag{10}
\]

另一方面，无论 `B>0` 还是 `B=0`，上一节的 gap numerator 公式降模 4 都统一给出

\[
\gamma\equiv-h\pmod4
\]

（因为任意 `5` 次幂均为 `1 mod 4`）。因此

\[
\boxed{
h\equiv1\pmod4
\qquad(w=1,3).}
\tag{11}
\]

---

## 5. Q-side orientation lock

minimal-diagonal odd-prime supply 精确写成

\[
h=qs,
\qquad q\mid Q,
\]

其中 `s` 是 `b_1` 中所有 `1 mod 4` prime-power blocks 的 whole-block selector。

所以必有

\[
\boxed{s\equiv1\pmod4.}
\tag{12}
\]

由 (7)、(11)：

\[
\boxed{
 w\in\{1,3\}
 \Longrightarrow
 q\equiv1\pmod4,
}
\tag{13}
\]

\[
\boxed{
 w\in\{2,4\}
 \Longrightarrow
 q\equiv3\pmod4.
}
\tag{14}
\]

这给 deep strict-2-low sector 一个新的 prime-supply 方向性：Q-side 因子不能再从 `Q` 的全部 divisors 中任意选取。

特别地，对 even `w`，任何 2-deep candidate 都要求 `Q` 实际提供一个 `3 mod 4` divisor；若某个 fixed layer 的 `Q` 没有这种供给，则该层的整个 2-deep sector立即为空。

---

## 6. 5-adic strict-low 的 Legendre lock

记

\[
n_5=v_5(N),
\qquad N_5=N/5^{n_5}.
\]

若

\[
B>n_5,
\]

则 second term 严格承担五进低赋值。提出 `5^{n_5-B}` 后，单位为

\[
2^{1-A}\gamma QN_5.
\]

又 `Q≡1 mod 5`，故必须有

\[
\boxed{
\left(\frac{2^{1-A}\gamma N_5}{5}\right)=1.
}
\tag{15}
\]

定义

\[
\lambda_2:=
\begin{cases}
0,&A>0,\\
k+x,&A=0,
\end{cases}
\]

则 `lambda_2>=0`，而 gap numerator 在模 5 下统一给出

\[
\gamma\equiv-h2^{\lambda_2}\pmod5.
\tag{16}
\]

由于

\[
\left(\frac{-1}{5}\right)=1,
\qquad
\left(\frac2{5}\right)=-1,
\]

(15)-(16) 化成

\[
\boxed{
\left(\frac{hN_5}{5}\right)
=(-1)^{1-A+\lambda_2}.
}
\tag{17}
\]

所以 5-deep strict-low 也不只有 `B≡n_5 mod 2` 的 valuation parity；其 5-adic 单位特征被精确锁定。

---

## 7. 当前 deep 核心

结合 `deep-gap-valuation-normal-form.md`，deep sector 现在同时受到：

1. `A,B` 的 resonance/奇偶格；
2. strict 2-low 的 mod-8 square-unit lock (1)；
3. Q-side orientation (13)-(14)；
4. strict 5-low 的 Legendre lock (17)；
5. primitive cross-corridor caps 与 decade window。

因此后续 fixed-layer 或统一 deep 证书应直接按这些局部单位类筛 `h=q s`，而不再只按 `(A,B)` 的赋值奇偶扫描。

---

<a id="source-deep-gap-valuation-normal-form"></a>

> 整合来源：`deep-gap-valuation-normal-form.md`

# A1 minimal diagonal: deep-gap valuation normal form

> 日期：2026-08-19。依赖 `gap-denominator-normal-form.md` 与 minimal-diagonal valuation normal form。
> 当前统一范围可取 `k=g>=26`。

本文研究 reduced denominator 不整除 `10^k` 的 deep sector。

把归一化 gap 既约写成

\[
\boxed{
\Gamma_k:=10^k(N_0-\rho)
=\frac{\gamma}{2^A5^B},
}
\tag{1}
\]

其中

\[
A,B\ge0,
\qquad
\gcd(\gamma,2^A5^B)=1.
\]

central sector 恰为 `A=B=0`；deep sector 至少有一个正指数。

核心结论：`A,B` 与原来的 2/5 resonance thresholds 精确对齐，并带有平方赋值奇偶锁。特别地：

- `w=2,4` 时
  \[
  \boxed{A>0\Longrightarrow A\text{ 为奇数};}
  \]
- `w=1,3` 时，若 `n_2:=v_2(N)`，则
  \[
  A=1+n_2
  \]
  是二进 resonance；严格低侧只允许
  \[
  \boxed{A\equiv1+n_2\pmod2;}
  \]
- 若 `n_5:=v_5(N)`，则
  \[
  B=n_5
  \]
  是五进 resonance；当 `B>n_5` 时必须
  \[
  \boxed{B\equiv n_5\pmod2.}
  \]

状态：**已严格完成。**

---

## 1. deep excess 与原 reduced denominator

沿用 `gap-denominator-normal-form.md`：

\[
\rho=\frac nd,
\qquad d=2^a5^b,
\qquad\gcd(n,d)=1.
\]

乘以 `10^k` 后，约去共同的 `2/5` 因子，得到 (1)，其中

\[
\boxed{
A=(a-k)_+,
\qquad
B=(b-k)_+.}
\tag{2}
\]

所以

\[
\boxed{
\text{deep sector}
\iff A>0\text{ or }B>0.}
\tag{3}
\]

---

## 2. 把 rational square 写到 gap 坐标

minimal diagonal 的 rational square 为

\[
V^2=K-2\rho DN,
\qquad D=10^kQ.
\]

由

\[
\rho=N_0-\frac{\Gamma_k}{10^k}
\]

得到

\[
\boxed{
V^2
=J+2\Gamma_k QN,}
\tag{4}
\]

其中

\[
\boxed{
J:=K-2N_0 10^kQN\in\mathbf Z.}
\tag{5}
\]

这一步把 deep denominator 完全移到第二项 `2 Gamma_k QN`。

---

## 3. `J` 的 2/5 赋值仍由 `K` 精确承担

记

\[
e=v_2(w),
\qquad n_2=v_2(N),
\qquad n_5=v_5(N).
\]

已有

\[
v_2(K)=2e,
\qquad v_5(K)=0,
\]

而 `Q` 与 `10` 互素。

第二整数项满足

\[
v_2(2N_0 10^kQN)\ge1+k>2e
\]

（当前 `k>=26`，而 `2e<=4`），以及

\[
v_5(2N_0 10^kQN)\ge k>0.
\]

所以两项赋值严格不同：

\[
\boxed{v_2(J)=2e,}
\tag{6}
\]

\[
\boxed{v_5(J)=0.}
\tag{7}
\]

---

## 4. 二进 deep excess

若 `A>0`，则 `gamma` 为奇数。由 (1)、(4)：

\[
v_2(2\Gamma_kQN)
=1+n_2-A.
\tag{8}
\]

与 (6) 比较。

### low-side

若

\[
1+n_2-A<2e,
\]

等价于

\[
\boxed{A>1+n_2-2e,}
\tag{9}
\]

则第二项严格承担 `V^2` 的二进赋值：

\[
v_2(V^2)=1+n_2-A.
\]

有理平方的赋值必须为偶数，因此

\[
\boxed{
A\equiv1+n_2\pmod2.}
\tag{10}
\]

### resonance

两项赋值相等恰在

\[
\boxed{A=1+n_2-2e.}
\tag{11}
\]

### high-side

若

\[
A<1+n_2-2e,
\]

则 `J` 严格承担低赋值，`v_2(J)=2e` 本身已经是偶数，所以这一层没有额外 parity obstruction。

---

## 5. 六类型的二进 deep 表

### `w=2`

这里

\[
e=1,
\qquad n_2=0.
\]

resonance 值为

\[
1+0-2=-1,
\]

不属于 `A>0`。所以每个 2-deep 状态都在 strict low-side，并由 (10)：

\[
\boxed{A=1,3,5,\ldots.}
\tag{12}
\]

### `w=4`

这里

\[
e=2,
\qquad n_2=0,
\]

resonance 值为 `-3`，同样不在 deep sector。因此

\[
\boxed{A=1,3,5,\ldots.}
\tag{13}
\]

### `w=1,3`

这里 `e=0`，而已知

\[
n_2\in\{0,1\}.
\]

若 `n_2=0`：

\[
\boxed{A=1\text{ resonance},}
\]

strict low-side `A>=2` 中 (10) 只允许

\[
\boxed{A=3,5,7,\ldots.}
\tag{14}
\]

特别地 `A=2` 被直接排除。

若 `n_2=1`：

\[
A=1\text{ 在 high-side},
\]

\[
\boxed{A=2\text{ resonance},}
\]

而 `A>=3` 的 strict low-side 只允许

\[
\boxed{A=4,6,8,\ldots.}
\tag{15}
\]

特别地 `A=3,5,7,...` 全部排除。

---

## 6. 五进 deep excess

若 `B>0`，则 `gamma` 不被 `5` 整除。由 (4)：

\[
v_5(2\Gamma_kQN)
=n_5-B.
\tag{16}
\]

与 `v_5(J)=0` 比较。

### low-side

若

\[
\boxed{B>n_5,}
\tag{17}
\]

则第二项严格承担五进赋值：

\[
v_5(V^2)=n_5-B.
\]

故

\[
\boxed{B\equiv n_5\pmod2.}
\tag{18}
\]

### resonance

\[
\boxed{B=n_5}
\tag{19}
\]

恰为五进 resonance。

### high-side

若

\[
0<B<n_5,
\]

则整数项 `J` 承担低赋值 `0`，没有新的 parity obstruction。

---

## 7. 与旧 `(x,y)` resonance line 完全一致

若原 reduced denominator 在 2 侧 deep：

\[
a=k+A,
\qquad x=-a=-k-A.
\]

旧二进 threshold 为

\[
x_*=2e-1-k-n_2.
\]

所以

\[
\boxed{
x-x_*=-(A-(1+n_2-2e)).}
\tag{20}
\]

因此 (9)、(11) 与 high-side 三种情况正好就是

\[
x<x_*,\qquad x=x_*,\qquad x>x_*.
\]

五进同理：若 `b=k+B`，则

\[
y=-k-B,
\qquad y_*=-k-n_5,
\]

故

\[
\boxed{y-y_*=-(B-n_5).}
\tag{21}
\]

所以 deep-gap denominator normal form 并没有引入新的独立分类；它把旧 resonance geometry 精确翻译成了“归一化 gap 的 reduced denominator excess”。

---

## 8. 当前意义

central sector 已经变成固定 24 个整数 gap，并进一步缩到 30 个 surviving type-gap combinations。

本文则把 genuinely noninteger gap 的 deep sector 变成：

- 一个 2-adic excess `A`，带显式 resonance level 与 parity lattice；
- 一个 5-adic excess `B`，带显式 resonance level `n_5` 与 parity lattice；
- 归一化实窗
  \[
  15.09<\gamma/(2^A5^B)<39.003.
  \]

特别地 even-`w` 的全部 2-deep 状态只可能出现在奇数 `A` 层。

下一步 deep sector 应继续在这些 parity-compatible 层上加入 square-unit residue（2-adic unit mod 8、5-adic unit mod 5）以及 primitive cross-corridor caps；已经无需再把所有 `A,B` 当作无结构二维格点。

---

<a id="source-deep-global-factorization"></a>

> 整合来源：`deep-global-factorization.md`

# A1 minimal diagonal: global double-deep factorization and excess renormalization

> 日期：2026-08-20。依赖 `deep-complement-height.md` 与 minimal-diagonal odd-prime supply。当前统一范围 `k=g>=31`。

本文抽出 `deep-moderate-factorization.md` 背后的**全局**恒等式；这些结论不要求 `A,B<=2k+3`。

对任意 double-deep

\[
\Gamma_k=\frac{\gamma}{D},
\qquad
D=2^A5^B,
\qquad A,B>0,
\qquad \gcd(\gamma,10)=1,
\]

都存在一个正整数 `t`，使

\[
\boxed{
(10\gamma T-wDN_0)
(100\gamma T-(10w-1)DN_0)
=t(DTN_0-\gamma).
}
\]

进一步，若 `h=qs` 是完整 odd-prime supply 分裂，则两个 factor 自动分别吸收 `s` 与 `q`，从而

\[
\boxed{ab=t}
\]

对某些正整数 `a,b`。

`deep-moderate-factorization.md` 中的 `Dr` 只是这里 `t` 在 moderate 区域的特殊写法。

状态：**已严格完成。**

---

## 1. global deep supply quadratic

沿用

\[
T=10^k,
\qquad
L=DT,
\qquad
h=DTN_0-\gamma=N_0L-\gamma.
\]

对 `D^4Qb_1` 做两级 Euclidean descent，得到整数 `U` 满足

\[
C_0D^4N_0^2
-U L N_0
+1000\gamma^2L^2
+\gamma U
+c_2D^2\gamma^2
=0,
\tag{1}
\]

其中

\[
C_0=w(10w-1),
\qquad
c_2=10(1-20w).
\]

与 moderate 文件相同，模 `D`、再模 `D^2` 连续给出

\[
\boxed{D^2\mid U.}
\tag{2}
\]

写

\[
U=D^2u.
\]

则

\[
\boxed{
C_0D^2N_0^2
-DuTN_0
+1000\gamma^2T^2
+\gamma u
+c_2\gamma^2
=0.
}
\tag{3}

---

## 2. 天然平方点与正整数 `t`

定义

\[
\boxed{u_0:=10\gamma(20w-1).}
\]

由 (3) 解出 `u/D`：

\[
\boxed{
\frac uD
=
\frac{
C_0N_0^2+1000\Gamma_k^2T^2+c_2\Gamma_k^2
}{TN_0-\Gamma_k}.
}
\tag{4}

使用

\[
0.1T<N_0\le T,
\qquad
15.09<\Gamma_k<39.003,
\qquad T\ge10^{31},
\]

可取安全界

\[
227000<\frac uD<15214000,
\]

而

\[
0<\frac{u_0}{D}<30813.
\]

因此

\[
\boxed{t:=u-u_0\in\mathbf Z_{>0}}
\tag{5}
\]

并且统一有

\[
\boxed{
196000<\frac tD<15214000.
}
\tag{6}

---

## 3. global factorization

把

\[
u=u_0+t
\]

代回 (3)。由于

\[
\gamma u_0+c_2\gamma^2=0,
\]

得到精确恒等式

\[
\boxed{
(wDN_0-10\gamma T)
((10w-1)DN_0-100\gamma T)
=t(DTN_0-\gamma).
}
\tag{7}

两个左侧括号均为负。定义正整数

\[
\boxed{X_1:=10\gamma T-wDN_0,}
\]

\[
\boxed{X_2:=100\gamma T-(10w-1)DN_0.}
\]

则

\[
\boxed{X_1X_2=t h.}
\tag{8}

---

## 4. prime supply 仍精确分流

写完整 odd-prime supply

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\qquad \gcd(q,s)=1.
\]

由

\[
DTN_0\equiv\gamma\pmod h
\]

分别模 `s,q`：

\[
TX_1\equiv\gamma b_1\equiv0\pmod s,
\]

\[
TX_2\equiv\gamma Q\equiv0\pmod q.
\]

因为 `T` 与 `q,s` 互素：

\[
\boxed{s\mid X_1,}
\qquad
\boxed{q\mid X_2.}
\tag{9}

所以存在正整数 `a,b`：

\[
\boxed{X_1=sa,}
\qquad
\boxed{X_2=qb.}
\]

结合 (8)、`h=qs`：

\[
\boxed{ab=t.}
\tag{10}

这条 factor-pair identity 对整个 double-deep 都成立。

---

## 5. `t` 的 2/5 congruence

把 (3) 模 `D`：

\[
1000\gamma^2T^2+\gamma u+c_2\gamma^2\equiv0\pmod D.
\]

用 `u_0=-c_2 gamma` 与 `t=u-u_0`：

\[
\boxed{
t\equiv-1000\gamma T^2\pmod D.
}
\tag{11}

又

\[
\boxed{
v_2(1000T^2)=v_5(1000T^2)=2k+3.}
\tag{12}

因此：

### 2-side

若 `A<=2k+3`，则

\[
\boxed{v_2(t)\ge A.}
\]

若 `A>2k+3`，由于 `gamma` 是 2-adic unit：

\[
\boxed{v_2(t)=2k+3.}
\tag{13}

### 5-side

若 `B<=2k+3`，则

\[
\boxed{v_5(t)\ge B.}
\]

若 `B>2k+3`：

\[
\boxed{v_5(t)=2k+3.}
\tag{14}

---

## 6. excess renormalization

定义 bounded positive rational

\[
\boxed{r_*:=\frac tD.}
\]

由 (6)：

\[
\boxed{196000<r_*<15214000.}
\tag{15}

由 (13)-(14)，`r_*` 的 reduced denominator 精确为

\[
\boxed{
\operatorname{den}(r_*)
=2^{(A-2k-3)_+}
 5^{(B-2k-3)_+}.
}
\tag{16}

所以超过 `2k+3` 的 deep excess 不会消失；它被完整地下沉成新的 bounded rational `r_*` 的 reduced denominator。

moderate 区域

\[
A,B\le2k+3
\]

恰好等价于

\[
\boxed{r_*\in\mathbf Z,}
\]

此时 `r_*=r`，恢复 `deep-moderate-factorization.md`。

---

## 7. extreme-excess 层数已有绝对粗上界

由 decade window

\[
\rho=\frac{h}{TD}\ge\frac T{10}
\]

以及 `h<=Qb_1<1000T^4`，得到

\[
\boxed{D<10000T^2.}
\tag{17}

因此

\[
A<2k\log_2 10+\log_2 10000,
\]

\[
B<2k\log_5 10+\log_5 10000.
\]

特别地，对 `k>=31`：

- `A` 不可能跨过四个完整的 `2k+3` blocks；
- `B` 不可能跨过两个完整的 `2k+3` blocks。

所以 excess renormalization 的层级本身只有绝对有限深度；真正需要继续研究的是如何把 bounded rational `r_*` 的剩余 `2/5` denominator 与 factor pair (10)、unit-square locks 和 complement-height 联立。

---

## 8. 与 moderate three-pattern 的关系

当 `r_*` 为整数时，(10) 变成

\[
ab=Dr,
\]

而 `deep-moderate-three-pattern.md` 已把整个 moderate region 压成 LL/LH/HL 三种显式模板。

因此 double-deep 的当前主线可以分为：

1. **moderate (`r_*` integer)**：已经是 three-pattern finite-width problem；
2. **extreme (`r_*` noninteger)**：其 denominator 正好记录 `A,B` 超过 `2k+3` 的 excess，并且 excess 层数由 (17) 绝对受限。

---

<a id="source-deep-hl-5adic-hensel-lock"></a>

> 整合来源：`deep-hl-5adic-hensel-lock.md`

# A1 minimal diagonal: `HL` exact 5-adic Hensel lock

> 日期：2026-08-20。依赖 `deep-moderate-factorization.md` 与 `deep-double-5high-collapse.md`。当前范围 `k=g>=31`。

moderate double-deep 现只剩 `HL`。本文从 moderate quadratic 中提取一个精确的 5-adic valuation identity；它比仅有的 `B+2nu_5=v_5(r)` 更强，因为它锁定了 gap numerator `gamma` 与 prefix integer `N_0` 的一个 Hensel combination。

状态：**已严格完成。**

---

## 1. HL 参数

记

\[
a_2:=v_2(r),
\qquad
a_5:=v_5(r),
\qquad
\nu:=v_5(N_0).
\]

HL 的 5-low identity 为

\[
\boxed{B+2\nu=a_5.}
\tag{1}
\]

因此

\[
Y:=B+\nu=a_5-\nu\le10,
\]

以及

\[
\boxed{d:=k+1-Y=k+1-B-\nu>0.}
\tag{2}

double-deep 的 reduced gap numerator `gamma` 与 5 互素。

---

## 2. moderate quadratic in `Gamma`

由 `deep-moderate-factorization.md` 的 factor identity，令

\[
\Gamma:=\gamma/D,
\qquad
C_0=w(10w-1),
\]

可写成

\[
\boxed{
1000T^2\Gamma^2
+\bigl(r-10(20w-1)N_0T\bigr)\Gamma
+C_0N_0^2-rTN_0
=0.
}
\tag{3}

移项：

\[
\boxed{
r\Gamma+C_0N_0^2
=10(20w-1)N_0T\Gamma
+rTN_0
-1000T^2\Gamma^2.
}
\tag{4}

---

## 3. 右侧三项的 5-adic valuation

因为 `20w-1` 是 5-adic unit，且

\[
v_5(\Gamma)=-B,
\]

第一项有

\[
v_5\bigl(10(20w-1)N_0T\Gamma\bigr)
=k+1+\nu-B.
\tag{5}

第二项：

\[
v_5(rTN_0)
=a_5+k+\nu
=k+B+3\nu.
\]

与 (5) 的差为

\[
2B+2\nu-1\ge1.
\tag{6}

第三项：

\[
v_5(1000T^2\Gamma^2)
=2k+3-2B.
\]

与 (5) 的差为

\[
k+2-B-\nu=d+1>0.
\tag{7}

所以 (4) 右侧第一项**唯一**取得最小 5-adic valuation。不存在额外 cancellation。

因此

\[
\boxed{
v_5(r\Gamma+C_0N_0^2)=k+1+\nu-B.}
\tag{8}

---

## 4. integer form

乘以

\[
D=2^A5^B
\]

得到整数：

\[
D(r\Gamma+C_0N_0^2)
=r\gamma+C_0DN_0^2.
\]

由 (8)：

\[
\boxed{
v_5(r\gamma+C_0DN_0^2)=k+1+\nu.}
\tag{9}

这已经把一个随 `k` 增长的 exact valuation 直接压到 gap numerator / decimal prefix 的二项组合上。

进一步写

\[
r=5^{a_5}r_5,
\qquad
N_0=5^\nu n,
\qquad
5\nmid r_5n\gamma.
\]

由 (1)：

\[
a_5=B+2\nu.
\]

提出共同因子 `5^(B+2nu)`：

\[
r\gamma+C_0DN_0^2
=5^{B+2\nu}
\left(
 r_5\gamma+C_0 2^A n^2
\right).
\]

结合 (9)：

\[
\boxed{
v_5\left(r_5\gamma+C_0 2^A n^2\right)=d.}
\tag{10}

也就是精确 Hensel congruence

\[
\boxed{
r_5\gamma+C_0 2^A n^2\equiv0\pmod{5^d},}
\tag{11}

但

\[
\boxed{
r_5\gamma+C_0 2^A n^2\not\equiv0\pmod{5^{d+1}}.}
\tag{12}

这里

\[
d=k+1-B-\nu
\]

随 `k` 线性增长。

---

## 5. HL 的参数化版本

HL 还有

\[
A=2k+3-a_2.
\]

因此 (10) 可完全写成有限 `r` 与一个随 `k` 的 5-adic Hensel equation：

\[
\boxed{
v_5\left(
 r_5\gamma
 +C_0\,2^{2k+3-a_2}n^2
\right)
=k+1-a_5+\nu.}
\tag{13}

其中

\[
0\le\nu\le\left\lfloor\frac{a_5-1}{2}\right\rfloor,
\]

所以对固定 `r`，`nu,B,Y` 都来自绝对有限集合。

---

## 6. 当前意义

moderate LL 已由 exact modular exhaustion 全部关闭，所以 (13) 现在直接作用于唯一 surviving moderate branch `HL`。

HL 当前同时满足：

1. finite typewise `r` window；
2. `r_10` / `(alpha,beta)` mod-4 orientation；
3. whole-block partition `alpha*beta=r_10`；
4. adjugate gcd lock `gcd(N_0,gamma)|r_10`；
5. 本文 exact `5^d || (...)` Hensel lock；
6. Q-side strict-2-low orientation / proper-divisor loss。

下一步应把 (13) 与 stripped equations

\[
2\beta\bar s-\alpha\bar q=5^d,
\]

\[
\beta q-5\alpha s=2^{c'}n_0
\]

联立，尝试把 growing Hensel depth `d` 转成有限 periodic / descent obstruction。

---

<a id="source-deep-hl-forced-contact-lift"></a>

> 整合来源：`deep-hl-forced-contact-lift.md`

# A1 minimal diagonal: moderate HL forces a genuine contact Q-side lift

> 日期：2026-08-20。依赖 `deep-hl-one-exponent-divisor-family.md`、`deep-complement-height.md`、`deep-contact-q-resultant-loss.md`。当前 fixed frontier 为 `k>=32`。

`deep-contact-q-resultant-loss.md` 证明 contact square 的 ideal `q^2` lifting 最多损失

\[
g:=\gcd(q,C)<1599T.
\]

本文证明在 moderate HL 中

\[
\boxed{q>1683T>g.}
\]

因此异常 resultant 不可能吞掉整个 Q-side supply：至少有一个 selected Q-primary block 在 contact factor 中发生**严格 exponent amplification**。

状态：**已严格完成。**

---

## 1. complement divisor `v` 的上界

moderate HL 的 stripped complement equation：

\[
2\beta u-\alpha v=5^d>0,
\]

所以

\[
\boxed{\alpha v<2\beta u.}
\tag{1}

乘以 `v`，并用

\[
M=uv:
\]

\[
\alpha v^2<2\beta M.
\]

因此

\[
\boxed{v^2<\frac{2\beta}{\alpha}M.}
\tag{2}

`deep-complement-height.md` 给

\[
\mu:=\frac{MD}{T^2}<10001.
\]

所以

\[
M<10001\frac{T^2}{D}.
\]

代入 (2)：

\[
\boxed{
v<T\sqrt{\frac{20002\beta}{\alpha D}}.}
\tag{3}

---

## 2. 转成 `q=Q/v` 的下界

minimal diagonal

\[
Q=100T^2-(10w-1).
\]

当前 `T>=10^32`，当然有安全界

\[
\boxed{Q>99T^2.}
\tag{4}

因此由 (3)：

\[
\boxed{
q=\frac Qv
>99T\sqrt{\frac{\alpha D}{20002\beta}}.}
\tag{5}

---

## 3. uniform moderate HL 输入

HL 中

\[
A=2k+3-v_2(r).
\]

全部 typewise `r` windows 均有

\[
r<15,214,000,
\]

所以

\[
\boxed{v_2(r)\le23.}
\]

又 double-deep 要求

\[
B\ge1.
\]

故

\[
\boxed{
D=2^A5^B
\ge5\cdot2^{2k+3-23}
=5\cdot2^{2k-20}.}
\tag{6}

同时

\[
\alpha\ge1,
\qquad
\beta\le r_{10}<15,214,000.
\tag{7}

把 (6)-(7) 代入 (5)：

\[
q
>99T
\sqrt{
\frac{5\cdot2^{2k-20}}
{20002\cdot15,214,000}
}.
\tag{8}

右侧除 `T` 外每增加一个 `k` 会额外乘 2。因此最弱层就是当前首个未关闭 fixed layer `k=32`。

直接计算安全常数：

\[
99\sqrt{
\frac{5\cdot2^{44}}
{20002\cdot15,214,000}
}
>1683.
\]

所以

\[
\boxed{q>1683T.}
\tag{9}

---

## 4. resultant exceptional part 不可能覆盖整个 `q`

contact resultant theorem 给

\[
\boxed{g:=\gcd(q,C)<1599T.}
\tag{10}

结合 (9)：

\[
\boxed{q>g.}
\tag{11}

写

\[
q=\prod p^{e_p},
\qquad
g=\prod p^{c_p},
\qquad c_p=\min(e_p,v_p(C)).
\]

若每个 selected block 都有

\[
e_p\le v_p(C),
\]

则 `c_p=e_p` 对全部 p，意味着 `g=q`，与 (11) 矛盾。

因此至少存在一个

\[
\boxed{p^e\Vert q}
\]

满足

\[
\boxed{e>v_p(C).}
\tag{12}

---

## 5. contact factor 中出现严格 exponent amplification

`deep-contact-q-resultant-loss.md` 已证明，对 `p^e||q`，某个 contact factor

\[
L_\pm=Db_1C\pm Z
\]

至少含

\[
p^{2e-\min(e,v_p(C))}.
\]

在 (12) 的 block 上：

\[
\min(e,v_p(C))=v_p(C)<e.
\]

因此

\[
\boxed{
2e-v_p(C)>e,}
\]

且

\[
\boxed{
p^{2e-v_p(C)}\mid L_-
\quad\text{or}\quad
p^{2e-v_p(C)}\mid L_+.}
\tag{13}

所以 moderate HL 中至少一个 Q-side selected prime block一定发生真正的 exponent amplification；不能全部只以原 exponent `e` 穿过 contact square。

---

## 6. 当前意义

moderate HL 的剩余 arithmetic 现在同时满足：

1. finite `r` signatures + one-exponent divisor family；
2. Q-side supply `q` 超线性：`q>1683T`；
3. exceptional contact gcd 仅 `O(T)`；
4. 因而至少一个 Q-primary block必须在 contact factor中被提升到严格大于原 `q` exponent。

下一步应针对这个 forced lifted block研究：

- 与 `q|Q=10^(2k+2)-(10w-1)` 的 p-adic exponent；
- 与 contact factor `L_+-L_-=2Z` 的 gcd；
- 与 complementary divisor `v=Q/q=O(T/sqrt D)` 的小尺度结构。

这已经把 contact square 从“额外必要条件”变成了 moderate HL 中必然出现的具体 prime-power event。

---

<a id="source-deep-hl-hensel-dependency-audit"></a>

> 整合来源：`deep-hl-hensel-dependency-audit.md`

# A1 minimal diagonal: HL Hensel lock dependency audit

> 日期：2026-08-20。依赖 `deep-four-factor-frame.md`、`deep-moderate-adjugate-gcd-lock.md`、`deep-hl-5adic-hensel-lock.md`。当前范围 `k=g>=31`。

本文纠正一个证明架构问题：`deep-hl-5adic-hensel-lock.md` 中的 growing-depth 5-adic valuation identity 虽然公式本身正确，但它**不是**独立于 four-factor frame 的新 obstruction。事实上，完整的整除深度以及“恰好到这一层、不再多一层”都可由 stripped four-factor identities 直接推出。

因此后续不能把该 Hensel lock 与 four-factor frame 当作两层独立筛重复计数。

状态：**依赖关系已严格完成。**

---

## 1. HL 记号

在 moderate HL 中写

\[
r=2^{a_2}5^{a_5}r_{10},
\qquad \alpha\beta=r_{10},
\qquad (r_{10},10)=1.
\]

令

\[
\nu=v_5(N_0),
\qquad \nu_2=v_2(N_0),
\qquad N_0=2^{\nu_2}5^\nu n_0,
\]

其中 `(n_0,10)=1`。HL 给

\[
B+2\nu=a_5,
\qquad
A=2k+3-a_2.
\]

定义

\[
c=k+1-a_2+\nu_2,
\qquad
d=k+1-a_5+\nu.
\]

stripped supply / complement equations 为

\[
\boxed{\beta q-5\alpha s=2^c n_0,}
\tag{1}
\]

\[
\boxed{2\beta u-\alpha v=5^d,}
\tag{2}
\]

其中

\[
h=qs,
\quad su=b_1,
\quad qv=Q.
\]

令

\[
\boxed{C:=2^c n_0.}
\]

adjugate small remainders 给

\[
\boxed{2uC-5^d q=\alpha,}
\tag{3}
\]

\[
\boxed{Cv-5^{d+1}s=\beta.}
\tag{4}

---

## 2. Hensel combination

`deep-hl-5adic-hensel-lock.md` 的组合是

\[
E:=r_5\gamma+C_0 2^A n^2,
\]

其中

\[
r_5=r/5^{a_5}=2^{a_2}\alpha\beta,
\qquad n=N_0/5^\nu=2^{\nu_2}n_0,
\qquad C_0=w(10w-1).
\]

由 `A=2k+3-a_2` 与 `c=k+1-a_2+nu_2`：

\[
\boxed{2^A n^2=2^{a_2+1}C^2.}
\tag{5}

因此

\[
\boxed{
\frac{E}{2^{a_2}}
=\alpha\beta\gamma+2C_0C^2.}
\tag{6}

---

## 3. 用 four-factor frame 展开

在 double-deep 中

\[
\gamma=DTN_0-h.
\]

另一方面

\[
Qb_1=huv
=1000T^4+c_2T^2+C_0,
\qquad c_2=10(1-20w),
\]

故

\[
C_0=huv-1000T^4-c_2T^2.
\]

代入 (6)：

\[
\begin{aligned}
\frac{E}{2^{a_2}}
={}&\alpha\beta DTN_0
+h(2uvC^2-\alpha\beta)\\
&-2(1000T^4+c_2T^2)C^2.
\end{aligned}
\tag{7}

而 (3)-(4) 直接给

\[
2uC=\alpha+5^dq,
\qquad
Cv=\beta+5^{d+1}s.
\]

于是

\[
\begin{aligned}
2uvC^2
&=(\alpha+5^dq)(\beta+5^{d+1}s)\\
&=\alpha\beta
+5^d\bigl(\beta q+5\alpha s+5^{d+1}h\bigr).
\end{aligned}
\tag{8}

把 (8) 放回 (7)：

\[
\boxed{
\begin{aligned}
\frac{E}{2^{a_2}}
={}&\alpha\beta DTN_0\\
&+h5^d(\beta q+5\alpha s+5^{d+1}h)\\
&-2(1000T^4+c_2T^2)C^2.
\end{aligned}}
\tag{9}

---

## 4. exact valuation 自动出现

记

\[
Y:=B+\nu\ge1.
\]

由

\[
d=k+1-B-\nu,
\]

第一项在除以 `5^d` 后仍至少含

\[
5^{2Y-1},
\]

所以模 5 消失。

最后一项含 `T^2`，而 `d<=k`，除以 `5^d` 后同样仍被 5 整除。

因此 (9) 除以 `5^d` 并降模 5，只剩中间项：

\[
\boxed{
\frac{E}{2^{a_2}5^d}
\equiv h\,\beta q
=\beta q^2s
\pmod5.}
\tag{10}

`q,s,beta` 都是 5-adic units，所以右侧非零。于是

\[
\boxed{v_5(E)=d.}
\tag{11}

即

\[
\boxed{
v_5\left(
 r_5\gamma+C_0 2^{2k+3-a_2}n^2
\right)
=k+1-a_5+\nu.}
\tag{12}

这正是旧 Hensel lock 的完整结论，包括“不再多整除一个 5”。

---

## 5. 结论

所以 (12) 不是 four-factor frame 之外的新约束，而是

\[
\boxed{
\text{four-factor + decimal }Qb_1\text{ identity}
\Longrightarrow
\text{HL exact Hensel lock}.}
\]

后续 HL 证明中：

- 可以使用 (12) 作为方便的压缩坐标；
- 但不能把它与 (1)-(4) 当成统计独立的第二层 obstruction；
- 纯 5-adic contact-square lifting 也不会提供额外深度：对 5-adic unit，是否为平方完全由 mod-5 Legendre class 决定。

因此 HL 的下一真正独立输入必须来自**原 rational-contact square 的全局结构**、prime-source 结构或新的实/整除约束，而不是重复 Hensel lifting。

---

<a id="source-deep-hl-local-signature-count"></a>

> 整合来源：`deep-hl-local-signature-count.md`

# A1 minimal diagonal: moderate HL local-signature reduction

> 日期：2026-08-20。依赖 `deep-contact-sign-window.md`、`deep-double-2high-master.md`、`deep-2high-mod8-lock.md`、`deep-2high-mod5-lock.md` 与 `deep-moderate-block-partition.md`。

本文不宣称关闭 HL；目标是把后续 one-exponent divisor families 的 finite coefficient set 精确量化。只使用已经证明互相独立/安全的 local necessary conditions。

状态：**finite signature reduction 已严格审计。**

---

## 1. 输入 `r` windows

使用 contact-sign sharpened windows：

\[
\begin{array}{c|c}
(z,w)&r\\ \hline
(1,1)&973440\le r\le10885221\\
(1,2)&734410\le r\le8400003\\
(1,3)&529000\le r\le6236387\\
(1,4)&357210\le r\le4394372\\
(3,1)&519840\le r\le15204352\\
(3,2)&428490\le r\le13677244.
\end{array}
\]

HL 是 double-deep，所以

\[
v_5(r)=a_5\ge1.
\]

这些 windows 中全部 `5|r` 的整数合计

\[
\boxed{11,051,041}.
\]

---

## 2. finite local cells

对每个

\[
r=2^{a_2}5^{a_5}r_{10}
\]

枚举有限

\[
0\le\nu_5\le\lfloor(a_5-1)/2\rfloor,
\]

并令

\[
B=a_5-2\nu_5.
\]

只保留满足以下必要条件的 cell：

1. master parity `eta=-a_2` 与 prefix 2-adic branch兼容；
2. `deep-2high-mod8-lock.md`：
   \[
   r_{10}\equiv-5^{B+1}QN_2\pmod8;
   \]
3. `deep-2high-mod5-lock.md`：
   \[
   \left(\frac{wr_{10}N_5}{5}\right)=(-1)^A;
   \]
4. odd `w=1,3` 时，存在真正的 whole-block partition
   \[
   \alpha\beta=r_{10},\quad
   \alpha\equiv\beta\equiv3\pmod4.
   \]
   这等价于 `r_10` 至少含两个 residue `3 mod4` 的 prime-power blocks；
5. even `w` 时旧 orientation `alpha=1` 已提供一个安全 partition witness，所以这里只需前述 local locks。

prefix local compatibility 通过 `N_0 mod 16*5^6` 完整枚举。由于当前 `a_5<=10`，所以 `nu_5<=4`；`5^6` 足以精确分辨全部 `v_5(N_0)` cells。若 prefix norm `N` 在模 `5^6` 上仍为 0，则对其下一 5-adic unit class保留两种 Legendre 可能，故这是安全上集，不会误删真实 candidate。

---

## 3. 精确计数

最终 surviving `r` counts：

\[
\boxed{
\begin{array}{c|r}
(z,w)&\text{locally compatible }r\\ \hline
(1,1)&579692\\
(1,2)&383278\\
(1,3)&328609\\
(1,4)&201854\\
(3,1)&863426\\
(3,2)&662434
\end{array}}
\]

总计

\[
\boxed{3,019,293}.
\]

所以 local-independent filters 已把初始 `5|r` coefficient set

\[
11,051,041
\]

压缩约 72.7%。

---

## 4. 与 one-exponent family 的接口

每个 surviving finite signature 再选择允许的 `nu_5,B` 与 whole-block `(alpha,beta)`，随后 `deep-hl-one-exponent-divisor-family.md` 把全部 unbounded dependence 压到

\[
d=k+1-(B+\nu_5),
\]

以及

\[
2\beta u-\alpha v=5^d,
\]

\[
u\mid10^{2d+2Y-1}-w,
\qquad
v\mid10^{2d+2Y}-(10w-1).
\]

因此后续 proof search 不应再扫描 arbitrary `(r,k,A,B)`；应直接从这 3,019,293 个 finite `r` signatures 进入 single-exponent divisor analysis。

---

<a id="source-deep-hl-mod4-orientation"></a>

> 整合来源：`deep-hl-mod4-orientation.md`

# A1 minimal diagonal: `HL` mod-4 orientation filter

> 日期：2026-08-20。依赖 `deep-moderate-block-partition.md`、`deep-moderate-adjugate-gcd-lock.md` 与 `deep-gap-unit-square.md`。当前范围 `k=g>=31`。

虽然 `HL` 在 factor-pair 分类中叫 2-high / 5-low，但它的 denominator excess

\[
A=2k+3-v_2(r)
\]

对原 rational-contact square 来说显然处于 strict 2-adic low-side。因此 strict-2-low 的 Q-side orientation 必须继续使用。

本文把该 orientation 与 `HL` stripped equations 联立，得到 `alpha,beta,r_10` 的固定 mod-4 类。

状态：**已严格完成。**

---

## 1. `HL` 的两条 stripped equations

沿用

\[
r_{10}=\alpha\beta,
\qquad \gcd(\alpha,\beta)=1,
\]

以及

\[
u\mid b_1,
\quad v\mid Q,
\quad h=qs.
\]

`HL` 有

\[
\boxed{2\beta u-\alpha v=5^d,}
\tag{1}

以及

\[
\boxed{\beta q-5\alpha s=2^{c'}n_0,}
\tag{2}

其中 `c'>=1`，当前实际上 `c'` 随 `k` 很大。

whole-block selector 给

\[
\boxed{s\equiv1\pmod4.}
\tag{3}

---

## 2. strict-2-low Q-side orientation

因为 `A~2k`，必有

\[
A>1+v_2(N)-2v_2(w),
\]

所以 `deep-gap-unit-square.md` 的 strict-2-low orientation 对全部 HL 状态有效：

\[
\boxed{
q\equiv
\begin{cases}
1\pmod4,&w=1,3,\\
3\pmod4,&w=2,4.
\end{cases}}
\tag{4}

同时

\[
Q\equiv
\begin{cases}
3\pmod4,&w=1,3,\\
1\pmod4,&w=2,4.
\end{cases}
\]

---

## 3. `alpha mod 4`

由 (1)，因为 `5^d≡1 mod4`：

### odd `w`

此时 `u` 为奇数，所以

\[
2\beta u\equiv2\pmod4.
\]

因此

\[
\alpha v\equiv1\pmod4.
\]

又 `qv=Q`、`q≡1`、`Q≡3 mod4`，所以

\[
v\equiv3\pmod4.
\]

故

\[
\boxed{\alpha\equiv3\pmod4\qquad(w=1,3).}
\tag{5}

### even `w`

此时 `u` 为偶数，所以

\[
2\beta u\equiv0\pmod4.
\]

(1) 给

\[
\alpha v\equiv3\pmod4.
\]

而 `q≡3`、`Q≡1 mod4`，所以

\[
v\equiv3\pmod4.
\]

因此

\[
\boxed{\alpha\equiv1\pmod4\qquad(w=2,4).}
\tag{6}

所以四类型统一还有

\[
\boxed{v\equiv3\pmod4.}
\tag{7}

---

## 4. `beta mod 4`

当前 `c'` 至少为 `k+1-v_2(r)>=9`，所以 (2) 右侧被 4 整除。结合 `s≡1 mod4`：

\[
\beta q\equiv\alpha\pmod4.
\]

- odd `w`：`q≡1`、`alpha≡3`；
- even `w`：`q≡3`、`alpha≡1`。

两种情况都给

\[
\boxed{\beta\equiv3\pmod4.}
\tag{8}

---

## 5. `r_10` residue

由 `r_10=alpha*beta`：

\[
\boxed{
r_{10}\equiv1\pmod4\qquad(w=1,3),}
\tag{9}

\[
\boxed{
r_{10}\equiv3\pmod4\qquad(w=2,4).}
\tag{10}

这和 LL strict-2-low 的 residue 条件比较：

\[
LL:\quad
r_{10}\equiv
\begin{cases}
1,&w=1,2,4,\\
3,&w=3,
\end{cases}\pmod4.
\]

因此对 `w=2,3,4`，LL 与 HL 要求的 `r_10 mod4` 正好相反。

所以固定 `(w,r)` 后：

\[
\boxed{
w=2,3,4\Longrightarrow\text{strict LL 与 HL 至多存活一个 branch}.}
\tag{11}

`w=1` 两者都要求 `r_10≡1 mod4`，仍需后续条件区分。

---

## 6. 当前用途

moderate double-deep 已只剩 `LL`、`HL`。本文使 HL 的 whole-block partition 进一步带 orientation：

- `beta` 必须是 `3 mod4`；
- `alpha` 的 mod-4 类由 `w` 决定；
- `r_10` 的 residue 先于任何大整数 factorization 就能筛 branch。

后续对有限 `r` 做 modular / block-partition exhaustion 时应先应用 (9)-(11)。

---

<a id="source-deep-hl-one-exponent-divisor-family"></a>

> 整合来源：`deep-hl-one-exponent-divisor-family.md`

# A1 minimal diagonal: moderate HL as one-exponent divisor families

> 日期：2026-08-20。依赖 `deep-double-2high-master.md`、`deep-typewise-r-window.md`、`deep-moderate-block-partition.md`。本文只研究 master branch 的 moderate part `eta<=0`，即原 HL。

本文把 moderate HL 的 unbounded dependence 从 `k` 改写成一个单独指数 `d`。所有其余离散数据来自绝对有限集合。

状态：**归约严格完成；一指数 divisor family 尚待关闭。**

---

## 1. finite HL data

moderate HL 有有限整数

\[
r\in[r_{\min}(z,w),r_{\max}(z,w)],
\]

并记

\[
a_2=v_2(r),
\qquad a_5=v_5(r),
\qquad r_{10}=r/(2^{a_2}5^{a_5}).
\]

5-low identity：

\[
\boxed{B+2\nu_5=a_5.}
\tag{1}

所以 `nu_5` 只可取

\[
0\le\nu_5\le\left\lfloor\frac{a_5-1}{2}\right\rfloor,
\]

并且

\[
\boxed{B=a_5-2\nu_5,}
\qquad
\boxed{Y:=B+\nu_5=a_5-\nu_5.}
\tag{2}

因此对固定 `r,nu_5`，`B,Y` 都是绝对常数。

另外

\[
\alpha\beta=r_{10},
\qquad\gcd(\alpha,\beta)=1,
\]

且每个 `p^e||r_10` block 必须整个分给 `alpha` 或 `beta`。所以 `(alpha,beta)` 也是 finite whole-block partition。

---

## 2. 以 `d` 取代 `k`

HL 定义

\[
\boxed{d:=k+1-Y>0.}
\tag{3}

因为 `Y` 已固定：

\[
\boxed{k=d+Y-1.}
\tag{4}

所以所有十进制母体都变成 `d` 的显式 exponential polynomial。

---

## 3. complementary divisor 母体

minimal diagonal：

\[
b_1=10^{2k+1}-w,
\qquad
Q=10^{2k+2}-(10w-1).
\]

代入 (4)：

\[
\boxed{
b_1(d)=10^{2d+2Y-1}-w,}
\tag{5}

\[
\boxed{Q(d)=10^{2d+2Y}-(10w-1).}
\tag{6}

写 complementary divisors

\[
u=b_1/s,
\qquad v=Q/q.
\]

于是

\[
\boxed{u\mid b_1(d),
\qquad v\mid Q(d).}
\tag{7}

并且 `u` 不是任意 divisor：由于 `s` 只能使用 `b_1` 的 `1 mod4` whole prime-power blocks，`u` 必须包含

1. `b_1` 的全部 2-power；
2. `b_1` 的全部 `p=3 mod4` prime-power blocks；
3. 未被 `s` 选择的其余 `1 mod4` whole blocks。

---

## 4. one-exponent linear divisor equation

master stripped complement equation在 HL 中为

\[
\boxed{2\beta u-\alpha v=5^d.}
\tag{8}

结合 (5)-(7)，任何 moderate HL candidate 必须给出

\[
\boxed{
\begin{aligned}
&u\mid10^{2d+2Y-1}-w,\\
&v\mid10^{2d+2Y}-(10w-1),\\
&2\beta u-\alpha v=5^d,
\end{aligned}}
\tag{9}

其中

\[
(w,Y,\alpha,\beta)
\]

来自绝对有限集合。

所以原先的 unbounded variables

\[
(k,N_0,\gamma,A,B,q,s,u,v)
\]

在这条**必要条件**中已经只剩：

\[
\boxed{
\text{一个指数 }d
+\text{两个 complementary divisors }u,v.}
\]

---

## 5. 固定系数解格

因为 `gcd(alpha,2beta)=1`，任选一组 Bezout 解

\[
2\beta U_0-\alpha V_0=1.
\]

则 (8) 的全部整数解为

\[
\boxed{
u=5^dU_0+\alpha m,}
\]

\[
\boxed{v=5^dV_0+2\beta m,}
\tag{10}

其中 `m in Z`。

因此每个 fixed `(w,Y,alpha,beta)` family 还可以改写成单参数 lattice line (10) 与两个 exponential-divisor 条件 (7) 的交。

这给后续两条明确入口：

- 使用 `10^(2d+c)-const` 的 primitive/cyclotomic blocks；
- 对最小正解 `(u,v)` 尝试 Vieta / divisor descent。

---

## 6. 当前额外 finite filters

真正进入 (9) 前还应先应用已证明的：

- typewise contact-sign `r` window；
- `eta=-a_2` 的 2-adic parity；
- `r_10 mod8` master lock；
- `mod5` Legendre lock；
- `alpha,beta` whole-block partition；
- Q-side `q mod4` orientation / proper-divisor loss。

所以 (9) 是一个安全上层必要 family；实际 admissible finite parameter list 比“所有 r、所有 block partitions”更小。

---

<a id="source-deep-hl-q-superlinear"></a>

> 整合来源：`deep-hl-q-superlinear.md`

# A1 minimal diagonal: sharp superlinear Q-side supply in moderate HL

> 日期：2026-08-20。强化 `deep-hl-forced-contact-lift.md`。

旧 uniform proof 分别粗取 `D` 最小与 `beta` 最大，只得到 `q>1683T`。本文保留 HL 中 `D,beta,r` 的相关性，使 `v_2(r)` 精确消掉，得到：

\[
\boxed{q>1.09\times10^7 T\qquad(k\ge32).}
\]

因此 contact exceptional resultant 只占 `q` 的不到约 `1/6800`，而该比例随 k 指数改善。

状态：**已严格完成。**

---

## 1. 从 complement equation 到 q 下界

沿用

\[
2\beta u-\alpha v=5^d>0,
\qquad M=uv,
\]

所以

\[
v^2<\frac{2\beta}{\alpha}M.
\]

又

\[
M<10001\frac{T^2}{D}.
\]

因此

\[
v<T\sqrt{\frac{20002\beta}{\alpha D}}.
\]

而

\[
Q>99T^2,
\qquad q=Q/v,
\]

故

\[
\boxed{
\frac qT
>99\sqrt{\frac{\alpha D}{20002\beta}}.}
\tag{1}

---

## 2. 保留 `alpha beta=r_10`

因为

\[
\alpha\beta=r_{10},
\]

有

\[
\frac{\alpha D}{\beta}
=\frac{D\alpha^2}{r_{10}}
\ge\frac D{r_{10}}.
\tag{2}

HL 中记

\[
a_2=v_2(r),
\qquad a_5=v_5(r).
\]

则

\[
D=2^{2k+3-a_2}5^B,
\]

\[
r=2^{a_2}5^{a_5}r_{10}.
\]

所以出现关键 cancellation：

\[
\boxed{
\frac D{r_{10}}
=
\frac{2^{2k+3}5^{B+a_5}}r.}
\tag{3}

`a_2` 完全消失。

---

## 3. uniform finite-window lower bound

HL 为 double-deep，所以

\[
B\ge1,
\qquad a_5\ge1.
\]

因此

\[
5^{B+a_5}\ge25.
\]

contact-sign typewise windows 给全局

\[
r\le15,204,352.
\]

故 (3)：

\[
\boxed{
\frac D{r_{10}}
\ge
\frac{25\cdot2^{2k+3}}{15,204,352}.}
\tag{4}

结合 (1)-(2)：

\[
\boxed{
\frac qT
>
99\sqrt{
\frac{25\cdot2^{2k+3}}
{20002\cdot15,204,352}
}.}
\tag{5}

右侧每增加一个 k 精确乘 2。因此最弱是 `k=32`。

直接取安全十进制：

\[
99\sqrt{
\frac{25\cdot2^{67}}
{20002\cdot15,204,352}
}
>10,900,000.
\]

所以

\[
\boxed{q>10,900,000\,T.}
\tag{6}

---

## 4. 与 contact resultant 的比例

`deep-contact-q-resultant-loss.md`：

\[
g:=\gcd(q,C)<1599T.
\]

所以当前首层已满足

\[
\boxed{
\frac qg
>
\frac{10,900,000}{1599}
>6800.}
\tag{7}

并且 (5) 说明 k 每增加 1，右侧至少再乘 2：

\[
\boxed{
\frac qg>6800\cdot2^{k-32}.}
\tag{8}

因此 contact block theorem 中相对于 ideal `q^2` lifting 的 total loss `g` 极小；guaranteed extra amplification product `q/g` 从 k=32 起就至少是四位数，并指数增长。

---

## 5. complementary divisor 同时极小

由 `qv=Q<101T^2` 与 (6)：

\[
\boxed{
v<\frac{101}{10,900,000}T<10^{-5}T.}
\tag{9}

所以 moderate HL 的 Q-side 已呈现强烈的不对称：

\[
\boxed{q>10^7T,
\qquad v<10^{-5}T.}
\]

后续 one-exponent divisor analysis 应利用这个尺度，而不再把 `q,v` 当作两个可同尺度变化的 arbitrary divisors of Q。

---

<a id="source-deep-hl-tiny-complements"></a>

> 整合来源：`deep-hl-tiny-complements.md`

# A1 minimal diagonal: tiny complementary divisors in moderate HL

> 日期：2026-08-20。依赖 `deep-hl-q-superlinear.md` 与 complement-height identity。

本文证明 moderate HL 中两个 complementary divisors 都远小于 decimal center `T=10^k`：

\[
\boxed{u<5\cdot10^{-6}T,}
\qquad
\boxed{v<10^{-5}T.}
\]

相应 selected supply factors `s,q` 都远大于 T。

状态：**已严格完成。**

---

## 1. `v` 已由 sharp q bound 控制

`deep-hl-q-superlinear.md` 给

\[
q>10,900,000T.
\]

而

\[
Q<101T^2.
\]

所以

\[
\boxed{
v=Q/q<\frac{101}{10,900,000}T<10^{-5}T.}
\tag{1}

---

## 2. `5^d` 相对 `sqrt M` 很小

moderate HL 中

\[
M=uv,
\qquad
1000<\mu:=MD/T^2<10001.
\]

记

\[
a_2=v_2(r),
\qquad a_5=v_5(r),
\qquad d=k+1-(B+\nu_5).
\]

直接计算：

\[
\frac{T^2}{D5^{2d}}
=2^{a_2-3}5^{a_5-2}.
\]

因为

\[
a_2\ge0,
\qquad a_5\ge1,
\]

故

\[
2^{a_2-3}5^{a_5-2}\ge\frac1{40}.
\]

于是

\[
\boxed{
\frac M{5^{2d}}
=\mu\frac{T^2}{D5^{2d}}
>25.}
\tag{2}

所以

\[
\boxed{5^d<\frac{\sqrt M}{5}.}
\tag{3}

---

## 3. 用 complement quadratic 控制 `u`

stripped complement equation

\[
2\beta u-\alpha v=5^d
\]

结合 `uv=M`，把 `v=M/u` 代入：

\[
2\beta u^2-5^d u-\alpha M=0.
\]

正根：

\[
\boxed{
u=
\frac{5^d+\sqrt{5^{2d}+8\alpha\beta M}}
{4\beta}.}
\tag{4}

因为

\[
\alpha\beta=r_{10},
\]

由 (2)-(3)：

\[
5^d+\sqrt{5^{2d}+8r_{10}M}
<\sqrt M\left(\frac15+\sqrt{\frac1{25}+8r_{10}}\right).
\]

对 `r_10>=1` 可用安全界

\[
\frac15+\sqrt{\frac1{25}+8r_{10}}
<3.04\sqrt{r_{10}}.
\]

所以

\[
\boxed{
\frac uT
<0.76\sqrt{\frac{10001r_{10}}D}.}
\tag{5}

---

## 4. 再次利用 `D/r_10` cancellation

`deep-hl-q-superlinear.md` 已证明

\[
\frac D{r_{10}}
=\frac{2^{2k+3}5^{B+a_5}}r
\ge
\frac{25\cdot2^{2k+3}}{15,204,352}.
\]

所以

\[
\frac{r_{10}}D
\le
\frac{15,204,352}{25\cdot2^{2k+3}}.
\]

代入 (5)，最弱层 `k=32`：

\[
\frac uT
<0.76\sqrt{
\frac{10001\cdot15,204,352}
{25\cdot2^{67}}
}
<4.9\cdot10^{-6}.
\]

故取整洁安全界

\[
\boxed{u<5\cdot10^{-6}T.}
\tag{6}

以后 k 每增加 1，该相对界至少再缩小一半。

---

## 5. selected factors 反向巨大

因为

\[
b_1=10T^2-w>9T^2,
\]

由 `su=b1` 与 (6)：

\[
\boxed{
s>1.8\cdot10^6T.}
\tag{7}

而 q 已有

\[
\boxed{q>10.9\cdot10^6T.}
\tag{8}

所以 moderate HL 的 four-factor frame 呈现强烈尺度分离：

\[
\boxed{
\max(u,v)<10^{-5}T
\ll T
\ll\min(s,q).}
\tag{9}

---

## 6. 当前意义

one-exponent family

\[
2\beta u-\alpha v=5^d
\]

现在只发生在两个 `o(T)` complementary divisors 之间，而它们的母体 `b_1,Q` 都是 `Theta(T^2)`。

后续应优先利用：

- small-divisor structure of `10^(2d+c)-const`；
- primitive/cyclotomic blocks forced into the large selected factors `s,q`；
- contact Q-side lifted block now living inside a selected factor `q>>T` while its complement `v<<T`。

---

<a id="source-deep-ll-modular-exhaustion"></a>

> 整合来源：`deep-ll-modular-exhaustion.md`

# A1 minimal diagonal: complete moderate-`LL` modular exhaustion

> 日期：2026-08-20。依赖 `deep-ll-pell-normal-form.md`、`deep-typewise-r-window.md`、`deep-moderate-block-partition.md` 与原 rational-contact square。当前范围 `k=g>=31`。

本文关闭 moderate double-deep 的整个 `LL` branch：

\[
\boxed{\forall k\ge31,\quad \text{moderate LL is empty for all six prefix types}.}
\]

结合 `deep-double-5high-collapse.md`，moderate double-deep 从此只剩 `HL`。

状态：**已严格完成；附统一 C++ exact certificate。**

---

## 1. finite LL families

`deep-ll-pell-normal-form.md` 已证明 LL 中

\[
D=2^A5^B\mid r,
\qquad
R=r/D\in\mathbf Z_{>0},
\]

并把全部 `k`-依赖压进

\[
L=10^k/D.
\]

固定 `(z,w,r,D,gamma)` 后必须满足

\[
C_0N_0^2-uLN_0+1000\gamma^2L^2+\gamma R=0,
\]

其中

\[
C_0=w(10w-1),
\qquad
u=10\gamma(20w-1)+Dr.
\]

判别式为固定 generalized Pell family

\[
Y^2=A L^2+B,
\]

且 `B` 的完整 `Q_2/Q_5` squareclass 把 `gamma` 限入两个 `mod 40` classes。

`deep-typewise-r-window.md` 则给六类型绝对有限 `r` intervals。于是 LL 是一个绝对有限 fixed-family union。

---

## 2. 2-adic / block filters

写

\[
r_{10}=r/2^{v_2(r)}5^{v_5(r)}.
\]

对 even `w=2,4`：

\[
A>0\Longrightarrow A\text{ odd},
\]

且所有 LL 都在 original-contact strict 2-low，所以

\[
r_{10}\equiv1\pmod4.
\]

对 odd `w=1,3`，证书保留全部 resonance 小层：

- 若 `nu_2=0`：`A=1` resonance；strict-low 仅 `A>=3` odd；
- 若 `nu_2>0`：`A=1` high、`A=2` resonance；strict-low 仅 `A>=4` even。

只在 strict-low 子区使用：

\[
r_{10}\equiv1\pmod4\quad(w=1),
\]

\[
r_{10}\equiv3\pmod4\quad(w=3).
\]

所以没有把 odd-`w` resonance candidates 偷删掉。

---

## 3. odd-prime modular necessary condition

固定奇素数 `p!=2,5`。给定 fixed LL tuple 后，`10^k mod p` 只依赖

\[
k\bmod\operatorname{ord}_p(10).
\]

对每个这样的 residue，LL supply quadratic 关于 `N_0 mod p` 至多有两个根（退化线性情形单独精确处理）。每个根还必须通过原 rational-contact square modulo `p`。

因此每个 `p` 给出一个 exact allowed set

\[
S_p(z,w,r,D,\gamma)
\subseteq\mathbf Z/\operatorname{ord}_p(10)\mathbf Z.
\]

任何 exact candidate 的 `k` 必须同时属于所有选定 `S_p`。

---

## 4. common period 420

统一使用

\[
\boxed{
\mathcal P_0=
\{3,7,11,13,29,31,37,41,43,61,71,101,127\}.}
\]

这些素数都满足

\[
\operatorname{ord}_p(10)\mid420.
\]

所以每个 family 先被压成 `k mod 420` bitmask。

随后使用

\[
\boxed{
\mathcal P_1=
\{17,19,73,89,113,137,251,337,1009,4201\}.}
\]

先做 individual CRT incompatibility pruning，再把所有 order 与 `420` 联合提升到完整周期

\[
\boxed{277200.}
\]

最后在 `k mod277200` 上使用

\[
\boxed{
\mathcal P_2=
\{67,151,181,199,211,239,241,271,281,421,631,661,1933,2161,2689\},}
\]

这些素数的阶均整除 `277200`。

其中：

- `p=661`, `ord=220` 用于清除 `(1,1)` 中唯一额外顽固 residue family；
- `p=199`, `ord=99` 用于清除 `(3,1)` 中唯一额外顽固 residue family。

---

## 5. 六类型 exact statistics

完整证书统计如下：

\[
\begin{array}{c|r|r|r|r|r|r}
(z,w)&\text{local}&P_0\text{ families}&k\bmod420\text{ states}&P_1\text{ survivors}&k\bmod277200\text{ families}&\text{final}\\ \hline
(1,1)&57,278,520&593,553&1,016,555&93,222&6,980&0\\
(1,2)&19,206,685&93,027&155,388&13,674&916&0\\
(1,3)&25,308,717&162,735&258,880&20,743&1,530&0\\
(1,4)&4,331,873&18,342&28,788&2,271&154&0\\
(3,1)&306,099,009&3,156,352&5,421,691&500,727&37,426&0\\
(3,2)&110,439,962&575,335&974,681&86,545&6,020&0
\end{array}
\tag{1}
\]

合计 local-compatible fixed families：

\[
\boxed{522,664,766.}
\]

最终 surviving periodic states：

\[
\boxed0.
\]

大类型 `(1,1),(3,1),(3,2)` 可按 `r` 区间分块运行；每块都独立使用相同的 all-`k` modular conditions，所以分块只是执行方式，不改变证明集合。

---

## 6. 两个唯一 residual families

在原 `P_2` cover 下，只有两个 family 曾留下单一极薄周期状态。

### `(1,1)`

\[
(r,D,\gamma)=(981640,10,299),
\]

只剩

\[
k\equiv251999,277199\pmod{277200}.
\]

`p=661`、`ord=220` 对这两类都没有共同 supply/contact root，因此删除。

### `(3,1)`

\[
(r,D,\gamma)=(5570560,1280,42167),
\]

只剩

\[
k\equiv249637\pmod{277200}.
\]

`p=199`、`ord=99` 下，该类对应 `k≡58 mod99`，而 supply quadratic 与 contact square 没有共同 `N_0 mod199` 根，因此删除。

所以 final `0` 不是搜索截断，而是完整有限周期不相容。

---

## 7. 结论

六类型均无 periodic state，所以

\[
\boxed{
\forall k\ge31,\quad
\text{moderate double-deep LL is impossible}.}
\tag{2}
\]

此前：

- `deep-double-5high-collapse.md` 已关闭 moderate `LH`；
- `deep-balanced-collapse.md` 已关闭 high-high / balanced；
- transition strips 已关闭。

因此 moderate double-deep 现在只剩

\[
\boxed{HL.}
\tag{3}
\]

而 extreme 中 5-extreme 已关闭，只剩 2-extreme `E_2`。故完整 double-deep 已缩成

\[
\boxed{
\text{double-deep}=HL_{\rm moderate}\cup E_2.
}
\tag{4}
\]

两支都是 **2-high / 5-low**；从此 double-deep 不再含任何 2-low surviving branch。

---

## 8. 可复核证书

统一脚本：

`../../../../../scripts/exact-lift/a1-only/research-checks/deep-denominator/check_a1_deep_ll_modular_exhaustion.cpp`

调用方式：

```bash
g++ -O3 -std=c++17 check_a1_deep_ll_modular_exhaustion.cpp -o /tmp/a1-ll
/tmp/a1-ll 1 4
```

也可分块：

```bash
/tmp/a1-ll 3 1 384160 1500000
```

全区间运行会断言表 (1) 的 exact counts；分块运行则断言该块 final survivor count 为 `0`。

---

<a id="source-deep-ll-pell-normal-form"></a>

> 整合来源：`deep-ll-pell-normal-form.md`

# A1 minimal diagonal: moderate `LL` fixed Pell normal form

> 日期：2026-08-20。依赖 `deep-moderate-factorization.md`、`deep-double-5high-collapse.md`、`deep-typewise-r-window.md`。当前范围 `k=g>=31`。

本文证明 moderate double-deep 的 `LL` 分支已经和 central sector 一样，归约成**绝对有限个固定系数 generalized Pell families**。

核心点：LL 中 `D|r`，而 `r` 有绝对 typewise 上界，所以 `D,gamma,r` 都与 `k` 无关且绝对有限。全部 `k`-依赖只剩

\[
L=T/D.
\]

状态：**归约与 local squareclass 严格完成；剩余 nonsquare families 的 finite modular exhaustion 待做。**

---

## 1. LL 中 `D|r`

LL 有

\[
v_2(r)=A+2\nu_2+e,
\qquad
v_5(r)=B+2\nu_5,
\]

其中

\[
e=v_2(w).
\]

因此

\[
\boxed{D=2^A5^B\mid r.}
\tag{1}
\]

定义

\[
\boxed{R:=r/D\in\mathbf Z_{>0}.}
\tag{2}
\]

又由 `deep-typewise-r-window.md`：

\[
r<15,204,353.
\]

所以

\[
\boxed{D<15,204,353.}
\tag{3}
\]

由于

\[
15.09<\Gamma_k=\gamma/D<39.003,
\]

得到

\[
\boxed{0<\gamma<39.003D<6\times10^8.}
\tag{4}
\]

因此 `(D,gamma,r)` 全部属于绝对有限整数集合。

---

## 2. 从 moderate quadratic 除去 `D^2`

`deep-moderate-factorization.md` 的 quadratic 为

\[
C_0D^2N_0^2
-DuTN_0
+1000\gamma^2T^2
+\gamma Dr
=0,
\tag{5}
\]

其中

\[
C_0=w(10w-1),
\qquad
\boxed{u=10\gamma(20w-1)+Dr.}
\tag{6}
\]

LL 中 `D|T`，因为 `A<=23,B<=10` 而 `k>=31`。令

\[
\boxed{L:=T/D\in\mathbf Z.}
\tag{7}
\]

把 (5) 除以 `D^2`，并使用 `R=r/D`：

\[
\boxed{
C_0N_0^2-uLN_0+1000\gamma^2L^2+\gamma R=0.
}
\tag{8}
\]

所有系数 `C_0,u,gamma,R` 都与 `k` 无关；唯一的 unbounded variable ray 是

\[
L=10^k/D.
\]

---

## 3. fixed generalized Pell family

把 (8) 看成关于 `N_0` 的二次方程。判别式必须是整数平方：

\[
\boxed{
Y^2=A_{\gamma,r,D}L^2+B_{\gamma,r,D},
}
\tag{9}
\]

其中

\[
\boxed{
A_{\gamma,r,D}:=u^2-4000C_0\gamma^2,
}
\tag{10}
\]

\[
\boxed{
B_{\gamma,r,D}:=-4C_0\gamma R<0.
}
\tag{11}

定义 natural point

\[
u_0:=10\gamma(20w-1).
\]

已有恒等式

\[
u_0^2-4000C_0\gamma^2=100\gamma^2.
\]

而 `u=u_0+Dr>u_0`，所以

\[
\boxed{A_{\gamma,r,D}>100\gamma^2>0.}
\tag{12}
\]

故每个 fixed parameter tuple 都是一条正主系数、负固定 norm 的 generalized Pell family。

---

## 4. square-`A` 退化族统一无解

若

\[
A_{\gamma,r,D}=S^2,
\]

则 (9) 为

\[
Y^2=(SL)^2-|B|.
\]

由 (12)：

\[
S>10\gamma>150D.
\]

于是

\[
SL>150D\frac TD=150T\ge1.5\times10^{33}.
\]

另一方面由 (3)-(4)、`C_0<=156`、`R=r/D<15,204,353` 可取极粗安全界

\[
|B|<6\times10^{18}.
\]

所以

\[
0<|B|<2SL-1.
\]

从而

\[
(SL-1)^2<(SL)^2-|B|<(SL)^2,
\]

矛盾。因此

\[
\boxed{
A_{\gamma,r,D}\text{ square}
\Longrightarrow
\text{LL family empty}.}
\tag{13}
\]

后续只需处理 nonsquare `A`。

---

## 5. `B` 必须是完整 2/5-adic squareclass

写

\[
R=2^{2\nu_2+e}5^{2\nu_5}r_{10},
\qquad
r_{10}=r/2^{v_2(r)}5^{v_5(r)}.
\]

又写

\[
w=2^e w_0,
\qquad w_0\text{ odd}.
\]

因为 double-deep 中 `gamma` 与 10 互素，(11) 给

\[
v_2(B)=2+2e+2\nu_2,
\qquad
v_5(B)=2\nu_5.
\]

由 `v_2(r)<=23,v_5(r)<=10` 和 `k>=31`，这两个固定赋值都严格小于 `2v_2(L),2v_5(L)`。所以 (9) 模任意深 `2/5` 次幂强迫

\[
\boxed{B\in\mathbf Q_2^{\times2}\cap\mathbf Q_5^{\times2}.}
\tag{14}
\]

提出全部偶次 prime powers 后，两个单位条件统一落到

\[
\boxed{
-\gamma w_0(10w-1)r_{10}\equiv1\pmod8,
}
\tag{15}
\]

以及

\[
\boxed{
\left(\frac{-\gamma w_0(10w-1)r_{10}}5\right)=1.
}
\tag{16}
\]

所以对固定 `(w,r,D,nu_2,nu_5)`：

- `gamma mod 8` 唯一；
- `gamma mod 5` 只有两个 quadratic-character classes；
- CRT 后 `gamma` 只落在两个 `mod 40` residue classes。

这正是 central modular exhaustion 之前使用过的同型 local-squareclass funnel。

---

## 6. 当前 LL 核心

moderate LL 现在可按绝对有限参数

\[
\boxed{(z,w,r,\nu_2,\nu_5,D,\gamma)}
\]

组织，其中：

1. `r` 在 `deep-typewise-r-window.md` 的 typewise finite interval；
2. `D|r` 且 `D=2^A5^B`，`A,B>0`；
3. `gamma` 在 `15.09D..39.003D` 的 typewise 更窄 interval；
4. `gamma` 只允许 (15)-(16) 的两个 `mod40` classes；
5. square-`A` families 已全部删除；
6. nonsquare family 只需检查
   \[
   Y^2=A L^2+B,
   \qquad L=10^k/D.
   \]

因此 LL 已经不再是 unbounded coefficient problem。下一步可沿 central 的经验，对这些 fixed nonsquare families 做 period-prime modular cover；不需要 factor `b_1,Q`。

---

<a id="source-deep-ll-w4-modular-exhaustion"></a>

> 整合来源：`deep-ll-w4-modular-exhaustion.md`

# A1 minimal diagonal: `(z,w)=(1,4)` moderate-LL modular exhaustion

> 日期：2026-08-20。依赖 `deep-ll-pell-normal-form.md`、`deep-typewise-r-window.md`、`deep-moderate-block-partition.md` 与原 rational-contact square。当前范围 `k=g>=31`。

本文关闭第一个完整 moderate-LL prefix type：

\[
\boxed{(z,w)=(1,4),\quad \text{moderate LL is empty for all }k\ge31.}
\]

方法与 central modular exhaustion 同型：不求 Pell 基本解，而是把 fixed LL supply quadratic 与原 contact square 在有限素数模下联立，再用 `10^k mod p` 的有限周期做 exact cover。

状态：**已严格完成；附 C++ exact certificate。**

---

## 1. 完整 finite LL parameter set

`deep-typewise-r-window.md` 给 `(1,4)`：

\[
\boxed{216090\le r\le4394372.}
\]

LL valuation identities 为

\[
v_2(r)=A+2\nu_2+2,
\qquad
v_5(r)=B+2\nu_5,
\]

其中 `A,B>0`。因为 `w=4`，deep 2-adic parity theorem 强迫

\[
\boxed{A\text{ odd}.}
\]

本类型所有 `A>0` 都是原 contact 的 strict 2-low，因此 `deep-moderate-block-partition.md` 还给

\[
\boxed{r_{10}\equiv1\pmod4.}
\]

固定 `(r,nu_2,nu_5)` 后

\[
D=2^A5^B
\]

固定，并且 `deep-ll-pell-normal-form.md` 给 typewise gap interval

\[
15.0949872D<\gamma<21.00225945D.
\]

`B` 的完整 `Q_2/Q_5` squareclass 进一步把 `gamma` 限在两个 `mod 40` classes。

对所有这些必要条件做 exact integer enumeration，共得到

\[
\boxed{4,331,873}
\tag{1}
\]

个 local-compatible fixed LL Pell families。

注意此集合故意仍包含 square-`A_{gamma,r,D}` 的退化 families，所以它是实际剩余核心的安全超集。

---

## 2. odd-prime modular condition

LL fixed quadratic 为

\[
C_0N_0^2-uLN_0+1000\gamma^2L^2+\gamma R=0,
\]

其中

\[
C_0=156,
\quad R=r/D,
\quad u=790\gamma+Dr,
\quad L=10^k/D.
\]

对奇素数 `p!=2,5`，给定

\[
(r\bmod p,D\bmod p,\gamma\bmod p,k\bmod\operatorname{ord}_p(10)),
\]

该式关于 `N_0 mod p` 是一个普通二次方程，因此至多需要检查两个根。

每个根还必须通过原 rational-contact square：写

\[
\rho=N_0-\frac{\gamma}{D10^k},
\]

则

\[
K-2\rho(10^kQ)\mathcal N
\]

必须是 `mod p` 的平方剩余。

因此每个 `p` 精确给出允许的 `k` residue set。

---

## 3. common period-420 stage

取

\[
\boxed{
\mathcal P_0=
\{3,7,11,13,29,31,37,41,43,61,71,101,127\}.}
\]

这些素数均满足

\[
\operatorname{ord}_p(10)\mid420.
\]

把 (1) 的每个 family 的允许 classes 拉回 `k mod 420` 后求交，得到：

\[
\boxed{
4,331,873\longrightarrow18,342\text{ families},
}
\tag{2}
\]

总 surviving `k mod420` states 为

\[
\boxed{28,788.}
\tag{3}
\]

---

## 4. supplemental individual CRT pruning

再使用

\[
\boxed{
\mathcal P_1=
\{17,19,73,89,113,137,251,337,1009,4201\}.}
\]

对每个 family，若其 `k mod420` mask 与某个 `p` 的允许 `k mod ord_p(10)` classes 在

\[
\gcd(420,\operatorname{ord}_p(10))
\]

上已经不兼容，则立即删除。

这一安全 pruning 把 (2) 压到

\[
\boxed{2,271}
\tag{4}
\]

个 families。

---

## 5. exact joint period `277200`

`P_1` 中所有乘法阶与 `420` 的最小公倍数恰为

\[
\boxed{277200.}
\]

所以对 (4) 的每个 family，可把 surviving `k mod420` mask 精确提升到

\[
k\bmod277200
\]

并同时与全部 `P_1` residue sets 求交。

完整联合交集后只剩

\[
\boxed{154}
\tag{5}
\]

个 families 具有任何周期状态。

---

## 6. final order-dividing cover

最后加入

\[
\boxed{
\mathcal P_2=
\{67,151,181,211,239,241,271,281,421,631,1933,2161,2689\}.}
\]

这些素数的 `ord_p(10)` 都整除 `277200`，因此无需再扩周期：直接在现有 `k mod277200` states 上逐素数相交即可。

结果：

\[
\boxed{154\longrightarrow0.}
\tag{6}
\]

没有任何 residue state 存活。

---

## 7. 结论

所有步骤只使用：

- exact typewise finite `r` window；
- LL valuation identities；
- strict-2-low parity / `r_10 mod4`；
- exact local `gamma mod40` squareclasses；
- fixed LL supply quadratic；
- 原 rational-contact square；
- finite multiplicative orders 与 CRT。

没有截断 `k`，也没有 factor `b_1,Q`。

因此：

\[
\boxed{
\forall k\ge31,
\quad
(z,w)=(1,4)\text{ moderate LL is impossible}.}
\tag{7}
\]

结合 `deep-double-5high-collapse.md`：`(1,4)` moderate double-deep 从此只可能位于 `HL`；`LL` 与已关闭的 `LH` 都已消失。

---

## 8. 可复核证书

脚本：

`../../../../../scripts/exact-lift/a1-only/research-checks/deep-denominator/check_a1_deep_ll_w4_modular_exhaustion.cpp`

最终断言统计：

```text
local=4331873
common_families=18342
common_k420_states=28788
after_individual_supplement=2271
joint_k277200_families=154
final=0
CERTIFICATE OK
```

---

<a id="source-deep-moderate-adjugate-gcd-lock"></a>

> 整合来源：`deep-moderate-adjugate-gcd-lock.md`

# A1 minimal diagonal: moderate adjugate small remainders and gcd lock

> 日期：2026-08-20。依赖 `deep-moderate-factor-quotients.md`、`deep-four-factor-frame.md`、`deep-moderate-block-partition.md` 与 `deep-double-5high-collapse.md`。当前范围 `k=g>=31`。

moderate double-deep 现只剩 `LL` 与 `HL`。本文把 supply / complement 两条线性式同时 strip 掉已知的 2/5 powers。对应的 `2x2` determinant 恰为 `r_10`，所以取 adjugate 后得到右端只有 `alpha,beta` 的小余数式。

最终统一得到

\[
\boxed{
\gcd(N_0,h)=\gcd(N_0,\gamma)\mid r_{10}.
}
\]

因此 prefix integer `N_0` 与 normalized-gap numerator `gamma` 的 gcd 被绝对小参数 `r_10<15,214,000` 控制。

状态：**已严格完成。**

---

## 1. 公共记号

写

\[
N_0=2^{\nu_2}5^{\nu_5}n_0,
\qquad\gcd(n_0,10)=1,
\]

\[
r_{10}=r/2^{v_2(r)}5^{v_5(r)},
\qquad
\alpha\beta=r_{10},
\qquad
\gcd(\alpha,\beta)=1.
\]

完整 supply / complement 为

\[
h=qs,
\qquad qv=Q,
\qquad su=b_1,
\]

所以

\[
\boxed{qv-10su=1.}
\tag{1}
\]

另外 `gcd(Q,b_1)=1` 给

\[
\gcd(q,u)=\gcd(s,v)=1.
\tag{2}

---

## 2. `HL` 的两条 stripped equations

HL 中令

\[
Y:=B+\nu_5,
\qquad d:=k+1-Y>0.
\]

`deep-moderate-factor-quotients.md` 给

\[
a=2^{k+1}5^Y\alpha,
\qquad
b=2^{k+2}5^Y\beta.
\]

从 complementary relation

\[
bu-av=10T
\]

除去 `2^(k+1)5^Y`：

\[
\boxed{
2\beta u-\alpha v=5^d.
}
\tag{3}

另一方面 supply relation

\[
qb-10sa=DN_0
\]

给

\[
2^{k+2}5^Y(\beta q-5\alpha s)
=2^{A+\nu_2}5^Y n_0.
\]

因为 HL 有

\[
A=2k+3-v_2(r),
\]

定义

\[
\boxed{
c':=A+\nu_2-k-2
=k+1-v_2(r)+\nu_2>0,}
\]

得到

\[
\boxed{
\beta q-5\alpha s=2^{c'}n_0.
}
\tag{4}

---

## 3. `HL` 的 adjugate small remainders

把

\[
X:=\beta q,
\quad Y_1:=5\alpha s,
\quad U:=2\beta u,
\quad V:=\alpha v.
\]

则 (3)-(4) 是

\[
X-Y_1=2^{c'}n_0,
\qquad
U-V=5^d.
\]

而由 (1)：

\[
XV-Y_1U
=\alpha\beta(qv-10su)
=r_{10}.
\tag{5}

因此

\[
(X-Y_1)V-(U-V)Y_1=r_{10},
\]

除以 `alpha`：

\[
\boxed{
2^{c'}n_0v-5^{d+1}s=\beta.
}
\tag{6}

同理

\[
(X-Y_1)U-(U-V)X=r_{10},
\]

除以 `beta`：

\[
\boxed{
2^{c'+1}n_0u-5^dq=\alpha.
}
\tag{7}

---

## 4. `LL` 的 adjugate small remainders

LL 中写

\[
u=2^e u_0,
\qquad e=v_2(w),
\]

并定义

\[
c=k+1-(A+\nu_2+e)>0,
\qquad
d=k+1-(B+\nu_5)>0.
\]

strip complementary relation 得

\[
\boxed{
\beta u_0-\alpha v=2^c5^d.
}
\tag{8}

strip supply relation 得

\[
\boxed{
\beta q-2^{e+1}5\alpha s=n_0.
}
\tag{9}

这里使用

\[
q b-10sa=DN_0
\]

以及 LL 的

\[
a=2^{A+\nu_2+e}5^{B+\nu_5}\alpha,
\quad
b=2^{A+\nu_2}5^{B+\nu_5}\beta.
\]

注意由 `u=2^e u_0`，(1) 等价于

\[
qv-2^{e+1}5su_0=1.
\tag{10}

和 HL 完全同样的 determinant 计算给

\[
\boxed{
n_0v-2^{c+e+1}5^{d+1}s=\beta,}
\tag{11}

\[
\boxed{
n_0u_0-2^c5^dq=\alpha.}
\tag{12}

---

## 5. gcd lock

从 HL 的 (7)：若 `p|n_0` 且 `p|q`，则 `p|alpha`。因此

\[
\gcd(n_0,q)\mid\alpha.
\]

从 (6)：

\[
\gcd(n_0,s)\mid\beta.
\]

LL 的 (11)-(12) 给出完全相同的结论。

而 `q|Q`、`s|b_1`、`gcd(Q,b_1)=1`，故 `q,s` 互素。因此

\[
\gcd(n_0,qs)
=\gcd(n_0,q)\gcd(n_0,s)
\mid\alpha\beta=r_{10}.
\]

由于 `h=qs` 与 10 互素：

\[
\boxed{
\gcd(N_0,h)=\gcd(n_0,h)\mid r_{10}.
}
\tag{13}

在 double-deep 中

\[
h=DTN_0-\gamma,
\]

所以

\[
\gcd(N_0,h)=\gcd(N_0,\gamma).
\]

最终：

\[
\boxed{
\gcd(N_0,\gamma)\mid r_{10}.
}
\tag{14}

又

\[
196000<r<15214000,
\]

故

\[
\boxed{
\gcd(N_0,\gamma)<15,214,000.
}
\tag{15}

---

## 6. 当前用途

moderate `LL/HL` 现在除了 `r`、block-partition `(alpha,beta)` 外，还满足 gap numerator 与 decimal prefix 的 absolute gcd lock (14)。

这可直接加入：

- `deep-moderate-root-normal-form.md` 的 reduced-denominator 恢复；
- `deep-complement-height.md` 的 rational denominator cancellation；
- 后续对 `N_0` / `gamma` 的 resultant 或 primitive-divisor 分析。

尤其不能再允许 `gcd(N_0,gamma)` 随 `k` 自由增长。

---

<a id="source-deep-moderate-block-partition"></a>

> 整合来源：`deep-moderate-block-partition.md`

# A1 minimal diagonal: moderate `r_10` block partition

> 日期：2026-08-20。依赖 `deep-moderate-factor-quotients.md`、`deep-four-factor-frame.md` 与 strict-2-low Q-side orientation。当前范围 `k=g>=31`。

本文记录 moderate branches 中一个离散化：把

\[
r_{10}:=r/2^{v_2(r)}5^{v_5(r)}
\]

写成 `alpha*beta` 时，`alpha,beta` 必须互素。因此 `r_10` 的每个 prime-power block 必须整个分配到一边，不能拆指数。

另外在 LL 的 strict 2-low 子区，Q-side orientation 继续给出一个 `r_10 mod 4` 过滤。

状态：**已严格完成。**

---

## 1. moderate factor quotients

`deep-moderate-factor-quotients.md` 给出

\[
\boxed{\alpha\beta=r_{10}},
\qquad
\gcd(\alpha\beta,10)=1.
\]

### LL

写

\[
u=2^e u_0,
\qquad e=v_2(w),
\qquad \gcd(u_0,10)=1.
\]

归一化 complementary relation

\[
bu-av=10T
\]

得到

\[
\boxed{
\beta u_0-\alpha v=2^c5^d,
}
\tag{1}

其中

\[
c=k+1-(A+\nu_2+e)>0,
\qquad
d=k+1-(B+\nu_5)>0.
\]

### HL

同理 high-2 / low-5 模板给

\[
\boxed{
2\beta u-\alpha v=5^d,
}
\tag{2}

其中

\[
d=k+1-(B+\nu_5)>0.
\]

（已关闭的 LH 也有完全对称的 pure-2 equation，但不再需要保留为剩余核心。）

---

## 2. `alpha,beta` 必须互素

因为

\[
u\mid b_1,
\qquad v\mid Q,
\qquad \gcd(b_1,Q)=1,
\]

有

\[
\gcd(u_0,v)=1.
\]

看 LL 的 (1)。左右两项 `beta*u_0` 与 `alpha*v` 都是奇数。若有奇素数 `p` 同时整除二者，则 `p` 必整除右侧 `2^c5^d`，所以 `p=5`。但 `alpha,beta,u_0,v` 全与 5 互素，矛盾。

因此

\[
\boxed{
\gcd(\beta u_0,\alpha v)=1.
}
\tag{3}

特别地

\[
\boxed{\gcd(\alpha,\beta)=1.}
\tag{4}

HL 的 (2) 同理：任何公共奇素数必须整除 `5^d`，但两项均与 5 互素，所以仍有 (4)。

于是若

\[
r_{10}=\prod p_i^{e_i},
\]

则每个完整 prime-power block `p_i^{e_i}` 必须整个进入 `alpha` 或整个进入 `beta`：

\[
\boxed{
\alpha=\prod_{i\in I}p_i^{e_i},
\qquad
\beta=\prod_{i\notin I}p_i^{e_i}.
}
\tag{5}

所以每个固定 `r` 最多只有

\[
\boxed{2^{\omega(r_{10})}}
\]

个 `(alpha,beta)` 分支，而不是普通 divisor count `tau(r_10)`。

---

## 3. LL 的 `u_0 mod 4`

whole-block selector `s` 只由 `1 mod 4` prime-power blocks 构成，所以

\[
\boxed{s\equiv1\pmod4.}
\]

而

\[
b_1=10^{2k+1}-w.
\]

去掉固定的 `2^e` 后：

\[
\boxed{
u_0\equiv-w_0\pmod4,}
\tag{6}

其中

\[
w=2^e w_0,
\qquad w_0\text{ odd}.
\]

因此：

\[
u_0\equiv
\begin{cases}
3\pmod4,&w=1,2,4,\\
1\pmod4,&w=3.
\end{cases}
\tag{7}

---

## 4. LL strict-2-low 的 `r_10 mod 4` filter

当前 `k>=31`，而 LL 有 `A<=23`，所以 (1) 右侧含至少 `2^2`；降模 4：

\[
\beta u_0\equiv\alpha v\pmod4.
\]

由于 odd units 模 4 中逆元等于自身，且 `alpha*beta=r_10`：

\[
\boxed{v\equiv r_{10}u_0\pmod4.}
\tag{8}

又

\[
qv=Q,
\]

而 strict 2-low 的 unit-square theorem 给

\[
q\equiv
\begin{cases}
1\pmod4,&w\text{ odd},\\
3\pmod4,&w\text{ even}.
\end{cases}
\tag{9}

直接代入 `Q mod 4` 与 (7)-(9)，得到

\[
\boxed{
r_{10}\equiv1\pmod4\qquad(w=1,2,4),}
\tag{10}
\]

\[
\boxed{
r_{10}\equiv3\pmod4\qquad(w=3).}
\tag{11}

这里 (10)-(11) 只在 LL 同时处于原 contact 的 strict 2-low 时使用；odd-`w` 的 2-adic resonance 小层仍单独保留。

---

## 5. 当前用途

moderate double-deep 已经只剩 `LL`、`HL`，且统一 `B<=10`。本文进一步把有限参数 `r` 的 quotient allocation 收紧成 whole-block partition。

后续 exhaustive modular work 应直接按

\[
(w,r,I)
\]

而不是 `(w,r,alpha,beta)` 的任意 divisor split 组织；LL strict-2-low 还可以先应用 (10)-(11) 删除错误的 `r_10 mod 4` 类。

---

<a id="source-deep-moderate-factor-quotients"></a>

> 整合来源：`deep-moderate-factor-quotients.md`

# A1 minimal diagonal: moderate factor quotient refinement

> 日期：2026-08-20。依赖 `deep-moderate-three-pattern.md` 与 `deep-four-factor-frame.md`。当前范围 `k=g>=31`。

`deep-moderate-three-pattern.md` 已证明 moderate double-deep 只有 LL/LH/HL 三种模板。本文把 factor pair

\[
X_1=sa,
\qquad
X_2=qb,
\qquad
ab=Dr
\]

中的全部 `2,5` 次幂精确剥离。

写

\[
a_2:=v_2(r),
\qquad
a_5:=v_5(r),
\]

\[
\boxed{
r_{10}:=\frac{r}{2^{a_2}5^{a_5}},
\qquad\gcd(r_{10},10)=1.}
\]

则三种模板中都存在正整数 `alpha,beta` 满足

\[
\boxed{\alpha\beta=r_{10}.}
\]

所以 strip 掉显式 `2/5` 幂后，未知 quotient 只来自一个绝对有限 divisor pair。

状态：**已严格完成。**

---

## 1. LL

LL 满足

\[
a_2=A+2\nu_2+e,
\qquad
a_5=B+2\nu_5,
\]

其中

\[
e=v_2(w),
\qquad
\nu_p=v_p(N_0).
\]

两个 factor 的精确 valuation 为

\[
v_2(X_1)=A+\nu_2+e,
\qquad
v_2(X_2)=A+\nu_2,
\]

\[
v_5(X_1)=v_5(X_2)=B+\nu_5.
\]

因为 `q,s` 与 10 互素，这也是 `a,b` 的 valuation。因此存在 `alpha,beta` 与 10 互素，使

\[
\boxed{
a=
2^{A+\nu_2+e}
5^{B+\nu_5}\alpha,}
\tag{1}

\[
\boxed{
b=
2^{A+\nu_2}
5^{B+\nu_5}\beta.}
\tag{2}

把 (1)-(2) 相乘，并使用 LL 两个 valuation identity，得到

\[
\boxed{\alpha\beta=r_{10}.}
\tag{3}

---

## 2. LH

LH 为 2-low / 5-high：

\[
a_2=A+2\nu_2+e,
\]

\[
B=2k+3-a_5.
\]

2-adic valuation 仍为 low branch：

\[
v_2(a)=A+\nu_2+e,
\qquad
v_2(b)=A+\nu_2.
\]

5-adic high branch 则精确为

\[
v_5(a)=k+1,
\qquad
v_5(b)=k+2.
\]

所以

\[
\boxed{
a=
2^{A+\nu_2+e}
5^{k+1}\alpha,}
\tag{4}

\[
\boxed{
b=
2^{A+\nu_2}
5^{k+2}\beta,}
\tag{5}

并且仍然

\[
\boxed{\alpha\beta=r_{10}.}
\tag{6}

此前只知道 strip 掉 `5^{k+1},5^{k+2}` 后乘积为 `2^A r_5`；(4)-(6) 把 2-adic low branch 也同时剥净，故剩余 quotient 真正只来自 `r_{10}`。

---

## 3. HL

完全对称。HL 为 2-high / 5-low：

\[
A=2k+3-a_2,
\]

\[
a_5=B+2\nu_5.
\]

2-adic high branch：

\[
v_2(a)=k+1,
\qquad
v_2(b)=k+2.
\]

5-adic low branch：

\[
v_5(a)=v_5(b)=B+\nu_5.
\]

因此

\[
\boxed{
a=
2^{k+1}
5^{B+\nu_5}\alpha,}
\tag{7}

\[
\boxed{
b=
2^{k+2}
5^{B+\nu_5}\beta,}
\tag{8}

\[
\boxed{\alpha\beta=r_{10}.}
\tag{9}

---

## 4. 与 four-factor frame 联立

`deep-four-factor-frame.md` 还给出

\[
qb-10sa=DN_0,
\tag{10}

\[
\bar s b-\bar q a=10T
\tag{11}

（double-deep 中 `lambda=1`）。

因此在 LL/LH/HL 任一模板中，代入本文的 `(a,b)` 后：

- `alpha,beta` 只需遍历 `r_{10}` 的 divisor pairs；
- `A,B` 要么绝对小，要么由 `k,a_2,a_5` 线性确定；
- `nu_2,nu_5` 在 low side 被 `a_2,a_5` 限制在绝对有限集合；
- Q-side / `b_1`-side divisors 同时受到 (10)-(11)。

因此 moderate double-deep 的剩余离散参数已经可取为

\[
\boxed{
(w,r,\alpha,\beta,\nu_2,\nu_5,\text{LL/LH/HL})
}
\]

加上 `k`；不再需要独立扫描 `(A,B,a,b)`。

下一步可把 (10)-(11) 对每种模板除去已知的巨大 `2/5` 幂，得到适合 periodic modular exhaustion 的线性同余系统。

---

<a id="source-deep-moderate-factorization"></a>

> 整合来源：`deep-moderate-factorization.md`

# A1 minimal diagonal: moderate double-deep factorization

> 日期：2026-08-20。依赖 `deep-balanced-collapse.md` 与 minimal-diagonal odd-prime supply。
> 当前统一范围 `k=g>=31`。

本文研究 double-deep

\[
\Gamma_k=\frac{\gamma}{D},
\qquad
D=2^A5^B,
\qquad A,B>0,
\qquad \gcd(\gamma,10)=1,
\]

中的 moderate 区域

\[
\boxed{A\le2k+3,\qquad B\le2k+3.}
\tag{1}
\]

核心结论是：这一看似二维的区域实际上只能落在两个绝对有限宽的边带中：

\[
\boxed{
A\le23
\quad\text{或}\quad
B\le10.
}
\tag{2}
\]

关键工具是一套 deep Euclidean descent，它把 supply divisibility 化成一个精确二因子分解。

状态：**已严格完成。**

---

## 1. deep Euclidean descent

记

\[
T=10^k,
\qquad
L:=DT,
\qquad
h:=DTN_0-\gamma=N_0L-\gamma.
\]

因为 double-deep 时 `lambda=1`，odd-prime supply 给

\[
h\mid P:=Qb_1.
\]

又 `gcd(h,D)=1`，所以

\[
h\mid D^4P.
\]

而

\[
\boxed{
D^4P
=1000L^4+c_2D^2L^2+C_0D^4,
}
\tag{3}
\]

其中

\[
c_2=10(1-20w),
\qquad
C_0=w(10w-1).
\]

对商 `(D^4P)/h` 按 `L` 做与 central sector 相同的两级 Euclidean division。由于

\[
\gcd(\gamma,L)=1,
\]

两个余数同余可以完全消去，得到某个整数 `U`，满足

\[
\boxed{
C_0D^4N_0^2
-U L N_0
+1000\gamma^2L^2
+\gamma U
+c_2D^2\gamma^2
=0.
}
\tag{4}
\]

这是 deep 版本的 supply quadratic。

---

## 2. `D^2 | U`

把 (4) 模 `D`。除 `gamma U` 外其余项都被 `D` 整除，因此

\[
\gamma U\equiv0\pmod D.
\]

由于 `gcd(gamma,D)=1`：

\[
D\mid U.
\]

写 `U=DU_1`，再把 (4) 模 `D^2`。此时除 `D gamma U_1` 外所有项都被 `D^2` 整除，所以

\[
D\gamma U_1\equiv0\pmod{D^2}.
\]

再次利用 `gcd(gamma,D)=1`：

\[
D\mid U_1.
\]

因此

\[
\boxed{D^2\mid U.}
\tag{5}
\]

写

\[
\boxed{U=D^2u,\qquad u\in\mathbf Z.}
\tag{6}
\]

将 (4) 除以 `D^2`，并使用 `L=DT`：

\[
\boxed{
C_0D^2N_0^2
-DuTN_0
+1000\gamma^2T^2
+\gamma u
+c_2\gamma^2
=0.
}
\tag{7}
\]

---

## 3. deep Pell normal form

把 (7) 看成关于 `N_0` 的二次方程。判别式除去显然平方因子 `D^2` 后，必须有整数 `y` 满足

\[
\boxed{
y^2=A_uT^2+B_u,}
\tag{8}
\]

其中

\[
\boxed{A_u=u^2-4000C_0\gamma^2,}
\]

\[
\boxed{B_u=-4C_0\gamma u-4C_0c_2\gamma^2.}
\]

定义天然平方点

\[
\boxed{u_0:=10\gamma(20w-1),}
\qquad
\boxed{v_0:=10\gamma.}
\]

因为

\[
u_0^2-v_0^2=4000C_0\gamma^2,
\]

并且 `c_2=-10(20w-1)`，所以

\[
\boxed{
A_u=u^2-(u_0^2-v_0^2),
}
\tag{9}
\]

\[
\boxed{
B_u=-4C_0\gamma(u-u_0).
}
\tag{10}

这与 central Pell normal form 具有完全相同的平方点结构，但参数 `gamma,D` 仍在变化。

---

## 4. `u-u0` 的 deep congruence

把 (7) 模 `D`。前两项消失，得到

\[
1000\gamma^2T^2+\gamma u+c_2\gamma^2\equiv0\pmod D.
\]

除以模 `D` 可逆的 `gamma`：

\[
u+c_2\gamma
\equiv-1000\gamma T^2\pmod D.
\]

而

\[
u_0=-c_2\gamma.
\]

因此

\[
\boxed{
 u-u_0
 \equiv-1000\gamma T^2
 \pmod D.
}
\tag{11}

当前

\[
v_2(1000T^2)=v_5(1000T^2)=2k+3.
\]

所以在 moderate 条件 (1) 下：

\[
\boxed{D\mid u-u_0.}
\tag{12}

写

\[
\boxed{u-u_0=Dr,\qquad r\in\mathbf Z.}
\tag{13}

---

## 5. `r` 是绝对有限正整数

从 (4) 直接解 `U`，再除以 `D^3`，令

\[
s:=N_0/T,
\qquad
\Gamma:=\gamma/D,
\]

得到精确式

\[
\boxed{
\frac uD
=
\frac{
C_0N_0^2+1000\Gamma^2T^2+c_2\Gamma^2
}{TN_0-\Gamma}.
}
\tag{14}

这里

\[
0.1<s\le1,
\qquad
15.09<\Gamma<39.003.
\]

当前 `T>=10^31`。用 `C_0>=0`、`c_2>=-790` 和上述窗口，可取安全界

\[
\boxed{
227000<\frac uD<15214000.
}
\tag{15}

另一方面

\[
0<\frac{u_0}{D}
=10\Gamma(20w-1)
<30813.
\]

故 (13) 给出

\[
\boxed{
196000<r<15214000.
}
\tag{16}

特别地

\[
\boxed{r>0,}
\]

且

\[
\boxed{v_2(r)\le23,}
\qquad
\boxed{v_5(r)\le10.}
\tag{17}

---

## 6. quadratic 精确因式分解

把

\[
u=u_0+Dr
\]

代回 (7)。注意

\[
\gamma u_0+c_2\gamma^2=0.
\]

剩余前三个主项具有判别式 `100`，并且恒等式

\[
\begin{aligned}
& C_0(DN_0)^2
-10(20w-1)(DN_0)(\gamma T)
+1000(\gamma T)^2\\
&\qquad=
(wDN_0-10\gamma T)
((10w-1)DN_0-100\gamma T).
\end{aligned}
\]

因此 (7) 精确化成

\[
\boxed{
(wDN_0-10\gamma T)
((10w-1)DN_0-100\gamma T)
=Dr(DTN_0-\gamma).
}
\tag{18}

因为

\[
10\Gamma-ws>150.9-4>0,
\]

\[
100\Gamma-(10w-1)s>1509-39>0,
\]

两个左侧括号都为负。定义正整数

\[
\boxed{X_1:=10\gamma T-wDN_0,}
\]

\[
\boxed{X_2:=100\gamma T-(10w-1)DN_0.}
\]

则

\[
\boxed{X_1X_2=Drh.}
\tag{19}

---

## 7. prime supply 自动把两个因子分流

完整 odd-prime supply 写成

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\qquad \gcd(q,s)=1.
\]

### `s` 进入 `X1`

模 `s` 有

\[
DTN_0\equiv\gamma.
\]

因为 `T` 对 `s` 可逆：

\[
TX_1
\equiv
10\gamma T^2-w\gamma
=\gamma(10T^2-w)
=\gamma b_1
\equiv0\pmod s.
\]

所以

\[
\boxed{s\mid X_1.}
\tag{20}

### `q` 进入 `X2`

同理：

\[
TX_2
\equiv
100\gamma T^2-(10w-1)\gamma
=\gamma Q
\equiv0\pmod q.
\]

故

\[
\boxed{q\mid X_2.}
\tag{21}

于是存在正整数 `a,b` 使

\[
\boxed{X_1=sa,}
\qquad
\boxed{X_2=qb.}
\tag{22}

由 (19)、`h=qs`：

\[
\boxed{ab=Dr.}
\tag{23}

这就是 moderate double-deep 的精确 factor-pair normal form。

---

## 8. 5-adic valuation dichotomy

记

\[
\nu_5=v_5(N_0),
\qquad
Y:=B+\nu_5.
\]

由于 `q,s` 与 `10` 互素，由 (22)-(23)：

\[
v_5(X_1)+v_5(X_2)=B+v_5(r).
\tag{24}

在 `X_1` 中两项赋值为

\[
k+1,\qquad Y;
\]

在 `X_2` 中为

\[
k+2,\qquad Y.
\]

### low branch: `Y<k+1`

两处都由 `DN_0` 项严格承担低赋值：

\[
2Y=B+v_5(r).
\]

所以

\[
\boxed{
B+2\nu_5=v_5(r)\le10.
}
\tag{25}

特别地

\[
\boxed{B\le10.}
\tag{26}

### high branch: `Y>k+2`

两处都由 `gamma*T` 项承担低赋值：

\[
2k+3=B+v_5(r),
\]

即

\[
\boxed{B=2k+3-v_5(r).}
\tag{27}

### transition strip

只剩

\[
\boxed{Y\in\{k+1,k+2\},}
\tag{28}

其中可能发生额外 cancellation，需要单独保留。

---

## 9. 2-adic valuation dichotomy

记

\[
\nu_2=v_2(N_0),
\qquad
X:=A+\nu_2,
\qquad
e=v_2(w).
\]

`X_1` 两项赋值为

\[
k+1,\qquad X+e,
\]

`X_2` 两项赋值为

\[
k+2,\qquad X.
\]

由 (22)-(23)：

\[
v_2(X_1)+v_2(X_2)=A+v_2(r).
\tag{29}

### low branch: `X+e<k+1`

两处 `DN_0` 项严格主导：

\[
(X+e)+X=A+v_2(r).
\]

所以

\[
\boxed{
A+2\nu_2+e=v_2(r)\le23.
}
\tag{30}

特别地

\[
\boxed{A\le23.}
\tag{31}

### high branch: `X>k+2`

两处 `gamma*T` 项严格主导：

\[
2k+3=A+v_2(r),
\]

因此

\[
\boxed{A=2k+3-v_2(r).}
\tag{32}

### transition strip

其余状态全落入宽度至多 `4` 的带：

\[
\boxed{
k+1-e\le A+\nu_2\le k+2.}
\tag{33}

---

## 10. fully-balanced collapse 把 moderate region 压成两条有限宽边带

`deep-balanced-collapse.md` 已证明：double-deep candidate 必须满足

\[
A+e+\nu_2<k
\quad\text{或}\quad
B+\nu_5<k.
\tag{34}

若第一条成立，则当然

\[
A+\nu_2+e<k<k+1,
\]

所以必在 2-adic low branch；由 (31)：

\[
A\le23.
\]

若第二条成立，则

\[
B+\nu_5<k<k+1,
\]

所以必在 5-adic low branch；由 (26)：

\[
B\le10.
\]

因此无论哪一条 shallow side 出现，都得到

\[
\boxed{
A\le23
\quad\text{或}\quad
B\le10.
}
\]

这证明了主结论 (2)。

---

## 11. 当前 double-deep 剩余几何

moderate double-deep 已从二维无界区域压成：

1. `A=1,...,23` 的有限宽 vertical strips；或
2. `B=1,...,10` 的有限宽 horizontal strips。

同时还保留更细的 valuation dichotomy：另一侧要么也绝对小，要么位于 `k+O(1)` transition strip，要么被精确锁到

\[
A=2k+3-v_2(r)
\quad\text{或}\quad
B=2k+3-v_5(r),
\]

其中 `r` 属于绝对有限区间 (16)。

因此 moderate double-deep 已不再需要二维 exponent search。下一步可以对有限 `A<=23` / `B<=10` 条带分别做 periodic modular exhaustion，或继续利用 factor-pair (22)-(23) 的 Q-side / `b_1`-side来源。

---

<a id="source-deep-moderate-root-normal-form"></a>

> 整合来源：`deep-moderate-root-normal-form.md`

# A1 minimal diagonal: moderate double-deep root normal form

> 日期：2026-08-20。依赖 `deep-moderate-factorization.md` 与 `deep-moderate-three-pattern.md`。当前范围 `k=g>=31`。

本文给 moderate double-deep 一个新的正规形：把 supply quadratic 改看成关于 gap numerator `gamma` 的二次方程后，deep denominator

\[
D=2^A5^B
\]

从根公式中**完全消失**。

设

\[
T=10^k,
\qquad
196000<r<15214000,
\]

并沿用

\[
N_0,\quad w,\quad
\Gamma_k=\gamma/D.
\]

核心结论：存在正整数 `Z` 满足

\[
\boxed{
Z^2=(10N_0T+r)^2+400N_0Tr(10T^2-w),
}
\tag{1}

而 normalized gap 唯一等于

\[
\boxed{
\Gamma_k=
\frac{
10(20w-1)N_0T-r+Z
}{2000T^2}.
}
\tag{2}

所以 `D` 只是右侧有理数约分后的 `2/5` denominator，而不再是独立变量。

状态：**已严格完成。**

---

## 1. 从 moderate supply quadratic 出发

`deep-moderate-factorization.md` 给出

\[
C_0D^2N_0^2
-DuTN_0
+1000\gamma^2T^2
+\gamma u
+c_2\gamma^2=0,
\tag{3}
\]

其中

\[
C_0=w(10w-1),
\qquad
c_2=10(1-20w),
\]

\[
u=u_0+Dr,
\qquad
u_0=10\gamma(20w-1).
\]

代入后关于 `gamma` 收集：

\[
1000T^2\gamma^2
+D\bigl(r-10(20w-1)N_0T\bigr)\gamma
+D^2\bigl(C_0N_0^2-N_0Tr\bigr)=0.
\tag{4}

---

## 2. 判别式恰为 `D^2 Z^2`

(4) 关于 `gamma` 的判别式为

\[
D^2\left(
100N_0^2T^2
+4000N_0T^3r
-400wN_0Tr
+20N_0Tr
+r^2
\right).
\]

括号重新组合：

\[
\begin{aligned}
&100N_0^2T^2+20N_0Tr+r^2
+400N_0Tr(10T^2-w)\\
&\qquad=(10N_0T+r)^2
+400N_0Tr(10T^2-w).
\end{aligned}
\]

因此 exact candidate 必须存在整数 `Z>0`，满足主式 (1)。

---

## 3. 只有 `+Z` 根可能为正

令

\[
H:=10(20w-1)N_0T-r.
\]

根公式给

\[
\Gamma_k=\frac{H\pm Z}{2000T^2}.
\tag{5}

计算

\[
\boxed{
Z^2-H^2
=4000N_0T^2(Tr-C_0N_0).
}
\tag{6}

因为

\[
r>196000,
\qquad
C_0=w(10w-1)\le156,
\qquad
N_0\le T,
\]

有

\[
Tr-C_0N_0>(196000-156)T>0.
\]

因此

\[
Z>|H|.
\]

所以

\[
H-Z<0,
\]

而 normalized gap 必须正。唯一可能根是

\[
\boxed{
\Gamma_k=\frac{H+Z}{2000T^2},
}
\]

即 (2)。

---

## 4. `D` 由根的约分唯一恢复

记

\[
\boxed{S:=H+Z.}
\]

则

\[
\Gamma_k=\frac{S}{2000T^2}.
\]

原定义 `Gamma_k=gamma/D` 已经既约，且 moderate double-deep 有 `A,B>0`。因为

\[
2000T^2=2^{2k+4}5^{2k+3},
\]

所以

\[
\boxed{
A=2k+4-v_2(S),
}
\tag{7}

\[
\boxed{
B=2k+3-v_5(S).
}
\tag{8}

因此 LL/LH/HL 的 denominator exponents 都只是同一个整数 `S` 的局部 valuation 输出。

---

## 5. conjugate product

令

\[
R:=Z-H>0.
\]

由 (6)：

\[
\boxed{
SR
=4000N_0T^2(Tr-C_0N_0).
}
\tag{9}

这给 2/5 两侧一个非常透明的 root-branch interpretation。

因为

\[
H=10(20w-1)N_0T-r,
\]

而 `v_2(r)<=23`、`v_5(r)<=10`、`k>=31`，有

\[
v_2(H)=v_2(r),
\qquad
v_5(H)=v_5(r).
\tag{10}

于是：

- 在 5-adic 中，`S=Z+H` 与 `R=Z-H` 的差是 `2H`，valuation 为 `v_5(r)`；故一个 root branch 保持 shallow valuation `v_5(r)`，另一个承担全部高 valuation。
- 在 2-adic 中，`2H` 的 valuation 为 `v_2(r)+1`；所以 shallow branch 的 valuation 是 `v_2(r)+1`，另一 branch 承担高 valuation。

这正对应 `deep-moderate-three-pattern.md` 的 low/high dichotomy。

---

## 6. `Z^2=r^2 mod T` 与 p-adic branch labels

由 (1) 直接模 `T`：

\[
\boxed{Z^2\equiv r^2\pmod T.}
\tag{11}

写

\[
a=v_2(r)\le23,
\qquad
b=v_5(r)\le10.
\]

由于 `k>=31>2a,2b`，标准 prime-power square-root lifting 给：

\[
\boxed{
Z\equiv\pm r\pmod{5^{k-b}},
}
\tag{12}

以及 2-adic 的四根合并为

\[
\boxed{
Z\equiv\pm r\pmod{2^{k-a-1}}.
}
\tag{13}

另一方面高十进制项使

\[
H\equiv-r
\]

模上述幂。因此：

- `Z congruent +r` 时 `S=H+Z` 发生大规模 cancellation，对应 **low denominator exponent**；
- `Z congruent -r` 时 `S` 留在 shallow root，因 (7)-(8) 对应 **high denominator exponent**。

所以 three-pattern 可重新标记为：

\[
\boxed{
\begin{array}{c|cc}
&2\text{-branch}&5\text{-branch}\\ \hline
LL&+&+\\
LH&+&-\\
HL&-&+
\end{array}}
\tag{14}

而 `(-,-)` 正是 high-high，已由 `deep-balanced-collapse.md` 排除。

---

## 7. normalized real equation

把 factorization

\[
(10\gamma T-wDN_0)
(100\gamma T-(10w-1)DN_0)
=Dr(DTN_0-\gamma)
\]

除以 `D^2T^2`，并令

\[
s=N_0/T,
\qquad \Gamma=\gamma/D,
\]

得到精确关系

\[
\boxed{
(10\Gamma-ws)
(100\Gamma-(10w-1)s)
=r\left(s-\frac{\Gamma}{T^2}\right).
}
\tag{15}

除了最后一个 `T^-2` 修正外，整个 moderate double-deep 的实数几何只由

\[
(w,r,s,\Gamma)
\]

控制，并且 `r` 已处于绝对有限区间。

下一步可直接在 root equation (1) / branch labels (12)-(14) 上做局部 lifting 或 periodic modular exhaustion，而无需重新引入二维 `(A,B)` 搜索。

---

<a id="source-deep-moderate-three-pattern"></a>

> 整合来源：`deep-moderate-three-pattern.md`

# A1 minimal diagonal: moderate double-deep three-pattern collapse

> 日期：2026-08-20。依赖 `deep-moderate-factorization.md` 与 `deep-balanced-collapse.md`。当前范围 `k=g>=31`。

`deep-moderate-factorization.md` 已在

\[
A,B>0,
\qquad
A,B\le2k+3
\]

中构造绝对有限整数

\[
196000<r<15214000,
\]

以及 factor pair

\[
X_1=sa,
\qquad
X_2=qb,
\qquad
ab=Dr,
\]

其中

\[
X_1=10\gamma T-wDN_0,
\]

\[
X_2=100\gamma T-(10w-1)DN_0.
\]

并且

\[
v_2(r)\le23,
\qquad
v_5(r)\le10.
\]

本文证明此前暂留的 2-adic / 5-adic transition strips 实际在 `k>=31` 全部为空。于是 moderate double-deep 只剩三个显式模板：low-low、low-high、high-low。

状态：**已严格完成。**

---

## 1. 5-adic transition `B+nu5=k+1` 不可能

记

\[
\nu_5=v_5(N_0),
\qquad
Y=B+\nu_5.
\]

若

\[
Y=k+1,
\]

则在 `X_1` 中两项的 5-adic valuation 都等于 `k+1`，因此

\[
v_5(X_1)\ge k+1.
\]

在 `X_2` 中两项赋值分别为 `k+2` 与 `k+1`，所以严格由后者承担：

\[
v_5(X_2)=k+1.
\]

由 `ab=Dr` 且 `q,s` 与 5 互素：

\[
v_5(X_1)+v_5(X_2)=B+v_5(r).
\]

因此

\[
B+v_5(r)\ge2k+2.
\]

但

\[
B=k+1-\nu_5,
\qquad
v_5(r)\le10,
\]

故右侧又满足

\[
B+v_5(r)\le k+11.
\]

当前 `k>=31` 时

\[
2k+2>k+11,
\]

矛盾。所以

\[
\boxed{B+\nu_5\ne k+1.}
\tag{1}
\]

---

## 2. 5-adic transition `B+nu5=k+2` 也不可能

若

\[
Y=k+2,
\]

则 `X_1` 中两项赋值为 `k+1` 与 `k+2`，故

\[
v_5(X_1)=k+1.
\]

而 `X_2` 两项均为 `k+2`，所以

\[
v_5(X_2)\ge k+2.
\]

于是

\[
B+v_5(r)\ge2k+3.
\]

另一方面

\[
B=k+2-\nu_5,
\]

故

\[
B+v_5(r)\le k+12.
\]

对 `k>=31`：

\[
2k+3>k+12,
\]

矛盾。因此

\[
\boxed{B+\nu_5\ne k+2.}
\tag{2}
\]

所以 5-adic transition strip 完全消失。

---

## 3. 2-adic transition strip整体不可能

记

\[
\nu_2=v_2(N_0),
\qquad
X=A+\nu_2,
\qquad
e=v_2(w)\in\{0,1,2\}.
\]

此前 transition strip 为

\[
\boxed{k+1-e\le X\le k+2.}
\tag{3}
\]

在 `X_1` 中两项赋值为

\[
k+1,\qquad X+e.
\]

由 (3)，二者最小值至少为 `k+1`，所以

\[
v_2(X_1)\ge k+1.
\]

在 `X_2` 中两项赋值为

\[
k+2,\qquad X,
\]

故

\[
v_2(X_2)\ge X\ge k+1-e.
\]

于是

\[
v_2(X_1)+v_2(X_2)
\ge2k+2-e.
\tag{4}
\]

但 `ab=Dr` 给

\[
v_2(X_1)+v_2(X_2)
=A+v_2(r).
\]

而 transition 中 `A<=X<=k+2`，再用 `v_2(r)<=23`：

\[
A+v_2(r)\le k+25.
\tag{5}
\]

对 `k>=31`、`e<=2`：

\[
2k+2-e\ge2k
>k+25.
\]

(4)-(5) 矛盾。因此

\[
\boxed{
 k+1-e\le A+\nu_2\le k+2
 \Longrightarrow\bot.
}
\tag{6}

所以 2-adic transition strip 也完全消失。

---

## 4. 两个素数侧现在都只有 low / high 两态

由 `deep-moderate-factorization.md` 的 valuation dichotomy，再结合 §§1–3：

### 2-adic low

\[
\boxed{
A+2\nu_2+e=v_2(r)\le23.
}
\tag{7}

### 2-adic high

\[
\boxed{
A=2k+3-v_2(r).
}
\tag{8}

### 5-adic low

\[
\boxed{
B+2\nu_5=v_5(r)\le10.
}
\tag{9}

### 5-adic high

\[
\boxed{
B=2k+3-v_5(r).
}
\tag{10}

不存在第三种 transition 状态。

---

## 5. high-high 被 fully-balanced collapse 排除

若 2、5 两侧同时 high，则由 (8)、(10)：

\[
A+e+\nu_2>k,
\qquad
B+\nu_5>k.
\]

这正落入 `deep-balanced-collapse.md` 已排除的 fully-balanced double-deep 区域。因此

\[
\boxed{\text{high-high impossible}.}
\tag{11}

所以 moderate double-deep 只剩三种模板。

---

## 6. 最终 three-pattern normal form

任意 moderate double-deep candidate 必须属于且只可能属于以下三类之一。

### LL: low-low

\[
\boxed{
A+2\nu_2+e=v_2(r),
\qquad
B+2\nu_5=v_5(r).
}
\tag{12}

特别地

\[
A\le23,
\qquad B\le10.
\]

### LH: 2-low / 5-high

\[
\boxed{
A+2\nu_2+e=v_2(r),
\qquad
B=2k+3-v_5(r).
}
\tag{13}

因此 `A<=23`，而 `B` 被 `k` 与有限参数 `v_5(r)` 精确锁定。

### HL: 2-high / 5-low

\[
\boxed{
A=2k+3-v_2(r),
\qquad
B+2\nu_5=v_5(r).
}
\tag{14}

因此 `B<=10`，而 `A` 被 `k` 与有限参数 `v_2(r)` 精确锁定。

综上：

\[
\boxed{
\text{moderate double-deep}
=\text{LL}\cup\text{LH}\cup\text{HL},
}
\tag{15}

其中

\[
196000<r<15214000.
\]

原来的二维 `(A,B)` 自由度已经完全消失。

---

## 7. high branch 上 factor pair 的巨大素数幂被精确分配

这个 three-pattern 还有一个直接可用的加强。

### LH

由 `B=2k+3-v_5(r)`，总 5-adic exponent 为

\[
B+v_5(r)=2k+3.
\]

而 high branch 中

\[
v_5(X_1)=k+1,
\qquad
v_5(X_2)=k+2.
\]

所以若写

\[
r=5^{v_5(r)}r_5,
\qquad 5\nmid r_5,
\]

则

\[
\boxed{
a=5^{k+1}a_0,}
\qquad
\boxed{b=5^{k+2}b_0,}
\]

并且

\[
\boxed{a_0b_0=2^A r_5.}
\tag{16}

右侧是绝对有界对象，因为 `A<=23`、`r<15214000`。

### HL

完全对称。写

\[
r=2^{v_2(r)}r_2,
\qquad 2\nmid r_2.
\]

则

\[
\boxed{a=2^{k+1}a_0,}
\qquad
\boxed{b=2^{k+2}b_0,}
\]

且

\[
\boxed{a_0b_0=5^B r_2.}
\tag{17}

这里 `B<=10`，所以右侧同样绝对有界。

这意味着 LH / HL 并不只是“一侧指数线性锁定”：除去显式的 `5^{k+1},5^{k+2}` 或 `2^{k+1},2^{k+2}` 后，两个 factor 的剩余 quotient 已经来自绝对有限 divisor set。

下一步应优先利用 (16)-(17) 与 `s|b_1,q|Q` 做 resultant / modular exhaustion。

---

<a id="source-deep-q-side-proper-divisor"></a>

> 整合来源：`deep-q-side-proper-divisor.md`

# A1 minimal diagonal: strict 2-deep Q-side proper-divisor cap

> 日期：2026-08-19。依赖 `deep-gap-unit-square.md`。

在 strict 2-adic low-side，已有

\[
h=qs,
\qquad q\mid Q,
\qquad s\equiv1\pmod4,
\]

以及 Q-side orientation

\[
w\text{ odd}\Longrightarrow q\equiv1\pmod4,
\]

\[
w\text{ even}\Longrightarrow q\equiv3\pmod4.
\]

本文把这个方向锁转成一个统一的 proper-divisor 与尺寸结论。

状态：**已严格完成。**

---

## 1. `Q mod 4`

minimal diagonal 中

\[
Q=10b_1+1,
\qquad b_1=10^{2k+1}-w.
\]

当前 `k>=26`，所以高十进制幂模 4 消失：

\[
b_1\equiv-w\pmod4.
\]

因此

\[
Q\equiv1-2w\pmod4.
\]

即

\[
\boxed{
Q\equiv3\pmod4\quad(w=1,3),
}
\tag{1}
\]

\[
\boxed{
Q\equiv1\pmod4\quad(w=2,4).
}
\tag{2}
\]

---

## 2. 补因子 `Q/q` 永远是 `3 mod 4`

### odd `w`

此时 `q≡1 mod4`，而 `Q≡3 mod4`。因为 `q` 为奇数，模 4 可逆，所以

\[
\boxed{Q/q\equiv3\pmod4.}
\tag{3}
\]

### even `w`

此时 `q≡3 mod4`，`Q≡1 mod4`。`3^{-1}≡3 mod4`，故仍有

\[
\boxed{Q/q\equiv3\pmod4.}
\tag{4}
\]

所以六类型统一：

\[
\boxed{
Q/q\equiv3\pmod4.
}
\tag{5}
\]

特别地

\[
\boxed{q<Q.}
\tag{6}
\]

strict 2-deep 中 Q-side 永远不能饱和地取完整 `Q`。

对 even `w` 还有 `q≡3 mod4`，因此

\[
\boxed{q>1.}
\tag{7}
\]

也就是说 even-`w` strict 2-deep 必须从 `Q` 中真正抽出一个非平凡 `3 mod 4` proper divisor。

---

## 3. 模 3 再给出统一尺寸 cap

令

\[
T=10^k.
\]

因为 `T≡1 mod3`，

\[
Q=100T^2-(10w-1)
\equiv1-(w-1)
=2-w
\pmod3.
\tag{8}
\]

所以

\[
3\mid Q
\iff w=2.
\tag{9}
\]

由 (5)，补因子 `Q/q` 是正整数且 `3 mod4`。

- 当 `w=2` 时，其最小可能值为 `3`，故
  \[
  \boxed{q\le Q/3.}
  \tag{10}
  \]
- 当 `w=1,3,4` 时，`3` 不整除 `Q`，因此 `Q/q` 不可能等于 `3`。正整数中下一个 `3 mod4` 的值是 `7`，故
  \[
  \boxed{q\le Q/7.}
  \tag{11}
  \]

于是统一尺寸表为

\[
\boxed{
\begin{array}{c|c}
w&q\text{ upper bound}\\ \hline
1&Q/7\\
2&Q/3\\
3&Q/7\\
4&Q/7
\end{array}}
\tag{12}
\]

---

## 4. 对 odd-prime supply 的新上界

完整 supply 为

\[
h=qs,
\]

其中 `s` 是 `b_1` 的 `1 mod4` whole-block selector。记全部可选 blocks 的乘积为 `B_+`，则

\[
s\le B_+.
\]

因此 strict 2-deep 中可统一加强原来的粗界 `h<=QB_+` 为

\[
\boxed{
h\le\frac{QB_+}{7}
\qquad(w=1,3,4),}
\tag{13}
\]

\[
\boxed{
h\le\frac{QB_+}{3}
\qquad(w=2).}
\tag{14}
\]

这个常数因子本身不足以关闭 deep sector，但它是 prefix-uniform 的真实供给损失，可直接塞回 finite exponent box / decade bound；更重要的是 even-`w` 还带有“`Q` 必须存在非平凡 `3 mod4` proper divisor”的结构条件。

---

## 5. 当前用途

后续 deep 证书不应再使用完整 `Q` 作为 Q-side 极值。strict 2-deep 可以直接使用 (12)-(14)。

对于 fixed `k`，若 `Q` 为素数，则 even-`w` 的 strict 2-deep 立即为空；更一般地，若 `Q` 没有 `3 mod4` proper divisor，则 even-`w` strict 2-deep 为空。

odd-`w` 虽允许 `q=1`，但 `q=Q` 已永久排除，并统一损失至少因子 `7`。

---

<a id="source-deep-root-factor-splitting"></a>

> 整合来源：`deep-root-factor-splitting.md`

# A1 minimal diagonal: moderate root-square factor splitting

> 日期：2026-08-20。依赖 `deep-moderate-root-normal-form.md` 与 `deep-four-factor-frame.md`。当前范围 `k=g>=31`。

本文审计 moderate root normal form 中的平方

\[
Z^2=(10N_0T+r)^2+400N_0Tr(10T^2-w).
\]

结论：该平方在 full four-factor frame 中并不是新的独立 obstruction；其差平方因子可以精确写成 supply / complementary divisors 的乘积。

状态：**已严格完成。**

---

## 1. 完成平方

定义

\[
\boxed{C:=200T^2-20w+1,}
\qquad
\boxed{X:=10N_0T+rC.}
\]

直接展开：

\[
\begin{aligned}
X^2-Z^2
&=r^2(C^2-1)\\
&=r^2(C-1)(C+1).
\end{aligned}
\]

而

\[
C-1=20(10T^2-w)=20b_1,
\]

\[
C+1=2(100T^2-10w+1)=2Q.
\]

所以

\[
\boxed{
(X-Z)(X+Z)=40r^2b_1Q.
}
\tag{1}
\]

---

## 2. 用 universal factor pair 分解两个根因子

moderate double-deep 有

\[
t=Dr,
\qquad
ab=t=Dr,
\]

以及

\[
X_1=sa,
\qquad
X_2=qb,
\]

\[
\bar q=Q/q,
\qquad
\bar s=b_1/s,
\]

\[
\bar s b-\bar q a=10T.
\]

由 root formula

\[
Z=2000T^2\Gamma-10(20w-1)N_0T+r.
\]

直接整理：

\[
X-Z
=20\left(rb_1-10T\frac{X_1}{D}\right).
\]

代入

\[
b_1=s\bar s,
\qquad X_1=sa,
\qquad r=ab/D,
\]

得到

\[
X-Z
=\frac{20sa}{D}(b\bar s-10T).
\]

再用

\[
b\bar s-10T=a\bar q,
\]

即

\[
\boxed{
X-Z=\frac{20a^2s\bar q}{D}.
}
\tag{2}
\]

由 (1) 或对称计算：

\[
\boxed{
X+Z=\frac{2b^2\bar s q}{D}.
}
\tag{3}

两式相乘恰好恢复 (1)。

---

## 3. `HL` 专门化

HL 中

\[
a=2^{k+1}5^Y\alpha,
\qquad
b=2^{k+2}5^Y\beta,
\]

\[
A=2k+3-v_2(r),
\qquad
B+2\nu_5=v_5(r),
\]

\[
\alpha\beta=r_{10}.
\]

记

\[
a_2=v_2(r),
\qquad a_5=v_5(r).
\]

则

\[
\frac{20a^2}{D}
=2^{a_2+1}5^{a_5+1}\alpha^2
=10\frac{r\alpha}{\beta},
\]

以及

\[
\frac{2b^2}{D}
=2^{a_2+2}5^{a_5}\beta^2
=4\frac{r\beta}{\alpha}.
\]

所以 HL 的 root factors 是

\[
\boxed{
X-Z=10\frac{r\alpha}{\beta}\,s\bar q,
}
\tag{4}
\]

\[
\boxed{
X+Z=4\frac{r\beta}{\alpha}\,\bar s q.
}
\tag{5}

由于 `alpha,beta` 是 `r_10` 的 coprime whole-block partition，两个系数均为整数。

---

## 4. `LL` 专门化

LL 中同理得到

\[
\boxed{
X-Z=20\,2^e\frac{r\alpha}{\beta}\,s\bar q,
}
\tag{6}

\[
\boxed{
X+Z=2^{1-e}\frac{r\beta}{\alpha}\,\bar s q,
}
\tag{7}

其中 `e=v_2(w)`；(7) 虽写有 `2^(1-e)`，由 LL 的 `v_2(r)=A+2nu_2+e` 可知整体系数始终为整数。

---

## 5. 审计意义

`deep-moderate-root-normal-form.md` 的 square `Z^2=...` 是由 supply quadratic 的判别式产生的。本文说明，一旦 full factor-pair / four-factor frame 已经成立，`X±Z` 被 (2)-(3) 显式构造，因此 root square 不能再被重复当作一层独立 arithmetic obstruction。

这解释了仅用 root-square + contact-square 的 odd-prime modular sieve 很弱：它没有加入真正新的 prime-source information。

后续 HL 攻击应优先使用：

- stripped complement / supply equations；
- Q-side orientation 与 whole-block source；
- first complement remainder；
- 5-adic Hensel lock；

而不应把 (1) 再计作“第三个独立平方”。

---

<a id="source-deep-single5-contact-dichotomy"></a>

> 整合来源：`deep-single5-contact-dichotomy.md`

# A1 minimal diagonal: strict single-5 contact-lift dichotomy

> 日期：2026-08-20。依赖 `deep-single5-first-remainder-height.md` 与 `deep-contact-q-square-blocks-universal.md`。

本文把 strict single-5-deep 进一步分成一个显式 low-ratio strip 与一个 forced contact-lift strip。

状态：**已严格完成；single-5 尚未整体关闭。**

---

## 1. strict single-5 coordinates

single-5：

\[
A=0,
\qquad D=5^B,
\qquad B>0.
\]

2-side 非 deep，记

\[
\lambda=2^{\lambda_2},
\qquad 0\le\lambda_2\le2k
\]

（strict 5-low 时由 cross-corridor `x<=k`）。

记

\[
\nu=v_5(N_0),
\qquad Y=B+\nu.
\]

`deep-single5-first-remainder-height.md` 可保留 `lambda_2` 后写成更精确形式：

\[
5^Y<R_1<390100\,2^{\lambda_2}10^k.
\]

使用

\[
390100<5^8,
\qquad2<5^{0.431},
\qquad10<5^{1.431},
\]

得到

\[
\boxed{
B+\nu
<8+1.431k+0.431\lambda_2.}
\tag{1}

旧 `2.3k+8` 是把 `lambda_2<=2k` 代入后的粗化。

---

## 2. contact forced-lift threshold

universal contact theorem给：若

\[
\frac D\lambda>K_{z,w}T,
\]

则 `q>gcd(q,C)`，必有 genuine Q-side exponent amplification。

single-5 中

\[
\frac D\lambda=\frac{5^B}{2^{\lambda_2}}.
\]

所以 forced-lift 条件是

\[
5^B>K_{z,w}\,2^{\lambda_2}10^k.
\tag{2}

等价地，使用安全十进制：

\[
\boxed{
B>\kappa_{z,w}+1.431k+0.431\lambda_2
\Longrightarrow
\text{forced contact lift},}
\tag{3}

其中可取

\[
\boxed{
\begin{array}{c|c}
(z,w)&\kappa_{z,w}\\ \hline
(1,1)&5.92\\
(1,2)&5.42\\
(1,3)&7.33\\
(1,4)&5.97\\
(3,1)&5.50\\
(3,2)&5.01
\end{array}}
\tag{4}

这些数均严格大于 `log_5 K_(z,w)`。

---

## 3. strict single-5 的两条带

因此每个 strict single-5 candidate 必落入以下之一。

### low-ratio strip

\[
\boxed{
B<\kappa_{z,w}+1.431k+0.431\lambda_2.}
\tag{5}

这里不保证 contact exponent amplification，但 denominator slope 已显式受控。

### forced-lift strip

若 (5) 不成立，则 contact square 必强迫至少一个 selected Q-primary block在 `L_-` 或 `L_+` 中出现 strict exponent amplification。

同时 first remainder 又要求 (1)：

\[
B+
u<8+1.431k+0.431\lambda_2.
\]

所以 forced-lift strip 在 B 方向的宽度最多只有

\[
\boxed{8-\kappa_{z,w}-\nu}
\tag{6}

个 5-adic exponent units（严格不等式意义下）。

六类型的最坏常数宽度约为：

\[
\begin{array}{c|c}
(z,w)&8-\kappa_{z,w}\\ \hline
(1,1)&2.08\\
(1,2)&2.58\\
(1,3)&0.67\\
(1,4)&2.03\\
(3,1)&2.50\\
(3,2)&2.99
\end{array}
\]

而 `nu>=1` 时还会再缩 1。

所以 strict single-5 的 contact-lift区域其实只是 first-remainder top edge 附近的绝对常数宽薄带。

---

## 4. 与 parity 联立

strict 5-low 已有

\[
B>v_5(N),
\qquad
B\equiv v_5(N)\pmod2.
\]

因此在 forced-lift strip 的宽度至多约 3 的情况下，每个 fixed

\[
(k,\lambda_2,\text{prefix 5-adic branch})
\]

实际上至多只剩 1--2 个 parity-compatible B。

这为后续把 single-5 top strip 做 periodic contact-block certificate 提供了有限接口。

---

## 5. 当前意义

strict single-5 已从一个 unbounded B-half-plane 变成：

1. 显式线性 low-ratio strip (5)；
2. first-remainder 顶部一个宽度 <3 的 forced-contact-lift strip。

下一步可分别：

- low-ratio strip：继续结合 denominator funnel / prefix 5-adic root branches；
- top strip：直接利用 universal contact Q-side lifted blocks。

---

<a id="source-deep-single5-first-remainder-height"></a>

> 整合来源：`deep-single5-first-remainder-height.md`

# A1 minimal diagonal: strict single-5-deep first-remainder height bound

> 日期：2026-08-20。依赖 `deep-first-complement-remainder.md`、`deep-gap-valuation-normal-form.md` 与 cross-corridor theorem。当前剩余 fixed frontier 从 `k>=32` 开始；本文结论实际只需远小于此的 k。

本文处理 single-5-deep：

\[
A=0,
\qquad B>0,
\]

并首先关闭其“过深”方向。在 strict 5-low 子区得到线性斜率上界

\[
\boxed{B+v_5(N_0)<2.3k+8.}
\]

状态：**strict 5-low 高度压缩已严格完成；single-5 尚未整体关闭。**

---

## 1. single-5 的 non-deep 2-side

因为 `A=0`，2-side 留在 numerator 的指数为

\[
\lambda_2=k+x\ge0,
\qquad
\lambda=2^{\lambda_2}.
\]

若当前位于 strict 5-low：

\[
B>n_5:=v_5(N),
\]

则

\[
y=-k-B<y_*=-k-n_5.
\]

cross-corridor 已证明：`y<y_*` 时不能同时有 `x>k`。所以

\[
\boxed{x\le k.}
\]

因此

\[
\boxed{0\le\lambda_2\le2k.}
\tag{1}

这一步把 non-deep 2-side 的 numerator compensation 限制在最多 `2k` 层。

---

## 2. first remainder

沿用 universal complement first remainder：

\[
MDN_0=1000\lambda T^3+R_1,
\]

\[
\boxed{0<R_1<390100\lambda T,}
\tag{2}

其中

\[
D=5^B,
\qquad v_5(M)=0.
\]

记

\[
\nu:=v_5(N_0),
\qquad Y:=B+\nu.
\]

左侧的 5-adic valuation 为

\[
\boxed{v_5(MDN_0)=Y.}
\tag{3}

主项因为 `lambda` 只含 2：

\[
\boxed{v_5(1000\lambda T^3)=3k+3.}
\tag{4}

---

## 3. `Y>=3k+3` 不可能

若

\[
Y>3k+3,
\]

则两项赋值不同，故

\[
v_5(R_1)=3k+3.
\]

若

\[
Y=3k+3,
\]

则 cancellation 只会让 `R_1` 更深，因此仍有

\[
5^{3k+3}\mid R_1.
\]

结合 (1)-(2)：

\[
5^{3k+3}
<R_1
<390100\,2^{2k}10^k
=390100\,2^{3k}5^k.
\]

于是必须有

\[
125\left(\frac{25}{8}\right)^k<390100.
\]

当前 `k>=32` 时左侧远大于右侧，矛盾。

所以

\[
\boxed{Y<3k+3.}
\tag{5}

---

## 4. strict slope bound

由 (5)，(3) 与 (4) 赋值严格不同，所以现在

\[
\boxed{v_5(R_1)=Y.}
\tag{6}

因此

\[
5^Y\le R_1
<390100\,2^{2k}10^k
=390100\,2^{3k}5^k.
\]

使用安全数值

\[
390100<5^8,
\qquad
2^3=8<5^{1.3},
\]

得到

\[
5^Y<5^{8+1.3k+k}.
\]

所以

\[
\boxed{
B+v_5(N_0)=Y<2.3k+8.}
\tag{7}

这是 strict single-5-deep 的统一 first-remainder height bound。

---

## 5. 与 resonance parity 联立

strict 5-low 原本还有

\[
B>n_5,
\qquad
B\equiv n_5\pmod2.
\]

现在再加 (7)。因此 single-5 的 strict-low lattice 从无界 half-plane 压成

\[
\boxed{
\begin{aligned}
&B>n_5,\\
&B\equiv n_5\pmod2,\\
&B+v_5(N_0)<2.3k+8,\\
&0\le\lambda_2\le2k.
\end{aligned}}
\]

并仍受 mod-5 unit Legendre lock。

---

## 6. 当前边界

本文没有处理：

- 5-adic resonance `B=n_5`；
- high-side `0<B<n_5`。

这些层需要与 prefix `v_5(N)` 的 Hensel branches 联用。

但 strict single-5 的“任意深 B”已经消失；其最大斜率严格低于 `2.3k`，后续可以再与 prefix 5-adic root lifting / contact sign 合并。

---

<a id="source-deep-typewise-r-window"></a>

> 整合来源：`deep-typewise-r-window.md`

# A1 minimal diagonal: typewise moderate `r` windows

> 日期：2026-08-20。依赖 `sharp-positive-tail-window.md` 与 `deep-moderate-factorization.md`。当前范围 `k=g>=31`。

moderate double-deep 中此前只使用统一粗界

\[
196000<r<15214000.
\]

本文把六个 prefix 类型各自的 sharpened gap window 保留下来，得到更窄的 exact integer intervals。

状态：**已严格完成。**

---

## 1. `r` 的 exact real formula

写

\[
T=10^k,
\qquad s:=N_0/T\in[0.1,1],
\qquad \Gamma:=\Gamma_k=\gamma/D.
\]

moderate factorization 中

\[
X_1=10\gamma T-wDN_0,
\qquad
X_2=100\gamma T-(10w-1)DN_0,
\]

\[
h=DTN_0-\gamma,
\qquad
X_1X_2=Drh.
\]

除去 `D^2 T^2` 后精确得到

\[
\boxed{
 r=
\frac{
(10\Gamma-ws)
(100\Gamma-(10w-1)s)
}{
s-\Gamma/T^2
}.
}
\tag{1}
\]

当前 `Gamma<39.003`、`T>=10^31`，分母严格为正。

---

## 2. 单调性

记分子

\[
P=(10\Gamma-ws)(100\Gamma-(10w-1)s)>0,
\]

分母

\[
H=s-\Gamma/T^2>0.
\]

对 `Gamma`：两个分子因子都严格增加，而 `H` 严格减少，所以

\[
\boxed{\partial_\Gamma r>0.}
\tag{2}
\]

对 `s`：两个分子因子都严格减少，所以 `partial_s P<0`，而 `partial_s H=1`。因此

\[
\partial_s r
=\frac{(\partial_sP)H-P}{H^2}<0.
\]

故

\[
\boxed{\partial_s r<0.}
\tag{3}
\]

所以每个类型的最小 `r` 在 `s=1`、typewise lower gap endpoint；最大 `r` 在 `s=0.1`、typewise upper endpoint。

---

## 3. typewise gap constants

`sharp-positive-tail-window.md` 的严格 typewise lower constants 可取：

\[
\begin{array}{c|c}
(z,w)&L_{z,w}\\ \hline
(1,1)&27.6949968\\
(1,2)&23.4949936\\
(1,3)&19.2949904\\
(1,4)&15.0949872\\
(3,1)&19.6949978\\
(3,2)&17.4949956
\end{array}
\]

同一文件的 typewise upper computation给出安全严格上界：

\[
\begin{array}{c|c}
(z,w)&U_{z,w}\\ \hline
(1,1)&33.00225945\\
(1,2)&29.00225945\\
(1,3)&25.00225945\\
(1,4)&21.00225945\\
(3,1)&39.00225945\\
(3,2)&37.00225945
\end{array}
\]

这些常数本来用 `epsilon<=10^-6` 推出，所以当前 `k>=31` 当然安全。

---

## 4. exact integer windows

把上述端点代入 (1)，并在最坏 `T=10^31` 下用 exact rational arithmetic 取严格整数内窗，得到：

\[
\boxed{
\begin{array}{c|c}
(z,w)&r\\ \hline
(1,1)&761760\le r\le10885221\\
(1,2)&542890\le r\le8400003\\
(1,3)&361000\le r\le6236387\\
(1,4)&216090\le r\le4394372\\
(3,1)&384160\le r\le15204352\\
(3,2)&299290\le r\le13677244
\end{array}}
\tag{4}
\]

因为 `Gamma/T^2` 随 `T` 增大而变小，上述 `T=10^31` 端点对全部更大 `k` 同样安全；脚本使用 exact fractions 审计这些整数截断。

---

## 5. valuation 改进

从 (4) 立即得到：

\[
\boxed{
v_2(r)\le22
\quad\text{for }(1,3),(1,4),}
\tag{5}
\]

其余四类型仍安全使用 `v_2(r)<=23`。

五进方面：

\[
5^{10}=9765625.
\]

所以

\[
\boxed{
v_5(r)\le9
\quad\text{for }(1,2),(1,3),(1,4),}
\tag{6}
\]

而 `(1,1),(3,1),(3,2)` 仍用 `v_5(r)<=10`。

当前 moderate double-deep 已全部处于 5-low，因此

\[
B+2\nu_5=v_5(r).
\]

于是进一步：

\[
\boxed{
B+2\nu_5\le9
\quad\text{for }(1,2),(1,3),(1,4),}
\tag{7}
\]

其余三类型有 `<=10`。

---

## 6. 当前用途

后续 LL/HL 的 finite `r` / block-partition exhaustion 不应再扫描统一粗窗。应直接按 (4) 的 typewise interval，并在入口先应用：

- `r_10 mod 4` branch filter；
- `v_5(r)` 的 typewise cap；
- `(1,3),(1,4)` 的更强 `v_2(r)<=22`。

这会进一步降低 moderate branch 的 finite parameter volume。

---

<a id="source-deep-universal-factorization"></a>

> 整合来源：`deep-universal-factorization.md`

# A1 minimal diagonal: universal deep factorization

> 日期：2026-08-20。依赖 `deep-complement-height.md` 与 minimal-diagonal odd-prime supply。当前统一范围 `k=g>=31`。

本文证明：`deep-global-factorization.md` 的核心 factor-pair 并非 double-deep 特例，而是对**所有 deep denominator states** 都成立。

沿用

\[
T=10^k,
\qquad
D=2^A5^B,
\qquad
\Gamma_k=\frac{\gamma}{D},
\qquad \gcd(\gamma,D)=1,
\]

并令非 deep 一侧留下的 numerator powers 为

\[
\lambda=2^{\lambda_2}5^{\lambda_5}.
\]

于是

\[
\boxed{DTN_0-\gamma=h\lambda.}
\tag{1}
\]

核心结论：存在正整数 `t`，使

\[
\boxed{
(10\gamma T-wDN_0)
(100\gamma T-(10w-1)DN_0)
=t h.
}
\tag{2}

若完整 odd-prime supply 写成 `h=qs`，则存在正整数 `a,b`：

\[
\boxed{
10\gamma T-wDN_0=sa,
}
\]

\[
\boxed{
100\gamma T-(10w-1)DN_0=qb,
}
\]

并且

\[
\boxed{ab=t.}
\tag{3}

状态：**已严格完成。**

---

## 1. 对 `lambda D^4 Qb1` 做 Euclidean descent

记

\[
L=DT,
\qquad
H:=DTN_0-\gamma=N_0L-\gamma=h\lambda.
\]

因为 `h|Qb_1`，有

\[
H=h\lambda\mid\lambda Qb_1.
\]

于是当然

\[
H\mid\lambda D^4Qb_1.
\]

而

\[
\boxed{
\lambda D^4Qb_1
=
1000\lambda L^4
+c_2\lambda D^2L^2
+C_0\lambda D^4,
}
\tag{4}

其中

\[
c_2=10(1-20w),
\qquad
C_0=w(10w-1).
\]

对商按 `L` 做两级 Euclidean division，与 central / double-deep 的推导完全相同，得到整数 `U`：

\[
\boxed{
C_0\lambda D^4N_0^2
-U L N_0
+1000\lambda\gamma^2L^2
+\gamma U
+c_2\lambda D^2\gamma^2
=0.
}
\tag{5}

---

## 2. 仍然有 `D^2 | U`

模 `D` 看 (5)，只有 `gamma U` 可能不含 `D`。因为 `gcd(gamma,D)=1`：

\[
D\mid U.
\]

写 `U=DU_1`，再模 `D^2`：

\[
D\gamma U_1\equiv0\pmod{D^2}.
\]

故

\[
D\mid U_1.
\]

所以

\[
\boxed{D^2\mid U.}
\tag{6}

写

\[
\boxed{U=D^2u.}
\]

将 (5) 除以 `D^2`：

\[
\boxed{
C_0\lambda D^2N_0^2
-DuTN_0
+1000\lambda\gamma^2T^2
+\gamma u
+c_2\lambda\gamma^2
=0.
}
\tag{7}

---

## 3. universal natural square point

定义

\[
\boxed{
u_0:=10\lambda\gamma(20w-1).}
\tag{8}

从 (5) 解出 `u/D`，使用 `Gamma_k=gamma/D`：

\[
\boxed{
\frac uD
=\lambda
\frac{
C_0N_0^2+1000\Gamma_k^2T^2+c_2\Gamma_k^2
}{TN_0-\Gamma_k}.
}
\tag{9}

因此与 double-deep 相比只是整体乘上 `lambda`。同一组实数窗口给出安全界

\[
227000\lambda<\frac uD<15214000\lambda,
\]

而

\[
0<\frac{u_0}{D}<30813\lambda.
\]

所以

\[
\boxed{t:=u-u_0\in\mathbf Z_{>0}}
\tag{10}

且

\[
\boxed{
196000\lambda
<\frac tD
<15214000\lambda.
}
\tag{11}

---

## 4. `lambda` 从 factorization 中完全消失

把

\[
u=u_0+t
\]

代回 (7)。由于

\[
\gamma u_0+c_2\lambda\gamma^2=0,
\]

其余主项为

\[
\lambda\left[
C_0(DN_0)^2
-10(20w-1)(DN_0)(\gamma T)
+1000(\gamma T)^2
\right]
+t(\gamma-DTN_0).
\]

方括号精确因式分解为

\[
(wDN_0-10\gamma T)
((10w-1)DN_0-100\gamma T).
\]

而由 (1)：

\[
\gamma-DTN_0=-h\lambda.
\]

所以整体除以 `lambda` 后得到

\[
\boxed{
(wDN_0-10\gamma T)
((10w-1)DN_0-100\gamma T)
=t h.
}
\tag{12}

这证明了 universal factorization。

定义两个正因子

\[
\boxed{X_1:=10\gamma T-wDN_0,}
\]

\[
\boxed{X_2:=100\gamma T-(10w-1)DN_0.}
\]

则

\[
\boxed{X_1X_2=t h.}
\tag{13}

---

## 5. Q-side / b1-side 仍自动分流

完整 odd supply 为

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\qquad \gcd(q,s)=1.
\]

(1) 给

\[
DTN_0\equiv\gamma\pmod h.
\]

因此

\[
TX_1\equiv\gamma b_1\equiv0\pmod s,
\]

\[
TX_2\equiv\gamma Q\equiv0\pmod q.
\]

`T` 与 `q,s` 互素，所以

\[
\boxed{s\mid X_1,}
\qquad
\boxed{q\mid X_2.}
\tag{14}

写

\[
X_1=sa,
\qquad
X_2=qb.
\]

由 (13)、`h=qs`：

\[
\boxed{ab=t.}
\tag{15}

因此 single-deep 与 double-deep 共享完全相同的 factor-pair / prime-supply skeleton。

---

## 6. universal congruence threshold

把 (7) 模 `D`。使用 `u_0=-c_2 lambda gamma`、`t=u-u_0`：

\[
\boxed{
 t\equiv-1000\lambda\gamma T^2\pmod D.
}
\tag{16}

右侧的 2/5 valuations 为

\[
\boxed{
 v_2(1000\lambda\gamma T^2)=2k+3+\lambda_2
}
\]

（当 `A>0` 时 `gamma` 是 2-adic unit；若 `A=0` 这一侧无 denominator excess），以及

\[
\boxed{
 v_5(1000\lambda\gamma T^2)=2k+3+\lambda_5
}
\]

在相应 deep side。

所以每个 deep prime side 都有统一 threshold

\[
\boxed{2k+3+\lambda_p.}
\tag{17}

超过 threshold 的 denominator excess 会精确转成 `t/D` 在该 prime 上的负 valuation；低于 threshold 则该 denominator prime power全部整除 `t`。

这把 single / double deep 的 excess geometry统一到同一个坐标系中。

---

## 7. 当前意义

此前：

- double-deep 有 global factorization；
- single-deep 主要通过 resonance / complement-height 单独处理。

本文说明二者其实拥有同一个 exact divisor skeleton：

\[
\boxed{
X_1=sa,
\qquad
X_2=qb,
\qquad
ab=t,
}
\]

以及同一个 shifted threshold

\[
2k+3+\lambda_p.
\]

因此下一阶段可以统一按 `t` 的 2/5 valuation 与 `a,b` 的 factor allocation 分类，而不再为 single / double deep 维护两套互不相干的算术框架。

---

<a id="source-deep-w1-joint-complement-minimum"></a>

> 整合来源：`deep-w1-joint-complement-minimum.md`

# A1 minimal diagonal: joint complement minimum for `w=1`

> 日期：2026-08-20。依赖 `deep-b1-sharp-mandatory-blocks.md` 与 strict-2 Q-side orientation。本文适用于 surviving double-deep 2-high master。

单独看 structural minima 只能得到 `u>=27`,`v>=7`，即 `M=uv>=189`。本文利用它们各自的 decimal divisibility period不能同时取到最弱值，严格提高为

\[
\boxed{w=1:\quad M=uv\ge621.}
\]

状态：**已严格完成。**

---

## 1. 3-primary branch of `u`

写

\[
n=2k+1,
\qquad r_3=v_3(n).
\]

LTE：

\[
v_3(b_1)=2+r_3.
\]

### r3 odd

若 `r3=1`：

\[
\boxed{u\ge27.}
\tag{1}

若 `r3>=3`：

\[
u\ge3^5=243.
\tag{2}

### r3 even

3-primary block exponent为偶数；因 `b1=3 mod4`，还需要另一个 `3 mod4` block，最小 prime至少 31。所以：

- `r3=0`: `u>=9*31=279`；
- `r3>=2`: 更大，至少 `3^4*31=2511`。

---

## 2. v 的 small `3 mod4` primes

strict-2 orientation给

\[
v=Q/q\equiv3\pmod4.
\]

而 `3 not|Q`、`11 not|Q` 对 w=1 恒成立。

### p=7

\[
Q=10^{2k+2}-9.
\]

模 7：

\[
10^2\equiv2,
\qquad9\equiv2.
\]

所以

\[
7\mid Q
\iff2^{k+1}\equiv2\pmod7
\iff2^k\equiv1\pmod7
\iff\boxed{k\equiv0\pmod3.}
\tag{3}

此时

\[
n=2k+1\equiv1\pmod3,
\]

故 `r3=0`，于是由上一节

\[
\boxed{7\mid v\Longrightarrow u\ge279.}
\tag{4}

因此该 branch：

\[
uv\ge279\cdot7=1953.
\]

### p=19

`ord_19(10)=18`，且直接计算

\[
10^{10}\equiv9\pmod{19}.
\]

所以

\[
19\mid Q
\iff2k+2\equiv10\pmod{18}
\iff\boxed{k\equiv4\pmod9.}
\tag{5}

于是

\[
n=2k+1\equiv9\pmod{18},
\]

特别地

\[
9\mid n,
\qquad r_3\ge2.
\tag{6}

因此 `r3=1` branch 不可能使用 p=19 作为 v 的 `3 mod4` source。

---

## 3. 分支合并

### r3=1

此时 `k=1 mod3`，所以由 (3) `7 not|Q`；又由 (5)-(6)，`19 not|Q`。

加上 universal `3,11 not|Q`，v 中 mandatory `3 mod4` prime至少是下一个

\[
\boxed{23.}
\]

结合 u>=27：

\[
\boxed{uv\ge27\cdot23=621.}
\tag{7}

### r3=0

u>=279，而 v>=7：

\[
uv\ge1953>621.
\]

### r3>=2

若 r3 odd，u>=243，而 k=1 mod3，所以 7 absent，v>=19：

\[
uv\ge243\cdot19>621.
\]

若 r3 even，u>=2511，显然更大。

综上：

\[
\boxed{M=uv\ge621.}
\tag{8}

---

## 4. immediate denominator cap

complement height：

\[
MD/T^2<10001.
\]

所以

\[
\boxed{
D<\frac{10001}{621}T^2<17T^2.}
\tag{9}

这应替换 `deep-2high-denominator-cap.md` 中 w=1 仅用独立 minima 得到的 `159T^2`；真正 joint cap 是 17。

---
