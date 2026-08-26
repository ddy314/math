# A1 minimal diagonal: modular-inverse lock inside the dual slot shell

> 日期：2026-08-27。依赖 `deep-2high-dual-slot-shell.md` 与 `deep-double-2high-master.md`。当前统一 frontier `k>=32`。
>
> 为避免与 contact-square 文献中的 `g=gcd(q,C)` 冲突，本文把 dual-slot supply gap 改记为
> \[
> G:=2^cn_0.
> \]

`deep-2high-dual-slot-shell.md` 写

\[
f:=5^d,
\qquad
R=mf+e,
\qquad
S=mG+e',
\]

\[
0<e<f,
\qquad
0<e'<G,
\]

并证明

\[
\boxed{eG-e'f=2r_{10}.}
\tag{1}
\]

本文指出：因为 `(f,G)=1`，(1) 已经把 `e,e'` 各自锁成唯一 modular-inverse residue。因此 dual shell 实际没有两个额外自由 fractional numerators；给定 `(f,G,r_10)` 后它们都唯一恢复。

状态：**严格完成；属于 four-factor / dual-shell 的坐标压缩，不作为独立 Hensel obstruction 重复计数。**

---

## 1. denominators 自动互素

full 2-high master 中

\[
f=5^d,
\qquad d>0,
\]

而

\[
G=2^cn_0,
\qquad (n_0,10)=1.
\]

所以

\[
\boxed{\gcd(f,G)=1.}
\tag{2}
\]

这使小行列式 (1) 可以分别模两个 denominator 完全求逆。

---

## 2. `e` 是唯一的 `mod 5^d` inverse residue

把 (1) 模 `f`：

\[
eG\equiv2r_{10}\pmod f.
\]

由 (2)，`G` 在 `mod f` 可逆，因此

\[
\boxed{
e\equiv2r_{10}G^{-1}\pmod f.}
\tag{3}
\]

又

\[
0<e<f,
\]

所以 (3) 在区间 `(0,f)` 中恰有一个代表，即

\[
\boxed{
e=\operatorname{res}_{(0,f)}
\left(2r_{10}G^{-1}\bmod f\right).}
\tag{4}
\]

因为 `(r_10,5)=1`，右侧非零，且立即有

\[
\boxed{\gcd(e,f)=1.}
\tag{5}
\]

特别地 `5\nmid e`；fractional part `e/f` 已经是既约分数。

---

## 3. `e'` 也是唯一的 `mod G` inverse residue

把 (1) 模 `G`：

\[
e'f\equiv-2r_{10}\pmod G.
\]

由 (2)：

\[
\boxed{
e'\equiv-2r_{10}f^{-1}\pmod G.}
\tag{6}
\]

配合

\[
0<e'<G,
\]

得到唯一代表

\[
\boxed{
e'=\operatorname{res}_{(0,G)}
\left(-2r_{10}f^{-1}\bmod G\right).}
\tag{7}
\]

因此 dual-slot coordinate

\[
(f,e,G,e')
\]

可严格缩成

\[
\boxed{(f,G)}
\]

再加固定 coefficient `r_10`；`e,e'` 由 (4),(7) 自动恢复。

---

## 4. exact gcd of the supply fractional numerator

因为 `f` 是 `mod G` unit，由 (6)：

\[
\boxed{
\gcd(e',G)=\gcd(2r_{10},G).}
\tag{8}
\]

写

\[
G=2^cn_0,
\qquad r_{10}\text{ odd},
\]

则

\[
\boxed{
\gcd(e',G)=2\gcd(r_{10},n_0),}
\tag{9}
\]

只要 `c>=1`。

当前 full master 实际有更强的 `c>=10`：

- moderate `eta=-a_2`，已有 `a_2=v_2(r)<=23`，故
  \[
  c=k+1-a_2+\nu_2\ge32+1-23=10;
  \]
- `eta>0` 时
  \[
  c=k+1+\eta+\nu_2\ge34.
  \]

所以 (6) 在 2-adic side 立即给

\[
\boxed{v_2(e')=1.}
\tag{10}
\]

也就是说 supply fractional numerator 永远恰含一个 factor 2。

---

## 5. reduced determinant form

令

\[
h_0:=\gcd(e',G)=\gcd(2r_{10},G),
\]

\[
e'=h_0E,
\qquad G=h_0G_0.
\]

由定义

\[
\gcd(E,G_0)=1,
\]

而 `(e,f)=1`。把 (1) 除以 `h_0`：

\[
\boxed{
eG_0-Ef=\frac{2r_{10}}{h_0}.}
\tag{11}
\]

因此

\[
\frac ef,
\qquad
\frac E{G_0}
\]

是两个既约分数，其 cross determinant 是 `2r_10` 的一个正因子。

并且

\[
\boxed{
\frac ef-\frac E{G_0}
=
\frac{2r_{10}/h_0}{fG_0}.}
\tag{12}
\]

这给 dual shell 一个标准的 reduced rational-neighbour 形式。

---

## 6. 与 exact reconstruction 联立

`deep-2high-dual-slot-shell.md` 还证明

\[
\boxed{4MG=(H+m)f+e,}
\qquad
H=20b_1+1.
\tag{13}
\]

模 `f` 看：

\[
e\equiv4MG\pmod f.
\]

再乘 `G` 并用 (3)：

\[
4MG^2\equiv2r_{10}\pmod f.
\]

所以

\[
\boxed{
2MG^2\equiv r_{10}\pmod{5^d}.}
\tag{14}
\]

这是一条 growing-depth 5-adic square congruence。

但 (14) 完全由 dual-shell / four-factor identities 推出，所以它与旧 `deep-hl-5adic-hensel-lock.md` 一样，**不能**再作为统计独立的第二个 Hensel obstruction。它的价值是把该 5-adic 信息写成 `(M,G,r_10,d)` 的非常短的 square-root interface。

---

## 7. four-factor equations 中删除 `e,e'` 自由度

原 symmetric slot equations：

\[
\begin{aligned}
4\beta u&=(m+1)f+e,\\
2\alpha v&=(m-1)f+e,\\
2\beta q&=(m+1)G+e',\\
10\alpha s&=(m-1)G+e'.
\end{aligned}
\tag{15}
\]

现在 `(4),(7)` 说明，对 fixed

\[
(\alpha,\beta,m,r_{10};f,G)
\]

右侧两个 remainder 已不需要枚举：

\[
\boxed{
\begin{aligned}
e&=[2r_{10}G^{-1}]_f,\\
e'&=[-2r_{10}f^{-1}]_G,
\end{aligned}}
\tag{16}
\]

其中 brackets 表示唯一 `0<residue<modulus` 代表。

因此后续 certificate 可以从

\[
(w,\xi,\alpha,\beta,m;f,e,G,e')
\]

进一步缩成

\[
\boxed{(w,\xi,\alpha,\beta,m;f,G).}
\tag{17}
\]

---

## 8. 与 contact-square `q^2` lifting 的接口

为避免同名，记 contact exceptional loss 为

\[
\delta_C:=\gcd(q,C),
\]

而 supply gap 始终记 `G`。

由 (15),(16)：

\[
\boxed{
q=
\frac{(m+1)G+[-2r_{10}f^{-1}]_G}{2\beta}.}
\tag{18}
\]

所以 contact-square theorem 中被平方提升的 selected factor `q`，现在是一个由 finite slot `m` 与单一 supply denominator `G` 决定的 exact modular-inverse linear form。

这是真正适合下一步 resultant / square-block analysis 的接口：后续应研究

\[
q^2/\delta_C
\]

如何进入 `L_-,L_+`，同时使用 (18) 而不是再把 `q` 当成独立 divisor variable。