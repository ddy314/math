# A2 descendant transported-error overdepth 的 linear resonance 与 fixed tangent gates

> **依赖：** `spontaneous-crt-descendant-projective-depth-reader.md`、`spontaneous-crt-descendant-quotient-gate.md`、`spontaneous-crt-universal-descendant-cubic.md`、`endpoint-lattice.md` 的 exact rational-root equation。
>
> **严格状态：**linear remainder overdepth若不是 quotient-level normalized cancellation，就必须来自 upstream `E_proj` 已比 common baseline更深。本文把 `E_proj` 恢复为 exact rational-root polynomial在两个真实 errors `F_Delta,L_proj` 上的 transport，并写出其一阶项。generic 情形下，额外 `E`-depth只可能是两个 normalized residual units的一次线性 cancellation；coefficient singularity只有 `J+zeta=0` 或 rational-root tangent `Phi_J=0`。前者在 descendant first layer上回到已有 `L=K^2-576K+1296` / alpha-height `G_D` gates；后者与 universal cubic消元后仅新增一个 quadratic `H_2(K)` 与一个 irreducible decic `H_10(K)`。两者真实都为正，primitive orientations分别为 `7 mod8` 与 `5 mod8`。因此 low tangent exception自身带 odd-inert surcharge，高 tangent exception total inert parity为偶。本文尚未排除 generic normalized transport resonance，因此不关闭 A2。

---

## 1. exact transported errors

沿用真实 rational-root polynomial

