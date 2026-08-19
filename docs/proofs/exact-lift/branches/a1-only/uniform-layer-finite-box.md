# A1 minimal diagonal: generic fixed-`k` finite-box theorem

> 日期：2026-08-19。本文把 `k=6` 的统一 tail certificate 抽象成任意固定 `k>=6` 的证明模板，并用它精确关闭 `k=6,...,23`。

当前范围：

\[
d=2,\qquad r=s=1,\qquad k=g\ge6.
\]

核心结论有两层。

第一层是结构定理：**对任意固定 `k`，第三块位数 `ell` 可以完全从搜索中消失，所有 candidate 都落入一个显式有限 `(h,x,y)` 盒。**

第二层是精确证书：对

\[
\boxed{6\le k\le23}
\]

所得有限盒全部没有通过 one-sided near-integer gap 的状态，因此

\[
\boxed{k=g=6,7,\ldots,23\text{ 全部为空}.}
\]

状态：**结构定理严格完成；`k=6..23` 由精确整数/有理数脚本严格复核。**

---

## 1. 固定 `k` 的输入

写

\[
\rho=\frac{b_3}{10^\ell}=h2^x5^y,
\qquad \gcd(h,10)=1.
\]

odd-prime supply theorem 给出有限集合

\[
h\in\mathcal H_{k,w},
\]

其中

\[
h=q\,s,\qquad q\mid Q,
\]

而 `s` 是 `b_1` 中所有 `1 mod 4` odd prime-power blocks 的 whole-block selector。

因此固定 `(k,w)` 后 `h` 的可能值有限，并与 `ell` 无关。

第三分母位数给出 decade

\[
\boxed{10^{k-1}\le\rho<10^k.}
\tag{1}
\]

positive-tail residual theorem 给出整数中心

\[
N_0=j-10^k+1
\]

以及严格单侧窗口

\[
\boxed{
5.09\,10^{-k}<N_0-\rho<50.45\,10^{-k}.
}
\tag{2}
\]

minimal-diagonal valuation normal form 给出

\[
X_0=Y_0=k,
\]

\[
x_*=2v_2(w)-1-k-v_2(N),
\qquad
y_*=-k-v_5(N).
\tag{3}
\]

cross-corridor exclusions 为

\[
x>x_*,\ y<y_*,\ x>k\Longrightarrow\bot,
\tag{4}
\]

\[
x<x_*,\ y>y_*,\ y>k\Longrightarrow\bot.
\tag{5}
\]

---

## 2. 不扫描整个 prefix 区间：用 `p`-adic root lifting 求 valuation maxima

由 (1)-(2)，可能的整数中心只需考虑

\[
10^{k-1}\le N_0\le10^k.
\tag{6}
\]

固定 `(k,z,w)` 后，写

\[
a_1=N_0+A_{k,z,w},
\qquad B_{k,z,w}=a_2b_1.
\]

则

\[
N=(N_0+A_{k,z,w})^2+B_{k,z,w}^2.
\tag{7}
\]

要找

\[
M_p(k,z,w)=\max_{N_0\text{ satisfying }(6)}v_p(N),
\qquad p\in\{2,5\},
\]

无需枚举 `9*10^(k-1)` 个整数中心。

从模 `p` 的根开始，把每个根 `r mod p^e` 提升为

\[
r+d p^e,\qquad d=0,\ldots,p-1,
\]

只保留满足

\[
N(r)\equiv0\pmod{p^{e+1}}
\]

且对应同余类与区间 (6) 有交的 lift。若某一级再无 lift，则前一级就是精确最大 valuation。

这是有限、精确的整数运算，并且复杂度只随实际 valuation 深度增长，而不随 prefix 区间长度指数增长。

定义六类型上的统一下界

\[
\underline x_*(k)
:=\min_{z,w,N_0}x_*,
\]

\[
\underline y_*(k)
:=\min_{z,w,N_0}y_*.
\tag{8}
\]

由 root-lifting 得到的 `M_2,M_5` 可精确计算这两个整数。

---

## 3. cross-corridor 自动给出两个全局禁象限

因为 `underline x_*`、`underline y_*` 不大于任何具体 prefix 的 `x_*,y_*`，由 (4)-(5) 立即得到安全的全局结论：

\[
\boxed{
x>k,\ y<\underline y_*(k)\Longrightarrow\bot,
}
\tag{9}
\]

\[
\boxed{
y>k,\ x<\underline x_*(k)\Longrightarrow\bot.
}
\tag{10}
\]

这两条已经足够把无界指数平面压成有限盒。

---

## 4. finite `h` supply + decade 给出显式有限 `(x,y)` box

令

\[
H_k:=\max_{w,h\in\mathcal H_{k,w}}h.
\]

### `x` 上界

若 `x>k`，由 (9) 必有

\[
y\ge\underline y_*(k).
\]

又 `h>=1`，故由 (1)

\[
2^x5^{\underline y_*(k)}<10^k.
\]

这给一个显式有限上界 `x<=X_max(k)`。

### `x` 下界

若 `x<underline x_*(k)`，由 (10) 必有 `y<=k`。于是

