# A2 source-discriminant and external double-root reduction

> **依赖：** `primitive-reduction.md`、`height-cofactor.md`，以及 `endpoint-lattice.md` 的 (16.101)、(16.424)、(16.432) 等 canonical identities。
>
> **严格状态：**本文继续处理 `height-cofactor.md` §9 留下的 endpoint-external common-prime channel。主要结果是恢复一个此前未显式列出的 source triangle，定义正的 source discriminant `D_W`，给出它与 `B_W` 的两个精确平方恒等式，并把 external double-root 从二次 Hensel 条件压成 source discriminant 与三个真实 decimal 线性代表的交点。本文仍**不宣称 A2 全局关闭**。

---

## 1. 统一记号

沿用当前 reflection endpoint：

\[
T=10^m,
\qquad
D=g2^m5^d,
\qquad
\lambda=m-d,
\]

\[
qW_q=DK-N,
\qquad
\alpha=TK+a_3=\omega W_q,
\qquad
H_0=c_uW_q.
\tag{1.1}
\]

并使用 `height-cofactor.md` 的缩写

\[
\boxed{z:=q5^\lambda.}
\tag{1.2}
\]

另有

\[
f=5^\lambda q+2c_u=z+2c_u.
\tag{1.3}
\]

本文件把 sphere scale `D` 与新的 source discriminant 区分开；后者记作 `\mathscr D_W`。

---

## 2. `已严格完成`：原拼接平面恢复出 source triangle

`endpoint-lattice.md` (16.432) 给出

\[
TN+a_3D=2^m5^dH_0.
\tag{2.1}
\]

另一方面由 (1.1)，

\[
\begin{aligned}
D\alpha-TqW_q
&=D(TK+a_3)-T(DK-N)\\
&=Da_3+TN.
\end{aligned}
\]

代入 `\alpha=\omega W_q`、(2.1) 与 `H_0=c_uW_q`：

\[
W_q(D\omega-Tq)=2^m5^dc_uW_q.
\]

`W_q>0`，故可约去：

\[
\boxed{D\omega-Tq=2^m5^dc_u.}
\tag{2.2}
\]

再除以 `2^m5^d`，利用 `D=g2^m5^d` 与

\[
\frac{T}{2^m5^d}=5^{m-d}=5^\lambda,
\]
得到新的全局整数恒等式

\[
\boxed{g\omega-q5^\lambda=c_u.}
\tag{2.3}
\]

即在 `z` 记号下

\[
\boxed{
z=g\omega-c_u,
\qquad
f=g\omega+c_u.
}
\tag{2.4}
\]

所以此前看起来独立的 `q`、`f` 两个 source endpoint，其实是同一个中心 `g\omega` 两侧的 difference/sum。

旧结果已有

\[
\gcd(g,c_u)=1,
\qquad
\gcd(\omega,c_u)=1.
\tag{2.5}
\]

故

\[
\boxed{
\gcd(g\omega,c_u)=1,
\qquad
\gcd(z,c_u)=\gcd(f,c_u)=1.
}
\tag{2.6}
\]

因为 `z,f` 都为正奇数，(2.4) 还重新恢复

\[
\boxed{\gcd(z,f)=1.}
\tag{2.7}
\]

这与旧的 `\gcd(q,f)=1` 一致，因为 `z=q5^\lambda` 且 `5\nmid f`。

---

## 3. `已严格完成`：source ratio 等于真实 denominator ratio

reflection endpoint 的 denominator formulas 为

\[
b_3=2^{M+m+1}5^dc_Qc_u,
\qquad
Q=2^{M+1}c_Qq.
\tag{3.1}
\]

乘以 `z=q5^\lambda`，并用 `d+\lambda=m`：

\[
\begin{aligned}
b_3z
&=2^{M+m+1}5^{d+\lambda}c_Qc_uq\\
&=2^{M+m+1}5^m c_Qc_uq\\
&=Tc_uQ.
\end{aligned}
\]

所以

\[
\boxed{b_3z=Tc_uQ,}
\tag{3.2}
\]

亦即

\[
\boxed{\frac z{c_u}=\frac{TQ}{b_3}.}
\tag{3.3}
\]

