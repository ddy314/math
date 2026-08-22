# A1 top layer: `s=1` far squared-tail phase

> 日期：2026-08-22。
>
> 依赖：`top-layer-s1-far-lowr-collapse.md` 与 `top-layer.md` 的 positive-excess decomposition。
>
> 范围：
> \[
> d=2,\qquad s=1,\qquad g\ge1,
> \]
> \[
> k\ge2g+1,
> \qquad
> 1\le r\le2k-g-2.
> \]

状态：**已严格完成 reduction。** 本文不再把 third-radius source 当作误差，而把它保留成第二个主相位。

定义前文 general-`r` 整数
\[
U_1=(5-z)10^{r+g}+10^g+J,
\]
以及
\[
\tau:=10^{k-g},
\qquad
\psi:=10^{g-1}r_3.
\]
由第三分数位数窗：
\[
\boxed{0<\psi<1.}
\tag{1}

最终得到
\[
\boxed{
0<
J+1-\frac\rho\tau
-5\cdot10^{r-3g}\psi^2
<\frac1{25}.
}
\tag{2}

因此 `J+1` 是由 denominator leading phase 与 squared third-ratio phase共同决定的唯一整数。

---

## 1. exact third-radius contribution

沿用
\[
S=2(\phi_1+\phi_2)-1
\]
与 exact phase identity
\[
1+\frac JH
=5\cdot10^rS-10w\varepsilon\phi_1,
\qquad H=10^g.
\tag{3}

positive-excess 中 third-radius source 恰为
\[
S_{\rm rad}=\frac{\zeta^2}{\varepsilon},
\qquad
\zeta=\frac{r_3}{10^{k+g+1}}.
\]
所以
\[
S_{\rm rad}
=\frac{r_3^2}{10^{2g+2}}.
\tag{4}

把 (4) 乘以 (3) 的系数 `5*10^r`，再乘 `H` 从 `J/H` 恢复到 `J`：
\[
H\cdot5\cdot10^rS_{\rm rad}
=5\cdot10^{r-g-2}r_3^2.
\]
由
\[
\psi=10^{g-1}r_3
\]
得到 exact identity
\[
\boxed{
H\cdot5\cdot10^rS_{\rm rad}
=5\cdot10^{r-3g}\psi^2.
}
\tag{5}

---

## 2. denominator phase

`top-layer-s1-far-lowr-collapse.md` 的 contact main-term audit 定义
\[
B_0=1-H^{-1}+\delta,
\qquad
\delta=\frac\rho{10^k},
\]
并证明乘 `5*10^r` 后
\[
B_0-2\varepsilon
<5\cdot10^rS_{\rm contact}
<B_0+2\varepsilon.
\tag{6}

乘 `H` 后，`B0` 的非整数部分恰为
\[
H\delta=\frac\rho{10^{k-g}}=\frac\rho\tau.
\tag{7}

---

## 3. lower bound after extracting both phases

仍记
\[
p=\phi_1,
\qquad q=\phi_2\in\{1/10,3/10\}.
\]
前文已证明
\[
W:=w/10^r<p
\]
以及
\[
2p+q^2-3p^2>0.31.
\]
因此 curvature source 与 denominator correction 的差满足
\[
5\cdot10^r\varepsilon(2p+q^2-p^2)
-10w\varepsilon p
>1.55\cdot10^r\varepsilon.
\tag{8}

`r>=1` 时右端大于 `15.5 epsilon`，严格覆盖 (6) 的 possible `2 epsilon` contact loss。`epsilon^2p^2` 仍为正。

所以从 (3) 中同时减去 contact center (7) 与 exact radius term (5) 后，得到
\[
\boxed{
J+1-\frac\rho\tau
-5\cdot10^{r-3g}\psi^2>0.
}
\tag{9}

---

## 4. upper width

上界时丢掉 (3) 中负的 denominator correction。除已抽出的 radius source外，只剩：

- contact error：乘 `H` 后小于 `2H epsilon`；
- curvature 两项：由 `2p+q^2-p^2<0.7` 与 `p^2<0.19`，乘 `H*5*10^r` 后小于
  \[
  3.51\cdot10^{r+g-2k}.
  \]

故
\[
0<
J+1-\frac\rho\tau
-5\cdot10^{r-3g}\psi^2
<2H\varepsilon+3.51\cdot10^{r+g-2k}.
\tag{10}

当前
\[
k\ge2g+1
\]
给
\[
2H\varepsilon<2\cdot10^{-5}.
\]
又由
\[
r\le2k-g-2
\]
得到
\[
3.51\cdot10^{r+g-2k}\le0.0351.
\]
所以右端严格小于
\[
0.03512<\frac1{25}=0.04.
\]
这证明 (2)。

---

## 5. one more strip closes immediately

若
\[
r=3g-1,
\]
则由 (1)：
\[
0<5\cdot10^{r-3g}\psi^2<\frac12.
\]
far condition 又给
\[
0<\frac\rho\tau<10^{2g-k}\le\frac1{10}.
\]
结合 (2)：
\[
0<J+1<rac12+rac1{10}+rac1{25}<1.
\]
但 §3 已证明 `J+1` 是正整数。矛盾。

因此原 low-`r` closure 可加强为
\[
\boxed{
 d=2,\ s=1,\ k\ge2g+1,
\quad 1\le r\le3g-1
\Longrightarrow\text{empty}.
}
\tag{11}

---

## 6. new high-`r` frontier

真正 radius-dominated 的首层是
\[
\boxed{r=3g.}
\]
此后 (2) 表明 `J+1` 读取
\[
5\cdot10^{r-3g}\psi^2
\]
的 leading decimal digits，误差宽度小于 `0.04`。

下一步不应再把 `r_3^2` 粗化，而应把 (2) 与
\[
\psi=10^{g-1}a_3/b_3
\]
的 exact decimal recovery 联立，形成平方 leading-digit / denominator congruence。