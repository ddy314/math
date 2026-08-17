# A1 top-layer half-gap lower-endpoint sharpening — 2026-08-17

本文对 `a1-top-layer-half-gap-shell-2026-08-17.md` 的保守下界做一个严格加强。

原文件已经证明

\[
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
<\frac{267}{500}.
\]

下界当时保守写成 `499/1000`。实际上 exact sphere 立即给出严格的

\[
\boxed{
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
>\frac12.
}
\]

因此最高层 `d=2,g\ge1` 的真实 half-gap shell 为

\[
\boxed{
\frac12
<
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
<\frac{267}{500}.
}

本文结论为 **已严格完成 / sharpening**。

---

## 1. `delta>alpha`

沿用

\[
R_0=1-\alpha,
\qquad
t=1-\delta.
\]

因为

\[
R^2=r_1^2+r_2^2+r_3^2>r_2^2,
\]

有

\[
R>r_2.
\]

除以 `A_0=10^kr_1>0`：

\[
R_0>t.
\]

因此

\[
\boxed{\delta>\alpha>0.}
\tag{1}
\]

---

## 2. 球面展开直接给 `delta/epsilon>1/2`

前文件已经得到精确恒等式

\[
2(\delta-\alpha)
=\varepsilon+q_0^2+\delta^2-\alpha^2.
\tag{2}
\]

由 (1)：

\[
\delta^2-\alpha^2>0.
\]

并且

\[
q_0^2>0.
\]

所以 (2) 立刻给出

\[
2(\delta-\alpha)>\varepsilon.
\]

从而

\[
\delta>\alpha+\frac\varepsilon2>rac\varepsilon2.
\]

即

\[
\boxed{
\frac\delta\varepsilon>\frac12.
}
\tag{3}
\]

---

## 3. 真实 carrier gap 的严格半单位下界

真实 gap 为

\[
D_0=A_0-r_2=\delta A_0.
\]

自然尺度

\[
H_0=M\varepsilon,
\qquad
M=10^{k+g+1}.
\]

而 residue kernel 中

\[
A_0=M+10^k\frac{U_1}{b_1}>M.
\]

所以

\[
\frac{A_0}{M}>1.
\]

结合 (3)：

\[
\frac{D_0}{H_0}
=
\frac\delta\varepsilon\frac{A_0}{M}
>\frac12.
\]

因此

\[
\boxed{
\frac{D_0}{10^{g+1-k}}>\frac12.
}
\tag{4}
\]

再用

\[
D_0=10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
\]

得到

\[
\boxed{
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
>\frac12.
}
\tag{5}
\]

---

## 4. 与既有上界合并

`a1-top-layer-half-gap-shell-2026-08-17.md` 已严格证明

\[
\frac{D_0}{10^{g+1-k}}<\frac{267}{500}.
\]

故最终壳层为

\[
\boxed{
\frac12
<
\frac{D_0}{10^{g+1-k}}
<\frac{267}{500}.
}
\tag{6}

其宽度仅为

\[
\frac{267}{500}-\frac12
=\frac{17}{500}
=0.034.
\]

---

## 5. `s=1` 两个子核的同步加强

当 `s=1` 时已知

\[
y=0,
\qquad z\in\{1,3\}.
\]

定义第一 residue contribution

\[
\Phi_1
=\frac{
10^kU_1/b_1
}{10^{g+1-k}}.
\]

第二项精确为

\[
\frac{U_2/b_2}{10^{g+1-k}}
=\frac z{10}.
\]

由 (6)：

### `z=1`

\[
\boxed{
\frac25<\Phi_1<\frac{217}{500}.
}
\tag{7}
\]

### `z=3`

\[
\boxed{
\frac15<\Phi_1<\frac{117}{500}.
}
\tag{8}
\]

所以第一余量分别严格位于 `2/5` 与 `1/5` 自然尺度的上侧；这正是 minimal-surplus 六类型核使用的加强版本。
