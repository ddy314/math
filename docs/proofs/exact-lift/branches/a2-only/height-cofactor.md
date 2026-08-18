# A2 height–cofactor bridge

> **依赖：** `endpoint-lattice.md` §§16.44–16.73、`prime-source.md`、`primitive-reduction.md`。
>
> **严格状态：**本文把 reduced numerator `W_q` 与本原 odd cofactor `\widehat{\mathcal T}_2` 直接接成逐 prime-power 的 gcd/valuation bridge，并将 denominator-saturation 与 height 的共同惰性素数压到三个固定素数：q-side 只剩 `23`，f-side 只剩 `7,43`。共同深度在三对象交集中至多一层。本文仍**不宣称 A2 全局关闭**。

---

## 1. 统一记号

沿用当前 reflection endpoint：

\[
T=10^m,
\qquad
\lambda=m-d,
\qquad
Q_0=c_Qq,
\]

\[
N=3D-C=c_-^2X,
\qquad
D=g2^m5^d,
\]

以及 `primitive-reduction.md` 已证明的

\[
\boxed{
H_0=c_uW_q,
\qquad
\alpha=TK+a_3=\omega W_q.
}
\tag{1.1}
\]

canonical factor equality 为

\[
H_0-Y_3=5^\lambda c_-^2X,
\qquad
H_0+Y_3=c_+^2Y,
\qquad
Y_3=ga_3.
\tag{1.2}
\]

所以

\[
\boxed{
H_0^2-Y_3^2
=5^\lambda c_Q^2XY.
}
\tag{1.3}
\]

另一方面 §16.44 的真正 `2,5`-本原 cofactor 是

\[
\boxed{
\widehat{\mathcal T}_2
=
2^mc_u^2g^2\mathscr S_0
-(c_Qq)^2 5^{2\lambda-d}XY,
}
\tag{1.4}
\]

其中

\[
\boxed{
\mathscr S_0
=T(K^2-26)-(2K-9)(2a_3+9T).
}
\tag{1.5}
\]

已有

\[
\widehat{\mathcal T}_2>0,
\qquad
\gcd(\widehat{\mathcal T}_2,10c_ug)=1,
\qquad
\widehat{\mathcal T}_2\equiv3\pmod4.
\tag{1.6}
\]

本文研究 `W_q` 与 (1.4) 的共同 odd-prime flow。

---

## 2. `已严格完成`：`\mathscr S_0` 在 reduced numerator 上精确线性化

由 (1.1)，

\[
a_3=\omega W_q-TK.
\tag{2.1}
\]

于是

\[
2a_3+9T
=2\omega W_q-T(2K-9).
\tag{2.2}
\]

代入 (1.5)：

\[
\begin{aligned}
\mathscr S_0
&=T(K^2-26)
-(2K-9)\bigl(2\omega W_q-T(2K-9)\bigr)\\
&=T\bigl(K^2-26+(2K-9)^2\bigr)
-2\omega(2K-9)W_q.
\end{aligned}
\]

定义

\[
\boxed{
F_W(K):=5K^2-36K+55.
}
\tag{2.3}
\]

其判别式恰为

\[
36^2-4\cdot5\cdot55=14^2,
\]
所以它在整数层完全分裂：

\[
\boxed{
F_W(K)=(K-5)(5K-11).
}
\tag{2.4}
\]

因此得到精确整数式

\[
\boxed{
\mathscr S_0
=T F_W(K)
-2\omega(2K-9)W_q.
}
\tag{2.5}
\]

这一步把原来的 numerator polynomial `\mathscr S_0` 直接接到 reduced numerator `W_q`；后续不再需要只通过 denominator gcd 间接接触两者。

---

## 3. `已严格完成`：`\widehat{\mathcal T}_2` 与 `W_q` 的全局 cofactor bridge

先用 (1.3) 改写 (1.4) 的 norm 项：

\[
(c_Qq)^2 5^{2\lambda-d}XY
=q^2 5^{\lambda-d}(H_0^2-Y_3^2).
\]

结合 (1.1)、`Y_3=ga_3`：

\[
\boxed{
\widehat{\mathcal T}_2
=
2^mc_u^2g^2\mathscr S_0
-q^2 5^{\lambda-d}
\bigl(c_u^2W_q^2-g^2a_3^2\bigr).
}
\tag{3.1}
\]

这里 `\lambda-d\ge0`，因为旧关系 `\nu_5=\lambda-2d\ge0`。

再把 (2.1)、(2.5) 代入 (3.1)。与 `W_q` 无关的常数项恰为

