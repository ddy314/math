# A2 spontaneous length bad-prime audit

> **依赖：** `spontaneous-angle.md`、`length-orbit.md`。
>
> **严格状态：**本文只审计 fully coupled spontaneous/external 系统的 **singular / bad-reduction Hensel gates**。两个 fixed octic 的整数判别式给出有限候选；逐个代回 discriminant character、decimal multiplicative orbit、原三方程和二阶 Hensel compatibility 后，没有任何 genuine singular Hensel tree survives。generic/simple local branches仍可能存在，所以本文**不宣称 A2 全局关闭**。

---

## 1. 两个 octic 的 discriminant

沿用 `length-orbit.md`

\[
\mathcal P_1(s),\qquad\mathcal P_2(s).
\]

精确判别式分解为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(\mathcal P_1)
={}&2^{88}3^{75}5^{38}7^{12}11^{28}13^4 23^4 89^2 101^4\\
&\cdot181^2 367^2\cdot102251\cdot630451\cdot136776907\\
&\cdot74218718085901254661^2,
\end{aligned}}
\tag{1.1}
\]

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(\mathcal P_2)
={}&2^{88}3^{101}5^{38}7^{24}11^{28}13^4 19^6 67^2 101^4 281^2\\
&\cdot8971\cdot5019481^2\cdot3833513^2\\
&\cdot833453052690874208617\\
&\cdot115850970866446584757213999^2.
\end{aligned}}
\tag{1.2}
\]

对 genuine non-`3` inert external prime，还必须有

\[
\left(\frac{55}{p}\right)=1,
\qquad p\nmid 2\cdot3\cdot5\cdot7\cdot11.
\tag{1.3}
\]

所以大部分 discriminant support 立即失去资格。下面只审计仍可能在 `F_p` 上产生 genuine bad root 的项。

---

## 2. `P_1`：三个移动 bad roots 中只有两个进入 decimal orbit，而二者都死在 `p^2`

### 2.1 `p=23`

`gcd(P_1,P_1')` 模 `23` 为

\[
s^2-3s+11.
\]

其判别式为 `11`，而

\[
\left(\frac{11}{23}\right)=-1.
\]

所以没有 `F_23` repeated length root。

### 2.2 `p=367`

唯一 repeated root 是

\[
s=0,
\]

但真实

\[
s=36\cdot10^{M-1}
\]

永远是单位，故排除。

### 2.3 `p=136776907`

唯一 repeated root 是

\[
s=8516046.
\]

这里

\[
\operatorname{ord}_p(10)=7598717,
\qquad [\mathbf F_p^\times:\langle10\rangle]=18.
\]

直接检查

\[
\left(8516046\cdot36^{-1}\right)^{7598717}
\not\equiv1\pmod p,
\]

所以该 root 不在 `36<10>` decimal orbit 中，排除。

### 2.4 `p=102251`

唯一 repeated length root

\[
s=81690
\]
确实在 decimal orbit 中。代回 `N_sp=R_spD=0` 后只有

\[
x=61220,
\qquad y=95782,
\qquad r_s=84227.
\]

它满足 q/f/source 分离条件，是 genuine 第一层解。但三方程

\[
(N_{sp},O_{sp},G_{sp})
\]
关于 `(s,x,r_s)` 的 Jacobian rank 为 `2`。写一次 Hensel 提升

\[
J\delta\equiv-\frac{F(s,x,r_s)}p\pmod p,
\]

右端不在 `J` 的像中，因此

\[
\boxed{\text{该解没有模 }102251^2\text{ 的提升}.}
\tag{2.1}
\]

### 2.5 `p=630451`

同理，repeated root

\[
s=271429
\]
在 decimal orbit 中，并恢复唯一第一层 genuine 解

\[
x=340435,
\quad y=610253,
\quad r_s=204669.
\]

Jacobian rank 同样为 `2`，二阶 Hensel compatibility 无解：

\[
\boxed{\text{不存在模 }630451^2\text{ 的提升}.}
\tag{2.2}
\]

所以 `P_1` 不留下任何 genuine singular p-adic tree。

---

## 3. `P_2`：`19` 的 bad root 非 genuine，`8971` 死在二阶，`67` 实际 nonsingular

### 3.1 `p=19`

`P_2` 的 repeated eliminant root 是

\[
s=-3\equiv16\pmod{19}.
\]

代回 `N_sp,R_spD` 的公共根只有

\[
x=0,
\]

与真实 denominator unit 条件矛盾。因此这不是 `length-orbit.md` 的 genuine `s=2` branch；后者本来就是 simple root。

### 3.2 `p=8971`

唯一 repeated root

\[
s=6356
\]
进入 decimal orbit，并恢复第一层 genuine 解

\[
x=2914,
\quad y=6787,
\quad r_s=7633.
\]

但 Jacobian rank 为 `2`，二阶 compatibility 再次失败：

\[
\boxed{\text{不存在模 }8971^2\text{ 的提升}.}
\tag{3.1}
\]

### 3.3 `p=67`

repeated length root 为

\[
s=17.
\]

它位于 decimal orbit：

\[
\operatorname{ord}_{67}(10)=33,
\qquad
36\cdot10^{32}\equiv17\pmod{67},
\]

所以

\[
M\equiv0\pmod{33}.
\]

原三方程恢复两组 genuine 解：

\[
\boxed{
(s,x,y,r_s)
=(17,53,35,63),
\quad
(17,37,35,57)
\pmod{67}.}
\tag{3.2}
\]

它们的 Jacobian determinants 分别为

\[
\boxed{32,\quad49\pmod{67},}
\tag{3.3}
\]

都非零。因此 `67` 虽是 **eliminant repeated root**，但原三方程本身完全 nonsingular；两组解各自只有一条唯一 Hensel lift。

其余 `3 mod 4` discriminant candidate 中，`7` 与巨素数

\[
115850970866446584757213999
\]
均满足

\[
\left(\frac{55}{p}\right)=-1,
\]

而 `11` 为被分离的固定 coefficient prime，故不能进入 genuine external discriminant-zero。

---

## 4. `已严格完成`：genuine singular Hensel gate 已清空

综合 §§2–3：

\[
\boxed{
\text{fully coupled spontaneous/external 系统没有 surviving genuine singular Hensel tree}.}
\tag{4.1}
\]

精确地说：

- `23`：无 `F_p` repeated root；
- `367`：只有非单位 root；
- `136776907`：root 不在 decimal orbit；
- `102251,630451,8971`：genuine 第一层解存在，但没有 `p^2` lift；
- `19` 的 repeated eliminant root：只给 `x=0`；
- `67`：两组 genuine 解，但 full Jacobian 非零，所以各自唯一提升。

因此后续不再需要为“moving singular Hensel branching”保留一个开放素数族。所有 genuine surviving local channel 都是**simple / unique lift**。

这仍不是全局空性：simple branches 可以存在到任意 p-adic depth。下一步必须使用 `C` 的自然代表、secant additive CRT、`W_q` parity 或 Archimedean size 来排除这些唯一分支，而不是继续审计 polynomial discriminant。