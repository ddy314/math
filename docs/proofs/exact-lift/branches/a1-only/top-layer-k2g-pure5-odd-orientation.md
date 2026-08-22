# A1 top layer: `k=2g` pure-5 `b1` complement orientation

> 日期：2026-08-22。
>
> 依赖：`top-layer-k2g-prime-shape-collapse.md`、global `kappa` square、`decimal-height-synchronization.md`。
>
> 范围：
> \[
> d=2,\quad r=s=1,\quad g\ge1,\quad k=2g,\quad J=0,
> \]
> primitive pruning 后 `(z,w)=(1,1),(1,3)`，且当前唯一 prime shape
> \[
> L=5^b,\qquad b\ge2\text{ even}.
> \]

状态：**已严格完成。** 本文只使用当前 full-A1 prefix 的 local valuations；不调用 minimal-diagonal 的 `1 mod 4` selector 规则。

最终得到：

1. `b1`-side 在 `m` 中必须按完整 primary blocks 选择；
2. 所有未选择 blocks 都只能走同一个 type-I linear form：
   \[
   \gcd(u,s+cv)=1,
   \qquad
   u\mid s+2cv;
   \]
3. 等价地
   \[
   u\mid m+2c.
   \]

---

## 1. pure-5 的 2-adic resonance normal form

令
\[
H=10^g,
\qquad
Q_0=10b_1+1.
\]
前文给
\[
Q=HQ_0,
\qquad
G=Hb_1,
\qquad
D=H^2Q_0,
\]
以及
\[
v_2(N)=v_5(N)=0,
\qquad
v_2(K)=v_5(K)=2g.
\]