\[
2^mg^2T
\left(
 c_u^2F_W(K)+q^25^{2\lambda}K^2
\right),
\]
因为

\[
5^{\lambda-d}T^2
=2^mT5^{2\lambda}.
\]

定义新的 **height–cofactor resultant**

\[
\boxed{
\mathscr B_W
:=
c_u^2F_W(K)
+(q5^\lambda K)^2.
}
\tag{3.2}
\]

完整展开给出

\[
\boxed{
\widehat{\mathcal T}_2
=2^mg^2T\,\mathscr B_W
+W_q\mathscr E_W,
}
\tag{3.3}
\]

其中

\[
\begin{aligned}
\mathscr E_W={}&
-2^{m+1}c_u^2g^2\omega(2K-9)\\
&-q^25^{\lambda-d}c_u^2W_q
+q^25^{\lambda-d}g^2\omega^2W_q\\
&-2q^25^{\lambda-d}g^2\omega TK
\in\mathbf Z.
\end{aligned}
\tag{3.4}
\]

`primitive-reduction.md` 已证明 `W_q` 为奇数、`5\nmid W_q` 且 `\gcd(W_q,g)=1`。因此

\[
\gcd(2^mg^2T,W_q)=1.
\tag{3.5}
\]

由 (3.3) 得到全局 gcd identity：

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,W_q)
=
\gcd(\mathscr B_W,W_q).
}
\tag{3.6}
\]

更精确地，若

\[
p^h\Vert W_q,
\]

则

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),h\}
=
\min\{v_p(\mathscr B_W),h\}.
}
\tag{3.7}
\]

这正是此前缺失的逐 prime-power bridge：`W_q` 与 odd inert excess 不再是两套平行的素因子列表。

---

## 4. `已严格完成`：height bridge 在第三分子上变成两个低次数二元型

若奇素数 `p\mid W_q`，由 (1.1)

\[
TK+a_3\equiv0\pmod{p^h},
\qquad h=v_p(W_q),
\]
所以

\[
K\equiv-a_3T^{-1}\pmod{p^h}.
\tag{4.1}
\]

将 (4.1) 代入 `F_W`，乘去单位 `T^2`：

\[
\boxed{
T^2F_W(K)
\equiv
(a_3+5T)(5a_3+11T)
\pmod{p^h}.
}
\tag{4.2}
\]

再定义

\[
\boxed{
G_W(K):=F_W(K)+4K^2
=9K^2-36K+55.
}
\tag{4.3}
\]

同样有

\[
\boxed{
T^2G_W(K)
\equiv
9a_3^2+36a_3T+55T^2
=(3a_3+6T)^2+19T^2
\pmod{p^h}.
}
\tag{4.4}
\]

所以 q-side 对应的是两个线性 third-numerator factors；f-side 则对应判别数 `-19` 的正定二元型。

---

## 5. `已严格完成`：q-saturation 与 height/cofactor 的共同深度只可能是一层 `23`

设

\[
p\ne3,
\qquad p\equiv3\pmod4,
\]
并同时满足

\[
p^e\Vert q,
\qquad
p^e\mid\mathscr L_{23},
\qquad
h:=v_p(W_q)>0,
\qquad
\tau:=v_p(\widehat{\mathcal T}_2)>0.
\tag{5.1}
\]

这里

\[
2\mathscr L_{23}=2a_3+9T.
\]

令

\[
\boxed{s:=\min\{e,h,\tau\}\ge1.}
\tag{5.2}
\]

由 (3.7)，`p^s\mid\mathscr B_W`。而 `p^e\mid q`，所以 (3.2) 的平方项在模 `p^s` 下消失；`p\nmid c_u` 来自 height-prime 的既有本原性。故

\[
\boxed{p^s\mid F_W(K).}
\tag{5.3}
\]

另一方面 `p^h\mid W_q` 与 `p^e\mid(2a_3+9T)` 给出

\[
2(TK+a_3)\equiv0\pmod{p^h},
\qquad
2a_3+9T\equiv0\pmod{p^e}.
\]

在深度 `s` 上相减，因 `p\nmid T`：

\[
\boxed{p^s\mid2K-9.}
\tag{5.4}
\]

现在使用整数 Bézout identity

\[
\boxed{
4F_W(K)+23
=(2K-9)(10K-27).
}
\tag{5.5}
\]

(5.3)–(5.5) 强迫

\[
p^s\mid23.
\]

所以

\[
\boxed{
p=23,
\qquad
s=1.
}
\tag{5.6}
\]

