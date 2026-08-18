# A2 source→common gate 的自然整数代表与 corrected transverse audit

> **依赖：** `spontaneous-source-common-gate.md`、`spontaneous-source-equal-depth-nogo.md`、`spontaneous-source-saturation-parity.md`、`spontaneous-source-prefix-simple.md`。
>
> **严格状态：**本文把 source→additive-common 的 first-layer gate `C_src(x,tau)` 精确乘回真实 denominator defect，并审计其 singular bad reduction。旧版 transverse checker 曾在 `F_p[epsilon]/(epsilon^3)` 中把 singular residue 当成精确零点，因而漏掉真实整数 representative 的 `p`-adic carry `C_src(x0,tau0)/p`；本文修正这一点。修正后，唯一 singular prime `p=1746991` 在 source half-depth `h>=2` 仍严格死亡，但 `h=1` 不死亡：二阶 full-system equation恰留下两个 normalized transverse templates `D=+-16651 mod p`。因此不存在沿 source half-depth 无界增长的 singular tree，但浅层 `h=1` 仍需继续审计。A2 仍未全局关闭。

---

## 1. source→common first-layer quadratic

在 source first layer

\[
d:=225x^2-y=0,
\qquad
\Phi_s=(99x-4)r_s-2x-4=0,
\]
有

\[
y=225x^2,
\qquad
r_s=\frac{2(x+2)}{99x-4}.
\]

把 `Theta_dec=0` 恢复出的第三分子代回 exact sphere 后，清分母 numerator 精确为

\[
-x^2(25x^2+1)\mathcal C_{\rm src}(x,\tau)^2,
\qquad \tau=10^{-M},
\tag{1.1}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal C_{\rm src}(x,\tau)
={}&440(x+2)^2\tau^2\\
&+81(9401x^4-2392x^3-1600x^2-64x-64)\tau\\
&-324x(99x-4)(25x^2+1)(49x^2-4x-2).
\end{aligned}}
\tag{1.2}
\]

对 genuine source prime，`x(99x-4)(25x^2+1)` 均为单位，所以 source-supported angle prime进入 additive common first layer 必须且只需满足

\[
\boxed{\mathcal C_{\rm src}(x,10^{-M})\equiv0\pmod p.}
\tag{1.3}
\]

---

# 第一部分：自然整数代表

## 2. defect integerization

令

\[
F:=5^{M-1},
\qquad E:=2^{M-1},
\qquad
x=\frac{F+H}{10F},
\qquad
\tau=\frac1{10EF}.
\]

则

\[
10E^2F^6\,(10000\mathcal C_{\rm src})
=\mathcal K_{\rm src}(H,E,F),
\tag{2.1}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal K_{\rm src}
={}&4400F^2(H+21F)^2\\
&+81EF\mathcal P_4(H,F)\\
&-810E^2(H+F)(99H+59F)\\
&\qquad\cdot(H^2+2HF+5F^2)(49H^2+58HF-191F^2),
\end{aligned}}
\tag{2.2}
\]

\[
\boxed{
\begin{aligned}
\mathcal P_4(H,F)
={}&9401H^4+13684H^3F-175354H^2F^2\\
&-418156HF^3-878519F^4.
\end{aligned}}
\tag{2.3}
\]

对 genuine `p!=2,5`，`E,F` 为单位，因此作为 first-layer projected gate：

\[
\boxed{p^k\mid\mathcal C_{\rm src}
\iff p^k\mid\mathcal K_{\rm src}.}
\tag{2.4}
\]

注意：`C_src` 是限制在 `d=Phi_s=0` slice 后得到的投影。式 (2.4) **不能**单独读取 full higher source/common system 的 transverse depth；后文显式保留 `d,Phi_s`。

---

# 第二部分：projected singular bad set

## 3. fixed bad primes

把 `C_src` 看成 `tau` 的 quadratic：

\[
\Disc_\tau(\mathcal C_{\rm src})=81\mathcal D_{\rm sc}(x),
\tag{3.1}
\]