当前
\[
L=5^b,
\qquad b\ge2\text{ even}.
\]
5-side high completion height 为
\[
\boxed{
n=H_5=2g+\frac{3b}{2}.
}
\tag{1}

要让 2-side 达到同一高度，唯一可能是
\[
\boxed{v_2(\kappa)=g+1.}
\tag{2}

在该 resonance 中，令
\[
t_2:=v_2(\kappa+2G).
\]
共轭 numerator 的 2-denominator depths 为
\[
\{1,t_2-g\}.
\]
因此 surviving high sign 必满足
\[
t_2-g=n,
\]
即
\[
\boxed{t_2=3g+\frac{3b}{2}.}
\tag{3}

由于 base integer `10^gQG=H^3b1Q0` 的 2-depth 是 `3g`，(2) 给
\[
\boxed{v_2(M)=2g-1.}
\tag{4}

写
\[
\boxed{M=2^{2g-1}m,}
\qquad
(m,10)=1.
\tag{5}
由 `M|10^gQG`，
\[
\boxed{m\mid b_1Q_0.}
\tag{6}

定义
\[
\boxed{c:=5^{2g+b}.}
\tag{7}

---

## 2. `b1` primary blocks 不能被部分选择

固定奇素数
\[
p^E\Vert b_1.
\]
记
\[
f:=v_p(m),
\qquad
c_p:=E-f=v_p(\kappa).
\]
因为 `(b1,Q0)=1`，有
\[
p\nmid Q_0.
\]
又原第一分数既约，所以
\[
p\nmid a_1.
\]
由
\[
N=(a_1H)^2+(a_2b_1)^2
\]
可知
\[
\boxed{p\nmid DN.}
\tag{8}

假设部分选择：
\[
0<f<E.
\]
则
\[
0<c_p<E=v_p(G).
\]
因此
\[
v_p(\kappa+G)=v_p(\kappa+2G)=c_p.
\tag{9}

从
\[
W^2
=\kappa^2G^2C^2
-\kappa D^2N(\kappa+2G)
\tag{10}
\]
看两项深度：第一项至少
\[
2c_p+2E,
\]
第二项恰为
\[
2c_p.
\]
所以
\[
\boxed{v_p(W)=c_p.}
\tag{11}

normalized root numerator
\[
X_\sigma=\kappa G^2C+\sigma(\kappa+G)W
\]
中第一项深度至少 `c_p+2E>2c_p`，第二项恰为 `2c_p`。故两个 signs 都满足
\[
\boxed{v_p(X_\sigma)=2c_p.}
\tag{12}

而 raw denominator
\[
Y=\kappa^2(\kappa+2G)
\]
有
\[
\boxed{v_p(Y)=3c_p.}
\tag{13}

所以约分后仍残留 `p^{c_p}` 在 denominator 中，与 finite-decimal criterion 矛盾。

因此
\[
\boxed{
v_p(m)\in\{0,E\}
\qquad(p^E\Vert b_1).
}
\tag{14}

这说明 `m` 在 `b1` 侧必须按完整 primary blocks 选择。

---

## 3. whole-block coordinates

由 (14)，定义
\[
\boxed{s:=\gcd(m,b_1),}
\qquad
\boxed{u:=b_1/s.}
\]
则
\[
(s,u)=1
\]
且 `s,u` 分别是完整 `b1` primary blocks 的互补乘积。

由 `(b1,Q0)=1` 与 `m|b1Q0`，还可唯一写
\[
\boxed{m=sq,}
\qquad
\boxed{Q_0=qv,}
\]
其中
\[
(q,b_1)=1,
\qquad
(v,b_1)=1.
\]
于是
\[
\boxed{
\kappa=2^{g+1}5^{3g+b}uv,
}
\tag{15}
\]
\[
\boxed{G=2^g5^g su.}
\tag{16}

由 (15)-(16)：
\[
\boxed{
\kappa+2G
=2^{g+1}5^g u(s+cv),
}
\tag{17}
\]
\[
\boxed{
\kappa+G
=2^g5^g u(s+2cv).
}
\tag{18}

---

## 4. type-II block 不可能

固定完整 complement block
\[
p^a\Vert u.
\]
令
\[
r:=v_p(s+cv),
\qquad
 d:=v_p(s+2cv),
\qquad
 f_C:=v_p(C).
\]
两个 linear forms 的差为 `cv`，而 `p` 不整除 `c,v,s`，所以
\[
\boxed{\gcd(s+cv,s+2cv)=1.}
\tag{19}

假设 type II：
\[
r>0.
\]
则
\[
\boxed{d=0.}
\tag{20}

在 `p` 上有
\[
v_p(\kappa)=v_p(G)=a,
\qquad p\nmid DN.
\]
由 (17)：
\[
v_p(\kappa+2G)=a+r,
\]
由 (18),(20)：
\[
v_p(\kappa+G)=a.
\]

square (10) 两项深度为
\[
4a+2f_C,
\qquad
2a+r.
\]
finite-decimal cancellation 的 local dichotomy 在 type II 中强迫
\[
\boxed{r\ge2a+2f_C.}
\tag{21}

因此
\[
v_p(W)\ge2a+f_C.
\]
从而两个共轭 numerators 都至少满足
\[
\boxed{v_p(X_\pm)\ge3a+f_C.}
\tag{22}

actual decimal sign 还必须完全消掉 raw denominator 中
\[
v_p(Y)=3a+r,
\]
所以
\[
\boxed{v_p(X_\sigma)\ge3a+r.}
\tag{23}

另一方面 exact product identity
\[
\boxed{
X_+X_-
=-\kappa(\kappa+2G)
\left(
\kappa^2G^2C^2-D^2N(\kappa+G)^2
\right)
}
\tag{24}
\]
中，括号内两项深度分别为
\[
4a+2f_C,
\qquad
2a.
\]
第二项严格更浅，所以
\[
v_p(\text{bracket})=2a.
\]
结合
\[
v_p(\kappa)=a,
\qquad
v_p(\kappa+2G)=a+r,
\]
得到
\[
\boxed{v_p(X_+X_-)=4a+r.}
\tag{25}

但 (22)-(23) 给
\[
\begin{aligned}
v_p(X_+X_-)
&\ge(3a+r)+(3a+f_C)\\
&>4a+r,
\end{aligned}
\]
矛盾。

所以
\[
\boxed{p\nmid s+cv}
\tag{26}

对每个 `p|u` 成立，即
\[
\boxed{\gcd(u,s+cv)=1.}
\tag{27}

---

## 5. 所有 complement blocks 强迫进入 type I

由 (27)，对 `p^a||u`：
\[
v_p(\kappa+2G)=a.
\]
所以 raw denominator 在 `p` 上恰有
\[
v_p(Y)=3a.
\]

由 square (10)，此时
\[
v_p(W)=a.
\]
第一 numerator term `kappa G^2 C` 深度至少 `3a`。若
\[
v_p(s+2cv)<a,
\]
则第二 term `(kappa+G)W` 深度严格小于 `3a`，两个 signs 都无法清掉 raw denominator。

因此必要地
\[
\boxed{p^a\mid s+2cv.}
\tag{28}

对所有完整 blocks 相乘：
\[
\boxed{u\mid s+2cv.}
\tag{29}

结合 (27)：
\[
\boxed{
\gcd(u,s+cv)=1,
\qquad
u\mid s+2cv.
}
\tag{30}

---

## 6. 消去 `q,v`

由
\[
m=sq,
\qquad
Q_0=qv,
\]
且 `(q,u)=1`，(29) 等价于乘 `q`：
\[
u\mid m+2cQ_0.
\]
又
\[
Q_0=10b_1+1\equiv1\pmod u.
\]
所以最终得到
\[
\boxed{u\mid m+2c.}
\tag{31}

其中
\[
\boxed{u=b_1/\gcd(m,b_1),\qquad c=5^{2g+b}.}
\]

这是一条完全由当前 full-A1 pure-5 decimal recovery 推出的 one-sided odd orientation；没有使用 minimal-diagonal 的 `3 mod 4` supply selector。

---

## 7. 当前用途

当前 pure-5 terminal 同时满足：

- real phase shell：
  \[
  w=1:\quad29.9<t<30.5,
  \]
  \[
  w=3:\quad21.9<t<22.5;
  \]
- high-2 resonance；
- `m|b1 Q0`；
- `b1`-side whole-block selection (14)；
- one-sided orientation
  \[
  u|m+2\cdot5^{2g+b}.
  \]

下一步应把 (31) 与 phase shell 的 `m` 窄区间联立，优先得到 `u`（等价 selected `s`）的高度限制；然后再处理 Q0-side exceptional blocks。
