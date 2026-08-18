# A2 fixed `23` `eta=2` `c=2` 的 centered canonical root

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-centered-a3-map.md`、`spontaneous-cq-fixed23-eta2-c2-full-a3-crt.md`、`spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`。
>
> **严格状态：**令 `u=varrho*a_3`。前一文件已使 binary root `u mod2^m` 完全 source-only，而 long-5 root对 `varrho` 线性。本文证明 canonical `c_Q=1587` residue 在 centered 变量中也完全消去 `c_u,theta,g,varrho`：对完整 allocation `c_Q=c_-c_+`，有 `u=-(21/2)5^(3lambda) mod c_-` 与相反符号的 `mod c_+` root。注意 `varrho` 不是完整的 `c_Q`-unit：它被 `3` 整除、但仍是 `23`-进 unit。该事实不影响推导，因为本文在 canonical 方向只乘 `varrho`，不对它取模 `c_Q` 的逆。于是 full local data中只有 `5^(lambda-1)` coordinate仍依赖具体 source divisor；`2^m` 与 `c_Q` 两个方向均可预计算。

---

## 1. centered variable modulo `c_Q`

当前

\[
c_Q=1587=3\cdot23^2,
\qquad
S:=5^{3\lambda}+c_Qc_u,
\]

\[
g\theta=S,
\qquad
\varrho=20L_*-\theta,
\]

\[
L_*=2^{\lambda+1}5^\lambda c_u.
\tag{1.1}

exact Hensel relation为

\[
\theta=c_Q\omega-L_*.
\]
所以

\[
\boxed{\theta\equiv-L_*\pmod{c_Q}.}
\tag{1.2}

又

\[
\varrho=20L_*-\theta,
\]
故

\[
\boxed{\varrho\equiv21L_*\pmod{c_Q}.}
\tag{1.3}

source primitive separation给

\[
\gcd(L_*,c_Q)=1.
\]
因此 `theta` 是完整的 `c_Q`-unit。对 `varrho` 则必须分别读取 `3` 与 `23`：

\[
\boxed{3\mid\varrho,}
\tag{1.4a}

因为 `21L_*` 被 `3` 整除；而

\[
\boxed{23\nmid\varrho,}
\tag{1.4b}

因为 `21L_*` 是 `23`-进 unit。也就是说

\[
\boxed{\gcd(\varrho,23)=1,
\qquad 3\mid\varrho.}
\tag{1.5}

本文后续不在模 `c_Q` 下对 `varrho` 取逆，所以这一非单位性不会造成任何除法问题。

由于 `c_Q\mid b_3` 且 `\gcd(a_3,b_3)=1`，还有

\[
\boxed{3\nmid a_3.}
\tag{1.6}

故 centered variable

\[
u:=\varrho a_3
\]
自动满足

\[
\boxed{3\mid u.}
\tag{1.7}

本文暂不宣称 `v_3(varrho)=1`；更高 `3`-进深度仍可能发生。

---

## 2. `g mod c_Q` 与具体 divisor `theta` 无关

由

\[
g\theta=S
\]
模 `c_Q`：

\[
g(-L_*)
\equiv5^{3\lambda}
\pmod{c_Q}.
\]
所以

\[
\boxed{
g
\equiv
-5^{3\lambda}L_*^{-1}
\pmod{c_Q}.}
\tag{2.1}

将 `L_*` 展开也可写成

\[
\boxed{
g
\equiv
-5^{2\lambda}
(2^{\lambda+1}c_u)^{-1}
\pmod{c_Q}.}
\tag{2.2}

这里逆元合法，因为 `L_*` 与 `c_Q` 互素。于是固定 `(lambda,c_u)` 后，canonical `a_3 mod c_Q` root与具体 source divisor完全无关。

---

## 3. centered canonical root 完全消去 source content

定义

\[
\boxed{u:=\varrho a_3.}
\tag{3.1}

endpoint directed factors给

\[
a_3\equiv\frac g2\pmod{c_-},
\qquad
 a_3\equiv-\frac g2\pmod{c_+}.
\tag{3.2}

由 (1.3)、(2.1)：

\[
\varrho\frac g2
\equiv
21L_*\cdot
\frac{-5^{3\lambda}L_*^{-1}}2
\pmod{c_Q}.
\]
所以

\[
\boxed{
\varrho\frac g2
\equiv
-\frac{21}{2}5^{3\lambda}
\pmod{c_Q}.}
\tag{3.3}

把 (3.2) 乘 `varrho`，得到：

### minus canonical side

\[
\boxed{u
\equiv
-\frac{21}{2}5^{3\lambda}
\pmod{c_-}.}
\tag{3.4-}

### plus canonical side

\[
\boxed{u
\equiv
+\frac{21}{2}5^{3\lambda}
\pmod{c_+}.}
\tag{3.4+}

这里 `2` 与 `5` 在 `c_Q` 上都是 units，因此两个 residue 都良定义；若相应 modulus 含 `3`，右边自然为 `0 mod3`，与 (1.7) 一致。若相应 modulus含 `23^2`，右边则是 `23`-进 unit。

最关键的是：

\[
\boxed{
\text{centered canonical residue只依赖 }(\lambda,c_-,c_+),
\text{与 }c_u,\theta,g,\varrho\text{ 全部无关}.}
\tag{3.5}

---

## 4. full centered local system

`spontaneous-cq-fixed23-eta2-c2-centered-a3-map.md` 已给：

### binary direction

\[
\boxed{u\equiv u_2(\lambda,c_u)\pmod{2^m},}
\tag{4.1}

其中 `u_2` 是

\[
u^2+c_Qc_u u+
\frac{(5^{3\lambda}+c_Qc_u)^2}{4}
\equiv0\pmod{2^m}
\]
的唯一 odd root。

### long Gaussian direction

固定 `iota^2=-1 mod5^(lambda-1)`：

\[
\boxed{u
\equiv
-\frac{c_Qc_u}{2}
-\frac{45c_Qc_u}{2}\,
\iota\,2^{3\lambda+2}\varrho
\pmod{5^{\lambda-1}}.}
\tag{4.2}

### canonical direction

由 (3.4±) 对 `c_-,c_+` 唯一拼成

\[
\boxed{u\equiv u_Q(\lambda,c_-,c_+)\pmod{1587}.}
\tag{4.3}

因此在三个互素模数

\[
2^m,\qquad5^{\lambda-1},\qquad1587
\]
中，只有中间的 `5`-adic coordinate含具体 source divisor `varrho`，而且是线性 dependence。

---

## 5. source-divisor dependence降为单一 affine coordinate

令

\[
B:=5^{\lambda-1}.
\]
固定 `(lambda,c_u,iota)` 后定义 constants

\[
A_5:=-\frac{c_Qc_u}{2},
\]

\[
B_5:=-\frac{45c_Qc_u}{2}
\iota2^{3\lambda+2}.
\]
那么

\[
\boxed{u_{(5)}(\varrho)=A_5+B_5\varrho\pmod B.}
\tag{5.1}

而 `u mod2^m` 与 `u mod1587` 都固定。因此 full CRT representative作为 `varrho` 的函数，已经降为“固定两个 coordinates + 一个 mod-B affine coordinate”的格点轨道。

这提供了比 `a_3`-坐标更适合无界分析的形式：不再有 modular inverse dependence。

---

## 6. proof boundary

本文没有把 `u` 的 full CRT cell直接转回 third-digit interval；因为真实 Archimedean relation

\[
u=\varrho a_3
\]
中的 `varrho` 本身随 source divisor变化。当前严格收益是 local algebra的大幅简化：

\[
\boxed{
\text{divisor dependence}
\quad\text{只存在于一个 }5^{\lambda-1}\text{-adic affine coordinate}.}
\]

下一步应利用 centered real window

\[
L_*/4<\varrho<L_*/2
\]
与 `theta|S`，研究 affine orbit (5.1) 是否能进入 full canonical `a_3` cell；或把这个 affine orbit转成对 source divisor的更深 congruence。