当前 endpoint 有 `b_3/T=w<843/1000<1`，而 `Q>1`，所以

\[
\boxed{z>c_u.}
\tag{3.4}
\]

事实上 `z/c_u>Q`，尺度分离极强。

---

## 4. `已严格完成`：正 source discriminant 与全局 inert parity supplier

`height-cofactor.md` 的二次式判别式使用

\[
49c_u^2-55z^2.
\]

由 (3.4) 它严格为负。定义正整数

\[
\boxed{
\mathscr D_W:=55z^2-49c_u^2>0.
}
\tag{4.1}
\]

`c_u,z` 都是奇数，因此

\[
\mathscr D_W
\equiv55-49
\equiv6\pmod8.
\]

于是

\[
\boxed{
\mathscr D_W\equiv6\pmod8,
\qquad
\frac{\mathscr D_W}{2}\equiv3\pmod4.
}
\tag{4.2}
\]

所以 `\mathscr D_W/2` 自身必含 `3 mod 4` 素数到奇次，并且总奇赋值 parity 为奇：

\[
\boxed{
\sum_{\substack{r\equiv3\ (4)}}
v_r(\mathscr D_W/2)
\equiv1\pmod2.
}
\tag{4.3}
\]

这提供了一个完全独立于 `\widehat{\mathcal T}_2\equiv3 (mod 4)` 的 source-side inert-prime supplier；但两者尚未证明必须使用同一个 prime，故 (4.3) 本身还不是 closure。

---

## 5. `已严格完成`：`\mathscr D_W` 与全部旧 source/denominator 因子的 overlap 固定化

由 (2.4)–(2.7) 可以直接逐模数观察 `\mathscr D_W`。

### 5.1 与 `c_u`

模 `c_u`：

\[
\mathscr D_W\equiv55z^2\pmod{c_u}.
\]

且 `\gcd(z,c_u)=1`，故

\[
\boxed{\gcd(\mathscr D_W,c_u)\mid55.}
\tag{5.1}
\]

特别地，若 `11\mid c_u`，则 `z` 为 `11`-进单位，第一项 `55z^2` 赋值恰为 `1`，而 `49c_u^2` 赋值至少为 `2`，所以

\[
\boxed{11\mid c_u\Longrightarrow v_{11}(\mathscr D_W)=1.}
\tag{5.2}
\]

若 `11\nmid c_u`，则 `11\nmid\mathscr D_W`。

### 5.2 与 `g`、`\omega`

由 `z=g\omega-c_u`，模 `g` 或模 `\omega` 都有 `z\equiv-c_u`。故

\[
\mathscr D_W
\equiv(55-49)c_u^2
=6c_u^2
\pmod g,
\]

以及同样的模 `\omega` 同余。结合 (2.5)：

\[
\boxed{
\gcd(\mathscr D_W,g)\mid6,
\qquad
\gcd(\mathscr D_W,\omega)\mid6.
}
\tag{5.3}
\]

所以任何非 `3` 的奇素数 divisor of `\mathscr D_W` 都不能来自 `g` 或 `\omega`。

### 5.3 与 `q`

因为 `z=q5^\lambda`，模 `q`：

\[
\mathscr D_W\equiv-49c_u^2\pmod q.
\]

旧 source split 给 `\gcd(q,c_u)=1`，故

\[
\boxed{\gcd(\mathscr D_W,q)\mid49.}
\tag{5.4}
\]

而且 `7`-primary 深度可以精确计价。若 `e=v_7(q)\ge1`，写
`z=7^ez_0`，其中 `7\nmid z_0c_u`。若 `e>1`，两项赋值分别至少 `4` 与恰 `2`，故 `v_7(\mathscr D_W)=2`。若 `e=1`，

\[
\frac{\mathscr D_W}{7^2}
=55z_0^2-c_u^2
\equiv-z_0^2-c_u^2\not\equiv0\pmod7,
\]

因为 `-1` 在模 `7` 下为非平方。因此统一有

\[
\boxed{7\mid q\Longrightarrow v_7(\mathscr D_W)=2.}
\tag{5.5}
\]

若 `7\nmid q`，则 (5.4) 直接给 `7\nmid\mathscr D_W`。所以 `7` 从不向 (4.3) 贡献奇 parity。