\[
\boxed{
\Phi(J,R)
=J(J+2\zeta)(K-J)^2-R(J+\zeta)^2,}
\tag{1.1}

其中真实 endpoint满足

\[
\Phi(J,R)=0.
\]

两个 descendant/additive approximations为

\[
R_0=R+K^2L,
\qquad
J_0=J+\frac{F}{U},
\tag{1.2}

其中

\[
\boxed{L:=\mathscr L_{\rm proj},}
\qquad
\boxed{F:=F_\Delta,}
\qquad
\boxed{U:=2K-9.}
\]

已有 exact identity

\[
\boxed{
\mathscr E_{\rm proj}
=\frac{65536U^4}{K^8}
\left[\Phi(J+F/U,R+K^2L)-\Phi(J,R)\right].}
\tag{1.3}

在 genuine noncentral sector，前面的 scale为 p-unit。

---

## 2. first-order transported resonance

对 (1.3) 关于 `F,L` 展开。因为 constant term由 `Phi(J,R)=0` 消失，一阶项为

\[
\boxed{
\frac{\Phi_J(J,R)}U F
-K^2(J+\zeta)^2L.}
\tag{2.1}

其余每一项对 `(F,L)` 的总次数至少为2。

设

\[
f=v_p(F),
\qquad
\ell=v_p(L),
\qquad
k=\min(f,\ell)\ge1.
\]

若 coefficient均为 units：

\[
p\nmid\Phi_J(J,R)(J+\zeta)KU,
\tag{2.2}
\]
则：

- `f<ell` 时，唯一最低项来自 `F`，所以
  \[
  \boxed{v_p(E_{proj})=f;}
  \tag{2.3}
  \]
- `ell<f` 时，唯一最低项来自 `L`，所以
  \[
  \boxed{v_p(E_{proj})=\ell.}
  \tag{2.4}
  \]

因此 generic upstream overdepth只能在

\[
\boxed{f=\ell=:h}
\tag{2.5}

发生。写

\[
F=p^hF_0,
\qquad
L=p^hL_0,
\]
其中 `F_0,L_0` 为 units，则因二次项至少含 `p^(2h)`：

\[
\boxed{
 v_p(E_{proj})>h
\iff
\frac{\Phi_J}U F_0
-K^2(J+\zeta)^2L_0
\equiv0\pmod p.}
\tag{2.6}

这就是 generic transported-error normalized resonance。

---

## 3. the two coefficient-singular mechanisms

(2.1) 的系数退化只可能来自

\[
\boxed{J+\zeta\equiv0\pmod p}
\tag{3.1}

或

\[
\boxed{\Phi_J(J,R)\equiv0\pmod p.}
\tag{3.2}

`K,U` 已由 genuine/noncentral separation保证为 units。

### 3.1 `J+zeta=0`

在 exact root `Phi=0` 上，若 `J+zeta=0`，则

\[
\Phi=-J^2(K-J)^2=0.
\]

所以

\[
J=0
\quad\text{或}\quad
J=K.
\]

若 `J=0`，则 `zeta=0`。再代 descendant first-layer `F=0`：

\[
16(2K-9)^2=63K^2,
\]
即

\[
\boxed{K^2-576K+1296=0.}
\tag{3.3}

若 `J=K`，则 `zeta=-K`，所以

\[
\alpha=T(K+\zeta)=0,
\]
回到已经单列的 alpha-supported sector；`F=0` 同时给

\[
\boxed{G_D(K)=11K^2-240K+432=0.}
\tag{3.4}

因此 `J+zeta` singularity没有产生新的 generic pure-spontaneous gate。

---

## 4. rational-root tangent elimination

现在处理

\[
\Phi_J=0.
\]

在 `J+zeta` 为 unit且使用 exact `Phi=0` 消去 `R` 后：

\[
\boxed{
\Phi_J
=\frac{2(J-K)}{J+\zeta}
\left(
J^3+3J^2\zeta+3J\zeta^2-K\zeta^2
\right).}
\tag{4.1}

将 descendant first-layer substitutions

\[
J=J_0(K,\zeta),
\qquad
R=R_0(K,\zeta)
\]
代回 `Phi_J`，清去 `2K-9` denominator；再与 universal cubic

\[
\mathcal E_{63}(K,\zeta)=0
\]
关于 `zeta` 求 resultant。exact factorization为

\[
\boxed{
\begin{aligned}
\operatorname{Res}_{\zeta}
(\mathcal E_{63},\operatorname{num}\Phi_J(J_0,R_0))
={}&-2^{43}3^2(2K-9)^{13}\\
&\cdot(K^2-576K+1296)^2\\
&\cdot G_D(K)^2\\
&\cdot H_2(K)H_{10}(K),
\end{aligned}}
\tag{4.2}

其中

\[
\boxed{H_2(K)=47K^2+144K-416,}
\tag{4.3}

以及 primitive irreducible decic

\[
\boxed{
\begin{aligned}
H_{10}(K)={}&388341K^{10}-601739280K^9
+229469500800K^8\\
&+1907909697024K^7+388001070336K^6\\
&+472180427182080K^5-5611474473205760K^4\\
&+24390734431518720K^3-51182973630480384K^2\\
&+52664489116434432K-21375786688708608.
\end{aligned}}
\tag{4.4}

前三个 factors分别是已知 central、`J+zeta` zero-root、height/alpha-supported gates。故 genuine alpha-free noncentral tangent support新增的只有

\[
\boxed{H_2(K)=0\quad\text{或}\quad H_{10}(K)=0.}
\tag{4.5}

---

## 5. low tangent gate is positive primitive `7 mod 8`

因为 `K=2k_0` 且 `k_0` odd：

\[
H_2=188k_0^2+288k_0-416.
\]

第一项精确有 `v_2=2`，其它两项至少有 `v_2=5`。因此

\[
\boxed{v_2(H_2)=2.}
\tag{5.1}

除以4：

\[
\frac{H_2}{4}
\equiv47k_0^2
\equiv7\pmod8.
\tag{5.2}

当前 `K>9*10^11`，显然

\[
\boxed{H_2>0.}
\tag{5.3}

所以 low tangent singular gate自身携带 odd-inert parity surcharge。

---

## 6. high tangent gate is positive primitive `5 mod 8`

对 `H_10` 各项使用 `v_2(K)=1`。唯一最低项是 leading term：

\[
v_2(388341K^{10})=10.
\]

第二浅层已经是 `13`，故

\[
\boxed{v_2(H_{10})=10.}
\tag{6.1}

又

\[
388341\equiv5\pmod8,
\]
而 odd `k_0^{10}≡1 mod8`，因此

\[
\boxed{H_{10}/2^{10}\equiv5\pmod8.}
\tag{6.2}

正性也可完全初等地读取。对 `K>=2000`：

\[
388341K^{10}-601739280K^9>0.
\]

另外分别用 positive lower-degree terms覆盖三个剩余 negative terms：

\[
229469500800K^8>5611474473205760K^4,
\]

\[
1907909697024K^7>51182973630480384K^2,
\]

\[
472180427182080K^5>21375786688708608.
\]

其余显示项为正或不需要用于下界。因此

\[
\boxed{H_{10}>0\qquad(K\ge2000).}
\tag{6.3}

当前 endpoint远强于该条件。

所以 high tangent gate的 positive primitive part为 `5 mod8`，total inert parity为偶。

---

## 7. updated overdepth frontier

upstream `E_proj` overdepth现在严格分成：

1. generic equal-depth transported resonance (2.6)；
2. old `J+zeta` / alpha-height gates；
3. new low tangent `H_2`, positive primitive `7 mod8`；
4. new high tangent `H_10`, positive primitive `5 mod8`。

结合 Euclidean quotient theorem，same-prime recycling已被连续压成两层 normalized resonance，加上少量 fixed singular carriers；其中所有 low-degree singular escape都额外支付 odd-inert parity。

下一步最窄的 generic target是把 (2.6) 与 descendant parent depths `a_p,b_p` 直接联立，判断 unequal parent depths是否已经自动排除 transported resonance。

A2 仍为 `待证`。
