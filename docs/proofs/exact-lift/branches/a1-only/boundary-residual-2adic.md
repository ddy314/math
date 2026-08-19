# A1 minimal diagonal first-boundary 2-adic collapse

> 日期：2026-08-19。依赖 `positive-tail-residual.md`。当前无界前沿已经是
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge6.
> \]
> 本文只研究第一条可能的 non-saturated 尾长
> \[
> \boxed{\ell=k-1.}
> \]

由 positive residual theorem，此时

\[
\boxed{
b_3=N_0 10^{k-1}-t,
\qquad
N_0=j-10^k+1,
\qquad
t\in\{1,2,3,4,5\}.}
\tag{1}
\]

本文把 rational-contact square identity 直接模 `32/64`，得到：

- `w=2` 时只有 `t=3` 可能；进一步
  \[
  \boxed{
  z=1:\ N_0\equiv0,2\pmod8,
  \qquad
  z=3:\ N_0\equiv4,6\pmod8;
  }
  \]
- `w=4` 时只有
  \[
  \boxed{t=1}
  \]
  可能；
- `w=1,3` 时，若 `t` 为奇数，则必须
  \[
  \boxed{N_0\equiv0\pmod2.}
  \]
  `t=2,4` 在这一层没有额外二进排除。

所以第一 non-saturated boundary 的六个 `(z,w)` 类型已被压成一个很小的 residual/parity 表。

状态：**已严格完成。**

---

## 1. boundary 上判别平方自动整数化

沿用 diagonal rational-contact integer identity

\[
\boxed{
V^2=K-2\rho D\mathcal N,
}
\tag{2}
\]

其中

\[
\mathcal N=a_1^2+(a_2b_1)^2,
\qquad
D=10^kQ,
\qquad
Q=10b_1+1,
\]

以及

\[
K=G^2C^2-D^2\mathcal N,
\qquad G=b_1.
\]

在 `ell=k-1` 上

\[
\rho=\frac{b_3}{10^{k-1}},
\]

所以

\[
2\rho D\mathcal N
=2\frac{b_3}{10^{k-1}}10^kQ\mathcal N
=20b_3Q\mathcal N.
\]

故 (2) 化为

\[
\boxed{
V^2=R,
\qquad
R:=K-20b_3Q\mathcal N\in\mathbf Z.
}
\tag{3}
\]

若 `V` 是有理数且 `V^2` 是整数，则 `V` 本身是整数。因此 exact candidate 必须满足

\[
\boxed{R\text{ 是整数平方}.}
\tag{4}
\]

这允许直接使用模 `2^a` 的平方剩余。

---

## 2. `R mod 32` 的统一公式

因为 `k>=6`，所有出现的高十进制幂在模 `32` 下消失。由 minimal diagonal 数据：

\[
b_1=10^{2k+1}-w,
\qquad
a_2=10^{2k+1}-z,
\]

得到

\[
G\equiv-w\pmod{32},
\qquad
a_2\equiv-z\pmod{32}.
\]

又

\[
C=a_1 10^{2k+1}+a_2
\equiv-z\pmod{32}.
\]

由于 `D` 被 `2^k` 整除，`D^2 mathcal N` 在模 `32` 下为零，因此

\[
\boxed{
K\equiv(zw)^2\pmod{32}.}
\tag{5}
\]

另一方面

\[
Q=10b_1+1
\equiv1-10w\pmod{32}.
\tag{6}
\]

由 (1) 且 `10^{k-1}` 被 `32` 整除：

\[
\boxed{b_3\equiv-t\pmod{32}.}
\tag{7}
\]

最后

\[
a_1\equiv j\equiv N_0-1\pmod{32},
\]

从而

\[
\boxed{
\mathcal N
\equiv(N_0-1)^2+(zw)^2
\pmod{32}.}
\tag{8}
\]

代入 (3)：

\[
\boxed{
R\equiv
(zw)^2
+20t(1-10w)
\left((N_0-1)^2+(zw)^2\right)
\pmod{32}.}
\tag{9}
\]

这就是第一 boundary 的统一局部平方核。

---

## 3. `w=2`：五个 residual 只剩 `t=3`

当 `w=2` 时 `b_1` 为偶数。原问题有

\[
\gcd(a_1,b_1)=1,
\]

所以 `a_1` 必为奇数。又

\[
a_1\equiv N_0-1\pmod2,
\]

故

\[
\boxed{N_0\text{ 为偶数}.}
\tag{10}
\]

这里 `z=1` 或 `3`，两者都给

\[
(zw)^2=(2z)^2\equiv4\pmod{32}.
\]

并且

\[
1-10w=1-20\equiv13\pmod{32}.
\]

因为 `N_0-1` 为奇数：

\[
(N_0-1)^2+(2z)^2
\equiv1+4=5\pmod8.
\]

式 (9) 因而化为

\[
\boxed{
R\equiv4+20t\pmod{32}.}
\tag{11}
\]

模 `32` 的平方剩余中，被 `4` 整除的只有

\[
0,4,16.
\]

对 `t=1,2,3,4,5`：

\[
4+20t
\equiv
24,12,0,20,8
\pmod{32}.
\]

只有 `t=3` 是平方剩余。因此

\[
\boxed{w=2\Longrightarrow t=3.}
\tag{12}
\]

---

## 4. `w=2,t=3` 的模 `64` residue class

仍设 `w=2,t=3`。由于 (10) 的 `N_0` 为偶数，即使 `k=6`，

\[
N_0 10^{k-1}
\]

也已经被 `64` 整除，所以

