# A1 top layer: `k=2g-2` pure-5 collapse

> 日期：2026-08-22。
>
> 依赖：`top-layer-k2gm2-tail-center.md`、global `kappa` square、`decimal-height-synchronization.md`。
>
> 范围：
> \[
> d=2,\quad r=s=1,\quad g\ge3,\quad k=2g-2,
> \quad J\in\{0,\dots,108\}.
> \]

状态：**已严格关闭 pure-5 branch**
\[
\boxed{L=5^b.}
\]

`g>=5` 使用 phase/resonance finite certificate；`g=3,4` 已由 full small-layer global-terminal certificate 整层归零。

---

## 1. explicit prefix scale

令
\[
H=10^g,
\qquad
\tau=10^{g-2}=H/100.
\]
此时
\[
2k+1=4g-3,
\]
故
\[
b_1=10^{4g-3}-w,
\qquad
Q_0=10b_1+1,
\]
\[
Q=\tau Q_0,
\qquad
G=\tau b_1,
\qquad
D=H\tau Q_0.
\]

`top-layer-k2gm2-tail-center.md` 给
\[
\boxed{
0<(J+1)\tau-\rho<4000/H^2.
}
\tag{1}

假设
\[
L=5^b.
\]
令
\[
A:=((J+1)\tau)L-M>0.
\]
则
\[
\boxed{0<AH^2<4000\,5^b.}
\tag{2}
并特别有
\[
\boxed{5^b>H^2/4000.}
\tag{3}

---

## 2. `g>=5` 的 5-high side

以下先取 `g>=5`。

显式 prefix 给
\[
v_5(N)=0,
\qquad
v_5(K)=2g-4,
\]
且
\[
v_5(10^gQG)=3g-4.
\]

若 `L=5^b`，则
\[
v_5(\kappa)=3g-4+b.
\]
由 (3) 已有 `b>=3`。当 `b>=3`，`kappa` square 内第二项严格更浅，得到
\[
v_5(W^2)=8g-10+b.
\]
因此 square parity 强迫
\[
\boxed{b\text{ 为偶数}.}
\]
故
\[
\boxed{b>=4\text{ even}.}
\tag{4}

root numerator / denominator valuation 给
\[
\boxed{
H_5=2g-3+\frac{3b}{2}.
}
\tag{5}

---

## 3. 2-side 唯一 low resonance

记
\[
e=v_2(w).
\]
对 `g>=5`：
\[
v_2(N)=2e,
\qquad
v_2(K)=2g-4+2e.
\]
base 2-depth 是
\[
3g-4+e.
\]

要让 2-side 追上 (5)，唯一可能的 low resonance 是
\[
\boxed{v_2(\kappa)=g-1+e.}
\tag{6}
所以
\[
\boxed{v_2(M)=2g-3.}
\tag{7}

写
\[
\boxed{M=2^{2g-3}m,}
\qquad (m,10)=1,
\qquad m\mid b_1Q_0.
\tag{8}

令
\[
c:=5^{2g+b-2}.
\]
从 `kappa+2G` exact factorization 与共轭 root product可得两个 2-denominator depths为
\[
\{1,\ 1+v_2(m+cQ_0)\}.
\]
与 (5) 同步因此精确要求
\[
\boxed{
v_2(m+5^{2g+b-2}Q_0)
=2g-4+\frac{3b}{2}.
}
\tag{9}

---

## 4. gap integer and exact residue

由 (2),(8) 定义
\[
\boxed{
a:=(J+1)5^{g+b-2}-2^{g-1}m.}
\tag{10}
则
\[
A=2^{g-2}a,
\qquad a\in\mathbf Z_{>0},
\]
并且
\[
0<2^{3g-2}5^{2g-b}a<4000.
\]
所以
\[
\boxed{
1\le a
\le
\left\lfloor
\frac{4000\,5^b-1}{2^{3g-2}5^{2g}}
\right\rfloor.
}
\tag{11}

把 (9) 乘 `2^(g-1)`。若
\[
R:=2g-4+\frac{3b}{2},
\qquad
E:=R+g-1,
\]
以及
\[
B_0
:=(J+1)5^{g+b-2}
+2^{g-1}5^{2g+b-2}Q_0,
\]
则 (9) 等价于
\[
\boxed{v_2(B_0-a)=E,}
\]
也即
\[
\boxed{a\equiv B_0+2^E\pmod{2^{E+1}}.}
\tag{12}

---

## 5. phase/divisor height gives `g<=16`

由 (2)：
\[
AH^2
=5^b\frac{(J+1)H^3}{100}
-H^2M.
\]
模 `m`：
\[
AH^2
\equiv
5^b\frac{(J+1)H^3}{100}
\pmod m.
\]
因为 `(m,10)=1`：
\[
\gcd\left(m,\frac{(J+1)H^3}{100}\right)
=\gcd(m,J+1)
\le109.
\]
因此
\[
\frac{m}{\gcd(m,J+1)}\mid AH^2,
\]
结合 (2)：
\[
\boxed{m<436000\,5^b.}
\tag{13}

另一方面由 (1)、`J>=0`：
\[
\rho>H/100-4000/H^2>H/101
\]
对 `g>=3` 成立。由 (8)：
\[
\boxed{
m>
\frac8{101}\left(\frac52\right)^g5^b.
}
\tag{14}

(13),(14) 消掉 `5^b`：
\[
\left(\frac52\right)^g<5,504,500.
\]
而
\[
(5/2)^{17}>5,504,500.
\]
故
\[
\boxed{g<=16.}
\tag{15}

---

## 6. exact large-layer certificate

脚本

`scripts/exact-lift/a1-only/research-checks/top-layer/check_a1_k2gm2_pure5_phase_divisor_certificate.py`

枚举
\[
5\le g\le16,
\quad J=0,\dots,108,
\]
六类型与所有满足 (3),(4),(14)、`m<=b1Q0` 的 `b`。

每个 state 用 (11),(12) 枚举 exact `a`，恢复 `m`，检查 (9)，最后只检查必要条件
\[
m\mid b_1Q_0.
\]

输出并断言
\[
\boxed{328308\text{ states},}
\]
\[
\boxed{23554\text{ gap-}a\text{ candidates},}
\]
\[
\boxed{0\text{ divisor survivors}.}
\tag{16}

所以
\[
\boxed{g>=5\Longrightarrow\text{pure-5 empty}.}
\tag{17}

---

## 7. `g=3,4` full terminal certificate

脚本

`scripts/exact-lift/a1-only/research-checks/top-layer/check_a1_k2gm2_small_layers_full_terminal.py`

不使用 prime-shape 假设，直接枚举全部 `2/5`-smooth `L`、divisor `M` 与两个 formal roots。

输出：
\[
\boxed{g=3:\ 5,408,362\text{ tests},}
\]
\[
\boxed{g=4:\ 9,450,518\text{ tests},}
\]
两层 survivor 都是
\[
\boxed0.
\tag{18}

因此小层 pure-5 当然也为空。

---

## 8. closure

由 (17),(18)：
\[
\boxed{
 d=2,\quad r=s=1,\quad k=2g-2,\quad L=5^b
 \Longrightarrow\text{empty}.
}
