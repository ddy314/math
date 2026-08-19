# A2 q-denominator inert carrier 与 descendant common support 完全分离

> **依赖：** `spontaneous-denominator-depth-matrix.md`、`endpoint-lattice.md` §§16.71–16.73、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descent-overlap-nogo.md`。
>
> **严格状态：**完整 q-saturation 中，additive denominator carrier由 `K^2-26` 读取，third-block saturation给 `2a_3+9T=0`，而 canonical square-side allocation对每个 q-prime无条件给 `N=DK`。本文把这三条 first-layer关系代入 descended common equation `F63^(16)`；它塌成 `-K(31K+144)`。与 `K^2-26` 的 resultant只有 `2,5,17`，其中唯一 odd non-5 prime `17` 为 `1 mod4`。因此整个 genuine non-3 inert q-denominator carrier与 `Rstar_63/Dhat_63` common support完全不相交，包括旧 fixed `11,23` special branches。本文是 complete support separation lemma，不关闭 A2。

---

## 1. q-denominator carrier data

固定 genuine non-`3` inert prime `p` 属于 saturated q-denominator additive carrier。于是存在

\[
p^e\Vert q,
\qquad
p^e\mid\mathscr L_{23},
\qquad e\ge1.
\]

其中

\[
\mathscr L_{23}=\frac{9T}{2}+a_3.
\]

所以 first layer有

\[
\boxed{2a_3+9T\equiv0\pmod p.}
\tag{1.1}

`spontaneous-denominator-depth-matrix.md` 给 additive q-side pure-prefix root

\[
\boxed{K^2-26\equiv0\pmod p.}
\tag{1.2}

另一方面 canonical square-side allocation在 `endpoint-lattice.md` (16.416) 对每个 q-prime、在进入 rational-root分支以前就已经给

\[
\boxed{N\equiv DK\pmod p.}
\tag{1.3}

这里

\[
N=3D-C.
\]

所有 genuine q-prime满足 `p∤D`，所以定义

\[
\delta:=C/D
\]
并由 (1.3)：

\[
\boxed{\delta\equiv3-K\pmod p.}
\tag{1.4}

该关系对 generic branch 与 fixed `11,23` 都成立；后两者只是 higher-depth budget不同，不改变 first-layer canonical allocation。

---

## 2. descendant common equation under q-saturation

若同一个 `p` 还进入 descendant common support，则

\[
p\mid\widehat{\mathscr D}_{63}
\]
并等价于

\[
p\mid F_{63}^{(16)},
\]
其中

\[
\boxed{
\begin{aligned}
F_{63}^{(16)}={}&
16(2K-9)
\{g((2K-12)T-2a_3)+5^\lambda C\}\\
&-63gTK^2.
\end{aligned}}
\tag{2.1}

对 q-prime有

\[
\gcd(p,2\cdot5\cdot gT)=1.
\]

使用

\[
gT=D5^\lambda
\]
把 (2.1) 除以 unit `gT`。由 (1.1)：

\[
\frac{F_{63}^{(16)}}{gT}
\equiv
32\delta K-144\delta+K^2-384K+432
\pmod p.
\tag{2.2}

再代入 canonical allocation (1.4)：

\[
\boxed{
\frac{F_{63}^{(16)}}{gT}
\equiv-K(31K+144)
\pmod p.}
\tag{2.3}

---

## 3. q-root and descendant root have no inert common prime

由 (1.2)，对 genuine non-`2,13` prime有 `K` 为 unit。当前关注 non-3 inert prime，因此当然可消去 `K`。若 descendant common仍成立，(2.3) 强迫

\[
\boxed{31K+144\equiv0\pmod p.}
\tag{3.1}

与 q-root联立，直接 resultant：

\[
\boxed{
\operatorname{Res}_K(K^2-26,31K+144)
=-4250
=-2\cdot5^3\cdot17.}
\tag{3.2}

所以 odd non-5 common prime只可能是

\[
p=17.
\]

但

\[
17\equiv1\pmod4,
\]
并非 inert prime。因此

\[
\boxed{
\operatorname{Supp}_{\rm inert}^{\rm gen}(q\text{-denominator carrier})
\cap
\operatorname{Supp}(G_\Delta)
=\varnothing,}
\tag{3.3}

其中

\[
G_\Delta=\gcd(\mathscr R_{63}^\star,\widehat{\mathscr D}_{63}).
\]

---

## 4. fixed `11,23` require no separate exception

旧 q-carrier audit在 higher depth中保留 fixed `11,23`：

- `11`：middle/third 双因子预算；
- `23`：third branch 与 height depth同步。

但 (1.3) 是对所有 q-prime的 canonical first-layer statement，(1.1) 与 (1.2) 在 fixed branches同样成立。因此 §§2–3 已自动包含 `11,23`。

事实上二者均不整除 (3.2) 的 resultant：

\[
11,23\nmid4250.
\]

故

\[
\boxed{
11,23\notin\operatorname{Supp}(G_\Delta)
\quad\text{when they act as q-denominator carriers}.}
\tag{4.1}

这不禁止 `11,23` 通过其它已知 prime-source label出现；这里只关闭 q-denominator → descendant-common 的复用通道。

---

## 5. consequence for descendant common parity

`spontaneous-crt-descendant-common-parity.md` 把危险 `Z=1,G_Delta=3 mod4` 的 common parity来源分为 old-pool 与 external kernel。

本文删除 entire q-denominator old-pool contribution：

\[
\boxed{
\text{q-denominator inert parity cannot be the common descendant supplier}.}
\tag{5.1}

因此 common inert parity目前可来自：

1. fixed equal-depth target labels `31/179`；
2. source-common overlap（受 `18K-55` 与 `H_S63` 的 square-root-depth双收费）；
3. f-denominator channel（尚待下一步审计）；
4. genuine endpoint-external/spontaneous common kernel。

A2 仍为 `待证`。
