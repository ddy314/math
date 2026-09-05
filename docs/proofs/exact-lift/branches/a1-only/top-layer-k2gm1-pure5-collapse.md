# A1 top layer: `k=2g-1` pure-5 collapse

> 日期：2026-08-22。
>
> 依赖：`top-layer-minimal-offdiagonal-J-compression.md`、`top-layer.md` 的 exact positive-excess identity、global `kappa` square、`decimal-height-synchronization.md`。
>
> 范围：
> \[
> d=2,\qquad r=s=1,\qquad g\ge2,\qquad k=2g-1.
> \]
>
> `J` compression 已给
> \[
> J\in\{0,1,\dots,9\}.
> \]

状态：**已严格关闭 pure-5 denominator branch**
\[
\boxed{L=5^b.}
\]

大层 `g>=4` 使用无因子分解的 phase/resonance certificate；`g=2,3` 直接枚举完整 global terminal，不借用大层 valuation simplification。

---

## 1. `k=2g-1` 的显式 prefix

令
\[
H:=10^g,
\qquad
\tau:=10^{g-1}=H/10.
\]

因为
\[
2k+1=4g-1,
\]
故
\[
\boxed{b_1=10^{4g-1}-w,}
\qquad
\boxed{b_2=\tau,}
\]
\[
\boxed{a_2=10^{4g-1}-z,}
\]
以及
\[
\boxed{
 a_1=H^5+\bigl(10(5-z-w)+1\bigr)H+J.
}
\tag{1}
\]

六类型仍为
\[
(z,w)\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
\tag{2}
\]

写
\[
Q_0:=10b_1+1.
\]
则
\[
Q=\tau Q_0,
\qquad
G=\tau b_1,
\qquad
D=HQ=H\tau Q_0.
\tag{3}
\]

---

## 2. off-diagonal 超薄 gap

把 `top-layer.md` 的 positive-excess identity 在 `k=2g-1` 中保留第三 contact 主项，可得
\[
\boxed{
0<(J+1)\tau-\rho<\frac{400}{H^2}.
}
\tag{4}
\]

这条式子是本分支的 real phase input。

现在假设 pure-5：
\[
\boxed{L=5^b.}
\tag{5}
\]

令
\[
A:=((J+1)\tau)L-M\in\mathbf Z_{>0}.
\]
由 (4)：
\[
\boxed{0<AH^2<400\,5^b.}
\tag{6}
\]

特别地 `A>=1` 给
\[
\boxed{5^b>H^2/400.}
\tag{7}
\]
因此对 `g>=2` 已自动排除 `b=1`；后文大层中 pure-5 high parity 将给 `b>=3` odd。

---

## 3. `g>=4` 的 pure-5 local normal form

以下先假设
\[
\boxed{g\ge4.}
\]

记
\[
e:=v_2(w)\in\{0,1,2\}.
\]

