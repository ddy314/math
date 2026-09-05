# A1 top layer: uniform pure-5 collapse in the stable inner wedge

> 日期：2026-08-22。
>
> 依赖：`top-layer-inner-wedge-uniform-phase.md`、`top-layer-inner-wedge-digit-lock.md`。
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
> 并假设稳定 inner-wedge 条件
> \[
> \boxed{g-u\ge3.}
> \]

状态：**pure-5 denominator axis 严格全空。**

即
\[
\boxed{L=5^b\Longrightarrow\text{empty}.}
\]

---

## 1. small `b` 已被 real gap 排除

uniform phase theorem 给
\[
L>\frac{H^2}{40\cdot10^u}.
\tag{1}

若
\[
b\le u,
\]
则
\[
L=5^b\le5^u.
\]
而 `g-u>=3` 给
\[
\frac{H^2}{40\cdot10^u}
=\frac{10^{2g-u}}{40}
\ge\frac{10^{u+6}}{40}
>5^u.
\]
与 (1) 矛盾。

所以任何 pure-5 candidate 必须满足
\[
\boxed{b>u.}
\tag{2}

因此可使用 uniform pure-5 low-2 resonance normal form。

---

## 2. pure-5 normal form

`top-layer-inner-wedge-uniform-phase.md` 给：
\[
\boxed{b\equiv u\pmod2,}
\]
\[
\boxed{
M=2^{2g-u-1}m,
}
\qquad
(m,10)=1,
\qquad
m\mid b_1Q_0.
\tag{3}

本文甚至不需要继续使用 exact 2-adic resonance；phase gap 与 divisor structure已经足够矛盾。

令
\[
s:=J+1.
\]
leading-decimal lock 给
\[
\boxed{10^{u-1}<s\le10^u.}
\tag{4}

又
\[
\tau=10^{g-u}=2^{g-u}5^{g-u}.
\]
positive integer gap
\[
A:=s\tau5^b-M
\]
因此精确因出
\[
\boxed{
A=2^{g-u}a,
}
\tag{5}
其中
\[
\boxed{
a=s5^{g-u+b}-2^{g-1}m>0.}
\tag{6}

---

## 3. `m/gcd(m,s)` divides the tiny gap integer

由 `(m,10)=1`，特别地 `5` 是模 `m` 的 unit。由 (6)：
\[
a\equiv s5^{g-u+b}\pmod m.
\]
所以
\[
\gcd(m,a)=\gcd(m,s).
\]
因此
\[
\boxed{
\frac{m}{\gcd(m,s)}\mid a.
}
\tag{7}

由 (4)：
\[
\gcd(m,s)\le s\le10^u,
\]
于是
\[
\boxed{m\le sa\le10^u a.}
\tag{8}

---

## 4. phase upper bound on `a`

uniform phase gap 是
\[
0<AH^2<40\cdot10^u5^b.
\]
代入 (5) 与
\[
H^2=2^{2g}5^{2g}
\]
：
\[
2^{3g-u}5^{2g}a
<40\cdot2^u5^{u+b}.
\]
所以
\[
\boxed{
a<40\,2^{2u-3g}5^{u+b-2g}.}
\tag{9}

结合 (8)：
\[
\boxed{
m<40\,2^{3u-3g}5^{2u+b-2g}.}
\tag{10}

---

## 5. slope gives incompatible lower bound

由 slope window
\[
\rho=M/L\ge H/10
\]
与 (3)：
\[
\frac{2^{2g-u-1}m}{5^b}
\ge\frac{H}{10}.
\]
整理：
\[
\boxed{
m\ge2^{u-g}5^{g+b-1}.}
\tag{11}

(10),(11) 联立并消掉 `b`：
\[
1<40\,2^{2u-2g}5^{2u-3g+1}.
\tag{12}

记
\[
d:=g-u=k-g.
\]
稳定区 `g-u>=3` 即
\[
d\ge3.
\]
于是 (12) 右边写成
\[
40\,2^{-2d}5^{1-u-3d}.
\]
因为 `u>=1,d>=3`：
\[
40\,2^{-2d}5^{1-u-3d}
\le40\cdot2^{-6}5^{-9}<1,
\]
与 (12) 矛盾。

所以
\[
\boxed{L=5^b\Longrightarrow\text{empty}.}
\tag{13}

---

## 6. consequence

稳定 inner wedge 中：

- mixed `2^a5^b,a,b>0` 已由 `top-layer-inner-wedge-mixed-collapse.md` 关闭；
- pure-2 已由 `top-layer-inner-wedge-pure2-collapse.md` 关闭；
- pure-5 由本文关闭。

因此整个 stable inner wedge 已空。
