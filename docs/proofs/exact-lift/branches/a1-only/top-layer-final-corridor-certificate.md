# A1 top layer: final `k-g=1,2` corridor certificate

> 日期：2026-08-22。
>
> 依赖：`top-layer-uniform-offdiagonal-tail-center.md`、`top-layer-final-corridor-reduction.md`、`global-terminal-bridge.md`、`decimal-height-synchronization.md`。
>
> 可复核脚本：
>
> `scripts/exact-lift/a1-only/research-checks/top-layer/check_a1_final_corridor_certificate.py`

状态：**严格关闭。** 本文关闭
\[
\boxed{
d=2,\qquad r=s=1,\qquad k-g\in\{1,2\}.
}
\]

---

## 1. analytic reduction before the certificate

`top-layer-final-corridor-reduction.md` 已证明：

1. mixed `L=2^a5^b` with `a,b>0` 全空；
2. pure-2 只需七个小层
   \[
   (g,c)=(2,1),(3,1),(4,1),(5,1),(6,1),(3,2),(4,2),
   \qquad c=k-g;
   \]
3. pure-5 只可能
   \[
   (g,c,w)=(2,1,2)\text{ or }(2,1,4).
   \]

所以 finite certificate 不承担任何无界步骤。

---

## 2. `J` is not enumerated

uniform tail center 给
\[
0<((J+1)\tau L-M)H\tau<40L,
\qquad \tau=10^c.
\tag{1}
\]
并且
\[
J+1=\left\lceil\frac{M}{L\tau}\right\rceil.
\tag{2}
\]

因此对每个 divisor state `(M,L)`，`J` 是唯一整数，不存在 `10^u` 规模的额外枚举。

脚本完整枚举：

- hard-coded、逐 prime 验证的 `b1,Q0` 完整分解；
- `M | H tau^2 b1 Q0` 的全部 divisors；
- pure-2 或 pure-5 axis 上 slope-compatible 的全部 `L`；
- (1) 的 exact integer thin-shell inequality。

经过这一层，所有七个 small layers 加 pure-5 exceptional types 合计仅剩
\[
\boxed{26}
\]
个 `(g,c,w,shape,M,L,J)` phase states。

其中分布为：

- `(g,c,w,shape)=(2,1,1,pure2)`：11 states；
- `(2,1,4,pure2)`：4 states；
- `(2,1,4,pure5)`：11 states；
- 其余解析允许的小层：phase hit 为 0。

特别地 `(2,1,2,pure5)` 虽通过 analytic height bound，但 thin shell 自身已经给 0 state。

---

## 3. global terminal test

对 26 个 phase states，按合法 `(z,w)` types 展开后共进行
\[
\boxed{37}
\]
次 global terminal test。

每次重新构造完整 prefix：
\[
b_1=10^{2g+2c+1}-w,
\qquad b_2=10^c,
\]
\[
a_2=10^{2g+2c+1}-z,
\]
\[
a_1
=10^{3g+2c+2}
+\bigl(10(5-z-w)+1\bigr)10^g
+J.
\]
再构造
\[
Q=10^c(10b_1+1),
\qquad G=10^cb_1,
\qquad D=10^gQ,
\]
\[
C=a_1 10^{2g+2c+1}+a_2,
\qquad
N=(a_1b_2)^2+(a_2b_1)^2,
\]
\[
K=G^2C^2-D^2N.
\]

由
\[
\kappa=\frac{10^gLQG}{M}
\]
检查 global square
\[
\boxed{
W^2=\kappa(\kappa K-2GD^2N).
}
\tag{3}
\]

只有当 (3) 为非负整数平方时才继续；然后对两个 signs
\[
X_\sigma=\kappa G^2C+\sigma(\kappa+G)W,
\]
\[
Y=\kappa^2(\kappa+2G)
\]
进行 exact decimal recovery：

1. reduced root `u/v` 满足
   \[
   1/10\le u/v<1;
   \]
2. `v` 只含 `2,5`；
3. decimal-height synchronization
   \[
   \max(v_2(v),v_2(L))
   =
   \max(v_5(v),v_5(L))
   \ge1;
   \]
4. numerator 与 `M` 的 odd-to-10 part 互素。

结果：
\[
\boxed{
\text{global-terminal survivors}=0.
}
\tag{4}

脚本最终断言：

```text
phase_states=26
terminal_tests=37
survivors=0
```

全程只使用整数运算、`isqrt`、gcd、valuation 与 primality-check；没有浮点判定或概率筛选。

---

## 4. conclusion

analytic reduction 与 certificate 联立，得到
\[
\boxed{
 d=2,\quad r=s=1,\quad k-g\in\{1,2\}
 \Longrightarrow\text{empty}.
}
\]

这补上 minimal-surplus off-diagonal 的最后两个 corridor。