\[
\begin{aligned}
\mathcal D_{\rm sc}(x)={}&8012458881x^8-332013104x^7+1027170624x^6\\
&+111485312x^5+130846848x^4+25281536x^3\\
&+12020736x^2+888832x+331776.
\end{aligned}
\tag{3.2}
\]

其 `x`-判别式精确分解：

\[
\boxed{
\Disc_x(\mathcal D_{\rm sc})
=2^{96}3^55^4 11^4 101^{24}\cdot109\cdot233
\cdot1746991\cdot405504443^2.}
\tag{3.3}
\]

所以 genuine non-`3` inert projected singularity 只需审计

\[
11,\quad1746991,\quad405504443.
\]

- `p=11`：`dC/dtau` 在 `F_11` 无根，因此无 finite singular projection；
- `p=405504443`：`gcd(D_sc,D_sc')` 是一个在 `F_p` 无根的二次式；
- 只剩
  \[
  \boxed{p=1746991.}
  \]

该 prime 唯一 genuine singular residue为

\[
\boxed{x_0=1362653,\qquad \tau_0=807263\pmod p.}
\tag{3.4}
\]

且

\[
\mathcal C_{\rm src}
=\partial_x\mathcal C_{\rm src}
=\partial_\tau\mathcal C_{\rm src}=0\pmod p.
\tag{3.5}
\]

所有 source/noncentral denominator factors均为单位。

---

## 4. projected gate 本身不能升到 `p^2`

取 (3.4) 的最小非负整数 representatives。直接 exact evaluation：

\[
\boxed{
\frac{\mathcal C_{\rm src}(x_0,\tau_0)}p
\equiv1642591\not\equiv0\pmod p.}
\tag{4.1}
\]

因为两个一阶 projected derivatives 都被 `p` 整除，任意

\[
x=x_0+pX,\qquad\tau=\tau_0+pT
\]
仍满足

\[
\boxed{v_p(\mathcal C_{\rm src})=1.}
\tag{4.2}
\]

这只证明 `d=Phi=0` 的 projected gate不能自己升到 `p^2`，**并不**排除 source transverse correction。

---

# 第三部分：corrected transverse audit

## 5. source equal-depth coordinates

若

\[
p^{2h}\Vert\sigma,\qquad h\ge1,
\]
且进入唯一可能产生 angle extra 的 equal-depth shell，写

\[
\varepsilon=p^h,
\qquad
d=\varepsilon D,\quad D\in\mathbf Z_p^\times,
\]

\[
\Phi_s=\varepsilon^2\phi,
\qquad
r_s=\frac{2(x+2)+\varepsilon^2\phi}{99x-4}.
\tag{5.1}
\]

angle extra-lift唯一给

\[
\phi\equiv
\frac{8(x+2)}{50625(99x-4)x^5}D^2\pmod p.
\tag{5.2}
\]

在 `p=1746991,(x_0,tau_0)` 上：

\[
\boxed{\phi\equiv1007439D^2\pmod p.}
\tag{5.3}
\]

---

## 6. exact tangency 与 valuation data

令 `S_Theta` 为用 `Theta_dec=0` 恢复第三分子后代回 sphere 的 rational residual。沿 source linear line `Phi_s=0`，在

\[
y_0=225x^2
\]
处有 exact tangency

\[
\boxed{
\left.\partial_y\mathscr S_\Theta\right|_{y=y_0}
=\mathcal C_{\rm src}(x,\tau)
\frac{\mathcal P_d(x,\tau)}
{23328(x+2)^4(50x^2+2-\tau)^3}.}
\tag{6.1}
\]

在 singular residue (3.4)，不仅 `C_src=0 mod p`，对应 `P_d` 也被 `p` 整除；exact integer/rational evaluation 给出：

\[
\boxed{
\begin{array}{c|c|c}
\text{coefficient}&v_p&\text{normalized residue}\\ \hline
\mathscr S_\Theta|_{d=\Phi=0}&2&572710\\
\partial_d\mathscr S_\Theta|_0&2&707577\\
\frac12\partial_d^2\mathscr S_\Theta|_0&0&32070\\
\partial_{\Phi}\mathscr S_\Theta|_0&0&1066442=-680549
\end{array}}
\tag{6.2}
\]

