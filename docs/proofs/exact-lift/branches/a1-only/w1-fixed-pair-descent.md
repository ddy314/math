# A1 minimal diagonal: `w=1` fixed-pair descent on the top 2-high endpoint

> 日期：2026-08-21。依赖当前分支 README 中的 `w=1` joint endpoint、`deep-double-2high-master`、`deep-2high-mod8-lock`、`deep-2high-mod5-lock`、`deep-contact-mandatory3-lock` 与 `deep-contact-sign-window`。当前统一范围 `k=g>=32`。

本文继续处理已经缩成

\[
\boxed{w=1,\qquad D/T^2\ge12,\qquad (u,v)=(27,23)}
\]

的 double-deep top endpoint。这里

\[
T=10^k,
\qquad
D=2^{2k+3+\eta}5^B,
\qquad
Y=B+\nu_5<k+1,
\]

\[
d=k+1-Y>0,
\qquad
c=k+1+\eta+\nu_2,
\qquad
\alpha\beta=r_{10}.
\]

前一层已经严格得到

\[
\boxed{k\equiv19\text{ or }52\pmod{99}}.
\]

本文的主要新结论是：

\[
\boxed{v_2(m)=2,}
\qquad
\boxed{r_{10}\equiv1\pmod8,}
\qquad
\boxed{\left(\frac{r_{10}}5\right)=-1,}
\]

以及真正改变高度量级的

\[
\boxed{Y<0.139k+7,}
\qquad
\boxed{d>0.861k-6.}
\]

因此该 top endpoint 的 5-low depth 已从旧的 `Y<k+1` 压到只有约 `0.139k`；同时 `eta` 被推到极深 pure-2 区：

\[
\boxed{\eta>4.321k-16.}
\]

状态：**已严格完成（作为必要条件压缩；尚未排除整个 fixed-pair branch）。**

---

## 1. fixed coefficient equation 的完整参数化

endpoint master equation为

\[
\boxed{54\beta-23\alpha=5^d.}
\tag{1}
\]

模 23：

\[
54\beta\equiv5^d\pmod{23}.
\]

因为 `54=8 mod 23` 且 `8^{-1}=3 mod 23`，存在唯一整数 `m` 使

\[
\boxed{\beta=3\cdot5^d+23m.}
\tag{2}
\]

代回 (1)：

\[
\boxed{\alpha=7\cdot5^d+54m.}
\tag{3}
\]

所以

\[
\boxed{
r_{10}=\alpha\beta
=(7\cdot5^d+54m)(3\cdot5^d+23m).}
\tag{4}
\]

又 `alpha,beta` 都是 5-adic units。由 (2)-(3) 模 5：

\[
\alpha\equiv4m,
\qquad
\beta\equiv3m\pmod5,
\]

故

\[
\boxed{5\nmid m.}
\tag{5}
\]

---

## 2. 第二条 master equation 化成单个近整关系

这里

\[
s=\frac{b_1}{27}
=\frac{10^{2k+1}-1}{27}.
\]

已有 `k=8 mod 11`。因此 `2k+1=17 mod 22`，而

\[
10^{17}\equiv17\pmod{23}.
\]

于是

\[
s\equiv\frac{16}{27}\equiv4\pmod{23},
\]

从而

\[
23\mid5s+3.
\]

定义

\[
\boxed{
R:=\frac{5s+3}{23}
=\frac{5\cdot10^{2k+1}+76}{621}
=\frac{50T^2+76}{621}.}
\tag{6}
\]

endpoint supply equation

\[
5^{d+1}s+\beta=23\cdot2^c n_0
\]

代入 (2) 后，除以 23 得

\[
\boxed{5^dR+m=2^c n_0.}
\tag{7}
\]

这是 fixed-pair branch 的核心一维方程。

---

## 3. top endpoint 自动落在极深 pure-2 side

因为 double-deep 且 5-low，

\[
B\le Y<k+1,
\]

故

\[
B\le k.
\]

另一方面

\[
\delta:=\frac D{T^2}
=2^{3+\eta}5^{B-2k}\ge12.
\]

所以

\[
2^\eta
\ge\frac{12}{8}5^{2k-B}
\ge\frac32 5^k
>2^k.
\]

因此

\[
\boxed{\eta>k.}
\tag{8}
\]

特别地

\[
\boxed{c=k+1+\eta+\nu_2>2k+1.}
\tag{9}
\]

所以当前 `D/T^2>=12` 条带完全属于旧 `eta>0` pure-2 extreme side；这里没有 moderate state。

---

## 4. 参数 `m` 的精确 2-adic 阶

由 (6)，因为 `k>=32`：

\[
50T^2\equiv0\pmod8,
\qquad76\equiv4\pmod8,
\]

而 621 为奇数，所以

\[
\boxed{v_2(R)=2.}
\tag{10}
\]

(7) 的右侧被 `2^c` 整除，且 `c>2`。因此 `5^dR` 与 `m` 必须先在精确的 2-adic depth 2 相消；否则和的 2-adic 阶只能是两者较小者。故