即

\[
\boxed{
\min\!\left\{
 v_{23}(q),
 v_{23}(W_q),
 v_{23}(\widehat{\mathcal T}_2)
\right\}=1
}
\tag{5.7}
\]

对任何真正同时进入 q-saturation、height 与 odd cofactor 的 `23` 成立。

这比 `primitive-reduction.md` 的“q-height 交集只可能是 `23`”更强：不仅素数被固定，**三对象共享的 prime-power 深度也不可能超过一层**。

---

## 6. `已严格完成`：f-saturation 与 height/cofactor 只可能是一层 `7` 或 `43`

现在设

\[
p^e\Vert f,
\qquad
p^e\mid\mathscr L_{23},
\qquad
h:=v_p(W_q)>0,
\qquad
\tau:=v_p(\widehat{\mathcal T}_2)>0,
\tag{6.1}
\]

仍令

\[
s:=\min\{e,h,\tau\}\ge1.
\tag{6.2}
\]

由

\[
f=5^\lambda q+2c_u
\]
得到完整深度

\[
q5^\lambda\equiv-2c_u\pmod{p^e}.
\tag{6.3}
\]

因此在模 `p^s` 下

\[
\mathscr B_W
\equiv
c_u^2\bigl(F_W(K)+4K^2\bigr)
=c_u^2G_W(K).
\]

结合 (3.7) 与 `p\nmid c_u`：

\[
\boxed{p^s\mid G_W(K).}
\tag{6.4}
\]

同 §5，height 与 saturation 给出

\[
p^s\mid2K-9.
\tag{6.5}
\]

而 `G_W` 满足第二个整数 Bézout identity

\[
\boxed{
4G_W(K)-301
=(2K-9)(18K+9).
}
\tag{6.6}
\]

故

\[
p^s\mid301=7\cdot43.
\]

`301` 平方自由，所以

\[
\boxed{
p\in\{7,43\},
\qquad
s=1.
}
\tag{6.7}
\]

也就是

\[
\boxed{
\min\!\left\{
 v_p(f),
 v_p(W_q),
 v_p(\widehat{\mathcal T}_2)
\right\}=1,
\qquad p=7\text{ or }43.
}
\tag{6.8}
\]

这把上一轮留下的无限 reciprocity class 压成了**两个固定素数**。

---

## 7. `已严格完成 / 审计降级`：f-height 的二次特征只是在 `7,43` 上的 shadow

由 (4.4)，任何 f-side common height prime 在简单层满足

\[
(3a_3+6T)^2\equiv-19T^2\pmod p.
\]

对 `p\ne19`：

\[
\left(\frac{-19}{p}\right)=1.
\]

当 `p\equiv3 (mod 4)` 时，二次互反律化为

\[
\boxed{\left(\frac p{19}\right)=1.}
\tag{7.1}
\]

但 §6 已把 saturation-height common prime 固定为 `7,43`，而直接检查

\[
\boxed{
\left(\frac7{19}\right)
=
\left(\frac{43}{19}\right)
=1.
}
\tag{7.2}
\]

同样，`primitive-reduction.md` 先前得到的

\[
\left(\frac p{23}\right)=-1,
\qquad
\left(\frac p5\right)\left(\frac p{11}\right)=1
\tag{7.3}
\]

对 `p=7,43` 都自动成立。

因此这些 quadratic signatures 在新的 finite resultant 之后不再提供额外排除力：

\[
\boxed{
\begin{array}{c|ccc}
p&(p/23)&(p/5)(p/11)&(p/19)\\ \hline
7&-1&1&1\\
43&-1&1&1
\end{array}}
\tag{7.4}
\]

后续若继续处理 `7,43`，必须使用更高 `p`-进深度、真实十进制代表或 Archimedean 大小；继续叠加同层 Legendre character 不会关闭它们。

---

## 8. `已严格完成`：denominator-height common inert support 已变成固定浅层集合

将 §§5–6 合并。若非 `3` inert prime 同时满足

1. `p\mid W_q`；
2. `p\mid\widehat{\mathcal T}_2`；
3. 它属于一个已饱和的 denominator primary factor `p^e\Vert qf`，即 `p^e\mid\mathscr L_{23}`；

则

\[
\boxed{
\begin{array}{c|c|c}
\text{side}&p&\min(v_p(\text{den}),v_p(W_q),v_p(\widehat{\mathcal T}_2))\\ \hline
q&23&1\\
f&7\text{ or }43&1.
\end{array}}
\tag{8.1}
\]

