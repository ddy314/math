# A1 minimal diagonal: central-gap 2-adic collapse

> 日期：2026-08-19。依赖 `gap-denominator-normal-form.md` 与 rational-contact square identity。
> 当前统一前沿可取 `k=g>=26`。

central denominator sector 已知

\[
\Gamma:=10^k(N_0-\rho)\in\{16,17,\ldots,39\},
\]

且

\[
B:=10^k\rho=N_0 10^k-\Gamma\in\mathbf Z.
\]

本文把 rational-contact square identity 模 `64/256`，得到：

- `w=1,3` 时
  \[
  \boxed{\Gamma\in\{16,18,20,22,24,26,28,30,32,34,36,38\};}
  \]
  且 `Gamma=2 mod 4` 时 `N_0` 必为偶数；
- `w=2` 时
  \[
  \boxed{\Gamma\in\{16,22,30,32,38\};}
  \]
- `w=4` 时
  \[
  \boxed{\Gamma\in\{24,26\}.}
  \]

因此六个 prefix 类型原先 `6*24=144` 个 central type-gap 组合被压到

\[
3\cdot12+2\cdot5+1\cdot2=\boxed{48}.
\]

状态：**已严格完成。**

---

## 1. representation-independent integer square

统一判别平方可写成

\[
V^2=K-2\rho D\mathcal N,
\]

其中

\[
D=10^kQ.
\]

central sector 中 `B=10^k rho` 为整数，因此

\[
\boxed{
R:=K-2BQ\mathcal N\in\mathbf Z,
\qquad V^2=R.
}
\tag{1}
\]

若有 exact candidate，则 `R` 必为整数平方。

注意这里不需要把 `B` 解释成原始第三块分母；它只是由 `rho` 定义出的整数。因而结论与实际 `ell` 无关。

---

## 2. 模 `2^m` 的稳定核

对任何固定 `m<=k`，所有含 `10^k` 或更高次十进制幂的 prefix 项在模 `2^m` 下消失。特别地对当前 `k>=26`，可安全使用 `m=6,8`。

minimal diagonal 数据给出

\[
G=b_1\equiv-w,
\qquad
C\equiv-z,
\]

所以

\[
\boxed{K\equiv(zw)^2\pmod{2^m}.}
\tag{2}
\]

同时

\[
Q\equiv1-10w\pmod{2^m}.
\tag{3}
\]

又

\[
a_1\equiv N_0-1,
\qquad
a_2b_1\equiv zw,
\]

故

\[
\boxed{
\mathcal N\equiv(N_0-1)^2+(zw)^2
\pmod{2^m}.}
\tag{4}
\]

最后

\[
B=N_0 10^k-\Gamma\equiv-\Gamma\pmod{2^m}.
\tag{5}
\]

代入 (1)：

\[
\boxed{
R\equiv
(zw)^2
+2\Gamma(1-10w)
\left((N_0-1)^2+(zw)^2\right)
\pmod{2^m}.}
\tag{6}
\]

这是 central-gap 的统一 2-adic square kernel。

---

## 3. odd `w`：所有 odd `Gamma` 消失

取 `w in {1,3}`。此时 `zw` 为奇数，所以模 `8`

\[
(zw)^2\equiv1,
\qquad 1-10w\text{ 为奇数}.
\]

若 `N_0` 偶，则 `(N_0-1)^2+1=2 mod 8`，所以当 `Gamma` 为奇数时

\[
R\equiv1+4\equiv5\pmod8,
\]

不是平方剩余。

若 `N_0` 奇，则 `(N_0-1)^2+1` 为奇数，odd `Gamma` 给

\[
R\equiv3\text{ 或 }7\pmod8,
\]

同样不是平方。

因此

\[
\boxed{
w\in\{1,3\}\Longrightarrow\Gamma\text{ 必为偶数}.}
\tag{7}
\]

结合 `16<=Gamma<=39`：

\[
\boxed{
\Gamma\in\{16,18,20,22,24,26,28,30,32,34,36,38\}.}
\tag{8}
\]

再看 `Gamma=2 mod 4`。若 `N_0` 奇，则 (6) 模 `8` 给 `R=5 mod 8`；所以

\[
\boxed{
 w\in\{1,3\},\quad \Gamma\equiv2\pmod4
 \Longrightarrow N_0\equiv0\pmod2.}
\tag{9}
\]

---

## 4. `w=2`：模 `32` 只剩五个 gap

当 `w=2`，`b_1` 为偶数。由 `gcd(a_1,b_1)=1`，`a_1` 为奇数，因此

\[
\boxed{N_0\text{ 为偶数}.}
\tag{10}
\]

把 (6) 模 `32`，并枚举 `N_0 mod 32` 的偶数类与整数平方剩余，可得到且仅得到

\[
\boxed{
\Gamma\in\{16,22,30,32,38\}.}
\tag{11}
\]

这一集合对 `z=1` 与 `z=3` 相同。

模 `64` 还给出 residue class：

- `(z,w)=(1,2)`：
  - `Gamma=22` 时 `N_0=4,6 mod 8`；
  - `Gamma=30,38` 时 `N_0=0,2 mod 8`；
  - `Gamma=16,32` 只要求 `N_0` 偶。
- `(z,w)=(3,2)`：
  - `Gamma=22` 时 `N_0=0,2 mod 8`；
  - `Gamma=30,38` 时 `N_0=4,6 mod 8`；
  - `Gamma=16,32` 只要求 `N_0` 偶。

这些 residue 条件可在后续 decimal-supply/resultant 攻击中直接使用。

---

## 5. `w=4`：模 `256` 只剩两个 gap

这里唯一类型是 `(z,w)=(1,4)`，同样有 `N_0` 偶。

从 (6) 开始逐级检查平方剩余：

- mod `16` 只剩 `16,18,24,26,32,34`；
- mod `32` 只剩 `16,24,26,32`；
- mod `64` 只剩 `24,26,32`；
- mod `256` 最终只剩
  \[
  \boxed{24,26.}
  \]

因此

\[
\boxed{(z,w)=(1,4)\Longrightarrow\Gamma\in\{24,26\}.}
\tag{12}
\]

---

## 6. central core 的新大小

六类型分别剩余：

- `(1,1)`：12 个；
- `(1,3)`：12 个；
- `(3,1)`：12 个；
- `(1,2)`：5 个；
- `(3,2)`：5 个；
- `(1,4)`：2 个。

总计

\[
\boxed{48}
\]

个 type-gap 组合。

这里的压缩完全独立于 `b_1,Q` 的具体 factorization，也独立于 `ell`。下一步 central sector 只需把这 48 个固定局部类型与

\[
c_\Gamma h=N_0 10^k-\Gamma,
\qquad h=q s,
\]

及 `q|Q` / whole-block selector 联用。