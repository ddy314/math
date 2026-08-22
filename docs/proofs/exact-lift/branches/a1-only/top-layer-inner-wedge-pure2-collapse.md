# A1 top layer: uniform pure-2 collapse in the stable inner wedge

> 日期：2026-08-22。
>
> 依赖：`top-layer-inner-wedge-uniform-phase.md`、`top-layer-inner-wedge-digit-lock.md`、global `kappa` square、`decimal-height-synchronization.md`。
>
> 范围：
> \[
> d=2,\qquad r=s=1,
> \]
> 定义
> \[
> u:=2g-k,
> \qquad 1\le u\le g-1,
> \]
> 并假设稳定 prefix 条件
> \[
> \boxed{g-u\ge3.}
> \]

状态：**pure-2 denominator axis 严格全空。**

即
\[
\boxed{L=2^a\Longrightarrow\text{empty}.}
\]

---

## 1. uniform pure-2 normal form

`top-layer-inner-wedge-uniform-phase.md` 已经关闭 `a<=u+1` 的 mixed用途，并给 pure-2 真正需要研究的 generic high region
\[
\boxed{a>u+1.}
\tag{1}

square parity 给
\[
\boxed{a\equiv u-1\pmod2,}
\tag{2}
以及 exact 2-completion height
\[
\boxed{
H_2
=2g+\frac{3(a-u)+1}{2}.
}
\tag{3}

5-side 若要同步，唯一可能是 low resonance
\[
\boxed{v_5(\kappa)=g-u.}
\]
因此
\[
\boxed{v_5(M)=2g-u.}
\]
写
\[
\boxed{M=5^{2g-u}m,}
\qquad
(m,10)=1,
\qquad
m\mid b_1Q_0.
\tag{4}

令
\[
R:=2g+\frac{3(a-u)+1}{2}.
\]
exact 5-adic root allocation 给
\[
\boxed{
v_5(m+2^{2g-u-1+a}Q_0)=R,
}
\tag{5}
等价于
\[
\boxed{
m\equiv-2^{2g-u-1+a}Q_0\pmod{5^R}.}
\tag{6}

---

## 2. decimal block and phase gap

令
\[
s:=J+1.
\]
`top-layer-inner-wedge-digit-lock.md` 给
\[
\boxed{10^{u-1}<s\le10^u.}
\tag{7}
写
\[
\boxed{s=5^\nu j,}
\qquad 5\nmid j.
\tag{8}

又
\[
\tau=10^{g-u}=2^{g-u}5^{g-u}.
\]
定义 positive integer gap
\[
A:=s\tau2^a-M.
\]
uniform phase theorem 给
\[
\boxed{0<AH^2<40\cdot10^u2^a.}
\tag{9}

下面按 `nu<g` 与 `nu>=g` 分流。两支都由同一 resonance positive-representative contradiction关闭。

---

# Part I. `nu<g`

## 3. exact gap valuation

若
\[
\nu<g,
\]
则
\[
v_5(s\tau2^a)=g-u+\nu
<2g-u=v_5(M).
\]
所以
\[
\boxed{v_5(A)=g-u+\nu.}
\tag{10}

写
\[
\boxed{A=5^{g-u+\nu}a_0,}
\]
则
\[
\boxed{
a_0
=2^{a+g-u}j-5^{g-\nu}m,
}
\tag{11}
并由 `A>0`：
\[
\boxed{0<a_0<2^{a+g-u}j.}
\tag{12}

---

## 4. phase lower bound on `a`

由 (9),(10) 与 `H^2=2^{2g}5^{2g}`：
\[
2^{2g}5^{3g-u+\nu}
<40\,2^{a+u}5^u.
\]
因此
\[
2^a>
\frac{2^{2g-u}5^{3g-2u+\nu}}{40}.
\]
使用
\[
5>2^2,
\qquad
40<2^6,
\]
得到
\[
\boxed{
a>8g-5u+2\nu-6.}
\tag{13}

稳定条件 `g-u>=3` 使 (13) 自动推出
\[
\boxed{2a>10g-4u+5.}
\tag{14}
因为
\[
2(8g-5u+2\nu-6)-(10g-4u+5)
=6(g-u)+4\nu-17>0.
\]

---

## 5. resonance positive representative

把 (6) 代入 (11)：
\[
\boxed{
a_0\equiv B_0\pmod{5^{R+g-\nu}},}
\tag{15}
其中
\[
\boxed{
B_0
:=2^{a+g-u}j
+2^{a+2g-u-1}5^{g-\nu}Q_0.
}
\tag{16}

显然
\[
\boxed{B_0>2^{a+g-u}j>a_0.}
\tag{17}

当前
\[
2k+1=4g-2u+1,
\]
所以
\[
Q_0<10^{4g-2u+2}.
\]
第二项支配第一项，安全取
\[
\boxed{
B_0
<2^{a+6g-3u+2}5^{5g-2u+2-\nu}.
}
\tag{18}

模数指数为
\[
R+g-\nu
=3g-\nu+\frac{3(a-u)+1}{2}.
\]
(18) 小于模数的充分条件是
\[
2^{a+6g-3u+2}
<5^{(3a+u-4g-3)/2}.
\tag{19}

由 `5>2^2`，右边严格大于
\[
2^{3a+u-4g-3}.
\]
而 (14) 恰给
\[
3a+u-4g-3>a+6g-3u+2.
\]
所以 (19) 成立：
\[
\boxed{B_0<5^{R+g-\nu}.}
\tag{20}

于是
\[
0<a_0<B_0<5^{R+g-\nu}
\]
但 (15) 要求二者同余，矛盾。

因此
\[
\boxed{\nu<g\Longrightarrow\text{empty}.}
\tag{21}

---

# Part II. `nu>=g`

## 6. stronger gap valuation

现在假设
\[
\nu\ge g.
\]
则第一项 `s tau 2^a` 的 5-depth至少为 `2g-u`，与 `M` 同深或更深。因此
\[
A
=5^{2g-u}a_1,
\]
其中
\[
\boxed{
a_1
=2^{a+g-u}5^{\nu-g}j-m
\in\mathbf Z_{>0}.}
\tag{22}

由 (9)：
\[
2^{2g}5^{4g-u}
<40\,2^{a+u}5^u,
\]
所以
\[
2^a>
\frac{2^{2g-u}5^{4g-2u}}{40}.
\]
再次用 `5>2^2,40<2^6`：
\[
\boxed{a>10g-5u-6.}
\tag{23}

稳定条件立刻给
\[
\boxed{2a>10g-4u+5.}
\tag{24}
因为
\[
2(10g-5u-6)-(10g-4u+5)
=10g-6u-17
=4u+10(g-u)-17>0.
\]

---

## 7. same representative contradiction

由 (6),(22)：
\[
\boxed{
a_1\equiv B_1\pmod{5^R},}
\tag{25}
其中
\[
\boxed{
B_1
:=2^{a+g-u}5^{\nu-g}j
+2^{a+2g-u-1}Q_0.
}
\tag{26}

显然
\[
B_1>2^{a+g-u}5^{\nu-g}j>a_1.
\tag{27}

由 digit lock `s<=10^u`：
\[
5^{\nu-g}j=\frac{s}{5^g}
\le\frac{10^u}{5^g},
\]
所以第一项远小于以下统一安全界；结合 `Q0<10^(4g-2u+2)`：
\[
\boxed{
B_1
<2^{a+6g-3u+2}5^{4g-2u+2}.
}
\tag{28}

模数是
\[
5^R,
\qquad
R=2g+\frac{3(a-u)+1}{2}.
\]
(28) 小于模数的充分条件仍然化成
\[
2^{a+6g-3u+2}
<5^{(3a+u-4g-3)/2},
\]
与 Part I 的 (19) 完全相同。

由 (24) 该条件成立，因此
\[
0<a_1<B_1<5^R,
\]
却由 (25) 同余，矛盾。

故
\[
\boxed{\nu\ge g\Longrightarrow\text{empty}.}
\tag{29}

---

## 8. theorem

(21),(29) 穷尽 `nu`。

因此
\[
\boxed{
 d=2,\quad r=s=1,\quad g-u\ge3,
 \quad L=2^a
 \Longrightarrow\text{empty}.
}
\tag{30}

结合 `top-layer-inner-wedge-mixed-collapse.md`，稳定 inner wedge 当前唯一 remaining denominator axis 是
\[
\boxed{L=5^b.}
\]
