# A1 top layer: close the `k=2g` pure-5 terminal

> 日期：2026-08-22。
>
> 依赖：`top-layer-k2g-pure5-real-phase-shell.md`、`top-layer-k2g-pure5-odd-orientation.md`、`top-layer-k2g-prime-shape-collapse.md`。
>
> 范围：
> \[
> d=2,\quad r=s=1,\quad g\ge1,\quad k=2g,\quad J=0,
> \]
> primitive pruning 后 `(z,w)=(1,1),(1,3)`，且当前最后 prime shape
> \[
> L=5^b,\qquad b\ge2\text{ even}.
> \]

状态：**已严格完成。pure-5 terminal 为空。**

核心分两步：

1. width-`3/5` real phase shell + fixed polynomial resultants 把无界 `g` 压成 `g<=56/54`；
2. exact high-2 resonance 在该 finite box 中只产生 12 个 gap-integer candidates，逐个恢复 `m` 后全部违反 `m|b1*Q0`。

有限证书：

`scripts/exact-lift/a1-only/research-checks/top-layer/check_a1_k2g_pure5_phase_divisor_certificate.py`

只使用 Python 整数运算；不做整数分解，不使用浮点判定。

---

## 1. pure-5 integer gap

令
\[
H:=10^g,
\qquad
L=5^b,
\qquad
M=2^{2g-1}m,
\]
其中
\[
(m,10)=1,
\qquad
m\mid P:=b_1Q_0.
\tag{1}
\]