这里第一行就是旧 checker 漏掉的 `p`-adic carry。它来自真实整数 representative 的

\[
\mathcal C_{\rm src}(x_0,\tau_0)=p\cdot(1642591+O(p)).
\]

---

## 7. `已严格完成`：`h=1` 留下两个 transverse templates

取 `h=1`：

\[
d=pD,\qquad\Phi_s=p^2\phi.
\]

因为 projected `x,tau` 一阶修正不改变 `C_src/p mod p`，而 `partial_d S` 已有额外 `p^2`，二阶 sphere 方程精确化为

\[
\boxed{
\frac{\mathscr S_\Theta}{p^2}
\equiv572710+32070D^2-680549\phi\pmod p.}
\tag{7.1}
\]

代入 angle correction (5.3)：

\[
\boxed{
572710+286982D^2\equiv0\pmod{1746991}.}
\tag{7.2}
\]

即

\[
D^2\equiv1231223\pmod p.
\tag{7.3}
\]

而该 residue 是平方，恰有两个根：

\[
\boxed{D\equiv16651\quad\text{或}\quad1730340=-16651\pmod p.}
\tag{7.4}
\]

两根均为单位；对应 angle correction相同：

\[
\boxed{\phi\equiv987987\pmod p.}
\tag{7.5}
\]

因此旧版“`h=1` 无 lift”结论撤回。正确结论是：

\[
\boxed{
\text{the unique singular projected prime has exactly two normalized }h=1
\text{ transverse templates at second order}.}
\tag{7.6}
\]

这两条模板是否继续满足更高 common/additive depth，需要独立审计；本文不宣称它们为空。

---

## 8. `已严格完成`：`h>=2` 仍严格死亡

若 `h>=2`，由 (4.2) projected slice 的 `C_src` 始终只有一层，所以 `C_src^2` 在 sphere 中产生不可消失的 depth-2 主项，normalized residue就是 (6.2) 的 `572710`。

source transverse 项的最低可能深度为：

- linear `d`：`v_p(partial_d S)+h >= 2+h >=4`；
- quadratic `d^2`：`2h>=4`；
- `Phi_s` correction：`2h>=4`。

因此没有任何 transverse term能触及 depth `2` 主项：

\[
\boxed{
h\ge2\Longrightarrow\text{no full source/common lift at }p=1746991.}
\tag{8.1}
\]

所以 singular behavior在 source half-depth方向已经完全有界：

\[
\boxed{
\text{no singular source→common tree can persist to unbounded }h;
\text{ only the two shallow }h=1\text{ templates survive this audit}.}
\tag{8.2}
\]

---

# 第四部分：与 simple source prefix 的接口

## 9. `e`-Hensel 仍是 unit-slope

`spontaneous-source-prefix-simple.md` 给出

\[
D_{\rm src}
=\frac{9E^2}{4}(5F^2+18FH+9H^2)+9EF e,
\tag{9.1}
\]

所以 genuine source prime上

\[
\partial_eD_{\rm src}=9EF
\]
为单位。每个 `(H,M,p^h)` 只唯一确定一个 `e mod p^h`：

\[
4Fe\equiv-E(5F^2+18FH+9H^2)\pmod{p^h}.
\tag{9.2}
\]

而 `K_src` 不含 `e`，故消去 `e` 不会产生新的 residual。simple source/common frontier仍是 `(H,M)` common orbit + 唯一 `e` representative。

---

## 10. 更新后的严格 frontier

source-supported common channel目前严格分成：

1. **generic simple projected roots**：继续做 decimal/natural-representative synchronization；
2. **唯一 singular projected prime `1746991`**：
   - `h>=2` 已严格排除；
   - `h=1` 恰保留 `D=+-16651` 两个 normalized transverse templates；
3. source prefix `e` 始终是唯一 simple lift；
4. source base primary `p^{2h}` 对 angle parity仍为偶深。

因此下一步不应再做 projected singular-discriminant hunting。最具体的新任务是：对 `p=1746991,h=1,D=+-16651,phi=987987` 做下一层 full endpoint/common compatibility，或回到 generic simple `(H,M)` orbit的 natural representative。