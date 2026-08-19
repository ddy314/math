# A2 source parity reuse 与 `O/J` cross-pair 的 pure-length projection

> **依赖：** `spontaneous-source-parity-collision-gate.md`、`source-discriminant.md`、`spontaneous-height-parity-ledger.md`、`spontaneous-residual-parity-doubling.md`。
>
> **严格状态：**本文审计 source odd/odd parity reused prime进一步命中 angle/additive cross-pair `O_± / J_H` 的必要条件。source collision先固定 `18K-55=0`，source discriminant再把 third denominator从 angle sheet消掉，得到 third-free平方 gate。与 `J_H=0` 对 `B` 消元后，resultant精确分成两个固定八次 pure-length polynomials `Phi_1(N),Phi_2(N)`；真实 cross-pair overlap只能命中 `Phi_1(10^M)Phi_2(10^M)=0 mod r`。随后完整审计 projection 的 repeated roots：所有 genuine singular candidates除 fixed `67` 的两个 simple full states外都为 boundary、非 decimal orbit或在 `p^2` linearization时死亡。因此该 cross-pair没有 hidden singular Hensel tree，只剩 simple decimal-exponent synchronization。本文不排除 simple roots，故不关闭 A2。

---

## 1. source-reuse equations

固定 genuine source odd/odd reused inert prime `r`，处在 unit-separated sector。已有

