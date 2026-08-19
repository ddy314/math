# A1 minimal diagonal: moderate `r_10` block partition

> 日期：2026-08-20。依赖 `deep-moderate-factor-quotients.md`、`deep-four-factor-frame.md` 与 strict-2-low Q-side orientation。当前范围 `k=g>=31`。

本文记录 moderate branches 中一个离散化：把

\[
r_{10}:=r/2^{v_2(r)}5^{v_5(r)}
\]

写成 `alpha*beta` 时，`alpha,beta` 必须互素。因此 `r_10` 的每个 prime-power block 必须整个分配到一边，不能拆指数。

另外在 LL 的 strict 2-low 子区，Q-side orientation 继续给出一个 `r_10 mod 4` 过滤。

状态：**已严格完成。**

---

## 1. moderate factor quotients

`deep-moderate-factor-quotients.md` 给出

\[
\boxed{\alpha\beta=r_{10}},
\qquad
\gcd(\alpha\beta,10)=1.
\]

### LL

写

\[
u=2^e u_0,
\qquad e=v_2(w),
\qquad \gcd(u_0,10)=1.
\]

归一化 complementary relation

\[
bu-av=10T
\]

得到

\[
\boxed{
\beta u_0-\alpha v=2^c5^d,
}
\tag{1}

其中

\[
c=k+1-(A+\nu_2+e)>0,
\qquad
d=k+1-(B+\nu_5)>0.
\]

### HL

同理 high-2 / low-5 模板给

\[
\boxed{
2\beta u-\alpha v=5^d,
}
\tag{2}

其中

\[
d=k+1-(B+\nu_5)>0.
\]

（已关闭的 LH 也有完全对称的 pure-2 equation，但不再需要保留为剩余核心。）

---

## 2. `alpha,beta` 必须互素

因为

\[
u\mid b_1,
\qquad v\mid Q,
\qquad \gcd(b_1,Q)=1,
\]

有

\[
\gcd(u_0,v)=1.
\]

看 LL 的 (1)。左右两项 `beta*u_0` 与 `alpha*v` 都是奇数。若有奇素数 `p` 同时整除二者，则 `p` 必整除右侧 `2^c5^d`，所以 `p=5`。但 `alpha,beta,u_0,v` 全与 5 互素，矛盾。

因此

\[
\boxed{
\gcd(\beta u_0,\alpha v)=1.
}
\tag{3}

特别地

\[
\boxed{\gcd(\alpha,\beta)=1.}
\tag{4}

HL 的 (2) 同理：任何公共奇素数必须整除 `5^d`，但两项均与 5 互素，所以仍有 (4)。

于是若

\[
r_{10}=\prod p_i^{e_i},
\]

则每个完整 prime-power block `p_i^{e_i}` 必须整个进入 `alpha` 或整个进入 `beta`：

\[
\boxed{
\alpha=\prod_{i\in I}p_i^{e_i},
\qquad
\beta=\prod_{i\notin I}p_i^{e_i}.
}
\tag{5}

所以每个固定 `r` 最多只有

\[
\boxed{2^{\omega(r_{10})}}
\]

个 `(alpha,beta)` 分支，而不是普通 divisor count `tau(r_10)`。

---

## 3. LL 的 `u_0 mod 4`

whole-block selector `s` 只由 `1 mod 4` prime-power blocks 构成，所以

\[
\boxed{s\equiv1\pmod4.}
\]

而

\[
b_1=10^{2k+1}-w.
\]

去掉固定的 `2^e` 后：

\[
\boxed{
u_0\equiv-w_0\pmod4,}
\tag{6}

其中

\[
w=2^e w_0,
\qquad w_0\text{ odd}.
\]

因此：

\[
u_0\equiv
\begin{cases}
3\pmod4,&w=1,2,4,\\
1\pmod4,&w=3.
\end{cases}
\tag{7}

---

## 4. LL strict-2-low 的 `r_10 mod 4` filter

当前 `k>=31`，而 LL 有 `A<=23`，所以 (1) 右侧含至少 `2^2`；降模 4：

\[
\beta u_0\equiv\alpha v\pmod4.
\]

由于 odd units 模 4 中逆元等于自身，且 `alpha*beta=r_10`：

\[
\boxed{v\equiv r_{10}u_0\pmod4.}
\tag{8}

又

\[
qv=Q,
\]

而 strict 2-low 的 unit-square theorem 给

\[
q\equiv
\begin{cases}
1\pmod4,&w\text{ odd},\\
3\pmod4,&w\text{ even}.
\end{cases}
\tag{9}

直接代入 `Q mod 4` 与 (7)-(9)，得到

\[
\boxed{
r_{10}\equiv1\pmod4\qquad(w=1,2,4),}
\tag{10}
\]

\[
\boxed{
r_{10}\equiv3\pmod4\qquad(w=3).}
\tag{11}

这里 (10)-(11) 只在 LL 同时处于原 contact 的 strict 2-low 时使用；odd-`w` 的 2-adic resonance 小层仍单独保留。

---

## 5. 当前用途

moderate double-deep 已经只剩 `LL`、`HL`，且统一 `B<=10`。本文进一步把有限参数 `r` 的 quotient allocation 收紧成 whole-block partition。

后续 exhaustive modular work 应直接按

\[
(w,r,I)
\]

而不是 `(w,r,alpha,beta)` 的任意 divisor split 组织；LL strict-2-low 还可以先应用 (10)-(11) 删除错误的 `r_10 mod 4` 类。