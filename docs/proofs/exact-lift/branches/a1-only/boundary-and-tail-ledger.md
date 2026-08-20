# A1-only Boundary And Tail Ledger

> 本文件是细粒度研究记录的机械归并账本。各来源的标题、正文和证明状态原样保留；账本中的局部闭合、有限证书或降级路线均不表示该分支或主不存在性命题已经关闭。

## 来源索引

- [`boundary-decimal-supply.md`](#source-boundary-decimal-supply)
- [`boundary-prime-sieve.md`](#source-boundary-prime-sieve)
- [`boundary-residual-2adic.md`](#source-boundary-residual-2adic)
- [`gap-denominator-normal-form.md`](#source-gap-denominator-normal-form)
- [`near-integer-tail.md`](#source-near-integer-tail)
- [`positive-tail-residual.md`](#source-positive-tail-residual)
- [`residual-shell-supply.md`](#source-residual-shell-supply)
- [`sharp-positive-tail-window.md`](#source-sharp-positive-tail-window)
- [`short-tail-saturation.md`](#source-short-tail-saturation)
- [`uniform-2adic-prefix.md`](#source-uniform-2adic-prefix)

<a id="source-boundary-decimal-supply"></a>

> 整合来源：`boundary-decimal-supply.md`

# A1 minimal diagonal boundary decimal-supply reduction

> 日期：2026-08-19。依赖 `positive-tail-residual.md`、`boundary-residual-2adic.md` 与 minimal-diagonal odd-prime supply。
> 当前范围：
> \[
> k=g\ge6,\qquad \ell=k-1.
> \]

第一 boundary 已有

\[
b_3=N_0 10^{k-1}-t,
\qquad
t\in\{1,2,3,4,5\}.
\]

本文指出：一旦 `t` 固定，`b_3` 的全部 `2/5` 指数也被 `t` 固定，因此第三分母不再需要枚举 `(x,y)`。若

\[
a_t:=2^{v_2(t)}5^{v_5(t)},
\qquad
\widehat t:=\frac{t}{a_t},
\]

则

\[
\boxed{b_3=a_t h,}
\tag{1}
\]

其中 `h` 正是 denominator prime graph 给出的有限 odd-prime supply。并且必须满足十进制同余

\[
\boxed{
h+\widehat t
\equiv0
\pmod{10^{k-1}/a_t}.}
\tag{2}
\]

恢复公式为

\[
\boxed{
N_0
=\frac{a_t(h+\widehat t)}{10^{k-1}}.
}
\tag{3}
\]

所以对固定 `k,w,t`，第一 boundary 的候选数至多就是有限的 `#h`，无需扫描 `N_0` 的整个 k-digit 区间。

状态：**已严格完成。**

---

## 1. `b_3` 的 `2/5` 赋值等于 `t` 的赋值

当前

\[
b_3=N_0 10^{k-1}-t.
\]

因为

\[
k\ge6,
\qquad
1\le t\le5,
\]

有

\[
v_2(t),v_5(t)<k-1.
\]

而第一项 `N_0 10^{k-1}` 同时至少被

\[
2^{k-1},\qquad5^{k-1}
\]

整除。因此低赋值项由 `t` 唯一承担：

\[
\boxed{v_2(b_3)=v_2(t),}
\tag{4}
\]

\[
\boxed{v_5(b_3)=v_5(t).}
\tag{5}
\]

令

\[
a_t=2^{v_2(t)}5^{v_5(t)}.
\]

把 `b_3` 的 `2/5` 部分提出后，剩余部分恰与 `10` 互素，所以

\[
\boxed{b_3=a_t h,
\qquad \gcd(h,10)=1.}
\tag{6}
\]

这里的 `h` 与 odd-prime supply theorem 中的 `h` 完全相同。

---

## 2. `h` 仍只来自 `Q` 与 `b_1` 的 whole blocks

已有 theorem 给出

\[
\boxed{h=q\,s,}
\tag{7}
\]

其中

\[
q\mid Q,
\]

而 `s` 是 `b_1` 中所有 `1 mod4` 奇素 prime-power blocks 的 whole-block selector。

因此对固定 `k,w`，`h` 属于一个显式有限集合

\[
\boxed{\mathcal H_{k,w}.}
\tag{8}
\]

这个集合只由

\[
b_1=10^{2k+1}-w,
\qquad
Q=10b_1+1
\]

的因子分解决定，与 `N_0`、`z`、第三分子本身无关。

---

## 3. residual 直接变成 `h` 的十进制同余

把

\[
t=a_t\widehat t,
\qquad \gcd(\widehat t,10)=1
\]

和 (6) 代回

\[
b_3=N_0 10^{k-1}-t:
\]

\[
a_t h
=N_0 10^{k-1}-a_t\widehat t.
\]

于是

\[
a_t(h+\widehat t)
=N_0 10^{k-1}.
\]

由于 `a_t|10^{k-1}`，得到

\[
\boxed{
\frac{10^{k-1}}{a_t}
\mid h+\widehat t.}
\tag{9}
\]

也就是主同余 (2)。

同时 `N_0` 被唯一恢复为

\[
\boxed{
N_0
=\frac{a_t(h+\widehat t)}{10^{k-1}}.}
\tag{10}
\]

再检查

\[
10^{k-1}\le N_0<10^k
\]

即可。

因此第一 boundary 的搜索方向应从

\[
N_0\text{ 的 }9\cdot10^{k-1}\text{ 个整数}
\]

彻底反转成

\[
\boxed{
h\in\mathcal H_{k,w}}
\]

的有限 supply 枚举。

---

## 4. 五个 residual 的具体同余

分别计算 `a_t,hat t`：

| `t` | `a_t` | `hat t` | 必要同余 |
|---:|---:|---:|---|
| `1` | `1` | `1` | `h+1 ≡ 0 (mod 10^{k-1})` |
| `2` | `2` | `1` | `h+1 ≡ 0 (mod 10^{k-1}/2)` |
| `3` | `1` | `3` | `h+3 ≡ 0 (mod 10^{k-1})` |
| `4` | `4` | `1` | `h+1 ≡ 0 (mod 10^{k-1}/4)` |
| `5` | `5` | `1` | `h+1 ≡ 0 (mod 10^{k-1}/5)` |

结合二进 boundary collapse：

### `w=2`

只有

\[
t=3,
\]

所以只需检查

\[
\boxed{
h\equiv-3\pmod{10^{k-1}}.}
\tag{11}
\]

### `w=4`

只有

\[
t=1,
\]

所以只需检查

\[
\boxed{
h\equiv-1\pmod{10^{k-1}}.}
\tag{12}
\]

这两个 even-`w` 类型尤其简单：每个合法 `h` 直接给至多一个 `N_0`，不存在任何额外 `2/5` exponent 搜索。

---

## 5. 对固定 k 的证书复杂度

设

\[
H_{k,w}=\#\mathcal H_{k,w}.
\]

第一 boundary 的完整 supply 检查只需要至多

\[
5H_{k,w}
\]

个小同余测试；对 even-`w` 实际只需

\[
H_{k,w}
\]

个。

这和旧的 `(h,x,y)` tail 枚举相比已经发生本质变化：第一 boundary 现在是一个**有限 divisor-congruence certificate**。

下一步可以：

1. 对当前首个未关闭层 `k=6` 给出完整 boundary certificate；
2. 搜索能统一排除 (11)、(12) 的 divisor congruence 机制；
3. 对奇 `w` 把本同余与 `boundary-prime-sieve.md` 的 mod `3/11` forbidden classes 联用。

---

<a id="source-boundary-prime-sieve"></a>

> 整合来源：`boundary-prime-sieve.md`

# A1 minimal diagonal boundary prime-supply sieve

> 日期：2026-08-19。依赖 `positive-tail-residual.md` 与 minimal-diagonal odd-prime supply。
> 当前只研究
> \[
> k=g\ge6,\qquad \ell=k-1,
> \]
> 因而
> \[
> b_3=N_0 10^{k-1}-t,
> \qquad
> t\in\{1,2,3,4,5\}.
> \]

本文把 denominator prime graph 从“因子供应描述”改写成对 prefix integer `N_0` 的显式同余筛。

核心结论：若奇素数 `p!=5` 不在第三分母的合法 supply 中，则

\[
\boxed{
N_0 10^{k-1}\not\equiv t\pmod p.
}
\tag{1}
\]

特别地：

1. 素数 `11` 在六个 minimal-diagonal 类型中**永远不可能进入第三分母**，所以
   \[
   \boxed{
   N_0\not\equiv(-1)^{k-1}t\pmod{11}.
   }
   \tag{2}
   \]
2. 对 `w=1,3,4`，素数 `3` 也没有合法 supply，因此
   \[
   \boxed{N_0\not\equiv t\pmod3.}
   \tag{3}
   \]
3. 对 `w=2`，素数 `7` 永远不在 supply 中；结合 `boundary-residual-2adic.md` 已有 `t=3`，得到
   \[
   \boxed{
   N_0 10^{k-1}\not\equiv3\pmod7.
   }
   \tag{4}
   \]

这些条件可以与 mod `8/64` 的平方筛直接叠加，形成第一 boundary 的 prefix residue sieve。

状态：**已严格完成。**

---

## 1. minimal diagonal 的奇素数 supply

已有 odd-prime supply theorem：写

\[
b_3=h2^u5^v,
\qquad \gcd(h,10)=1.
\]

则

\[
\boxed{h=q\,s,}
\tag{5}
\]

其中

\[
q\mid Q,
\qquad
Q=10b_1+1,
\]

而 `s` 是 `b_1` 中所有 `1 mod 4` 奇素数 prime-power blocks 的一个 whole-block selector。

等价地，对任意奇素数

\[
p\ne5,
\]

若 `p|b_3`，则至少满足以下一条：

- `p|Q`；
- `p|b_1` 且 `p≡1 mod4`。

特别地，若

\[
\boxed{
p\nmid Q
\quad\text{且}\quad
\bigl(p\nmid b_1\text{ 或 }p\equiv3\pmod4\bigr),
}
\tag{6}
\]

则必有

\[
\boxed{p\nmid b_3.}
\tag{7}
\]

---

## 2. boundary 上直接变成 `N_0` 的禁同余类

当前

\[
b_3=N_0 10^{k-1}-t.
\]

对 `p!=2,5`，`10` 在模 `p` 下可逆。因此 (7) 等价于

\[
N_0 10^{k-1}-t\not\equiv0\pmod p,
\]

即

\[
\boxed{
N_0 10^{k-1}\not\equiv t\pmod p.
}
\tag{8}
\]

或者写成

\[
\boxed{
N_0\not\equiv t\,10^{1-k}\pmod p.
}
\tag{9}
\]

所以每个缺失的 supply prime 都删掉 `N_0` 的一个精确 residue class。

---

## 3. `11` 是六类型共同的永久缺失素数

因为

\[
10\equiv-1\pmod{11}
\]

且 `2k+1` 为奇数：

\[
b_1=10^{2k+1}-w
\equiv-1-w\pmod{11}.
\]

对

\[
w\in\{1,2,3,4\}
\]

分别为

\[
-2,-3,-4,-5\pmod{11},
\]

都不为零。因此

\[
\boxed{11\nmid b_1.}
\tag{10}
\]

同时

\[
Q=10b_1+1
\equiv-b_1+1
\equiv w+2\pmod{11},
\]

即

\[
3,4,5,6\pmod{11},
\]

也都不为零。所以

\[
\boxed{11\nmid Q.}
\tag{11}
\]

因此 `11` 不可能出现在 `h` 中，也就不可能整除 `b_3`：

\[
\boxed{11\nmid b_3.}
\tag{12}
\]

由

\[
10^{k-1}\equiv(-1)^{k-1}\pmod{11},
\]

得到

\[
\boxed{
N_0\not\equiv(-1)^{k-1}t\pmod{11}.}
\tag{13}
\]

这是六种 `(z,w)`、所有 `k>=6` 共同拥有的固定素数筛。

---

## 4. `w!=2` 时 `3` 没有合法 supply

### `w=1`

模 `3`：

\[
b_1=10^{2k+1}-1\equiv0\pmod3.
\]

但

\[
3\equiv3\pmod4,
\]

所以这个 `b_1` prime block 禁止流向第三分母。

又

\[
Q=10b_1+1\equiv1\pmod3,
\]

故 Q-side 也没有 `3`。

### `w=3`

\[
b_1\equiv1-0\equiv1\pmod3,
\]

\[
Q\equiv10\cdot1+1\equiv2\pmod3.
\]

所以两侧都没有 `3`。

### `w=4`

\[
b_1\equiv1-1\equiv0\pmod3,
\]

但同样由于 `3≡3 mod4`，该 block 不能流入 `b_3`；并且

\[
Q\equiv1\pmod3.
\]

综上，对

\[
w\in\{1,3,4\}
\]

都有

\[
\boxed{3\nmid b_3.}
\tag{14}
\]

由于

\[
10^{k-1}\equiv1\pmod3,
\]

boundary 公式给出

\[
\boxed{N_0\not\equiv t\pmod3.}
\tag{15}
\]

特别地 `(z,w)=(1,4)` 已由二进筛锁成 `t=1`，所以

\[
\boxed{
(z,w)=(1,4)
\Longrightarrow
N_0\not\equiv1\pmod3.}
\tag{16}
\]

---

## 5. `w=2` 时 `7` 永远缺失

这里二进 boundary theorem 已给出

\[
\boxed{t=3.}
\]

考察 `p=7`。有

\[
10\equiv3\pmod7,
\]

而 `3` 的阶为 `6`。

对

\[
b_1=10^{2k+1}-2,
\]

按 `k mod3` 分类，`2k+1 mod6` 只可能为

\[
1,3,5.
\]

对应

\[
3^{2k+1}\equiv3,6,5\pmod7,
\]

所以

\[
b_1\equiv1,4,3\pmod7,
\]

永不为零。

于是

\[
Q=10b_1+1\equiv3b_1+1\pmod7
\]

对应

\[
4,6,3\pmod7,
\]

同样永不为零。因此

\[
\boxed{7\nmid b_1Q.}
\tag{17}
\]

所以 `7` 不能进入第三分母：

\[
\boxed{7\nmid b_3.}
\tag{18}
\]

结合 `t=3`：

\[
\boxed{
N_0 10^{k-1}\not\equiv3\pmod7.}
\tag{19}
\]

这是 `w=2` 两类型共同的额外 forbidden class。

---

## 6. 与二进 boundary 正规形叠加

`boundary-residual-2adic.md` 已给出：

\[
(z,w)=(1,2):
\quad t=3,
\quad N_0\equiv0,2\pmod8,
\]

\[
(z,w)=(3,2):
\quad t=3,
\quad N_0\equiv4,6\pmod8,
\]

\[
(z,w)=(1,4):
\quad t=1,
\quad N_0\equiv0\pmod2.
\]

现在还要分别避开：

- 所有类型的一个 mod `11` 类；
- `w=1,3,4` 的 `N_0≡t mod3`；
- `w=2` 的一个 k-dependent mod `7` 类。

所以第一 boundary 已经可以看成一个真正的**有限局部筛系统**，而不再是抽象的 S-unit 二维格点问题。

下一步应继续寻找少量永久缺失素数，或把这些禁同余类与 `gcd(a_1,b_1)=1`、`K>0` 的 prefix 条件耦合，争取对五 residual 做 prefix-uniform closure。

---

<a id="source-boundary-residual-2adic"></a>

> 整合来源：`boundary-residual-2adic.md`

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

---

<a id="source-gap-denominator-normal-form"></a>

> 整合来源：`gap-denominator-normal-form.md`

# A1 minimal diagonal: reduced-denominator gap normal form

> 日期：2026-08-19。本文以 `sharp-positive-tail-window.md` 为输入，把 gap-desert 问题按 `rho` 的既约 `2/5` 分母分裂。
> 当前只关心 fixed-layer 前沿 `k=g>=6`。

写

\[
\rho=h2^x5^y,
\qquad \gcd(h,10)=1,
\]

并定义

\[
a=\max(-x,0),
\qquad
b=\max(-y,0),
\qquad
d=2^a5^b.
\]

则 `rho=n/d` 为既约分数。

本文核心结论：

1. 任意 candidate 的既约分母满足
   \[
   \boxed{d>\frac{10^k}{39.003}.}
   \]
2. 若 `d|10^k`，则归一化 gap 只能是固定的 24 个整数
   \[
   \boxed{\Gamma\in\{16,17,\ldots,39\}.}
   \]
3. 在这一 central-denominator sector 中，指数被完全显式化：
   \[
   \boxed{x=-k+v_2(\Gamma),\qquad y=-k+v_5(\Gamma),}
   \]
   并有
   \[
   \boxed{
   2^{v_2(\Gamma)}5^{v_5(\Gamma)}h
   =N_0 10^k-\Gamma.
   }
   \]
4. 因而全部剩余无界性都被推入
   \[
   \boxed{a>k\quad\text{或}\quad b>k}
   \]
   的 deep-denominator sector。

状态：**已严格完成。**

---

## 1. 既约 residual

由 sharpened positive-tail theorem，

\[
15.09\,10^{-k}<N_0-\rho<39.003\,10^{-k},
\tag{1}
\]

且 `N_0=ceil(rho)`。

写既约分数

\[
\rho=\frac nd,
\qquad \gcd(n,d)=1,
\]

并定义

\[
\boxed{r:=N_0d-n.}
\tag{2}
\]

因为 `0<N_0-rho<1`，有

\[
1\le r<d.
\]

又

\[
r\equiv-n\pmod d,
\]

所以

\[
\boxed{\gcd(r,d)=1.}
\tag{3}
\]

特别地：若 `a>0` 则 `r` 为奇数；若 `b>0` 则 `5 not| r`。

定义归一化 gap

\[
\boxed{
\Gamma:=10^k(N_0-\rho)=\frac{10^k r}{d}.
}
\tag{4}
\]

由 (1)：

\[
\boxed{15.09<\Gamma<39.003.}
\tag{5}
\]

---

## 2. 分母的统一下界

由 `r>=1` 与 (4)-(5)：

\[
\frac{10^k}{d}<39.003.
\]

所以

\[
\boxed{
d>\frac{10^k}{39.003}.}
\tag{6}
\]

这已经说明任何 gap candidate 都必须有一个接近 `10^k` 尺度或更大的 terminating-decimal reduced denominator。

---

## 3. central denominator：`d|10^k`

现在假设

\[
\boxed{d\mid10^k,}
\tag{7}
\]

等价于

\[
a\le k,\qquad b\le k.
\]

由 (4)，`Gamma` 是正整数。结合 (5)：

\[
\boxed{
\Gamma\in\{16,17,\ldots,39\}.
}
\tag{8}
\]

### 3.1 `a,b` 都必须为正

若 `a=0`，则 `d=5^b`，于是

\[
\frac{10^k}{d}=2^k5^{k-b}
\]

被 `2^k` 整除。因 `k>=6`，任何正整数 `Gamma=r10^k/d` 至少为 `64`，与 (5) 矛盾。

同理，若 `b=0`，则 `Gamma` 被 `5^k>=15625` 整除，更不可能落在 (5)。

因此 central sector 自动满足

\[
\boxed{a>0,\qquad b>0.}
\tag{9}
\]

由 (3)：

\[
\boxed{\gcd(r,10)=1.}
\tag{10}
\]

---

## 4. 24 个整数 gap 精确恢复 `(x,y,r)`

由

\[
\Gamma
=r\,2^{k-a}5^{k-b}
\]

以及 `gcd(r,10)=1`，立即有

\[
v_2(\Gamma)=k-a,
\qquad
v_5(\Gamma)=k-b.
\]

所以

\[
\boxed{
a=k-v_2(\Gamma),}
\tag{11}
\]

\[
\boxed{
b=k-v_5(\Gamma).}
\tag{12}
\]

并且

\[
\boxed{
r=rac{\Gamma}{2^{v_2(\Gamma)}5^{v_5(\Gamma)}}.}
\tag{13}
\]

因为 `a,b>0`，此时 `x=-a,y=-b`，故

\[
\boxed{
x=-k+v_2(\Gamma),}
\tag{14}
\]

\[
\boxed{
y=-k+v_5(\Gamma).}
\tag{15}
\]

整个 central sector 的二维 exponent freedom 因而彻底消失，只剩固定集合 (8) 中的 24 个 `Gamma`。

---

## 5. `h` 的十进制 normal form

在 central sector 中 `x,y<0`，因此既约分子就是

\[
n=h.
\]

由 residual 定义

\[
h=N_0d-r.
\tag{16}
\]

令

\[
\boxed{
c_\Gamma:=2^{v_2(\Gamma)}5^{v_5(\Gamma)}.}
\tag{17}
\]

由 (11)-(13)：

\[
d=\frac{10^k}{c_\Gamma},
\qquad
r=\frac\Gamma{c_\Gamma}.
\]

代入 (16) 并乘以 `c_Gamma`：

\[
\boxed{
 c_\Gamma h=N_0 10^k-\Gamma.
}
\tag{18}
\]

所以对每个固定 `Gamma=16,...,39`，candidate odd supply 必须具有一个极端刚性的十进制尾：

\[
\boxed{
N_0=\frac{c_\Gamma h+\Gamma}{10^k}
\in[10^{k-1},10^k].
}
\tag{19}
\]

这为下一步把 odd-prime supply 与固定 24 个 decimal congruences 联用提供了统一入口。

---

## 6. deep denominator 是唯一剩余无界区

若不满足 `d|10^k`，因为

\[
d=2^a5^b,
\]

必有

\[
\boxed{a>k\quad\text{或}\quad b>k.}
\tag{20}
\]

因此 gap-desert 的统一证明可以严格拆成两个互不重叠的任务：

### A. central sector

\[
a\le k,\ b\le k,
\]

只需处理 24 个固定 `Gamma` 及 (18) 的十进制 supply condition。

### B. deep sector

\[
a>k\quad\text{或}\quad b>k.
\]

至少一个 reduced denominator exponent 穿过 prefix scale `k`，应继续与 typewise resonance/cross-corridor 联用。

相比原来的整个 `(x,y)` 平面，这已经把无界算术问题切成一个绝对有限 central core 与一个具有明确方向性的 deep sector。

---

<a id="source-near-integer-tail"></a>

> 整合来源：`near-integer-tail.md`

# A1 minimal diagonal second-order near-integer tail lock

> 日期：2026-08-19。本文只研究已经由 `diagonal.md` 缩到的无界 minimal diagonal
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge3.
> \]
> 目标是保留上一轮 sharp significand lock 中被统一替换掉的 `10^{-k}`，把误差从固定 `1.2\times10^{-3}` 改写成随 `k` 衰减的 `O(10^{-k})`，并在原始 `\rho` 尺度上得到固定常数窗口。

状态：**本文中的不等式与推论均已严格完成。**

---

## 1. 输入与记号

沿用 `diagonal.md` 的 minimal diagonal 记号。令

\[
\delta=10^{-k},
\qquad
\varepsilon=10^{-2k}=\delta^2,
\]

因此

\[
0<\delta\le10^{-3},
\qquad
0<\varepsilon\le10^{-6}.
\]

第三分母正规化为

\[
\rho=\frac{b_3}{10^\ell},
\qquad
\sigma=\frac{b_3}{10^{m_3}}
=\frac\rho{10^k}
=\delta\rho,
\]

且

\[
0.1\le\sigma<1.
\]

prefix remainder 写成

\[
u=\frac{j}{10^{k+1}}.
\]

六个 minimal-surplus 类型仍满足

\[
(z,w)\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\},
\]

并令

\[
c=5-z\in\{4,2\}.
\]

已有 half-gap kernel 给出

\[
0<\phi_1<0.434,
\qquad
\phi_2=\frac z{10}\le0.3.
\]

已有 sharp significand 推导中的精确关系为

\[
\boxed{
 u
=5E
-\frac{w\varepsilon}{2}E
-\frac{cw\varepsilon}{10},
}
\tag{1}
\]

其中

\[
E=2(\phi_1+\phi_2)-1.
\]

positive excess decomposition 为

\[
\begin{aligned}
E
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(1+\varepsilon\phi_1+\frac RM\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}
+\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
+\varepsilon^2\phi_1^2,
\end{aligned}
\tag{2}
\]

并且

\[
\frac{\mathfrak h}{M\varepsilon}
=
\frac\lambda\varepsilon(A+\sigma B),
\tag{3}
\]

其中

\[
A=(1+\varepsilon\phi_1)-\delta(1-\varepsilon\phi_2),
\]

\[
B=\frac RM-\frac{r_3}{M},
\]

\[
\frac\lambda\varepsilon
=
\frac1{100-(10w-1)\varepsilon}.
\]

本文只在这些已经证明的恒等式上做一轮保留 `\delta` 的误差 bookkeeping。

---

## 2. 不再把 `delta` 粗化成 `10^-3`

定义主中心

\[
\boxed{
X=1+\sigma-\delta.
}
\tag{4}
\]

注意

\[
1.099<X<2.
\]

### 2.1 `A` 的二阶误差

由定义

\[
A
=1-\delta
+\varepsilon\phi_1
+\delta\varepsilon\phi_2.
\]

利用

\[
\phi_1<0.434,
\qquad
\delta\phi_2\le0.001\cdot0.3=0.0003,
\]

得到

\[
\boxed{
1-\delta<A<1-\delta+0.435\varepsilon.
}
\tag{5}
\]

### 2.2 `B` 的二阶误差

已有 carrier bounds 给出

\[
1-\varepsilon\phi_2
<\frac RM
<1+\varepsilon\phi_1.
\]

最高层还有

\[
0<\frac{r_3}{M}<10^{-3k}=\delta^3
\le0.001\varepsilon.
\]

因此

\[
\boxed{
1-0.301\varepsilon
<B
<1+0.434\varepsilon.
}
\tag{6}
\]

### 2.3 外层 factor 的二阶误差

令

\[
F=1+\varepsilon\phi_1+\frac RM.
\]

由同一组 bounds：

\[
\boxed{
2-0.3\varepsilon
<F
<2+0.868\varepsilon.
}
\tag{7}
\]

另一方面 `w\le4`，故

\[
\frac\lambda\varepsilon
\le
\frac1{100-39\varepsilon}
=
0.01\frac1{1-0.39\varepsilon}.
\]

当 `\varepsilon\le10^{-6}` 时

\[
(1+0.391\varepsilon)(1-0.39\varepsilon)
=1+0.001\varepsilon-0.15249\varepsilon^2>1,
\]

所以

\[
\boxed{
0.01
<\frac\lambda\varepsilon
<0.01(1+0.391\varepsilon).
}
\tag{8}
\]

---

## 3. 第一 positive source 的 `delta`-精确中心

记 (2) 的第一项为

\[
S_1
:=
\frac\lambda\varepsilon(A+\sigma B)F.
\]

### 3.1 下界

由 (5)–(8)：

\[
A+\sigma B
>
(1-\delta)+\sigma(1-0.301\varepsilon)
=X-0.301\sigma\varepsilon.
\]

因此

\[
S_1
>
0.01
(X-0.301\sigma\varepsilon)
(2-0.3\varepsilon).
\]

展开：

\[
\begin{aligned}
S_1
>{}&0.02X
-0.003X\varepsilon
-0.00602\sigma\varepsilon
+0.000903\sigma\varepsilon^2.
\end{aligned}
\]

因为 `X<2`、`sigma<1`，得到安全粗化

\[
\boxed{
S_1>0.02X-0.0121\varepsilon.
}
\tag{9}
\]

### 3.2 上界

由 (5)–(8)：

\[
A+\sigma B
<X+0.869\varepsilon.
\]

所以

\[
S_1
<
0.01(1+0.391\varepsilon)
(X+0.869\varepsilon)
(2+0.868\varepsilon).
\]

对右侧直接展开。一次项系数在 `X<2` 时严格小于

\[
0.01\bigl(0.868\cdot2+2\cdot0.869+2\cdot0.391\cdot2\bigr)
=0.05038.
\]

二次与三次项在 `\varepsilon\le10^{-6}` 下总计小于
`2\times10^{-8}\varepsilon`。因此可安全写成

\[
\boxed{
S_1<0.02X+0.0504\varepsilon.
}
\tag{10}
\]

于是第一 source 的真正中心是

\[
\boxed{0.02(1+\sigma-\delta),}
\]

而不是上一轮统一粗化后使用的 `0.02(1+sigma)`。

---

## 4. 全 excess 的二阶夹逼

其余三个 source 都是非负项。

第三半径项满足

\[
0<\frac{(r_3/M)^2}{\varepsilon}
<10^{-4k}=\varepsilon^2.
\tag{11}
\]

曲率项满足

\[
0<2\phi_1+\phi_2^2-\phi_1^2<0.958,
\]

故

\[
0<
\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
<0.958\varepsilon.
\tag{12}
\]

最后

\[
0<\varepsilon^2\phi_1^2
<0.189\varepsilon^2.
\tag{13}
\]

由 (9)–(13)：

\[
\boxed{
0.02X-0.0121\varepsilon
<E
<0.02X+1.009\varepsilon.
}
\tag{14}
\]

特别地，因为 `X<2`、`varepsilon<=10^-6`，有

\[
\boxed{E<0.041.}
\tag{15}
\]

---

## 5. 从 `u` 恢复到原始 `rho` 尺度

把 (14) 代回精确式 (1)。

### 5.1 `u` 的下界

利用 `w\le4`、`c\le4` 和 (15)：

\[
\frac{w\varepsilon}{2}E
<2\varepsilon\cdot0.041
=0.082\varepsilon,
\]

\[
\frac{cw\varepsilon}{10}
\le1.6\varepsilon.
\]

所以

\[
\begin{aligned}
u
&>5(0.02X-0.0121\varepsilon)
-0.082\varepsilon
-1.6\varepsilon\\
&=0.1X-1.7425\varepsilon.
\end{aligned}
\]

即

\[
\boxed{
u>0.1X-1.7425\varepsilon.}
\tag{16}
\]

### 5.2 `u` 的上界

(1) 的后两项非负，因此

\[
u<5E.
\]

由 (14)：

\[
\boxed{
u<0.1X+5.045\varepsilon.}
\tag{17}
\]

合并：

\[
\boxed{
-1.7425\varepsilon
<
 u-\frac{1+\sigma-\delta}{10}
<5.045\varepsilon.
}
\tag{18}
\]

这就是上一版 sharp significand lock 的二阶版本。

---

## 6. near-integer tail theorem

因为

\[
10u=\frac j{10^k}=\delta j,
\qquad
\sigma=\delta\rho,
\]

把 (18) 乘以 `10/delta` 得

\[
-17.425\delta
<
j-10^k-\rho+1
<50.45\delta.
\tag{19}
\]

而 `k>=3` 给出 `delta<=10^-3`。所以全体无界 minimal diagonal 上统一有

\[
\boxed{
-0.0175
<
j-10^k-\rho+1
<0.0505.
}
\tag{20}
\]

令

\[
\boxed{N=j-10^k+1\in\mathbb Z.}
\tag{21}
\]

则 (20) 等价于

\[
\boxed{
N-0.0505
<\rho
<N+0.0175.
}
\tag{22}
\]

也就是说，虽然 `rho` 本身处在随 `k` 增长的 decade

\[
10^{k-1}\le\rho<10^k,
\]

但它到一个明确整数 `N` 的距离始终小于 `0.0505`，且上、下两侧还具有明显不对称性。

这是一个 **与 `k` 无关的常数窗口**。

---

## 7. 十进制尾位直接坍缩

若 `rho` 不是整数，记其小数部分为 `{rho}`。

由 (22) 只有两种可能：

\[
\rho\ge N
\Longrightarrow
0<\{\rho\}<0.0175,
\]

或

\[
\rho<N
\Longrightarrow
0.9495<\{\rho\}<1.
\]

连同整数情形可统一写成

\[
\boxed{
\{\rho\}
\in
[0,0.0175)
\cup
(0.9495,1).
}
\tag{23}
\]

由于

\[
\rho=\frac{b_3}{10^\ell},
\]

小数点恰好位于 `b_3` 的前 `k` 位之后。因此：

\[
\boxed{
\text{`b_3` 的前 `k` 位之后紧接的下一位十进制数字只能是 `0` 或 `9`.}
}
\tag{24}
\]

这比上一轮只同步 leading significand 的结论更强：现在第三分母在 prefix/tail 分界处已经出现一个真实的十进制 digit collapse。

---

## 8. 整数尾与小分母排除

### 8.1 整数尾精确化

若

\[
\rho\in\mathbb Z,
\]

则

\[
j-10^k-\rho+1
\]

也是整数。区间 (20) 中唯一的整数是 `0`，所以

\[
\boxed{
\rho=j-10^k+1.
}
\tag{25}
\]

特别地，若 normalized tail

\[
\rho=h2^x5^y
\]

满足

\[
x\ge0,
\qquad y\ge0,
\]

则 `rho` 自动为整数，因此

\[
\boxed{
 j=10^k-1+h2^x5^y.
}
\tag{26}
\]

这把 nonnegative `2/5` sector 中的 prefix remainder 与 odd-prime supply 变成了**精确等式**，不再只是 significand 近似。

### 8.2 非整数尾必须有较大约分母

若

\[
\rho=\frac ad
\]

为既约非整数有理数，则它到任一整数的距离至少为 `1/d`。

由 (22)：

\[
\operatorname{dist}(\rho,\mathbb Z)<0.0505.
\]

因此

\[
\boxed{d\ge20.}
\tag{27}
\]

对

\[
\rho=h2^x5^y,
\qquad \gcd(h,10)=1,
\]

其既约分母精确为

\[
\boxed{
d=2^{\max(-x,0)}5^{\max(-y,0)}.
}
\tag{28}
\]

所以任何非整数 tail state 都必须满足

\[
\boxed{
2^{\max(-x,0)}5^{\max(-y,0)}\ge20.
}
\tag{29}
\]

这在 `(x,y)` 平面上挖掉了 nonnegative quadrant 周围的一整圈小负指数状态。例如：

- 只有 `x<0` 时必须 `x\le-5`；
- 只有 `y<0` 时必须 `y\le-2`；
- `x=-1,y=-1` 的分母 `10` 不可能；
- `x=-2,y=-1` 的分母 `20` 是第一个未被该粗界自动排除的双负例子。

---

## 9. 对当前 A1 前沿的意义

此前 `k=g>=3` 的 diagonal 已有：

- `X_0=Y_0=k` 的统一 `2/5` cross-corridor cap；
- odd-prime supply
  \[
  h=qs,
  \qquad q\mid Q,
  \]
  且 `b_1` 侧只允许完整选择 `1 mod 4` prime-power blocks；
- sharp significand lock
  \[
  \left|\frac j{10^k}-(1+\sigma)\right|<0.0012.
  \]

本文把第三条升级成原始 `rho` 尺度上的常数刚性：

\[
\boxed{
\rho
=j-10^k+1+\eta,
\qquad
-0.0505<\eta<0.0175.
}
\tag{30}
\]

因此下一步不应再把 `rho` 当作整个 decade 中连续漂移的尾参数。真正剩余的 tail geometry 已分成两类：

1. **整数尾 sector**：直接使用精确式
   \[
   j=10^k-1+h2^x5^y;
   \]
2. **非整数尾 sector**：约分母至少为 `20`，并且 `b_3` 在 prefix/tail 分界后的第一位只能为 `0` 或 `9`。

这给 denominator prime graph、`2/5` resonance 和 decimal digit geometry 提供了一个新的共同接口。

---

<a id="source-positive-tail-residual"></a>

> 整合来源：`positive-tail-residual.md`

# A1 minimal diagonal positive tail residual

> 日期：2026-08-19。本文继续 `near-integer-tail.md`。仍处于
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge3.
> \]
> 记
> \[
> \rho=\frac{b_3}{10^\ell},\qquad
> N_0=j-10^k+1\in\mathbf Z.
> \]

本文把上一轮 near-integer 窗的符号彻底确定下来。核心结论是

\[
\boxed{
5.09\,10^{-k}
< N_0-\rho
<50.45\,10^{-k}.
}
\tag{1}
\]

因此 `rho` 永远严格位于整数 `N_0` 的左侧。特别地：

\[
\boxed{\text{minimal diagonal 的 saturated sector 在 }k\ge3\text{ 全部为空。}}
\tag{2}
\]

把误差乘回 `10^ell` 后，整数 residual

\[
 t=N_0 10^\ell-b_3
\]

满足

\[
\boxed{
5.09\,10^{\ell-k}<t<50.45\,10^{\ell-k}.
}
\tag{3}
\]

于是

\[
\boxed{\ell\le k-2\Longrightarrow\text{无候选},}
\tag{4}
\]

并且第一条可能的尾长边界 `ell=k-1` 精确只剩

\[
\boxed{t\in\{1,2,3,4,5\}.}
\tag{5}
\]

状态：**已严格完成。**

---

## 1. 输入与记号

沿用 `near-integer-tail.md`：

\[
\delta=10^{-k},\qquad
\varepsilon=10^{-2k}=\delta^2,
\]

\[
\sigma=\frac{\rho}{10^k}\in[0.1,1),
\qquad
u=\frac{j}{10^{k+1}},
\]

并定义

\[
\boxed{X=1+\sigma-\delta.}
\tag{6}
\]

minimal diagonal 的精确 gap/excess 关系为

\[
\boxed{
 u
=5E-\frac{w\varepsilon}{2}E
-\frac{cw\varepsilon}{10},
\qquad c=5-z\in\{4,2\}.
}
\tag{7}
\]

positive excess decomposition 写成

\[
E=S_1+S_2+
\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
+\varepsilon^2\phi_1^2,
\tag{8}
\]

其中 `S_2>=0`，而 `near-integer-tail.md` 已严格证明第一 source

\[
\boxed{
S_1>0.02X-0.0121\varepsilon.
}
\tag{9}
\]

上一轮为了得到双侧误差窗，没有使用曲率项的正下界。这里正是把它补回来。

---

## 2. 曲率项有统一的 `0.45 epsilon` 正供给

在 diagonal 中

\[
\phi_2=\frac z{10}
\]

且

\[
\phi_1=\frac{c+u}{10-w\varepsilon}.
\]

因为 `u>0`、`w epsilon>0`，有

\[
\phi_1>\frac c{10}.
\]

另一方面既有 half-gap kernel 给出

\[
\phi_1<0.434<1.
\]

对固定 `phi_2`，函数

\[
f(x)=2x+\phi_2^2-x^2
\]

在 `0<x<1` 上严格递增。

### `z=1`

此时

\[
c=4,\qquad \phi_2=0.1,\qquad \phi_1>0.4,
\]

故

\[
2\phi_1+\phi_2^2-\phi_1^2
>0.8+0.01-0.16
=0.65.
\]

### `z=3`

此时

\[
c=2,\qquad \phi_2=0.3,\qquad \phi_1>0.2,
\]

故

\[
2\phi_1+\phi_2^2-\phi_1^2
>0.4+0.09-0.04
=0.45.
\]

所以六个 prefix 类型统一满足

\[
\boxed{
2\phi_1+\phi_2^2-\phi_1^2>0.45.
}
\tag{10}
\]

结合 (8)、`S_2>=0`、最后一项非负以及 (9)：

\[
\boxed{
E>0.02X+0.4379\varepsilon.
}
\tag{11}
\]

这是决定 residual 符号的关键强化。

---

## 3. `10u-X` 严格为正

由精确式 (7)：

\[
10u=(50-5w\varepsilon)E-cw\varepsilon.
\]

因此

\[
10u-X
=(50-5w\varepsilon)E-cw\varepsilon-X.
\]

把 (11) 代入。由于 `50-5w epsilon>0`：

\[
\begin{aligned}
10u-X
&>(50-5w\varepsilon)
  (0.02X+0.4379\varepsilon)
  -cw\varepsilon-X\\
&=\varepsilon
\left(
21.895-cw-0.1wX-2.1895w\varepsilon
\right).
\end{aligned}
\tag{12}
\]

六类型中

\[
c\le4,\qquad w\le4,
\]

而

\[
X=1+\sigma-\delta<2.
\]

并且 `k>=3` 给出

\[
\varepsilon\le10^{-6}.
\]

故括号中的量严格大于

\[
21.895-16-0.8-2.1895\cdot4\cdot10^{-6}
>5.09.
\]

于是

\[
\boxed{
10u-X>5.09\varepsilon.
}
\tag{13}
\]

---

## 4. 转回原始 near-integer residual

由定义

\[
10u-X
=
\frac{j}{10^k}
-1
-\frac\rho{10^k}
+10^{-k}
=
\frac{N_0-\rho}{10^k}.
\]

所以 (13) 乘以 `10^k` 得

\[
\boxed{
N_0-\rho>5.09\,10^{-k}.
}
\tag{14}
\]

另一方面 `near-integer-tail.md` 已证明旧上界

\[
N_0-\rho<50.45\,10^{-k}.
\tag{15}
\]

合并即得到主结论 (1)：

\[
\boxed{
5.09\,10^{-k}
<N_0-\rho
<50.45\,10^{-k}.
}
\]

特别地

\[
\boxed{\rho<N_0.}
\tag{16}
\]

---

## 5. saturated sector 全部消失

saturated `L=1` 的定义是

\[
10^\ell\mid b_3.
\]

于是

\[
\rho=\frac{b_3}{10^\ell}\in\mathbf Z.
\]

同时 `N_0` 也是整数。

但对 `k>=3`，(1) 给出

\[
0<N_0-\rho<50.45\cdot10^{-3}<1.
\]

两个整数之差不可能严格落在 `(0,1)` 中。因此

\[
\boxed{
L=1\text{ 在 minimal diagonal }k\ge3\text{ 中为空。}
}
\tag{17}
\]

这比此前 `short-tail-saturation.md` 的“`ell<=k-2` 强制进入 saturated”更强：被强制进入的 saturated 状态本身已经不可能存在。

---

## 6. 整数 residual 的统一正窗

定义

\[
\boxed{
 t=N_0 10^\ell-b_3
=(N_0-\rho)10^\ell\in\mathbf Z.
}
\tag{18}
\]

由 (1)：

\[
\boxed{
5.09\,10^{\ell-k}
<t
<50.45\,10^{\ell-k}.
}
\tag{19}
\]

并且

\[
\boxed{t>0.}
\tag{20}
\]

### `ell<=k-2`

此时

\[
t<50.45\cdot10^{-2}=0.5045.
\]

与 `t` 为正整数矛盾。因此

\[
\boxed{
\ell\le k-2\Longrightarrow\text{无候选。}
}
\tag{21}
\]

所以任何剩余 candidate 必须满足

\[
\boxed{\ell\ge k-1.}
\tag{22}
\]

### `ell=k-1`

由 (19)：

\[
0.509<t<5.045.
\]

故

\[
\boxed{t\in\{1,2,3,4,5\}.}
\tag{23}
\]

### `ell=k`

同理：

\[
5.09<t<50.45,
\]

所以

\[
\boxed{t\in\{6,7,\ldots,50\}.}
\tag{24}
\]

这说明 genuinely-long tail 也不是完全连续的自由参数；每个固定 `ell-k` 都落在一个明确的有限 residual shell 中。

---

## 7. 对当前前沿的意义

结合 `k=1,2,3,4,5` 已有有限证书，当前无界 minimal diagonal 从此可以直接假设

\[
\boxed{k=g\ge6.}
\]

而第三尾同时满足

\[
\boxed{L>1,\qquad \ell\ge k-1,\qquad t>0.}
\]

第一条边界进一步只有

\[
\boxed{
ell=k-1,
\qquad
t\in\{1,2,3,4,5\}.
}
\]

因此下一步无需再研究 saturated short-tail；应直接攻击这五个 boundary residual，然后进入 `ell>=k` 的正 residual shells。

---

<a id="source-residual-shell-supply"></a>

> 整合来源：`residual-shell-supply.md`

# A1 minimal diagonal regular residual-shell supply

> 日期：2026-08-19。本文把 `boundary-decimal-supply.md` 从 `ell=k-1` 推广到任意 residual shell。
> 仍处于
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge6.
> \]

由 `positive-tail-residual.md`，定义

\[
N_0=j-10^k+1,
\qquad
 t=(N_0-\rho)10^\ell
=N_0 10^\ell-b_3\in\mathbf Z_{>0}.
\]

并有

\[
5.09\,10^{\ell-k}<t<50.45\,10^{\ell-k}.
\tag{1}
\]

本文证明：只要

\[
\boxed{
v_2(t)<\ell,
\qquad
v_5(t)<\ell,}
\tag{2}
\]

则令

\[
a_t=2^{v_2(t)}5^{v_5(t)},
\qquad
\widehat t=t/a_t,
\]

必有

\[
\boxed{b_3=a_t h,}
\tag{3}
\]

其中 `h` 属于 minimal-diagonal 的有限 odd-prime supply，并且

\[
\boxed{
\frac{10^\ell}{a_t}\mid h+\widehat t,
}
\tag{4}
\]

\[
\boxed{
N_0=\frac{a_t(h+\widehat t)}{10^\ell}.
}
\tag{5}
\]

因此每个满足 (2) 的 residual shell 都自动变成有限 divisor-congruence problem。

特别地，对全部 `k>=6` 的 `ell=k` shell，(1) 给

\[
\boxed{t\in\{6,7,\ldots,50\},}
\tag{6}
\]

而这些整数统一满足 (2)，所以 `ell=k` 整层都可以只枚举有限 `h` supply。

状态：**已严格完成。**

---

## 1. 赋值比较

由 residual 定义

\[
b_3=N_0 10^\ell-t.
\tag{7}
\]

第一项同时至少被

\[
2^\ell,
\qquad
5^\ell
\]

整除。

若 (2) 成立，则在 `p=2,5` 两个素数上，右侧两项赋值严格不同，因此低赋值项由 `t` 唯一承担：

\[
\boxed{v_2(b_3)=v_2(t),}
\tag{8}
\]

\[
\boxed{v_5(b_3)=v_5(t).}
\tag{9}
\]

所以提出完整 `2/5` 部分后

\[
b_3=a_t h,
\qquad \gcd(h,10)=1.
\]

这就是 (3)。

---

## 2. odd-prime supply 不随 `ell` 改变

minimal diagonal odd-prime theorem 已给出

\[
\boxed{h=q\,s,}
\]

其中

\[
q\mid Q,
\]

而 `s` 是 `b_1` 中 `1 mod4` odd prime-power blocks 的 whole-block selector。

因此对固定 `(k,w)`，可能的 `h` 始终属于同一个有限集合

\[
\mathcal H_{k,w},
\]

与 `ell,t,N_0` 无关。

---

## 3. 任意 regular shell 的十进制同余

写

\[
t=a_t\widehat t.
\]

把 (3) 代入 (7)：

\[
a_t h=N_0 10^\ell-a_t\widehat t.
\]

所以

\[
a_t(h+\widehat t)=N_0 10^\ell.
\]

因为 `a_t|10^ell`，得到

\[
\boxed{
\frac{10^\ell}{a_t}\mid h+\widehat t.
}
\]

并唯一恢复

\[
\boxed{
N_0=\frac{a_t(h+\widehat t)}{10^\ell}.
}
\]

这说明：对 regular residual，搜索变量应为 `(h,t)`，而不应扫描 `N_0` 或 `(x,y)`。

---

## 4. `ell=k` 自动全部 regular

取

\[
\ell=k.
\]

由 (1)：

\[
5.09<t<50.45,
\]

所以

\[
6\le t\le50.
\]

在该区间中

\[
v_2(t)\le5,
\qquad
v_5(t)\le2.
\]

而当前

\[
k=\ell\ge6.
\]

故

\[
v_2(t),v_5(t)<\ell
\]

对全部 `t=6,...,50` 自动成立。

所以

\[
\boxed{
\ell=k\text{ shell 完全属于 regular divisor-congruence regime.}
}
\tag{10}
\]

---

## 5. 后续 shell 的 exceptional residual

当 `ell-k` 增大时，(1) 中的 `t` 窗也按十倍增长；此时可能出现

\[
v_2(t)\ge\ell
\quad\text{或}\quad
v_5(t)\ge\ell.
\]

这些 residual 不能直接使用 (8)–(9)，因为 `N_0 10^ell` 与 `t` 可能在相同或更深的 `2/5` 层发生 cancellation。

因此长尾自然分成：

1. **regular residuals**：满足 (2)，直接使用有限 `h` congruence；
2. **deep-2/5 residuals**：至少一个赋值达到 `ell`，需要单独做 resonance/cancellation 分析。

这给 `ell>=k` 的 genuinely-long tail 一个新的、比旧 `(x,y)` 平面更细的分层。

---

<a id="source-sharp-positive-tail-window"></a>

> 整合来源：`sharp-positive-tail-window.md`

# A1 minimal diagonal: sharpened positive tail window

> 日期：2026-08-19。本文继续 `positive-tail-residual.md`，仍处于
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge3.
> \]
> 记
> \[
> \rho=\frac{b_3}{10^\ell},\qquad N_0=j-10^k+1.
> \]

本文把旧的统一窗口

\[
5.09\,10^{-k}<N_0-\rho<50.45\,10^{-k}
\]

严格加强为

\[
\boxed{
15.09\,10^{-k}<N_0-\rho<39.003\,10^{-k}.
}
\tag{1}
\]

等价地，归一化 gap

\[
\Gamma_k:=10^k(N_0-\rho)
\]

必须满足

\[
\boxed{15.09<\Gamma_k<39.003.}
\tag{2}
\]

状态：**已严格完成。**

---

## 1. 输入

沿用前文记号

\[
\delta=10^{-k},\qquad \varepsilon=10^{-2k},
\]

\[
X=1+\sigma-\delta,\qquad 1.099<X<2,
\]

\[
c=5-z,
\qquad
(z,w)\in\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
\]

已有精确关系

\[
10u=(50-5w\varepsilon)E-cw\varepsilon,
\tag{3}
\]

以及

\[
10u-X=\frac{N_0-\rho}{10^k}.
\tag{4}
\]

第一 positive source 已有双侧界

\[
0.02X-0.0121\varepsilon<S_1<0.02X+0.0504\varepsilon.
\tag{5}
\]

全 excess 为

\[
E=S_1+S_2+
\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
+\varepsilon^2\phi_1^2,
\tag{6}
\]

其中

\[
0<S_2<\varepsilon^2,
\qquad 0<\phi_1<0.434=\frac{217}{500},
\qquad \phi_2=\frac z{10}.
\tag{7}
\]

---

## 2. 类型相关曲率下界

函数

\[
f_z(x)=2x+\left(\frac z{10}\right)^2-x^2
\]

在 `0<x<1` 上严格递增。

### `z=1`

此时 `c=4` 且 `phi_1>0.4`，故

\[
f_1(\phi_1)>f_1(0.4)=0.65.
\tag{8}
\]

结合 (5)-(6) 中其余非负项：

\[
\boxed{E>0.02X+0.6379\varepsilon.}
\tag{9}
\]

### `z=3`

此时 `c=2` 且 `phi_1>0.2`，故

\[
f_3(\phi_1)>f_3(0.2)=0.45,
\]

从而

\[
\boxed{E>0.02X+0.4379\varepsilon.}
\tag{10}
\]

旧证明把 `cw<=16` 与曲率 `>0.45` 同时使用，但这两个最坏情况不能发生在同一类型；本文正是保留这点互斥信息。

---

## 3. 下界提高到 `15.09`

令

\[
a_z=
\begin{cases}
0.6379,&z=1,\\
0.4379,&z=3.
\end{cases}
\]

由 (3) 与 (9)-(10)：

\[
\begin{aligned}
10u-X
&>(50-5w\varepsilon)(0.02X+a_z\varepsilon)
-cw\varepsilon-X\\
&=\varepsilon
\left(
50a_z-cw-0.1wX-5wa_z\varepsilon
\right).
\end{aligned}
\tag{11}
\]

使用 `X<2` 与 `epsilon<=10^-6`，六类型的安全下界分别为：

| `(z,w)` | `(10u-X)/epsilon` 的严格下界 |
|---|---:|
| `(1,1)` | `>27.6949968` |
| `(1,2)` | `>23.4949936` |
| `(1,3)` | `>19.2949904` |
| `(1,4)` | `>15.0949872` |
| `(3,1)` | `>19.6949978` |
| `(3,2)` | `>17.4949956` |

因此统一有

\[
\boxed{10u-X>15.09\varepsilon.}
\tag{12}
\]

由 (4) 且 `epsilon=10^{-2k}`：

\[
\boxed{N_0-\rho>15.09\,10^{-k}.}
\tag{13}
\]

---

## 4. 曲率上界也按类型收紧

由于 `f_z` 在当前区间递增，并且 `phi_1<217/500`：

\[
f_1(\phi_1)
<2\frac{217}{500}+\frac1{100}
-\left(\frac{217}{500}\right)^2
=0.689644,
\tag{14}
\]

\[
f_3(\phi_1)
<2\frac{217}{500}+\frac9{100}
-\left(\frac{217}{500}\right)^2
=0.769644.
\tag{15}
\]

由 (5)-(7)：

\[
E<0.02X+A_z\varepsilon+1.189\varepsilon^2,
\tag{16}
\]

其中

\[
A_1=0.0504+0.689644=0.740044,
\]

\[
A_3=0.0504+0.769644=0.820044.
\]

---

## 5. 上界降低到 `39.003`

把 (16) 代入 (3)。在求上界时丢掉所有负 correction，可得

\[
\frac{10u-X}{\varepsilon}
<50A_z+50(1.189)\varepsilon-cw.
\tag{17}
\]

因 `epsilon<=10^-6`，六类型右侧最大值发生在 `(z,w)=(3,1)`：

\[
50(0.820044)+50(1.189)10^{-6}-2
=39.00225945
<39.003.
\tag{18}
\]

因此

\[
\boxed{10u-X<39.003\varepsilon,}
\tag{19}
\]

再由 (4)：

\[
\boxed{N_0-\rho<39.003\,10^{-k}.}
\tag{20}
\]

(13) 与 (20) 即给出主结论 (1)。

---

## 6. 对后续 finite-box / gap-desert 的意义

以后所有 minimal-diagonal fixed-layer certificate 都只需排除

\[
\boxed{15.09<10^k(\lceil\rho\rceil-\rho)<39.003.}
\tag{21}
\]

这里 `ceil(rho)=N_0` 由正号定理保证。

这个新窗口完全由连续几何与 prefix 类型信息推出，不使用任何 `k` 的有限枚举，因此可以直接作为全部 `k>=3` 的统一输入。

---

<a id="source-short-tail-saturation"></a>

> 整合来源：`short-tail-saturation.md`

# A1 minimal diagonal short-tail saturation collapse

> 日期：2026-08-19。本文继续 `near-integer-tail.md`，研究仍未关闭的 minimal diagonal
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge4.
> \]
> 记第三分子位数为
> \[
> \ell=n_3.
> \]

核心结论：

\[
\boxed{
\ell\le k-2
\Longrightarrow
10^\ell\mid b_3.
}
\]

因此所有 non-saturated 候选都必须满足

\[
\boxed{\ell\ge k-1.}
\]

并且第一条非饱和边界 `ell=k-1` 只剩七个显式整数 residual。

状态：**已严格完成。**

---

## 1. 把 near-integer gap 清成整数

沿用 near-integer theorem，令

\[
N=j-10^k+1\in\mathbb Z,
\qquad
\rho=\frac{b_3}{10^\ell}.
\]

对全部 `k>=3` 已证明

\[
\boxed{
-17.425\,10^{-k}
<N-\rho
<50.45\,10^{-k}.
}
\tag{1}
\]

乘以 `10^ell`。定义

\[
\boxed{
 t:=N10^\ell-b_3\in\mathbb Z.
}
\tag{2}
\]

则 (1) 精确变成

\[
\boxed{
-17.425\,10^{\ell-k}
<t
<50.45\,10^{\ell-k}.
}
\tag{3}
\]

关键变化是：连续误差现在夹住的是一个整数 `t`。

---

## 2. `ell<=k-2` 时 residual 只能为零

若

\[
\ell\le k-2,
\]

则

\[
10^{\ell-k}\le10^{-2}.
\]

所以 (3) 给出

\[
-0.17425<t<0.5045.
\]

区间中唯一整数是 `0`。因此

\[
\boxed{t=0.}
\tag{4}
\]

由定义 (2)：

\[
\boxed{
b_3=N10^\ell.}
\tag{5}
\]

故

\[
\boxed{10^\ell\mid b_3.}
\tag{6}
\]

这正是 `rational-contact.md` 中 saturated `L=1` 分支的定义。

于是得到统一结论

\[
\boxed{
\ell\le k-2
\Longrightarrow
L=1.
}
\tag{7}
\]

等价地，任何 non-saturated minimal-diagonal candidate 必须满足

\[
\boxed{
\ell\ge k-1.
}
\tag{8}
\]

这把第三块原先完全自由增长的位数参数第一次与 prefix 参数 `k` 直接绑定。

---

## 3. short-tail saturated sector 中 `tau` 被 prefix 精确决定

saturated 分支写成

\[
b_3=10^\ell\tau.
\]

由 (5) 立刻得到

\[
\boxed{
\tau=N=j-10^k+1.
}
\tag{9}
\]

而第三分母必须恰有 `m_3=k+ell` 位，所以

\[
10^{k-1}\le\tau<10^k.
\]

因此在 short-tail sector 中自动有

\[
\boxed{
10^{k-1}
\le j-10^k+1
<10^k.
}
\tag{10}
\]

也就是说 saturated 参数 `tau` 不再是独立自由变量，它就是 moving-prefix remainder `j` 的一个固定线性平移。

此外

\[
\theta=\frac{b_3}{10^\ell D}
=rac\tau D
=rac{j-10^k+1}{D},
\tag{11}
\]

因此 `theta` 同时完全脱离 `ell`。

这与旧 saturated rational-contact reduction 正好对接：固定 `(k,z,w,j)` 后，整个 contact quadratic 已经与第三块位数 `ell` 无关。

---

## 4. 第一条非饱和边界 `ell=k-1` 只有七个 residual

现在取

\[
\ell=k-1.
\]

由 (3)：

\[
-1.7425<t<5.045.
\]

所以

\[
\boxed{
 t\in\{-1,0,1,2,3,4,5\}.
}
\tag{12}
\]

因此

\[
\boxed{
 b_3=N10^{k-1}-t,
\qquad
t\in\{-1,0,1,2,3,4,5\}.
}
\tag{13}
\]

`t=0` 仍是 saturated；所有真正 non-saturated 的 `ell=k-1` 状态只剩六个非零 residual。

---

## 5. `ell=k-1` 非饱和状态的 `2/5` 指数被精确锁定

设 `t!=0` 且 `ell=k-1`。因为

\[
b_3=N10^\ell-t,
\]

有

\[
\gcd(b_3,10^\ell)=\gcd(t,10^\ell).
\]

所以既约正规化

\[
\rho=\frac{b_3}{10^\ell}
\]

的分母恰为

\[
\frac{10^\ell}{\gcd(t,10^\ell)}.
\]

写

\[
\rho=h2^x5^y,
\qquad
\gcd(h,10)=1.
\]

因为 `|t|<=5` 且 `ell=k-1>=3`，可直接得到

\[
\boxed{
 x=-(k-1-v_2(t)),
\qquad
 y=-(k-1-v_5(t)).
}
\tag{14}
\]

因此六个 nonzero residual 对应：

| `t` | `x` | `y` |
|---:|---:|---:|
| `-1` | `-(k-1)` | `-(k-1)` |
| `1` | `-(k-1)` | `-(k-1)` |
| `2` | `-(k-2)` | `-(k-1)` |
| `3` | `-(k-1)` | `-(k-1)` |
| `4` | `-(k-3)` | `-(k-1)` |
| `5` | `-(k-1)` | `-(k-2)` |

所以在第一条非饱和位数边界上，原本二维自由的 `(x,y)` 已完全消失：只剩由一个六值 residual `t` 决定的六条显式 valuation patterns。

---

## 6. 对 `k>=4` 前沿的结构性分裂

结合本文，尚未关闭的 minimal diagonal 可以严格分成：

### A. saturated short-tail sector

\[
\boxed{
\ell\le k-2,
\qquad
b_3=10^\ell(j-10^k+1),
}
\]

其中 `theta=(j-10^k+1)/D` 与 `ell` 无关。

### B. first nonsaturated boundary

\[
\boxed{
\ell=k-1,
}
\]

其中非饱和状态只有

\[
t\in\{-1,1,2,3,4,5\}
\]

及表 (14) 的六个精确 `(x,y)` patterns。

### C. genuinely long tail

\[
\boxed{
\ell\ge k.
}
\]

只有这一部分仍保留较大的 residual 自由度。

因此后续证明不应继续把 `ell` 当作完全无结构的无限参数。新的自然顺序是：先关闭 A，再关闭 B，最后研究 `ell>=k` 的长尾。

---

<a id="source-uniform-2adic-prefix"></a>

> 整合来源：`uniform-2adic-prefix.md`

# A1 minimal diagonal: uniform 2-adic prefix theorem

> 日期：2026-08-19。本文补充 `uniform-layer-finite-box.md` 中的 2-adic 部分。
> 当前范围
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge3.
> \]

核心结论：2-adic prefix valuation 根本不需要 root lifting。对所有合法 prefix，

\[
\boxed{
 w\text{ even}\Longrightarrow v_2(N)=0,
}
\tag{1}
\]

\[
\boxed{
 w\text{ odd}\Longrightarrow v_2(N)\le1.
}
\tag{2}
\]

因此 resonance threshold

\[
x_*=2v_2(w)-1-k-v_2(N)
\]

在六类型上的全局精确 floor 为

\[
\boxed{
\underline x_*(k)=-k-2.
}
\tag{3}
\]

状态：**已严格完成。**

---

## 1. 输入

minimal diagonal 中

\[
b_1=10^{2k+1}-w,
\qquad
a_2=10^{2k+1}-z,
\]

其中 `z` 始终为奇数，`w in {1,2,3,4}`，并且原问题始终带有

\[
\gcd(a_1,b_1)=1.
\tag{4}
\]

定义

\[
N=a_1^2+(a_2b_1)^2.
\tag{5}
\]

又因为 `2k+1>v_2(w)`，有

\[
v_2(b_1)=v_2(w).
\tag{6}
\]

同时 `a_2` 为奇数。

---

## 2. `w` 为偶数时 `N` 必为奇数

若 `w` 偶，则由 (6) `b_1` 为偶数。

结合 (4)，`a_1` 必为奇数。因此

\[
a_1^2\equiv1\pmod2,
\]

而

\[
(a_2b_1)^2\equiv0\pmod2.
\]

所以

\[
N\equiv1\pmod2,
\]

即

\[
\boxed{v_2(N)=0.}
\tag{7}
\]

这同时覆盖 `w=2` 与 `w=4`。

---

## 3. `w` 为奇数时 `v_2(N)` 至多为 1

若 `w` 奇，则 `b_1` 与 `a_2` 都为奇数，所以 `a_2b_1` 为奇数。

### `a_1` 偶

此时

\[
a_1^2\equiv0\pmod2,
\qquad
(a_2b_1)^2\equiv1\pmod2,
\]

故 `N` 为奇数：

\[
v_2(N)=0.
\]

### `a_1` 奇

任意奇数平方都满足

\[
x^2\equiv1\pmod8.
\]

因此

\[
N=a_1^2+(a_2b_1)^2\equiv1+1\equiv2\pmod8.
\]

所以此时恰有

\[
v_2(N)=1.
\]

综上：

\[
\boxed{w\text{ odd}\Longrightarrow v_2(N)\in\{0,1\}.}
\tag{8}
\]

---

## 4. resonance threshold 的闭式

已有

\[
x_*=2v_2(w)-1-k-v_2(N).
\tag{9}
\]

逐 `w` 得：

### `w=1,3`

`v_2(w)=0` 且 `v_2(N)<=1`，所以

\[
x_*\ge-k-2.
\tag{10}
\]

而允许 `a_1` 为奇的 prefix 确实可达到 `v_2(N)=1`，故这一 floor 是 sharp 的。

### `w=2`

`v_2(w)=1` 且由 (7) `v_2(N)=0`：

\[
\boxed{x_*=1-k.}
\tag{11}
\]

### `w=4`

`v_2(w)=2` 且 `v_2(N)=0`：

\[
\boxed{x_*=3-k.}
\tag{12}
\]

因此六类型统一的最小 threshold 为

\[
\boxed{\underline x_*(k)=-k-2.}
\tag{13}
\]

---

## 5. 对 fixed-layer certificate 的意义

`uniform-layer-finite-box.md` 原先通过模 `2^e` root lifting 计算每一层的 `x* floor`。本文说明该步骤可以永久删除：

\[
\boxed{x\text{-floor 直接写成 }-k-2.}
\]

以后只有 `5`-adic threshold

\[
y_*=-k-v_5(N)
\]

仍需要 root lifting 或进一步的统一解析估计。

此外 even-`w` 类型拥有比全局 floor 强得多的具体 threshold `(1-k)` 与 `(3-k)`，后续若需要做 typewise gap-desert 证明，应优先保留这一额外余量。

---