\[
10^{k-1}\le H_k2^x5^k,
\]

给出有限下界 `x>=X_min(k)`。

### `y` 上界

若 `y>k`，由 (10) 有 `x>=underline x_*(k)`，所以

\[
2^{\underline x_*(k)}5^y<10^k,
\]

得到 `y<=Y_max(k)`。

### `y` 下界

若 `y<underline y_*(k)`，由 (9) 的允许区形式有 `x<=k`，故

\[
10^{k-1}\le H_k2^k5^y,
\]

得到 `y>=Y_min(k)`。

因此对每个固定 `k>=6`：

\[
\boxed{
X_{\min}(k)\le x\le X_{\max}(k),
\qquad
Y_{\min}(k)\le y\le Y_{\max}(k).
}
\tag{11}
\]

这个盒与 `ell` 完全无关。

所以原先的第三尾无界问题已经严格转化为：

1. 有限 `h` supply；
2. 有限 `(x,y)` box；
3. exact rational `rho=h2^x5^y`；
4. decade (1)；
5. one-sided gap (2)。

---

## 5. `k=6..23` 的精确 certificate

`check_a1_top_diag_uniform_layers.py` 对每个 `k`：

1. 精确 factor `b_1,Q` 并构造完整 `H_{k,w}`；
2. 用 root lifting 求六类型的 exact `v_2(N),v_5(N)` maxima；
3. 推出 `underline x_*,underline y_*` 与 theorem-derived exponent box；
4. 只枚举落入 decade 的 exact rational states；
5. 检查 (2)。

结果如下。`H counts` 按 `w=1,2,3,4` 排列。

| `k` | `H counts` | `x* floor` | `y* floor` | exponent box `(xmin,xmax;ymin,ymax)` | decade states | gap hits |
|---:|---|---:|---:|---|---:|---:|
| 6 | `(64,32,2,8)` | -8 | -15 | `(-77,54;-29,12)` | 8,679 | 0 |
| 7 | `(128,12,128,32)` | -9 | -19 | `(-81,67;-31,13)` | 27,644 | 0 |
| 8 | `(128,24,16,256)` | -10 | -22 | `(-111,77;-43,15)` | 46,489 | 0 |
| 9 | `(16,192,32,8)` | -11 | -23 | `(-112,83;-43,17)` | 29,096 | 0 |
| 10 | `(128,24,32,24)` | -12 | -25 | `(-132,91;-51,19)` | 26,685 | 0 |
| 11 | `(32,48,48,8)` | -13 | -28 | `(-122,101;-46,21)` | 18,958 | 0 |
| 12 | `(3072,96,4,32)` | -14 | -32 | `(-157,114;-60,23)` | 497,994 | 0 |
| 13 | `(256,192,512,16)` | -15 | -32 | `(-173,117;-67,25)` | 161,213 | 0 |
| 14 | `(256,96,128,16)` | -16 | -36 | `(-178,130;-68,26)` | 86,637 | 0 |
| 15 | `(64,128,16,32)` | -17 | -39 | `(-194,140;-75,28)` | 45,800 | 0 |
| 16 | `(32,48,128,32)` | -18 | -41 | `(-209,148;-81,30)` | 50,952 | 0 |
| 17 | `(128,24,64,256)` | -19 | -43 | `(-218,156;-84,32)` | 103,730 | 0 |
| 18 | `(4096,20,32,128)` | -20 | -44 | `(-230,161;-89,34)` | 944,083 | 0 |
| 19 | `(1024,384,16,8)` | -21 | -49 | `(-237,176;-91,36)` | 335,288 | 0 |
| 20 | `(32,48,64,64)` | -22 | -50 | `(-255,182;-98,38)` | 54,299 | 0 |
| 21 | `(1024,32,256,64)` | -23 | -54 | `(-247,195;-94,39)` | 366,660 | 0 |
| 22 | `(4096,192,32,256)` | -24 | -55 | `(-280,200;-108,41)` | 1,225,045 | 0 |
| 23 | `(128,96,128,256)` | -25 | -58 | `(-292,211;-112,43)` | 177,478 | 0 |

因此严格得到

\[
\boxed{
6\le k=g\le23
\Longrightarrow
\text{minimal diagonal empty}.
}
\tag{12}
\]

结合旧 `k=1..5` certificates：

\[
\boxed{
1\le k=g\le23
\Longrightarrow
\text{minimal diagonal empty}.
}
\tag{13}
\]

---

## 6. 新的无界前沿

minimal diagonal 当前真正的首个未关闭层已经推进到

\[
\boxed{k=g\ge24.}
\]

更重要的是，未来固定层已经不需要枚举 `ell`、`j` 或完整 prefix box。计算规模由 `H_{k,w}` 的 divisor supply 和一个线性尺度的 exponent box 决定。

`k=6..23` 的数据还显示一个明显现象：允许 states 到最近整数的归一化距离

\[
10^k(\lceil\rho\rceil-\rho)
\]

在理论目标窗口 `[5.09,50.45]` 附近形成稳定空带。把这个“gap desert”提升成 `k`-uniform 的算术命题，是下一步比继续增加有限层更值得优先尝试的方向。