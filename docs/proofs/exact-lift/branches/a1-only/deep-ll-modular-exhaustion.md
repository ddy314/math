# A1 minimal diagonal: complete moderate-`LL` modular exhaustion

> 日期：2026-08-20。依赖 `deep-ll-pell-normal-form.md`、`deep-typewise-r-window.md`、`deep-moderate-block-partition.md` 与原 rational-contact square。当前范围 `k=g>=31`。

本文关闭 moderate double-deep 的整个 `LL` branch：

\[
\boxed{\forall k\ge31,\quad \text{moderate LL is empty for all six prefix types}.}
\]

结合 `deep-double-5high-collapse.md`，moderate double-deep 从此只剩 `HL`。

状态：**已严格完成；附统一 C++ exact certificate。**

---

## 1. finite LL families

`deep-ll-pell-normal-form.md` 已证明 LL 中

\[
D=2^A5^B\mid r,
\qquad
R=r/D\in\mathbf Z_{>0},
\]

并把全部 `k`-依赖压进

\[
L=10^k/D.
\]

固定 `(z,w,r,D,gamma)` 后必须满足

\[
C_0N_0^2-uLN_0+1000\gamma^2L^2+\gamma R=0,
\]

其中

\[
C_0=w(10w-1),
\qquad
u=10\gamma(20w-1)+Dr.
\]

判别式为固定 generalized Pell family

\[
Y^2=A L^2+B,
\]

且 `B` 的完整 `Q_2/Q_5` squareclass 把 `gamma` 限入两个 `mod 40` classes。

`deep-typewise-r-window.md` 则给六类型绝对有限 `r` intervals。于是 LL 是一个绝对有限 fixed-family union。

---

## 2. 2-adic / block filters

写

\[
r_{10}=r/2^{v_2(r)}5^{v_5(r)}.
\]

对 even `w=2,4`：

\[
A>0\Longrightarrow A\text{ odd},
\]

且所有 LL 都在 original-contact strict 2-low，所以

\[
r_{10}\equiv1\pmod4.
\]

对 odd `w=1,3`，证书保留全部 resonance 小层：

- 若 `nu_2=0`：`A=1` resonance；strict-low 仅 `A>=3` odd；
- 若 `nu_2>0`：`A=1` high、`A=2` resonance；strict-low 仅 `A>=4` even。

只在 strict-low 子区使用：

\[
r_{10}\equiv1\pmod4\quad(w=1),
\]

\[
r_{10}\equiv3\pmod4\quad(w=3).
\]

所以没有把 odd-`w` resonance candidates 偷删掉。

---

## 3. odd-prime modular necessary condition

固定奇素数 `p!=2,5`。给定 fixed LL tuple 后，`10^k mod p` 只依赖

\[
k\bmod\operatorname{ord}_p(10).
\]

对每个这样的 residue，LL supply quadratic 关于 `N_0 mod p` 至多有两个根（退化线性情形单独精确处理）。每个根还必须通过原 rational-contact square modulo `p`。

因此每个 `p` 给出一个 exact allowed set

\[
S_p(z,w,r,D,\gamma)
\subseteq\mathbf Z/\operatorname{ord}_p(10)\mathbf Z.
\]

任何 exact candidate 的 `k` 必须同时属于所有选定 `S_p`。

---

## 4. common period 420

统一使用

\[
\boxed{
\mathcal P_0=
\{3,7,11,13,29,31,37,41,43,61,71,101,127\}.}
\]

这些素数都满足

\[
\operatorname{ord}_p(10)\mid420.
\]

所以每个 family 先被压成 `k mod 420` bitmask。

随后使用

\[
\boxed{
\mathcal P_1=
\{17,19,73,89,113,137,251,337,1009,4201\}.}
\]

先做 individual CRT incompatibility pruning，再把所有 order 与 `420` 联合提升到完整周期

\[
\boxed{277200.}
\]

最后在 `k mod277200` 上使用

\[
\boxed{
\mathcal P_2=
\{67,151,181,199,211,239,241,271,281,421,631,661,1933,2161,2689\},}
\]

这些素数的阶均整除 `277200`。

其中：

- `p=661`, `ord=220` 用于清除 `(1,1)` 中唯一额外顽固 residue family；
- `p=199`, `ord=99` 用于清除 `(3,1)` 中唯一额外顽固 residue family。

---

## 5. 六类型 exact statistics

完整证书统计如下：

\[
\begin{array}{c|r|r|r|r|r|r}
(z,w)&\text{local}&P_0\text{ families}&k\bmod420\text{ states}&P_1\text{ survivors}&k\bmod277200\text{ families}&\text{final}\\ \hline
(1,1)&57,278,520&593,553&1,016,555&93,222&6,980&0\\
(1,2)&19,206,685&93,027&155,388&13,674&916&0\\
(1,3)&25,308,717&162,735&258,880&20,743&1,530&0\\
(1,4)&4,331,873&18,342&28,788&2,271&154&0\\
(3,1)&306,099,009&3,156,352&5,421,691&500,727&37,426&0\\
(3,2)&110,439,962&575,335&974,681&86,545&6,020&0
\end{array}
\tag{1}
\]

合计 local-compatible fixed families：

\[
\boxed{522,664,766.}
\]

最终 surviving periodic states：

\[
\boxed0.
\]

大类型 `(1,1),(3,1),(3,2)` 可按 `r` 区间分块运行；每块都独立使用相同的 all-`k` modular conditions，所以分块只是执行方式，不改变证明集合。

---

## 6. 两个唯一 residual families

在原 `P_2` cover 下，只有两个 family 曾留下单一极薄周期状态。

### `(1,1)`

\[
(r,D,\gamma)=(981640,10,299),
\]

只剩

\[
k\equiv251999,277199\pmod{277200}.
\]

`p=661`、`ord=220` 对这两类都没有共同 supply/contact root，因此删除。

### `(3,1)`

\[
(r,D,\gamma)=(5570560,1280,42167),
\]

只剩

\[
k\equiv249637\pmod{277200}.
\]

`p=199`、`ord=99` 下，该类对应 `k≡58 mod99`，而 supply quadratic 与 contact square 没有共同 `N_0 mod199` 根，因此删除。

所以 final `0` 不是搜索截断，而是完整有限周期不相容。

---

## 7. 结论

六类型均无 periodic state，所以

\[
\boxed{
\forall k\ge31,\quad
\text{moderate double-deep LL is impossible}.}
\tag{2}
\]

此前：

- `deep-double-5high-collapse.md` 已关闭 moderate `LH`；
- `deep-balanced-collapse.md` 已关闭 high-high / balanced；
- transition strips 已关闭。

因此 moderate double-deep 现在只剩

\[
\boxed{HL.}
\tag{3}
\]

而 extreme 中 5-extreme 已关闭，只剩 2-extreme `E_2`。故完整 double-deep 已缩成

\[
\boxed{
\text{double-deep}=HL_{\rm moderate}\cup E_2.
}
\tag{4}
\]

两支都是 **2-high / 5-low**；从此 double-deep 不再含任何 2-low surviving branch。

---

## 8. 可复核证书

统一脚本：

`../../../../../scripts/exact-lift/a1-only/check_a1_deep_ll_modular_exhaustion.cpp`

调用方式：

```bash
g++ -O3 -std=c++17 check_a1_deep_ll_modular_exhaustion.cpp -o /tmp/a1-ll
/tmp/a1-ll 1 4
```

也可分块：

```bash
/tmp/a1-ll 3 1 384160 1500000
```

全区间运行会断言表 (1) 的 exact counts；分块运行则断言该块 final survivor count 为 `0`。