\[
b_3\equiv-3\pmod{64}.
\]

其余高十进制幂显然也在模 `64` 下消失。

此时

\[
Q\equiv1-20\equiv45\pmod{64},
\]

故

\[
20tQ\equiv20\cdot3\cdot45\equiv12\pmod{64}.
\]

### `(z,w)=(1,2)`

有

\[
K\equiv4\pmod{64},
\qquad
\mathcal N\equiv(N_0-1)^2+4\pmod{64}.
\]

所以

\[
R\equiv52+12(N_0-1)^2\pmod{64}.
\]

奇数平方模 `16` 只有 `1,9`。若

\[
(N_0-1)^2\equiv1\pmod{16},
\]

则 `R≡0 mod64`；若等于 `9`，则 `R≡32 mod64`，不可能是平方。

因此

\[
N_0-1\equiv1,7\pmod8,
\]

即

\[
\boxed{
(z,w)=(1,2),\ t=3
\Longrightarrow
N_0\equiv0,2\pmod8.}
\tag{13}
\]

### `(z,w)=(3,2)`

此时

\[
K\equiv36\pmod{64},
\qquad
\mathcal N\equiv(N_0-1)^2+36\pmod{64}.
\]

得到

\[
R\equiv20+12(N_0-1)^2\pmod{64}.
\]

现在只有

\[
(N_0-1)^2\equiv9\pmod{16}
\]

能使 `R` 为平方剩余，因此

\[
\boxed{
(z,w)=(3,2),\ t=3
\Longrightarrow
N_0\equiv4,6\pmod8.}
\tag{14}
\]

---

## 5. `w=4`：模 `32` 只剩 `t=1,4`

这里唯一类型是

\[
(z,w)=(1,4).
\]

同样因为 `b_1` 为偶数，`N_0` 必为偶数。

有

\[
(zw)^2=16,
\qquad
1-10w=1-40\equiv25\pmod{32}.
\]

并且

\[
(N_0-1)^2+16\equiv1\pmod8.
\]

所以 (9) 化为

\[
\boxed{
R\equiv16+20t\pmod{32}.}
\tag{15}
\]

五个 residual 给出

\[
16+20t
\equiv
4,24,12,0,20
\pmod{32}.
\]

只有 `t=1,4` 尚可。因此

\[
\boxed{w=4\Longrightarrow t\in\{1,4\}.}
\tag{16}
\]

---

## 6. 模 `64` 再杀掉 `w=4,t=4`

对 `w=4`，`N_0` 为偶数，因此与 §4 同理，当前全部 `k>=6` 都允许把 (3) 模 `64`。

取 `t=4`：

\[
K\equiv16\pmod{64},
\qquad
Q\equiv1-40\equiv25\pmod{64},
\]

并且

\[
20tQ
=20\cdot4\cdot25
\equiv16\pmod{64}.
\]

由于 `N_0-1` 为奇数：

\[
\mathcal N
=(N_0-1)^2+16
\equiv1\pmod4.
\]

于是

\[
R\equiv16+16\mathcal N
\equiv32\pmod{64}.
\]

但整数平方不可能同余 `32 mod64`。故

\[
\boxed{
(z,w)=(1,4)
\Longrightarrow
t=1.}
\tag{17}
\]

---

## 7. `w` 为奇数：奇 residual 强迫 `N_0` 为偶数

剩余奇 `w` 类型为

\[
(1,1),\quad(1,3),\quad(3,1).
\]

这里 `zw` 为奇数，所以

\[
(zw)^2\equiv1\pmod8.
\]

又

\[
1-10w\equiv7\pmod8,
\qquad
20\equiv4\pmod8.
\]

因此 (9) 模 `8` 为

\[
R\equiv
1+4t\left((N_0-1)^2+1\right)
\pmod8.
\tag{18}
\]

- 若 `N_0` 为偶数，则 `N_0-1` 为奇数，括号为偶数，所以 `R≡1 mod8`；
- 若 `N_0` 为奇数，则括号为奇数，所以
  \[
  R\equiv1+4t\pmod8.
  \]

当 `t` 为奇数时，后一种情况给

\[
R\equiv5\pmod8,
\]

不可能是平方。因此

\[
\boxed{
w\in\{1,3\},\quad t\in\{1,3,5\}
\Longrightarrow N_0\equiv0\pmod2.}
\tag{19}
\]

`t=2,4` 在这一模 `8` 层没有新增限制。

---

## 8. 第一 boundary 的最终局部正规形

当前 `k>=6, ell=k-1` 的候选只可能落在：

| `(z,w)` | residual `t` | 额外条件 |
|---|---|---|
| `(1,1)` | `1,2,3,4,5` | `t` 奇时 `N_0` 偶 |
| `(1,3)` | `1,2,3,4,5` | `t` 奇时 `N_0` 偶 |
| `(3,1)` | `1,2,3,4,5` | `t` 奇时 `N_0` 偶 |
| `(1,2)` | `3` | `N_0≡0,2 (mod 8)` |
| `(3,2)` | `3` | `N_0≡4,6 (mod 8)` |
| `(1,4)` | `1` | `N_0` 偶（自动） |

因此 even-`w` 两族已经几乎完全刚化：

\[
\boxed{
w=2:\ t=3,
\qquad
w=4:\ t=1.}
\]

下一步应把这些 fixed residual 与 denominator prime supply

\[
h=q\,s,
\qquad q\mid Q,
\]

以及 `b_1` 侧 `1 mod 4` 的 whole-block selector 联用；第一 boundary 已经不再有二维 `(x,y)` 自由度。