### 5.4 与 `f`

模 `f=z+2c_u` 有 `z\equiv-2c_u`，故

\[
\mathscr D_W
\equiv(220-49)c_u^2
=171c_u^2
=9\cdot19\,c_u^2
\pmod f.
\]

结合 `\gcd(f,c_u)=1`：

\[
\boxed{\gcd(\mathscr D_W,f)\mid171.}
\tag{5.6}
\]

特别地，非 `3` overlap 只可能是固定素数 `19`。而若 `19^e\Vert f`，则

\[
\boxed{
\min\{v_{19}(\mathscr D_W),e\}=1.
}
\tag{5.7}
\]

因为 `\mathscr D_W\equiv171c_u^2 (mod 19^e)`，右侧在 `e\ge2` 时赋值恰为 `1`，在 `e=1` 时截断深度也恰为 `1`。

因此，除固定素数

\[
\boxed{3,5,7,11,19}
\tag{5.8}
\]

外，`\mathscr D_W` 的奇素因子与

\[
c_u,g,\omega,q,f
\]
全部分离。对 `3 mod 4` support 而言，`7` 的深度又总为偶数，所以真正的固定 parity gates 只剩 `3,11,19`。

---

## 6. `已严格完成`：`\mathscr B_W` 也有固定全局 parity

沿用 `height-cofactor.md`：

\[
\mathscr B_W
=c_u^2(5K^2-36K+55)+z^2K^2.
\tag{6.1}
\]

当前 `b_2` 为偶数且 `\gcd(a_2,b_2)=1`，所以 `a_2` 为奇数。于是

\[
P=9\cdot10^{M-1}+a_2
\]

为奇数，故

\[
K=10P\equiv2\pmod4,
\qquad
K^2\equiv4\pmod8.
\tag{6.2}
\]

对

\[
F_W(K)=5K^2-36K+55
\]
有

\[
F_W(K)\equiv3\pmod8.
\]

又 `c_u,z` 为奇数，所以

\[
\boxed{\mathscr B_W\equiv3+4\equiv7\pmod8.}
\tag{6.3}
\]

特别地

\[
\boxed{
\sum_{\substack{r\equiv3\ (4)}}v_r(\mathscr B_W)
\equiv1\pmod2.
}
\tag{6.4}
\]

因此 source discriminant `\mathscr D_W/2` 与 cofactor resultant `\mathscr B_W` 都各自携带奇 inert parity。后续的关键不再是“供应惰性素数”，而是证明两套 parity 必须通过同一个 common-prime kernel 对齐。

---

## 7. `已严格完成`：两个精确平方恒等式

定义

\[
\boxed{A_W:=5c_u^2+z^2,}
\qquad
\boxed{L_W:=A_WK-18c_u^2.}
\tag{7.1}
\]

直接配方：

\[
\begin{aligned}
A_W\mathscr B_W
&=A_W^2K^2-36A_Wc_u^2K+55A_Wc_u^2\\
&=L_W^2+c_u^2(55z^2-49c_u^2).
\end{aligned}
\]

所以

\[
\boxed{
A_W\mathscr B_W
=L_W^2+c_u^2\mathscr D_W.
}
\tag{7.2}
\]

还有一个更适合 double-root 的 identity。由

\[
55A_W-\mathscr D_W
=324c_u^2=(18c_u)^2,
\tag{7.3}
\]
可直接展开得到

\[
\boxed{
55\mathscr B_W-K^2\mathscr D_W
=c_u^2(18K-55)^2.
}
\tag{7.4}
\]

(7.2) 是 `\mathscr B_W` 的 discriminant completion；(7.4) 则把 double-root 的公共素因子直接变成一个线性 prefix root。

---

## 8. `已严格完成`：external double-root 等价于 `18K-55` 的线性交点

设

\[
p\ne3,
\qquad
p\equiv3\pmod4,
\]
并假设

\[
p\mid\mathscr D_W,
\qquad
p\mid\mathscr B_W.
\tag{8.1}
\]

若 `p=5` 或 `11` 需单列；对 endpoint-external height prime，旧本原性已有 `p\nmid c_u`。现在固定

