# A1 minimal diagonal: `HL` mod-4 orientation filter

> 日期：2026-08-20。依赖 `deep-moderate-block-partition.md`、`deep-moderate-adjugate-gcd-lock.md` 与 `deep-gap-unit-square.md`。当前范围 `k=g>=31`。

虽然 `HL` 在 factor-pair 分类中叫 2-high / 5-low，但它的 denominator excess

\[
A=2k+3-v_2(r)
\]

对原 rational-contact square 来说显然处于 strict 2-adic low-side。因此 strict-2-low 的 Q-side orientation 必须继续使用。

本文把该 orientation 与 `HL` stripped equations 联立，得到 `alpha,beta,r_10` 的固定 mod-4 类。

状态：**已严格完成。**

---

## 1. `HL` 的两条 stripped equations

沿用

\[
r_{10}=\alpha\beta,
\qquad \gcd(\alpha,\beta)=1,
\]

以及

\[
u\mid b_1,
\quad v\mid Q,
\quad h=qs.
\]

`HL` 有

\[
\boxed{2\beta u-\alpha v=5^d,}
\tag{1}

以及

\[
\boxed{\beta q-5\alpha s=2^{c'}n_0,}
\tag{2}

其中 `c'>=1`，当前实际上 `c'` 随 `k` 很大。

whole-block selector 给

\[
\boxed{s\equiv1\pmod4.}
\tag{3}

---

## 2. strict-2-low Q-side orientation

因为 `A~2k`，必有

\[
A>1+v_2(N)-2v_2(w),
\]

所以 `deep-gap-unit-square.md` 的 strict-2-low orientation 对全部 HL 状态有效：

\[
\boxed{
q\equiv
\begin{cases}
1\pmod4,&w=1,3,\\
3\pmod4,&w=2,4.
\end{cases}}
\tag{4}

同时

\[
Q\equiv
\begin{cases}
3\pmod4,&w=1,3,\\
1\pmod4,&w=2,4.
\end{cases}
\]

---

## 3. `alpha mod 4`

由 (1)，因为 `5^d≡1 mod4`：

### odd `w`

此时 `u` 为奇数，所以

\[
2\beta u\equiv2\pmod4.
\]

因此

\[
\alpha v\equiv1\pmod4.
\]

又 `qv=Q`、`q≡1`、`Q≡3 mod4`，所以

\[
v\equiv3\pmod4.
\]

故

\[
\boxed{\alpha\equiv3\pmod4\qquad(w=1,3).}
\tag{5}

### even `w`

此时 `u` 为偶数，所以

\[
2\beta u\equiv0\pmod4.
\]

(1) 给

\[
\alpha v\equiv3\pmod4.
\]

而 `q≡3`、`Q≡1 mod4`，所以

\[
v\equiv3\pmod4.
\]

因此

\[
\boxed{\alpha\equiv1\pmod4\qquad(w=2,4).}
\tag{6}

所以四类型统一还有

\[
\boxed{v\equiv3\pmod4.}
\tag{7}

---

## 4. `beta mod 4`

当前 `c'` 至少为 `k+1-v_2(r)>=9`，所以 (2) 右侧被 4 整除。结合 `s≡1 mod4`：

\[
\beta q\equiv\alpha\pmod4.
\]

- odd `w`：`q≡1`、`alpha≡3`；
- even `w`：`q≡3`、`alpha≡1`。

两种情况都给

\[
\boxed{\beta\equiv3\pmod4.}
\tag{8}

---

## 5. `r_10` residue

由 `r_10=alpha*beta`：

\[
\boxed{
r_{10}\equiv1\pmod4\qquad(w=1,3),}
\tag{9}

\[
\boxed{
r_{10}\equiv3\pmod4\qquad(w=2,4).}
\tag{10}

这和 LL strict-2-low 的 residue 条件比较：

\[
LL:\quad
r_{10}\equiv
\begin{cases}
1,&w=1,2,4,\\
3,&w=3,
\end{cases}\pmod4.
\]

因此对 `w=2,3,4`，LL 与 HL 要求的 `r_10 mod4` 正好相反。

所以固定 `(w,r)` 后：

\[
\boxed{
w=2,3,4\Longrightarrow\text{strict LL 与 HL 至多存活一个 branch}.}
\tag{11}

`w=1` 两者都要求 `r_10≡1 mod4`，仍需后续条件区分。

---

## 6. 当前用途

moderate double-deep 已只剩 `LL`、`HL`。本文使 HL 的 whole-block partition 进一步带 orientation：

- `beta` 必须是 `3 mod4`；
- `alpha` 的 mod-4 类由 `w` 决定；
- `r_10` 的 residue 先于任何大整数 factorization 就能筛 branch。

后续对有限 `r` 做 modular / block-partition exhaustion 时应先应用 (9)-(11)。