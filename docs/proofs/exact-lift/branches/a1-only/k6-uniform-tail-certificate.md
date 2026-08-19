# A1 minimal diagonal: uniform `k=g=6` tail certificate

> 日期：2026-08-19。本文把此前逐层推进到 `ell>=8` 的 `k=6` tail 改写成一个与 `ell` 无关的统一有限证书，并关闭整个 `k=g=6` minimal diagonal。

当前范围：

\[
d=2,\qquad r=s=1,\qquad k=g=6.
\]

结论：

\[
\boxed{k=g=6\text{ minimal diagonal is empty}.}
\]

状态：**已严格完成，并有精确整数/有理数脚本复核。**

---

## 1. 已有输入

写

\[
\rho=\frac{b_3}{10^\ell}=h2^x5^y,
\qquad \gcd(h,10)=1.
\]

odd-prime supply theorem 给出：对固定 `w`，`h` 只能属于有限集合 `H_{6,w}`；其大小为

\[
|H_{6,1}|=64,\quad |H_{6,2}|=32,\quad |H_{6,3}|=2,\quad |H_{6,4}|=8.
\]

第三分母位数给出

\[
10^5\le \rho<10^6.
\tag{1}
\]

positive residual theorem 又给出。令

\[
N_0=j-10^6+1\in\mathbf Z,
\]

则

\[
\boxed{
5.09\cdot10^{-6}
<N_0-\rho
<50.45\cdot10^{-6}.
}
\tag{2}
\]

因此任何 candidate 的 `rho` 都必须从下方落在某个整数 `N_0` 的极窄单侧邻域内。

minimal-diagonal valuation normal form 还给出

\[
X_0=Y_0=6,
\]

以及 resonance thresholds

\[
x_*=2v_2(w)-1-6-v_2(N),
\qquad
y_*=-6-v_5(N).
\tag{3}
\]

cross-corridor exclusion 为

\[
x>x_*,\ y<y_*,\ x>6\Longrightarrow\bot,
\tag{4}
\]

\[
x<x_*,\ y>y_*,\ y>6\Longrightarrow\bot.
\tag{5}
\]

---

## 2. 对全部 moving prefix 审计 `v_2(N),v_5(N)`

由 near-integer decade，可能的整数中心只需取

\[
10^5\le N_0\le10^6.
\]

对六个 `(z,w)` 类型，把

\[
j=N_0+10^6-1,
\]

代入

\[
a_1=10^{20}+(5-z-w)10^7+j,
\]

\[
b_1=10^{13}-w,
\qquad
a_2=10^{13}-z,
\]

\[
N=a_1^2+(a_2b_1)^2.
\]

对整个整数区间做精确有限审计。得到：

| `(z,w)` | `max v2(N)` | `max v5(N)` |
|---|---:|---:|
| `(1,1)` | 1 | 9 |
| `(1,2)` | 3 | 8 |
| `(1,3)` | 1 | 8 |
| `(1,4)` | 5 | 9 |
| `(3,1)` | 1 | 8 |
| `(3,2)` | 3 | 9 |

代回 (3)，六类型统一满足

\[
\boxed{x_*\ge-8,}
\qquad
\boxed{y_*\ge-15.}
\tag{6}
\]

注意这里扫描的是全部 `N_0`，没有先施加 `gcd(a_1,b_1)=1` 或 `K>0`；因此得到的是 admissible prefixes 的安全超集上界。

---

## 3. cross-corridor 把无限指数平面压成有限盒

由 (4)、(6)：若

\[
x>6,\qquad y<-15,
\]

则必有 `x>x_*`、`y<y_*`，故 impossible。因此

\[
\boxed{x>6\Longrightarrow y\ge-15.}
\tag{7}
\]

同理由 (5)：

\[
\boxed{y>6\Longrightarrow x\ge-8.}
\tag{8}
\]

现在利用 decade (1) 和 finite `h` supply 把每个坐标都封住。

令

\[
H_{\max}=\max_{w,h\in H_{6,w}}h
=1406469760899873417721519.
\]

### `x` 的上界

若 `x<=6` 已有界；若 `x>6`，由 (7) 有 `y>=-15`，并且 `h>=1`，所以

\[
\rho\ge2^x5^{-15}<10^6.
\]

精确比较幂得到

\[
\boxed{x\le54.}
\tag{9}
\]

### `x` 的下界

若 `x>=-8` 已有界；若 `x<-8`，由 (8) 的逆否形式在允许区中只能有 `y<=6`。于是

\[
10^5\le\rho\le H_{\max}2^x5^6.
\]

精确比较给出

\[
\boxed{x\ge-77.}
\tag{10}
\]

### `y` 的上界

若 `y>6`，由 (8) 有 `x>=-8`，故

\[
\rho\ge2^{-8}5^y<10^6,
\]

从而

\[
\boxed{y\le12.}
\tag{11}
\]

### `y` 的下界

若 `y<-15`，由 (7) 的允许区形式只能有 `x<=6`。于是

\[
10^5\le\rho\le H_{\max}2^65^y,
\]

精确比较得到

\[
\boxed{y\ge-29.}
\tag{12}
\]

因此任何 `k=6` candidate 都落入统一有限盒

\[
\boxed{
-77\le x\le54,
\qquad
-29\le y\le12.
}
\tag{13}
\]

这里已经完全消除了第三块位数 `ell`。

---

## 4. 完整 finite supply + near-integer certificate

对每个

\[
w\in\{1,2,3,4\},
\quad h\in H_{6,w},
\quad -77\le x\le54,
\quad -29\le y\le12,
\]

先施加两个 universal cross-corridor exclusion

\[
(x>6\ \&\ y<-15)
\quad\text{or}\quad
(y>6\ \&\ x<-8),
\]

再用精确有理数计算

\[
\rho=h2^x5^y.
\]

落入 decade (1) 的状态总数为

\[
\boxed{8679.}
\]

对每个这样的 `rho`，整数中心被唯一确定为

\[
N_0=\lceil\rho\rceil.
\]

最后检查单侧 gap (2)。结果：

\[
\boxed{
\#\{\text{near-integer hits}\}=0.
}
\tag{14}
\]

因此不存在任何满足所有必要条件的 `rho`，无论 `ell` 取何值。

于是得到

\[
\boxed{k=g=6\text{ 整个 minimal diagonal 为空}.}
\]

---

## 5. 意义

此前的 `ell=5,6,7` shell certificates 仍然是正确的局部证书，但现在被本结果统一覆盖。

更重要的是，本证明展示了新的无界层策略：

1. 对固定 `k` 先在全部整数中心上审计 `v_2(N),v_5(N)`；
2. 用 resonance + cross-corridor 得到 `x_*,y_*` 的统一下界；
3. 用 finite odd-prime supply 与 decade window 把 `(x,y)` 压成有限盒；
4. 最后只检查 one-sided near-integer gap。

这条路线不再枚举第三块位数 `ell`，因此适合继续攻击 `k>=7`。