\[
p\notin\{3,5,11\},
\qquad p\nmid c_u.
\tag{8.2}
\]

由 (7.4)，(8.1) 立即给

\[
p\mid c_u^2(18K-55)^2.
\]

所以

\[
\boxed{p\mid18K-55.}
\tag{8.3}
\]

反过来，若 `p\mid\mathscr D_W` 且 `p\mid18K-55`，则 (7.4) 给
`55\mathscr B_W\equiv0 (mod p)`；在 (8.2) 下 `p\nmid55`，故

\[
\boxed{
 p\mid\mathscr D_W,\ p\mid\mathscr B_W
\iff
 p\mid\mathscr D_W,\ p\mid18K-55.
}
\tag{8.4}
\]

这把 `height-cofactor.md` 的 quadratic double-root 条件严格线性化。

还可检查 leading coefficient 不会同时退化。若 `p\mid A_W` 且
`p\mid\mathscr D_W`，则由 (7.3)

\[
p\mid324c_u^2,
\]

在 (8.2) 下只能 `p=3`，矛盾。因此

\[
\boxed{p\mid\mathscr D_W,\ p\ne3\Longrightarrow p\nmid A_W.}
\tag{8.5}
\]

所以这里确实是标准 quadratic double root，不存在“判别式与 leading coefficient 同时消失”的隐藏退化。

---

## 9. `已严格完成`：加入 `W_q` 后得到三个真实 decimal 线性 target

现在进一步假设 `p` 是真正的 external common height prime：

\[
p\mid W_q,
\qquad
p\mid\widehat{\mathcal T}_2,
\qquad
p\nmid qf,
\tag{9.1}
\]

并处于 discriminant-zero 子支 `p\mid\mathscr D_W`。由
`height-cofactor.md` 的 gcd bridge，`p\mid\mathscr B_W`，故 §8 给

\[
18K-55\equiv0\pmod p.
\tag{9.2}
\]

首先，`p` 不能整除 `\omega`。若 `p\mid\omega`，由 source triangle
`z=g\omega-c_u` 有 `z\equiv-c_u (mod p)`，于是

\[
\mathscr D_W
\equiv(55-49)c_u^2
=6c_u^2\not\equiv0\pmod p
\]

（`p\ne2,3` 且 `p\nmid c_u`），矛盾。因此

\[
\boxed{p\nmid\omega.}
\tag{9.3}
\]

所以 `v_p(\alpha)=v_p(W_q)`，特别地 `p\mid\alpha=TK+a_3`。利用

\[
18\alpha
=T(18K-55)+(18a_3+55T),
\]
与 (9.2)：

\[
\boxed{p\mid18a_3+55T.}
\tag{9.4}
\]

另一方面

\[
qW_q=D(K-3)+C
\]
来自 `N=3D-C`。乘以 `18`：

\[
18qW_q
=D(18K-55)+(D+18C).
\]

由 `p\nmid q`、`p\mid W_q` 与 (9.2)：

\[
\boxed{p\mid D+18C.}
\tag{9.5}
\]

因此 external double-root common prime 必落入四路交点

\[
\boxed{
 p\mid
\gcd\bigl(
\mathscr D_W,
18K-55,
18a_3+55T,
D+18C
\bigr).
}
\tag{9.6}
\]

其中后三个量全部是真实 decimal/prefix representative，而不再含 Gaussian quotient 或未命名 angle variable。

特别地模 `p`：

\[
\boxed{
K\equiv\frac{55}{18},
\qquad
\frac{a_3}{T}\equiv-\frac{55}{18},
\qquad
\frac CD\equiv-\frac1{18}.
}
\tag{9.7}
\]

于是 `J_def=N/D=3-C/D` 同样满足

\[
\boxed{J_{\rm def}\equiv K\equiv55/18\pmod p.}
\tag{9.8}
\]

---

## 10. `已严格完成`：double-root 的 prime-power 深度只有一个等深 cancellation

仍在 §8 的假设下。记

\[
b:=v_p(\mathscr B_W),
\qquad
d_s:=v_p(\mathscr D_W),
\qquad
\ell:=v_p(18K-55).
\tag{10.1}
\]