\[
\boxed{v_2(m)=2.}
\tag{11}

更完整地，(7) 给 growing congruence

\[
\boxed{m\equiv-5^dR\pmod{2^c}.}
\tag{12}
\]

这里 (12) 只是 stripped master equation 本身的重写，不把旧 Hensel dependency 当作额外独立 obstruction。

---

## 5. `r_10` 的新 mod-8 / mod-5 固定类

由 (11)：

\[
m\equiv4\pmod8.
\]

若 `d` 偶，则

\[
\alpha\equiv\beta\equiv7\pmod8;
\]

若 `d` 奇，则

\[
\alpha\equiv\beta\equiv3\pmod8.
\]

两种情况都给

\[
\boxed{r_{10}=\alpha\beta\equiv1\pmod8.}
\tag{13}
\]

模 5，(5) 与 (2)-(3) 给

\[
r_{10}\equiv(4m)(3m)\equiv2m^2\pmod5.
\]

任意 5-adic unit square模 5 为 `1` 或 `4`，故 `2m^2` 为 `2` 或 `3`。因此

\[
\boxed{
\left(\frac{r_{10}}5\right)=-1.}
\tag{14}
\]

把 (13) 代回已有 master mod-8 lock，在 `w=1`、`Q=7 mod 8` 时得到

\[
\boxed{N_2\equiv5^{B+1}\pmod8.}
\tag{15}
\]

把 (14) 代回已有 mod-5 Legendre lock，则

\[
\boxed{
\left(\frac{N_5}{5}\right)=(-1)^\eta.}
\tag{16}
\]

对 odd `w=1` 又有 `eta mod2=v_2(N) mod2`，所以 (16) 也可写成

\[
\boxed{
\left(\frac{N_5}{5}\right)=(-1)^{v_2(N)}.}
\tag{17}
\]

(15)-(17) 是新的 prefix filters；本文不把它们误称为已经产生矛盾。

---

## 6. mod-3 再锁定 `eta+B` parity

先记录 `a_1` 的模 3 形式。minimal diagonal 有

\[
a_1
=10^{3k+2}+(5-z-w)10^{k+1}+j,
\qquad
N_0=j-T+1.
\]

模 3 中 `T=10^k=1`，所以

\[
\boxed{a_1\equiv N_0-z-w\pmod3.}
\tag{18}
\]

当前 `w=1`：

- `z=1` 时 `a_1=N_0+1 mod3`，而 `3|b_1` 与 `gcd(a_1,b_1)=1` 排除 `N_0=2 mod3`；
- `z=3` 时 `a_1=N_0-1 mod3`，同理排除 `N_0=1 mod3`。

所以原 contact-square mod-3 argument 在两个 `w=1` 类型都处于 unit case，并给

\[
\boxed{
r_{10}\equiv-(-1)^{\eta+B}(N_0+1)\pmod3.}
\tag{19}
\]

另一方面 (2)-(3) 给

\[
r_{10}\equiv-(-1)^d m\pmod3.
\tag{20}
\]

令

\[
S:=(-1)^{\eta+B}.
\]

由 (19)-(20)：

\[
(-1)^d m\equiv S(N_0+1)\pmod3.
\tag{21}
\]

把 (7) 模 3，并乘 `(-1)^d`：

\[
R+(-1)^dm
\equiv(-1)^{c+d}n_0\pmod3.
\]

现有 master definitions 给

\[
(-1)^{c+d}n_0\equiv S N_0\pmod3.
\]

代入 (21) 后，`N_0` 消去：

\[
\boxed{R\equiv-S\pmod3.}
\tag{22}
\]

又由 `v_3(2k+1)=1`，二项展开 `10=1+9` 给

\[
s=\frac{10^{2k+1}-1}{27}
\equiv\frac{2k+1}{3}\pmod3.
\]

且由 (6) `R=s mod3`。于是：

- `k=19 mod99` 时 `k=1 mod9`，故 `R=1 mod3`；
- `k=52 mod99` 时 `k=7 mod9`，故 `R=-1 mod3`。

结合 (22)：

\[
\boxed{
\begin{array}{c|c}
k\bmod99&\eta+B\bmod2\\ \hline
19&1\\
52&0
\end{array}}
\tag{23}
\]

这是 fixed pair 上新的短周期 parity lock。

---

## 7. normalized scale 把 `m/5^d` 压进绝对常数区间

令

\[
\boxed{x:=\frac m{5^d}.}
\]

由 (2)-(4)：

\[
\boxed{
\frac{r_{10}}{25^d}
=(7+54x)(3+23x).}
\tag{24}
\]

另一方面 master identities 给

\[
\boxed{
\delta\xi
=200\frac{r_{10}}{25^d}.}
\tag{25}
\]

当前 `delta>=12`，且 universal `xi>196000`，所以右侧对应的 product 大于 `11760`。由于 `alpha,beta>0` 且 (24) 在允许区间严格递增，得到

\[
\boxed{x>0.}
\tag{26}
\]

再用

\[
\delta<\frac{10001}{621},
\qquad
\xi<15,214,000,
\]

有

\[
(7+54x)(3+23x)
<\frac{10001}{621}\frac{15,214,000}{200}.
\]

而

\[
(7+54\cdot32)(3+23\cdot32)
=1,282,165
\]

严格大于右侧，因此

\[
\boxed{0<x<32.}
\tag{27}
\]

按 typewise contact lower/upper window 还能继续缩小 (27)，但下面的统一高度结论只需要这个粗绝对区间。

---

## 8. 一个深度 `2k+1` 的精确 2-adic remainder

把 (7) 乘 621，并使用

\[
621R=50T^2+76:
\]

\[
\boxed{
621m+76\cdot5^d
=621\cdot2^c n_0-50\cdot5^dT^2.}
\tag{28}
\]

右侧第一项的 2-adic 阶为 `c`，第二项的 2-adic 阶精确为

\[
1+2k.
\]

由 (9)，`c>2k+1`，所以两项赋值严格不同。因此

\[
\boxed{
v_2(621m+76\cdot5^d)=2k+1.}
\tag{29}
\]

特别地存在正奇数 `H` 使

\[
\boxed{
621m+76\cdot5^d=2^{2k+1}H.}
\tag{30}
\]

注意 (29) 是由 fixed-pair equation 与 top-strip scale 推出的 exact valuation；没有把依赖审计中已经降级的 Hensel square 当作新输入。

---

## 9. 5-low 高度从 `k` 量级降到 `0.139k`

由 (27)：

\[
621m+76\cdot5^d
=5^d(621x+76)
<5^d(621\cdot32+76).
\]

即

\[
2^{2k+1}
\le2^{2k+1}H
<19948\cdot5^d.
\tag{31}
\]

所以

\[
d>
(2k+1)\log_5 2-\log_5(19948).
\]

使用

\[
d=k+1-Y
\]

得到

\[
Y
<\bigl(1-2\log_5 2\bigr)k
+1-\log_5 2+\log_5(19948).
\tag{32}
\]

数值上

\[
1-2\log_5 2
=0.1386468838\ldots,
\]

\[
1-\log_5 2+\log_5(19948)
=6.7210886\ldots.
\]

因此可取整洁 safe bound

\[
\boxed{Y<0.139k+7.}
\tag{33}
\]

等价地

\[
\boxed{d>0.861k-6.}
\tag{34}
\]

这比原 master 的 `Y<k+1` 是数量级上的收缩。

---

## 10. pure-2 excess 同时被推到 `4.321k` 以上

由 `B<=Y` 与 (33)：

\[
B<0.139k+7.
\]

而 `delta>=12` 给

\[
2^\eta
\ge\frac32 5^{2k-B}
>\frac32 5^{1.861k-7}.
\]

所以

\[
\eta
>1.861\log_2(5)\,k
+\log_2(3/2)-7\log_2(5).
\]

右侧严格大于 `4.321k-16`，故

\[
\boxed{\eta>4.321k-16.}
\tag{35}
\]

于是

\[
\boxed{c>5.321k-15+\nu_2.}
\tag{36}
\]

fixed pair 因而同时具有：

- 很浅的 5-height `Y<0.139k+7`；
- 很深的 pure-2 excess `eta>4.321k-16`；
- growing congruence `m=-5^dR mod 2^c`，其深度超过约 `5.321k`。

---

## 11. first remainder 的显式 fixed-pair 形式

在 double-deep 中 `lambda=1`，first remainder满足

\[
621DN_0=1000T^3+R_1.
\]

由 (7) 与 `N_0=2^{\nu_2}5^{\nu_5}n_0` 可直接化简为

\[
\frac{621DN_0}{T^3}
=1000+\frac{20(621x+76)}{T^2}.
\]

因此

\[
\boxed{R_1=20T(621x+76).}
\tag{37}
\]

原 `14300T<R_1<390100T` 的一般窗口，在 fixed pair 中已被参数 `x=m/5^d` 完全显式化。

这给后续两个自然入口：

1. 把 typewise `Gamma/xi` window 继续塞入 (24)、(37)，进一步缩短 `x`；
2. 利用 (12)、(29)、(33)-(36) 研究显式 `R` 的超深二进近整，而不重复使用已知依赖的 contact Hensel lock。

---

## 12. 可复核脚本

对应研究核对：

```bash
uv run python scripts/exact-lift/a1-only/research-checks/deep-denominator/check_w1_joint_endpoint_periods.py
uv run python scripts/exact-lift/a1-only/research-checks/deep-denominator/check_w1_fixed_pair_local_locks.py
uv run python scripts/exact-lift/a1-only/research-checks/deep-denominator/check_w1_fixed_pair_height_collapse.py
```

这些脚本只核对短周期、局部剩余类与数值常数；本文的无界结论来自上面的整数恒等式与严格估值比较。
