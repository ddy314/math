# A1 top layer: `k=2g` pure-5 positive-root and mod-4 orientation

> 日期：2026-08-22。
>
> 依赖：`top-layer-k2g-pure5-real-phase-shell.md`、`top-layer-k2g-pure5-odd-orientation.md`、global `kappa` square terminal、`decimal-height-synchronization.md`。
>
> 范围：
> \[
> d=2,\quad r=s=1,\quad g\ge1,\quad k=2g,\quad J=0,
> \]
> primitive pruning 后
> \[
> (z,w)=(1,1),(1,3),
> \]
> 且当前唯一 prime shape
> \[
> L=5^b,\qquad b\ge2\text{ even}.
> \]

状态：**已严格完成。** 本文证明：

1. 实际第三块只能对应较大的形式根 `x_+`，而 `x_-<0`；
2. `b1`-side 被 `m` 选中的 whole primary blocks 只能来自 `p=1 mod 4`；
3. 因而在 pure-5 resonance normal form 中
   \[
   s\equiv q\equiv1\pmod4,
   \qquad
   v\equiv3\pmod4.
   \]

---

## 1. explicit prefix

令
\[
H:=10^g.
\]
当前两型均有
\[
b_1=10H^4-w,
\qquad
Q_0=10b_1+1,
\]
\[
G=Hb_1,
\qquad
D=H^2Q_0,
\]
以及
\[
a_1=H(100H^4+41-10w),
\qquad
a_2=10H^4-1,
\]
\[
C=a_1(10H^4)+a_2.
\]
所以
\[
C=1000H^9+10(41-10w)H^5+10H^4-1.
\tag{1}
\]
因为 `w=1` 或 `3`，有 `41-10w<=31`；又 `H>=10`，故
\[
\boxed{C<1001H^9.}
\tag{2}
\]
同时
\[
Q_0=100H^4-(10w-1)>99H^4,
\]
所以
\[
\boxed{D>99H^6.}
\tag{3}

---

## 2. 两个 normalized roots 的和小于 `0.021`

由 global root formula，normalized roots
\[
x_\sigma=\frac{X_\sigma}{Y}
\]
满足
\[
X_++X_-=2\kappa G^2C,
\qquad
Y=\kappa^2(\kappa+2G).
\]
又由
\[
\rho=\frac{10^gQG}{\kappa}
\]
和 `D=10^gQ`，直接化简得到
\[
\boxed{
x_++x_-
=\frac{2C\rho^2}{D(D+2\rho)}.
}
\tag{4}
\]

当前 slope window 给
\[
0<\rho<H.
\]
因此由 (2)-(3)，
\[
0<x_++x_-
<\frac{2CH^2}{D^2}
<\frac{2002}{9801H}.
\]
因 `H>=10`，
\[
\boxed{
0<x_++x_-<\frac{2002}{98010}<\frac{21}{1000}<\frac1{10}.
}
\tag{5}

---

## 3. 实际第三根全局固定为 `x_+`

合法第三块必须满足 exact decimal window
\[
\boxed{\frac1{10}\le x<1.}
\tag{6}
\]
而按定义
\[
x_+\ge x_-.
\]
若实际根是 `x_-`，则 `x_+>=x_- >=1/10`，从而
\[
x_++x_-\ge\frac15,
\]
与 (5) 矛盾。

因此实际根只能是
\[
\boxed{x=x_+.}
\tag{7}
\]
再由 (5)-(6)：
\[
x_-
=(x_++x_-)-x_+
<\frac{21}{1000}-\frac1{10}<0.
\]
所以
\[
\boxed{x_-<0.}
\tag{8}

这说明 pure-5 terminal 的 real sign 已完全固定；后续所有 local decimal cancellation 必须支持同一个 `+` sign。

---

## 4. selected `b1` primary blocks 只能是 `1 mod 4` primes

`top-layer-k2g-pure5-odd-orientation.md` 已证明，`m` 在 `b1` 侧按完整 primary blocks 选择。写
\[
m=sq,
\qquad
b_1=su,
\qquad
Q_0=qv,
\qquad
(s,u)=1.
\tag{9}
\]

固定一个被选择的 odd primary block
\[
p^E\Vert s.
\]
因为整个 `p^E` 已进入 `m`，在当前 `kappa` 中
\[
p\nmid\kappa.
\tag{10}
\]
另一方面 `p|b1|G`，且 `(b1,Q0)=1`，所以
\[
p\nmid D.
\]
原第一分数既约给 `p\nmid a1`；于是
\[
N=(a_1H)^2+(a_2b_1)^2
\equiv(a_1H)^2\not\equiv0\pmod p.
\tag{11}
\]

使用 square terminal 的等价形式
\[
W^2
=\kappa^2G^2C^2
-\kappa D^2N(\kappa+2G).
\tag{12}
\]
模 `p`，因 `p|G` 而 `p\nmid\kappa DN`：
\[
W^2
\equiv
-\kappa^2D^2N
\equiv
-(\kappa D a_1H)^2
\pmod p.
\tag{13}
\]
右侧非零。故 `-1` 必须是模 `p` 二次剩余，于是
\[
\boxed{p\equiv1\pmod4.}
\tag{14}

所以 `s` 的所有 prime divisors 均为 `1 mod 4`，从而
\[
\boxed{s\equiv1\pmod4.}
\tag{15}

---

## 5. high-2 resonance 固定 `q,v` 的 mod-4 orientation

沿用 pure-5 resonance normal form
\[
c:=5^{2g+b},
\]
以及
\[
\kappa+2G
=2^{g+1}5^g u(s+cv).
\]
同步条件给
\[
v_2(s+cv)=2g+\frac{3b}{2}-1\ge4.
\tag{16}
\]
乘以 odd `q`：
\[
\boxed{
2^{2g+3b/2-1}\mid m+cQ_0.
}
\tag{17}
\]

由于 `b` 为偶数，`2g+b` 为偶数，所以
\[
c\equiv1\pmod4.
\]
又 `b1` 为 odd，故
\[
Q_0=10b_1+1\equiv3\pmod4.
\]
从 (17) 模 4：
\[
\boxed{m\equiv1\pmod4.}
\tag{18}

而 `m=sq` 与 (15) 给
\[
\boxed{q\equiv1\pmod4.}
\tag{19}
最后 `Q0=qv` 且 `Q0=3 mod 4`，故
\[
\boxed{v\equiv3\pmod4.}
\tag{20}

因此 Q-side complement 必含 `3 mod 4` orientation；与此同时实际 decimal root 已由 (7) 全局固定为 `+` sign。

---

## 6. 当前 terminal

当前 pure-5 边界必须同时满足
\[
\boxed{x=x_+,\qquad x_-<0,}
\]
\[
\boxed{s\equiv q\equiv1\pmod4,\qquad v\equiv3\pmod4,}
\]
以及前文 one-sided `b1` complement law
\[
\boxed{\gcd(u,s+cv)=1,\qquad u\mid s+2cv.}
\]

后续应把 `v=3 mod 4` 的 Q-side primary mass 与固定的 `+` root square-lifting 对齐；不能再允许不同 Q-primary blocks 自由选择不同的 global root sign。