由 `p\mid\mathscr B_W` 可知 `p\nmid K`：否则 (6.1) 给
`\mathscr B_W\equiv55c_u^2 (mod p)`，与 `p\notin\{5,11\}` 矛盾。

所以 (7.4) 中 `55`、`K^2`、`c_u^2` 都是 `p`-进单位。若 `b\ne d_s`，两项赋值不同，故差的赋值就是较小者：

\[
\boxed{
\begin{aligned}
b<d_s&\Longrightarrow b=2\ell\ \text{为偶数},\\
d_s<b&\Longrightarrow d_s=2\ell\ \text{为偶数}.
\end{aligned}}
\tag{10.2}
\]

若 `b=d_s`，则两主项同深，只有一次 normalized cancellation 可继续提升，并且

\[
\boxed{2\ell\ge b=d_s.}
\tag{10.3}
\]

因此 double-root 的高阶行为不再有任意分支：

\[
\boxed{
\min\{b,d_s\}\text{ 若为奇数，必有 }b=d_s.
}
\tag{10.4}
\]

即 odd depth 只能发生在 `\mathscr B_W` 与 source discriminant **等深**后的一次 cancellation；若两者深度不同，较浅层自动为偶数。

结合 `height-cofactor.md`

\[
\min\{v_p(\widehat{\mathcal T}_2),v_p(W_q)\}
=
\min\{b,v_p(W_q)\},
\]
(10.2)–(10.4) 给出了 external common carrier 的第一条真正 higher-lift parity law。

---

## 11. `已严格完成`：固定 `23` 的 higher lift 只在深度 `2` 发生一次碰撞

`q`-side fixed intersection 的 `23` 还有一个独立的精确解释。回忆

\[
F_W(K)=(K-5)(5K-11).
\tag{11.1}
\]

在 special `23` root `2K\equiv9 (mod 23)` 下，

\[
K\equiv\frac{11}{5}\pmod{23},
\]
且 `K-5`、`5K+11` 都是 `23`-进单位。因此

\[
v_{23}(F_W(K))=v_{23}(5K-11).
\tag{11.2}
\]

关键的整数恒等式为

\[
\boxed{
25(K^2-26)
=(5K-11)(5K+11)-23^2.
}
\tag{11.3}
\]

特别地，`F_W` 的相关有理根

\[
K=\frac{11}{5}
\]
本身满足

\[
\boxed{
\left(\frac{11}{5}\right)^2-26
=-\frac{23^2}{25}.
}
\tag{11.4}
\]

所以 `11/5` 恰好已经是 `\sqrt{26}` 的模 `23^2` Hensel 近似，但不是一个真正的有理平方根。

令

\[
a:=v_{23}(5K-11).
\]

由 (11.3) 且 `5K+11` 为单位：

\[
\boxed{
\begin{aligned}
a<2&\Longrightarrow v_{23}(K^2-26)=a,\\
a>2&\Longrightarrow v_{23}(K^2-26)=2,\\
a=2&\Longrightarrow v_{23}(K^2-26)\ge2,
\end{aligned}}
\tag{11.5}
\]

最后一行的额外深度只能来自两个正规化 `23^2` 项的一次 cancellation。

这说明 special `23` 的高阶 q-prefix 行为不存在第二套无界 Hensel tree：`F_W` root 与 `\sqrt{26}` root 的差异被固定在**唯一阈值 `23^2`**。这与 `height-cofactor.md` 已证明的三对象共同深度只能一层相容，并进一步解释为什么 `23` 会作为唯一 q-height intersection 出现。

---

## 12. `已严格完成 / 审计降级`：全局 Jacobi reciprocity 不会自动闭环

(4.2) 与 (6.3) 给出

\[
\frac{\mathscr D_W}{2}\equiv3\pmod4,
\qquad
\mathscr B_W\equiv7\pmod8.
\]

看起来两边都是 odd inert parity supplier，似乎可以直接用 quadratic reciprocity 制造符号冲突。完整审计表明 generic coprime 层会精确自洽。

设

\[
D_0:=\mathscr D_W/2,
\]
并暂时假设

\[
\gcd(55\mathscr B_W,D_0)=1,
\qquad
11\nmid c_u.
\tag{12.1}
\]

