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