\[
\boxed{r\mid18K-55,}
\tag{1.1}

以及

\[
\boxed{r\mid\mathscr D_W=55z^2-49c_u^2.}
\tag{1.2}

source ratio为

\[
\frac z{c_u}=\frac{TQ}{b_3}.
\]

因此 (1.2) 乘去单位分母给

\[
\boxed{55T^2Q^2-49b_3^2\equiv0\pmod r.}
\tag{1.3}

另一方面 angle sheets为

\[
\mathcal O_\pm=T\mathcal U_\Omega\pm2A^2Qb_3,
\]

\[
\mathcal U_\Omega=(45B^2-2AN)^2-A^2B(99B-4N).
\]

若 `r|O_±`，平方并使用 (1.3)：

\[
T^2\mathcal U_\Omega^2
=4A^4Q^2b_3^2
\equiv\frac{220}{49}T^2A^4Q^4.
\]

因为 `r` 与 `7T` 分离，在 genuine reused sector得到 third-free gate

\[
\boxed{
\mathcal X_{OJ}
:=49\mathcal U_\Omega^2-220A^4Q^4
\equiv0\pmod r.}
\tag{1.4}

该 gate同时覆盖 `O_+` 与 `O_-`；此处只作必要 projection，不把平方后的额外 roots误当成充分条件。

---

## 2. impose the source collision linear sheet

由 (1.1)：

\[
K=9N+10A\equiv\frac{55}{18}\pmod r.
\]

在 polynomial elimination中因此代入

\[
\boxed{A=\frac{55-162N}{180}.}
\tag{2.1}

additive height companion为

\[
\boxed{
\mathcal J_H
=B^2(5K^2-36K+55)-Q^2N_0,}
\tag{2.2}

\[
Q=B+2N,
\qquad
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\]

若 cross-pair residual `J^circ` 被 `r` 整除，则 raw `J_H` 当然也被 `r` 整除。因此 genuine `O/J` cross-pair overlap必须满足

\[
\mathcal J_H=0,
\qquad
\mathcal X_{OJ}=0
\pmod r
\]
在 (2.1) 的 linear sheet上。

---

## 3. exact resultant factorization

把 (2.1) 代入 `J_H,X_OJ` 并清去有理分母，得到整数 polynomials

\[
J_*(B,N),\qquad X_*(B,N).
\]

直接对 `B` 求 resultant：

\[
\boxed{
\operatorname{Res}_B(J_*,X_*)
=C\,N^8(162N-55)^8\Phi_1(N)\Phi_2(N),}
\tag{3.1}

其中

\[
C=2^{28}3^{38}5^{16}7^4.
\tag{3.2}

两个 primitive octics为

\[
\boxed{\begin{aligned}
\Phi_1(N)={}&
152356364573249030359104N^8
-4097103068832023796480N^7\\
&+31384125262928360244960N^6
+18803025591118547565600N^5\\
&+2075376150266128766100N^4
+1943181330646900509000N^3\\
&+675406005318781110000N^2
-26358539660104162500N\\
&+244063541277015625,
\end{aligned}}
\tag{3.3}

\[
\boxed{\begin{aligned}
\Phi_2(N)={}&
40095472108377374070575040576N^8
+30284848824599488024870272000N^7\\
&+13738744691885641990863011040N^6
+4454752959867937104210016800N^5\\
&+1029832152338324301433146900N^4
+174239977384696722571611000N^3\\
&+19756759606772961743190000N^2
+621005812442557377412500N\\
&+5763793275102412515625.
\end{aligned}}
\tag{3.4}

`r` 为 odd/odd source reused prime。此前 `r=7` 不能承担 `D_W` odd parity，且 genuine sector排除 `2,3,5`，所以 `r∤C`。

`N=0` 为 decimal boundary；`162N-55=0` 等价于 `A=0` boundary。故 genuine overlap必要满足

\[
\boxed{
r\mid\Phi_1(N)\Phi_2(N).}
\tag{3.5}

真实 `N=10^M` 给 pure-length orbit

\[
\boxed{
r\mid\Phi_1(10^M)\Phi_2(10^M).}
\tag{3.6}

---

## 4. real-root audit: this is genuinely modular

令

\[
t:=162N-55.
\]

将 `N=(t+55)/162` 代入两个 octics并取 primitive numerator，得到的两个 degree-8 polynomials所有 coefficients均严格为正：

\[
\begin{aligned}
\widetilde\Phi_1(t)={}&104060401t^8+45333244000t^7+9201937926610t^6\\
&+1180976579420000t^5+105532829497813025t^4\\
&+6674082653480000000t^3+294411604662340000000t^2\\
&+8234566912000000000000t+107049369856000000000000,
\end{aligned}
\tag{4.1}

\[
\begin{aligned}
\widetilde\Phi_2(t)={}&3042830185641t^8+1711170805406040t^7\\
&+428435775972099610t^6+62469041502406486200t^5\\
&+5807836796958184695025t^4+352850034535729704600000t^3\\
&+13688106402633420340000000t^2\\
&+309923322789674880000000000t\\
&+3130230623959296000000000000.
\end{aligned}
\tag{4.2}

真实 endpoint有 `t=162N-55>0`，所以两者在实数上都严格为正。cross-pair contact只能来自 modular wrapping，不存在 real near-root解释。

---

## 5. repeated-root candidate audit

对 `Phi_1,Phi_2` 的 discriminants做 exact factorization，再限制到 source-reuse compatibility

\[
r\equiv3\pmod4,
\qquad
\left(\frac{55}{r}\right)=1,
\]
且排除 `2,3,5,7,11` unit exceptions后，finite repeated-root候选只需审计

\[
\boxed{19,23,67,367,8971,102251,630451,136776907.}
\tag{5.1}

逐一结果如下。

### `19`

唯一 full `J_*=X_*=0` state在 repeated `N=15` 上给

\[
B=0\pmod{19}.
\]

但 `B=2^{M+m+1}c_ug`，而 source discriminant与 `c_u,g` 的 non-fixed support分离，所以 reused `19` 必有 `19∤B`。该 state nongenuine。

### `23`

projection gcd为

\[
N^2+3N+11,
\]
在 `F_23` 无根，因此没有 finite repeated state。

### `367`

唯一 repeated root为

\[
N=0,
\]
是 boundary。

### `136776907`

唯一 finite repeated root为

\[
N=93550173\pmod{136776907}.
\]

而

\[
\operatorname{ord}_{136776907}(10)=7598717,
\]
且

\[
93550173^{7598717}\not\equiv1\pmod{136776907}.
\]

所以该 root不属于 decimal subgroup `〈10〉`，真实 `N=10^M` 永远不会命中。

---

## 6. the three genuine singular projection states die at `p^2`

剩余 singular candidates：

\[
8971,\qquad102251,\qquad630451.
\]

它们各自唯一的 full mod-`p` state为

\[
\boxed{(p,N,B)=(8971,8743,8433),}
\tag{6.1}

\[
\boxed{(102251,90859,35831),}
\tag{6.2}

\[
\boxed{(630451,110422,242244).}
\tag{6.3}

记 system

\[
F_1=J_*,\qquad F_2=X_*.
\]

在上述三个状态，Jacobian `d(F_1,F_2)/d(B,N)` 模 `p` 都 rank `1`。写

\[
B=B_0+pB_1,
\qquad
N=N_0+pN_1.
\]

除以 `p` 后的 augmented linear systems分别为

\[
\begin{array}{c|c}
p&(F_B,F_N\mid-F/p)\\ \hline
8971&(5124,6911\mid3110),\ (7124,6240\mid5864)\\
102251&(53480,77070\mid90010),\ (18723,47191\mid56760)\\
630451&(143149,160161\mid311616),\ (279823,277602\mid522614).
\end{array}
\tag{6.4}

逐个都有

\[
\boxed{
\operatorname{rank}(J)=1,
\qquad
\operatorname{rank}(J|b)=2.}
\tag{6.5}

因此三个 singular states全部无法 lift 到 `p^2`。

---

## 7. fixed `67` is simple, not singular

`p=67` 的 repeated projection root为

\[
N=1.
\]

full system有两个 states：

\[
\boxed{(B,N)=(53,1),(37,1)\pmod{67}.}
\tag{7.1}

对应 Jacobian determinants为

\[
\boxed{57,46\pmod{67},}
\tag{7.2}

均非零。

所以 `67` 只是两个 ordinary simple Hensel templates。它不能被本文局部排除，但不产生 singular branching。

---

## 8. strict conclusion

source odd/odd parity reused prime若进一步命中 `O/J` cross pair，则必须进入

\[
\boxed{\Phi_1(10^M)\Phi_2(10^M)=0\pmod r.}
\]

该 pure-length projection：

- 在真实正 endpoint无 real roots；
- 所有 genuine singular decimal candidates均在 boundary、subgroup filter或第一次 `p^2` lifting时消失；
- fixed `67` 只留下两个 simple templates；
- 其余 surviving roots全部属于 simple moving decimal synchronization。

所以 cross-pair overlap不再拥有 prefix/third continuous freedom，也没有 hidden singular Hensel tree。后续若要关闭它，应该研究 `10^M` 在 `Phi_1,Phi_2` simple roots上的 multiplicative orbit或 natural height，而不应继续做 discriminant singularity。

A2 仍为 `待证`。