由 (7.4) 模 `D_0`：

\[
55\mathscr B_W
\equiv c_u^2(18K-55)^2\pmod{D_0},
\]
所以

\[
\left(\frac{\mathscr B_W}{D_0}\right)
=
\left(\frac{55}{D_0}\right).
\tag{12.2}
\]

而由 `\mathscr D_W=55z^2-49c_u^2`，且 `5\nmid c_u`，有

\[
D_0\equiv3c_u^2\pmod5,
\qquad
D_0\equiv3c_u^2\pmod{11}.
\tag{12.3}
\]

因此

\[
\left(\frac{D_0}{5}\right)=-1,
\qquad
\left(\frac{D_0}{11}\right)=1.
\]

结合 `D_0\equiv3 (mod 4)` 的 reciprocity sign：

\[
\boxed{
\left(\frac{55}{D_0}\right)=1.
}
\tag{12.4}
\]

另一方面，由 (7.2) 模任意 `p\mid\mathscr B_W` 且 `p\nmid A_Wc_uD_0`：

\[
L_W^2\equiv-2c_u^2D_0\pmod p,
\]
故

\[
\left(\frac{D_0}{p}\right)
=
\left(\frac{-2}{p}\right).
\]

乘到整个 `\mathscr B_W`，并使用 `\mathscr B_W\equiv7 (mod 8)`：

\[
\left(\frac{D_0}{\mathscr B_W}\right)
=-1.
\tag{12.5}
\]

因为 `D_0\equiv\mathscr B_W\equiv3 (mod 4)`，二次互反律给

\[
\left(\frac{\mathscr B_W}{D_0}\right)
=-\left(\frac{D_0}{\mathscr B_W}\right)
=1,
\]
恰好与 (12.2)–(12.4) 相同。

所以

\[
\boxed{
\text{generic global Jacobi pass is an identity, not a contradiction.}
}
\tag{12.6}
\]

后续不能仅凭 `D_0,B_W` 都是 `3 mod 4` 再做一轮 Legendre/Jacobi bookkeeping；真正新信息必须来自 (9.6) 的 decimal linear representatives、(10.4) 的等深 cancellation，或固定 `3,11,19,23,7,43` 的 higher-lift gates。

---

## 13. 更新后的开放核

本轮把 `height-cofactor.md` 的 external channel 再压一层：

1. source 变量统一成
   \[
   \boxed{z=g\omega-c_u,\qquad f=g\omega+c_u};
   \]
2. 原判别式改成正整数
   \[
   \boxed{\mathscr D_W=55z^2-49c_u^2>0,\quad \mathscr D_W/2\equiv3\pmod4};
   \]
3. 除固定 `3,5,7,11,19` 外，`\mathscr D_W` 的奇素因子与 `c_u,g,\omega,q,f` 全部分离；`7` 的赋值永远为偶；
4. cofactor resultant 本身满足
   \[
   \boxed{\mathscr B_W\equiv7\pmod8};
   \]
5. double-root 精确等价于
   \[
   \boxed{p\mid\mathscr D_W,\quad p\mid18K-55};
   \]
6. 若再进入 height common channel，则还强迫
   \[
   \boxed{p\mid18a_3+55T,\quad p\mid D+18C};
   \]
7. double-root higher lift 的较浅赋值若为奇数，`\mathscr B_W` 与 `\mathscr D_W` 必须先达到同一深度；
8. special `23` 的 `F_W` root 与 `\sqrt{26}` root 只在固定阈值 `23^2` 发生一次 collision。

因此当前最值得继续推进的两个目标是：

- 对 (9.6) 求真正的 source/decimal resultant，优先利用 `C` 的自然代表 (16.101)–(16.104) 控制 `D+18C`；
- 把 (4.3)、(6.4)、`W_q/3^\delta\equiv1 (mod 4)` 三个 parity statement 接成一个 prime-flow conservation law，证明 `\widehat{\mathcal T}_2` 的 external odd carrier 必进入 `W_q` 或 `\mathscr D_W` 的 odd-depth kernel。

普通的 global Jacobi reciprocity 已由 §12 严格降级，不应再作为下一步主线。