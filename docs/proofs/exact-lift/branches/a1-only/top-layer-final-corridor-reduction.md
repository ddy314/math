# A1 top layer: final `k-g=1,2` corridor reduction

> 日期：2026-08-22。
>
> 依赖：`top-layer-uniform-offdiagonal-tail-center.md` 与 global divisor
> \[
> M\mid10^gQG.
> \]
>
> 范围：
> \[
> d=2,\qquad r=s=1,
> \qquad c:=k-g\in\{1,2\}.
> \]

状态：**已严格完成 reduction。** mixed denominators 全空；pure axes 被压到七个小 `(g,c)` 层，其中 pure-5 甚至只剩一个 typewise 小层。

令
\[
H:=10^g,
\qquad
\tau:=10^c,
\qquad
L=2^a5^b,
\qquad
\rho=M/L.
\]
由 uniform ultrathin center，令
\[
s:=J+1,
\qquad
A:=s\tau L-M.
\]
则
\[
\boxed{
10^{g-c-1}<s\le10^{g-c},
}
\tag{1}
\]
以及
\[
\boxed{
A\in\mathbf Z_{>0},
\qquad
AH\tau<40L.
}
\tag{2}
\]

当前 prefix 有
\[
b_1=10^{2g+2c+1}-w,
\qquad
Q_0=10b_1+1,
\]
\[
Q=\tau Q_0,
\qquad
G=\tau b_1.
\]
因此
\[
10^gQG=H\tau^2b_1Q_0.
\tag{3}
\]
又
\[
v_2(b_1)=e:=v_2(w),
\qquad v_5(b_1)=0,
\qquad v_2(Q_0)=v_5(Q_0)=0.
\tag{4}

---

## 1. mixed `L=2^a5^b`, `a,b>0`, 全空

若 `a,b>0`，由 `(L,M)=1`：
\[
(M,10)=1.
\]
由 (3)，于是
\[
M\mid b_1Q_0.
\]

模 `M` 看
\[
A=s\tau L-M.
\]
因为 `(M,tau L)=1`：
\[
\frac{M}{\gcd(M,s)}\mid A.
\]
所以由 (1)：
\[
M\le sA\le\frac H\tau A.
\]
结合 (2)：
\[
\frac ML
<\frac H\tau\frac{40}{H\tau}
=\frac{40}{\tau^2}
\le\frac{2}{5}.
\]
但第三尾 slope 要求
\[
\frac ML=\rho\ge\frac H{10}\ge10.
\]
矛盾。因此
\[
\boxed{a>0,\ b>0\Longrightarrow\text{empty}.}
\tag{5}

---

## 2. pure-5 axis 的统一高度界

现在
\[
L=5^b,
\qquad b>0.
\]
写
\[
M=2^tm,
\qquad m\text{ 为 }2,5\text{-unit}.
\]
由 (3),(4)：
\[
t\le g+2c+e.
\tag{6}
\]

模 `m` 看 gap `A`。因为 `(m,tau5^b)=1`：
\[
\frac m{\gcd(m,s)}\mid A.
\]
故
\[
m\le sA\le\frac H\tau A.
\]
于是由 (2),(6)：
\[
\rho=\frac M{5^b}
<2^{g+2c+e}\frac H\tau\frac{40}{H\tau}
=
40\frac{2^{g+2c+e}}{10^{2c}}.
\tag{7}
\]

和 slope lower bound
\[
\rho\ge H/10
\]
联立，约去 `2^g5^g` 后得到必要条件
\[
\boxed{
5^{g+2c}<400\,2^e.
}
\tag{8}
\]

对 `c=2`，`g>=3` 且 `e<=2`：
\[
5^{g+4}\ge5^7>1600\ge400\,2^e,
\]
所以 pure-5 全空。

对 `c=1`：若 `g>=3`，
\[
5^{g+2}\ge5^5>1600,
\]
也空。仅 `g=2` 时
\[
5^4=625<400\,2^e
\]
要求 `e>=1`，所以只可能
\[
\boxed{(g,c,w)=(2,1,2)\text{ or }(2,1,4).}
\tag{9}

---

## 3. pure-2 axis 的统一高度界

现在
\[
L=2^a,
\qquad a>0.
\]
写
\[
M=5^tm,
\qquad m\text{ 为 }2,5\text{-unit}.
\]
由 (3),(4)：
\[
t\le g+2c.
\tag{10}
\]

与上节相同，模 `m` 的 gap divisibility 给
\[
m\le sA\le\frac H\tau A.
\]
所以
\[
\rho=\frac M{2^a}
<5^{g+2c}\frac H\tau\frac{40}{H\tau}
=40\frac{5^{g+2c}}{10^{2c}}.
\tag{11}
\]
与 `rho>=H/10` 联立后得到
\[
\boxed{2^{g+2c}<400.}
\tag{12}

因此：

- `c=1`：只需
  \[
  \boxed{2\le g\le6};
  \]
- `c=2`：只需
  \[
  \boxed{3\le g\le4}.
  \]

即 pure-2 只剩七个小层
\[
\boxed{
(g,c)=(2,1),(3,1),(4,1),(5,1),(6,1),(3,2),(4,2).
}
\tag{13}

---

## 4. certificate frontier

综上，`k-g=1,2` 的所有候选已解析压缩成：

1. pure-2 的七个小层 (13)，四个 `w` 全保留；
2. pure-5 只有 (9)；
3. mixed 已由 (5) 统一关闭。

这些层的 `b1,Q0` 都至多 16 位量级，可用完整 factorization + global `kappa` terminal 做精确有限证书。更重要的是 `J` 不需要枚举：由 ultrathin center
\[
J+1=\left\lceil\frac{M}{L\tau}\right\rceil,
\]
再检查
\[
0<((J+1)\tau L-M)H\tau<40L.
\]
因此最终 finite certificate 规模极小。