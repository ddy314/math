# A1 minimal diagonal: single-5 resonance collapse from the sphere factor

> 日期：2026-08-22。
>
> 依赖：A1 common-quotient normalization、`diagonal.md`、`deep-single5-decimal-height-collapse.md`。
>
> 范围：minimal diagonal `k=g>=32`，single-5 deep sector
> \[
> D_{\rm gap}=5^B,
> \qquad B>k.
> \]

状态：**已严格完成；single-5 的 `v_5(N)=B` resonance 全部为空。**

---

## 1. minimal diagonal 的 prefix norm 与 ghost sphere

minimal diagonal 有

\[
b_2=1,
\qquad
G=b_1,
\]

以及 prefix norm

\[
\boxed{
N=a_1^2+(a_2b_1)^2.
}
\tag{1}
\]

令原整数球面 normalization 为

\[
q=\operatorname{lcm}(b_1,b_2,b_3),
\qquad
y_i=\frac{a_iq}{b_i},
\]

\[
y_1^2+y_2^2+y_3^2=H^2.
\]

则

\[
y_1^2+y_2^2
=\frac{q^2}{b_1^2}
\left(a_1^2+(a_2b_1)^2\right)
=\frac{q^2}{b_1^2}N.
\tag{2}
\]

---

## 2. single-5 中所有原分母都是 5-units

minimal diagonal

\[
b_1=10^{2k+1}-w,
\qquad1\le w\le4,
\]

所以

\[
5\nmid b_1.
\]

当然 `b_2=1`。

single-5 的 normalized gap 为

\[
5^BT\rho=h2^{\lambda_2},
\qquad(h,10)=1,
\qquad T=10^k.
\]

把 `rho=M/L` 约到最低项得到

\[
v_5(L)=B+k,
\qquad 5\nmid M.
\]

真实第三块满足

\[
10^n=\omega L,
\qquad b_3=\omega M.
\]

因为 `10^n/L` 在 5 侧恰好把 `5^{B+k}` 补齐，而 `M` 是 5-unit，实际 `b_3` 也是 5-unit：

\[
\boxed{5\nmid b_3.}
\tag{3}
\]

因此

\[
\boxed{5\nmid q.}
\tag{4}
\]

结合 `5\nmid b_1`，(2) 给出

\[
\boxed{
 v_5(y_1^2+y_2^2)=v_5(N).
}
\tag{5}
\]

---

## 3. sphere factor 强迫 `v5(N)>=B+k`

A1 safe common quotient 给

\[
\boxed{H-y_3=La}
\tag{6}
\]

对某个正整数 `a`。

而球面恒等式给

\[
\boxed{
(y_1^2+y_2^2)
=(H-y_3)(H+y_3).
}
\tag{7}
\]

由 (6)：

\[
v_5(H-y_3)
\ge v_5(L)
=B+k.
\]

所以从 (7)：

\[
v_5(y_1^2+y_2^2)
\ge B+k.
\]

再用 (5)：

\[
\boxed{
 v_5(N)\ge B+k.
}
\tag{8}

由于 single-5 deep 有 `B>k>=32`，特别地

\[
\boxed{v_5(N)>2k.}
\tag{9}

---

## 4. resonance 全部消失

`deep-single5-decimal-height-collapse.md` 此前从 `kappa` square 单独得到二分：

\[
v_5(N)=B
\quad\text{or}\quad
v_5(N)\ge B+k.
\]

本文的 (8) 直接排除第一项，因为 `k>0`：

\[
B<B+k.
\]

因此 single-5 的真正 strict frontier 是

\[
\boxed{
 v_5(N)\ge B+k.
}
\tag{10}

不存在任何 5-adic resonance cell。

---

## 5. 对剩余 terminal cells 的影响

### Cell II

`deep-single5-terminal-cells.md` 的 fixed cell

\[
(z,w)=(1,4),
\qquad B=k+1,
\qquad\lambda_2=1
\]

现在只剩

\[
\boxed{v_5(N)\ge2k+1.}
\]

由该文件的 prefix reduction，等价于

\[
\boxed{
5^{2k+1}\mid(10^k+N_0-1)^2+16.
}
\]

所以每个 `k` 至多两个 Hensel prefix residues；原 `v_5(N)=k+1` resonance 整支删除。

### Cell III

Cell III 的 divisor congruence

\[
v_2(h+5^{B+2k}Q)=B+k-2
\]

现在必须附带更强的

\[
\boxed{v_5(N)\ge B+k.}
\]

因此当前 minimal-diagonal deep frontier 只有两个真正核：

1. Cell II 的 two-Hensel-root high branch；
2. Cell III 的 high-contact divisor congruence + high prefix norm。