特别地

\[
\boxed{
\operatorname{Supp}^{\rm sat}_{3\bmod4}
(W_q,\widehat{\mathcal T}_2;qf)
\subseteq\{7,23,43\}.
}
\tag{8.2}
\]

所以“denominator odd excess”和“height odd carrier”不可能继续共享一个无界移动素数。任何无界移动的共同惰性素数都必须转入 endpoint-external channel。

---

## 9. `已严格完成`：endpoint-external common prime 被压成单个显式二次 Hensel 多项式

设

\[
p\ne3,
\qquad p\equiv3\pmod4,
\qquad
p\mid W_q,
\qquad
p\mid\widehat{\mathcal T}_2,
\qquad
p\nmid qf.
\tag{9.1}
\]

由 (3.6)，`p\mid\mathscr B_W`。写

\[
z:=q5^\lambda.
\]

则

\[
\boxed{
\mathscr B_W
=(5c_u^2+z^2)K^2
-36c_u^2K
+55c_u^2.
}
\tag{9.2}
\]

所以 endpoint-external common prime 不再是未命名 angle prime：它必须使一个显式二次式在真实 decimal prefix `K` 上消失。

它关于 `K` 的判别式为

\[
\boxed{
\Delta_W
=4c_u^2
\bigl(49c_u^2-55q^25^{2\lambda}\bigr).
}
\tag{9.3}
\]

因此模 `p` 有根必强迫

\[
\boxed{
49c_u^2-55q^25^{2\lambda}
\text{ 为 }0\text{ 或模 }p\text{ 平方}.
}
\tag{9.4}
\]

若 (9.4) 非零，则 `\mathscr B_W` 在模 `p` 上只有两个 simple root，之后每个 root 都唯一 Hensel 提升；若判别式为零，则共同 prime 被进一步压入单个 source-discriminant 接触

\[
\boxed{
p\mid49c_u^2-55q^25^{2\lambda}.}
\tag{9.5}
\]

此外 `p\nmid qf` 意味着归一化 source ratio

\[
\frac{q5^\lambda}{c_u}
\not\equiv0,-2\pmod p,
\tag{9.6}
\]

即 external channel 严格避开 q-side 与 f-side 两个 endpoint。

若需要直接使用第三分子而不是 `K`，(4.1) 还把 (9.2) 改写为

\[
\boxed{
 c_u^2(a_3+5T)(5a_3+11T)
 +(q5^\lambda a_3)^2
\equiv0\pmod p.
}
\tag{9.7}
\]

所以真正剩余的 moving common-prime 问题已经变成一个明确的二次 Hensel/resultant 问题，而不是抽象“spontaneous angle excess”。

---

## 10. 更新后的 A2 开放核

本轮没有证明 `A_2` 全局空性，但把 `primitive-reduction.md` 末尾的两条候选主线进一步压缩：

### 10.1 denominator 与 height 的共同 odd carrier

不再是无界素数族，而只剩

\[
\boxed{
q\text{-side}:23,
\qquad
f\text{-side}:7,43.
}
\tag{10.1}
\]

并且三对象共享的深度严格只有一层。要继续排除它们，需要研究“某一对象继续加深而另外两个已停止”的 higher-lift cancellation；普通二次特征已经没有新增信息。

### 10.2 endpoint-external common carrier

统一由

\[
\boxed{
\mathscr B_W
=c_u^2(K-5)(5K-11)+(q5^\lambda K)^2
}
\tag{10.2}
\]

控制，其判别式只含 source pair `(c_u,q5^\lambda)`：

\[
\boxed{
\Delta_W/(4c_u^2)
=49c_u^2-55q^25^{2\lambda}.
}
\tag{10.3}
\]

因此下一步最值得推进的是：

1. 对固定 `23,7,43`，把 `v_p(W_q)`、`v_p(\widehat{\mathcal T}_2)` 与 denominator exponent 超过共同第一层后的差值做一次显式 Hensel expansion；
2. 对 external common prime，把 (9.2)/(9.7) 与 source split 或 `D_{\rm src}` resultant 联立，优先处理判别式零通道 (9.5)；
3. 平行研究 `\widehat{\mathcal T}_2` 的 endpoint-external odd carrier 是否必须进入 `W_q`。如果能证明这一点，则 (8.2) 与 `W_q/3^\delta\equiv1 (mod 4)` 的偶 parity 会直接进入最终闭环。

继续单独追逐 `(N_0/p)=-1` 或 (7.3) 的 Legendre character 已经不会增加约束。