由 (1)-(3)：
\[
v_5(G)=g-1,
\qquad
v_5(D)=2g-1,
\]
且 `a2,b1,Q0,C,N` 在 5-adic side 均为 units，所以
\[
\boxed{v_5(N)=0,}
\qquad
\boxed{v_5(K)=2g-2.}
\tag{8}

base integer 满足
\[
v_5(10^gQG)=3g-2.
\]
若 `L=5^b,b>0`，则
\[
\boxed{v_5(\kappa)=3g-2+b.}
\tag{9}

当 `b>=2` 时 `kappa` square 的第二项严格更浅：
\[
v_5(\kappa K)=5g-4+b,
\]
\[
v_5(2GD^2N)=5g-3.
\]
于是 square parity 给
\[
\boxed{b\text{ 为奇数}.}
\tag{10}

结合 (7)：
\[
\boxed{b\ge3\text{ odd}.}
\tag{11}

root numerator / denominator 的直接 valuation 给 5-side completion height
\[
\boxed{
H_5=2g+\frac{3b-3}{2}.
}
\tag{12}

---

## 4. 2-side 的唯一 low resonance

对 `g>=4`，因为第一平方项在 `N` 中比第二项深，
\[
\boxed{v_2(N)=2e,}
\qquad
\boxed{v_2(K)=2g-2+2e.}
\tag{13}

又
\[
v_2(10^gQG)=3g-2+e.
\]

要让 2-side completion height追上 (12)，唯一可能的 low resonance 是
\[
\boxed{v_2(\kappa)=g+e.}
\tag{14}

所以
\[
\boxed{v_2(M)=2g-2.}
\tag{15}

写
\[
\boxed{M=2^{2g-2}m,}
\qquad
(m,10)=1.
\tag{16}

由于 `M|10^gQG`：
\[
\boxed{m\mid b_1Q_0.}
\tag{17}

从 `kappa+2G` 的 exact factorization 可得，令
\[
c:=5^{2g+b-1},
\]
则
\[
v_2(\kappa+2G)
=g+e+v_2(m+cQ_0).
\]
两个共轭 normalized root 的 2-denominator depths 恰为
\[
\{1,\ 1+v_2(m+cQ_0)\}.
\]
因此 exact decimal-height synchronization 与 (12) 强迫
\[
\boxed{
v_2(m+5^{2g+b-1}Q_0)
=2g+\frac{3b-5}{2}.
}
\tag{18}

---

## 5. gap integer `a`

由 (6)、(16) 定义
\[
\boxed{
 a:=(J+1)5^{g+b-1}-2^{g-1}m.
}
\tag{19}

则
\[
A=2^{g-1}a,
\qquad a\in\mathbf Z_{>0}.
\]

于是 (6) 等价于
\[
0<
2^{3g-1}5^{2g-b}a
<400.
\]
也即
\[
\boxed{
1\le a
\le
\left\lfloor
\frac{400\,5^b-1}{2^{3g-1}5^{2g}}
\right\rfloor.
}
\tag{20}

另一方面把 (18) 乘 `2^(g-1)`。令
\[
R:=2g+\frac{3b-5}{2},
\qquad
E:=R+g-1,
\]
以及
\[
B_0
:=(J+1)5^{g+b-1}
+2^{g-1}5^{2g+b-1}Q_0.
\]
由 (19)：
\[
B_0-a=2^{g-1}(m+5^{2g+b-1}Q_0).
\]
故 (18) 精确等价于
\[
\boxed{
v_2(B_0-a)=E.}
\tag{21}

即
\[
\boxed{
a\equiv B_0+2^E\pmod{2^{E+1}}.}
\tag{22}

(20),(22) 把每个 `(g,w,J,b)` state 的可能 `a` 压成一个 exact arithmetic progression 与一个有限区间的交。

---

## 6. 一个无需 resultant 的高度界：`g<=10`

由 (6)：
\[
AH^2
=5^b\frac{(J+1)H^3}{10}
-H^2M.
\]
又 `M=2^(2g-2)m`，所以模 `m`：
\[
AH^2
\equiv
5^b\frac{(J+1)H^3}{10}
\pmod m.
\]

因为 `(m,10)=1`，
\[
\gcd\left(m,\frac{(J+1)H^3}{10}\right)
=\gcd(m,J+1)
\le J+1\le10.
\]
因此
\[
\boxed{
\frac{m}{\gcd(m,J+1)}\mid AH^2.
}
\]
结合 (6)：
\[
\boxed{m<4000\,5^b.}
\tag{23}

另一方面，由 (4)、`J>=0`：
\[
\rho>\tau-400/H^2.
\]
对 `g>=2,H>=100`：
\[
\tau-400/H^2>H/11.
\]
于是
\[
\frac{2^{2g-2}m}{5^b}=\rho>H/11,
\]
即
\[
\boxed{
m>
\frac4{11}\left(\frac52\right)^g5^b.
}
\tag{24}

(23),(24) 消掉 `5^b`：
\[
\left(\frac52\right)^g<11000.
\]
而
\[
(5/2)^{11}>11000.
\]
所以
\[
\boxed{g\le10.}
\tag{25}

因此所有 `g>=4` pure-5 states 已严格落入
\[
\boxed{4\le g\le10.}
\]

---

## 7. 大层 exact certificate

脚本：

`scripts/exact-lift/a1-only/research-checks/top-layer/check_a1_k2gm1_pure5_phase_divisor_certificate.py`

它只使用整数运算，不 factor `b1,Q0`。

有限盒：
\[
4\le g\le10,
\qquad
J=0,\dots,9,
\]
六类型，以及满足 (7)、(11)、(24) 与 `m<=b1Q0` 的所有 odd `b`。

脚本逐 state 用 (20),(22) 枚举 exact `a`，再由 (19) 恢复 `m`，检查 (18)，最后只检查最原始必要条件 (17)。

输出并断言
\[
\boxed{12420\text{ states},}
\]
\[
\boxed{1457\text{ gap-}a\text{ candidates},}
\]
\[
\boxed{0\text{ divisor survivors}.}
\tag{26}

所以
\[
\boxed{g\ge4\Longrightarrow\text{pure-5 empty}.}
\tag{27}

---

## 8. `g=2,3`：直接 global-terminal certificate

`g=2,3` 不需要、也不应强行套用 §3-4 的大层 valuation simplification。

脚本：

`scripts/exact-lift/a1-only/research-checks/top-layer/check_a1_k2gm1_pure5_small_layers.py`

直接完整 factor 这两个小层的 `b1,Q0`，并枚举所有满足 slope window
\[
H/10\le M/5^b<H
\]
的 5-unit divisor `M|10^gQG`。

每个 state 直接检查：

1. global `kappa` square
   \[
   \kappa(\kappa K-2GD^2N)=W^2;
   \]
2. 两个 formal normalized roots；
3. root 是否在 `[1/10,1)`；
4. reduced denominator 是否只含 `2,5`；
5. exact decimal-height synchronization；
6. odd-part numerator coprimality。

这里甚至没有使用 primitive gcd pruning，因此仍是在一个必要条件超集上检查。

输出：
\[
\boxed{g=2:\ 34160\text{ exact terminal tests},}
\]
\[
\boxed{g=3:\ 40170\text{ exact terminal tests},}
\]
且两层均有
\[
\boxed{0\text{ survivors}.}
\tag{28}

`g=1` 时 `k=2g-1=g=1`，属于已关闭的 minimal diagonal，不是当前 off-diagonal。

---

## 9. closure

由 (27),(28)：
\[
\boxed{
 d=2,\quad r=s=1,\quad k=2g-1,\quad L=5^b
 \Longrightarrow\text{empty}.
}
\tag{29}

所以 `k=2g-1` 当前若仍有 candidate，只能落在 pure-2 branch
\[
\boxed{L=2^a.}
\]

下一步只需关闭该 pure-2 branch；完成后整个 `k=2g-1` boundary 即关闭。