定义
\[
\boxed{A:=HL-M\in\mathbf Z_{>0}.}
\tag{2}
\]
real phase variable 为
\[
\boxed{t=\frac{AH^2}{5^b}.}
\tag{3}

`top-layer-k2g-pure5-real-phase-shell.md` 已严格证明：

- `w=1`：
  \[
  \frac{299}{10}<t<\frac{305}{10};
  \tag{4a}
  \]
- `w=3`：
  \[
  \frac{219}{10}<t<\frac{225}{10}.
  \tag{4b}
  \]

记
\[
\alpha_1=299,
\qquad
\alpha_3=219.
\]
定义正整数 remainder
\[
\boxed{
\mathcal E:=10AH^2-\alpha_w5^b.
}
\tag{5}
\]
由 (4)：
\[
\boxed{0<\mathcal E<6\,5^b.}
\tag{6}

---

## 2. `m/gcd` 必须塞进小 remainder

由 `A=H5^b-M`：
\[
\begin{aligned}
\mathcal E
&=10H^2(H5^b-M)-\alpha_w5^b\\
&=5^b(10H^3-\alpha_w)-10H^2M.
\end{aligned}
\tag{7}
\]

令
\[
F_w(H):=10H^3-\alpha_w,
\qquad
d:=\gcd(m,F_w(H)).
\tag{8}
\]
因为 `m|M`，(7) 模 `m` 给
\[
\mathcal E\equiv5^bF_w(H)\pmod m.
\]
又 `(m,5)=1`，所以
\[
\boxed{\frac md\mid\mathcal E.}
\tag{9}
\]
结合 (6)：
\[
\boxed{m<6d\,5^b.}
\tag{10}

---

## 3. `d` 被 fixed resultants 控制

当前
\[
b_1=10H^4-w,
\qquad
Q_0=100H^4-(10w-1),
\qquad
m\mid b_1Q_0.
\tag{11}
\]

若一个 prime power 同时进入 `m` 与 `F_w(H)`，它必来自 `b1` 或 `Q0` 与 `F_w` 的共同因子。对整数多项式，共同值的 gcd 整除相应 resultant。因此
\[
d\mid
\operatorname{Res}_H(b_1,F_w)
\operatorname{Res}_H(Q_0,F_w).
\tag{12}
\]

### `w=1`

这里 `F_1=10H^3-299`。exact resultants 为
\[
|\operatorname{Res}(10H^4-1,10H^3-299)|
=7992538791000,
\]
\[
|\operatorname{Res}(100H^4-9,10H^3-299)|
=7992538793710000.
\]
其分解为
\[
2^3 3\,5^3\,347\,7677751,
\]
以及
\[
2^4 5^4 29^2\,1063\,894037.
\]
因为 `(m,10)=1`，可删去全部 `2,5` 因子，得到安全常数
\[
\boxed{
d\le C_1:=6388067634729952180461.}
\tag{13}

### `w=3`

这里 `F_3=10H^3-219`。exact resultants 为
\[
|\operatorname{Res}(10H^4-3,10H^3-219)|
=2300257251000,
\]
\[
|\operatorname{Res}(100H^4-29,10H^3-219)|
=2300257277110000.
\]
其分解为
\[
2^3 3^3 5^3\,1511\,56383,
\]
以及
\[
2^4 5^4\,13\,51343\,344629.
\]
所以
\[
\boxed{
d\le C_3:=529118348083779382461.}
\tag{14}

---

## 4. 无界 `g` 被彻底有限化

由 (4) 有 `t<31`，故
\[
\rho=H-\frac{t}{H^2}>\frac H2
\qquad(H\ge10).
\tag{15}
\]
又
\[
M=\rho5^b=2^{2g-1}m,
\]
所以
\[
m>
\frac{(H/2)5^b}{2^{2g-1}}
=\left(\frac52\right)^g5^b.
\tag{16}
\]

与 (10) 合并并约去 `5^b`：
\[
\boxed{\left(\frac52\right)^g<6d.}
\tag{17}

使用 (13)-(14)：

- `w=1`：
  \[
  (5/2)^g<6C_1
  \Longrightarrow
  \boxed{g\le56};
  \tag{18a}
  \]
- `w=3`：
  \[
  (5/2)^g<6C_3
  \Longrightarrow
  \boxed{g\le54}.
  \tag{18b}
  \]

因此 pure-5 不再含任何无界高度。

---

## 5. `b` 也有 factorization-free finite cap

因为 `m|P`，有
\[
m\le P.
\tag{19}
\]
而 (16) 给
\[
m>\left(\frac52\right)^g5^b.
\]
所以必要地
\[
\boxed{5^{g+b}<2^gP.}
\tag{20}

另一方面旧 ultrathin gap 已给
\[
\boxed{95\,5^b>H^2.}
\tag{21}

因此对每个有限 `g`，只需枚举同时满足：

1. `b>=2` even；
2. (20)；
3. (21)

的有限多个 `b`。

总计恰有
\[
\boxed{12738}
\tag{22}
个 `(g,w,b)` states。

---

## 6. phase shell 只留下 12 个 gap integers

由
\[
A=H5^b-M
=2^g\left(5^{g+b}-2^{g-1}m\right),
\]
定义
\[
\boxed{a:=5^{g+b}-2^{g-1}m\in\mathbf Z_{>0}.}
\tag{23}
\]
则
\[
t=2^{3g}5^{2g-b}a.
\tag{24}
\]
所以 phase shell 等价于严格整数区间：

- `w=1`：
  \[
  299\,5^b
  <10\,2^{3g}5^{2g}a
  <305\,5^b;
  \tag{25a}
  \]
- `w=3`：
  \[
  219\,5^b
  <10\,2^{3g}5^{2g}a
  <225\,5^b.
  \tag{25b}
  \]

现在使用 pure-5 **exact** high-2 resonance：
\[
\boxed{
v_2(m+5^{2g+b}Q_0)
=2g+\frac{3b}{2}-1.
}
\tag{26}

定义
\[
B_0:=5^{g+b}+2^{g-1}5^{2g+b}Q_0.
\]
由 (23)：
\[
B_0-a
=2^{g-1}(m+5^{2g+b}Q_0).
\]
因此 (26) 等价于
\[
\boxed{
v_2(B_0-a)
=3g+\frac{3b}{2}-2.
}
\tag{27}

令
\[
e:=3g+\frac{3b}{2}-2.
\]
则 (27) 可直接写成单一 residue class
\[
\boxed{
a\equiv B_0+2^e\pmod{2^{e+1}}.}
\tag{28}

certificate 对 (18)--(21) 的所有 12738 states，把 (25) 与 (28) 精确相交。全盒只留下
\[
\boxed{12}
\tag{29}
个整数 `a`。

没有概率筛选；(28) 是 exact valuation 的充要 residue condition。

---

## 7. 12 个状态全部失败原始 divisor condition

对每个 surviving `a`，按 (23) 唯一恢复
\[
\boxed{m=\frac{5^{g+b}-a}{2^{g-1}}.}
\tag{30}

certificate 随后只检查最原始、不可放松的必要条件
\[
\boxed{m\mid b_1Q_0.}
\tag{31}

输出为
\[
\boxed{
\texttt{states}=12738,
\quad
\texttt{gap\_a\_candidates}=12,
\quad
\texttt{divisor\_survivors}=0.
}
\tag{32}

因此不存在 pure-5 candidate：
\[
\boxed{
L=5^b\Longrightarrow\varnothing
\quad\text{on }k=2g,J=0.
}
\tag{33}

---

## 8. consequence for the `k=2g,J=0` boundary

`top-layer-k2g-gap-smallL-collapse.md` 已关闭 `L=1,2`；
`top-layer-k2g-prime-shape-collapse.md` 已关闭 mixed-high、`2*5^b` 与 pure-2，并把最后 frontier 压成 pure-5。
本文又证明 pure-5 为空。

故
\[
\boxed{
 d=2,\ r=s=1,\ g\ge1,\ k=2g,\ J=0
 \Longrightarrow\varnothing.
}
\tag{34}

由于 `top-layer-minimal-offdiagonal-J-compression.md` 已证明 `k=2g` 必有 `J=0`，实际上整个最外窄楔边界
\[
\boxed{k=2g}
\]
在 minimal `(r,s)=(1,1)` off-diagonal 中全部关闭。