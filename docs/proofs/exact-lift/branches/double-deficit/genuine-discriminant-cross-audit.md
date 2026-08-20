# DD genuine-Gaussian discriminant cross determinant 的 Archimedean audit

> **依赖：** [`genuine-discriminant-carrier.md`](genuine-discriminant-carrier.md)、[`good-prefix-polarization.md`](good-prefix-polarization.md) 与 [`frontier.md`](frontier.md) 的 terminal constants。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。上一文件给出
> \[
> C_{\rm same}^2\mid\Omega y_2-Wy_3,
> \qquad
> C_{\rm opp}^2\mid\Omega y_2+Wy_3.
> \]
> 本文计算两项的真实 Archimedean 比例。结果是
> \[
> \frac{\Omega y_2}{Wy_3}=10^{-9S+o(S)}.
> \]
> 因而 `same` determinant 对 sufficiently large frontier 永不为零，且 `same/opp` 两个 determinant 都由 `Wy3` 主导，没有任何正线性 Archimedean cancellation。于是“新 discriminant carrier + 原 sphere carrier直接取 raw cross determinant”不能靠高度小性关闭 genuine branch。
>
> 这不否定新 carrier 的 p-adic 信息；它说明下一步必须先从 `Theta_same/Theta_opp` 中抽出 genuinely small source/digit cofactor，不能直接使用 raw determinant 高度。

---

## 1. terminal digit polarization

沿用

\[
S=m_1+m_2.
\]

prefix polarization 已给

\[
\boxed{
(n_1,m_1,n_2,m_2)
=(S,0,0,S)+o(S).
}
\tag{1.1}
\]

因此按 base-10 logarithmic height：

\[
\boxed{
\log a_1=S+o(S),
\qquad
\log b_2=S+o(S),
}
\tag{1.2}
\]

\[
\boxed{
\log a_2=o(S),
\qquad
\log b_1=o(S).
}
\tag{1.3}
\]

这里及下文 `log` 均按 `log_10` 理解；改变固定底数只会整体缩放常数。

由

\[
Q=b_1 10^{m_2}+b_2,
\qquad
G=b_1b_2,
\]

两项均为正，得到

\[
\boxed{
\log Q=S+o(S),
\qquad
\log G=S+o(S).
}
\tag{1.4}

---

## 2. `kappa` 的高度恰为 `2S`

统一 tail weight 满足固定窗口

\[
QG<\kappa\le10QG.
\]

结合 `(1.4)`：

\[
\boxed{
\log\kappa=2S+o(S).
}
\tag{2.1}

而

\[
\frac G\kappa<\frac1Q=10^{-S+o(S)},
\]

所以

\[
\boxed{
\log(\kappa+G)=2S+o(S),
\qquad
\frac{\kappa+G}{\kappa}=1+10^{-S+o(S)}.
}
\tag{2.2}

---

## 3. DD coefficient `mathscr C` 的高度为 `4.5S`

frontier constants 为

\[
\frac{n_3}{S}	o6.308883577618\ldots,
\qquad
\frac{m_3}{S}	o2.808883577618\ldots.
\]

因此

\[
\boxed{d_3=n_3-m_3=3.5S+o(S).}
\tag{3.1}

又由

\[
s_2=n_2-m_2=-S+o(S),
\]

得到

\[
\boxed{k_{12}=s_2+d_3=2.5S+o(S).}
\tag{3.2}

DD unified coefficient 为

\[
\mathscr C
=10^{m_2+k_{12}}a_1+10^{d_3}a_2.
\]

第一项高度：

\[
(m_2+k_{12})+\log a_1
=(S+2.5S+S)+o(S)
=4.5S+o(S).
\]

第二项只有

\[
d_3+\log a_2
=3.5S+o(S).
\]

两项为正，因此不存在 cancellation，且

\[
\boxed{
\log\mathscr C=4.5S+o(S).}
\tag{3.3}

---

## 4. `N_12` 与 discriminant correction 的高度

写

\[
x=a_1b_2,
\qquad
y=a_2b_1.
\]

由 §1：

\[
\log x=2S+o(S),
\qquad
\log y=o(S).
\]

故

\[
\mathcal N_{12}=x^2+y^2
\]

满足

\[
\boxed{
\log\mathcal N_{12}=4S+o(S).
}
\tag{4.1}

定义 discriminant 主平方尺度

\[
M_{\rm disc}:=\kappa G\mathscr C.
\]

由 `(1.4)`、`(2.1)`、`(3.3)`：

\[
\boxed{
\log M_{\rm disc}=7.5S+o(S),
\qquad
\log M_{\rm disc}^2=15S+o(S).
}
\tag{4.2}

而 correction

\[
R_{\rm disc}
:=Q^2\mathcal N_{12}\kappa(\kappa+2G)
\]

满足

\[
\boxed{
\log R_{\rm disc}
=(2+4+2+2)S+o(S)
=10S+o(S).
}
\tag{4.3}

所以

\[
\boxed{
\frac{R_{\rm disc}}{M_{\rm disc}^2}
=10^{-5S+o(S)}.
}
\tag{4.4}

由 exact discriminant identity

\[
W^2=M_{\rm disc}^2-R_{\rm disc},
\]

得到 sufficiently large frontier 上 `W>0`，并且

\[
\boxed{
\frac W{M_{\rm disc}}
=1+O(10^{-5S+o(S)}),
\qquad
\log W=7.5S+o(S).
}
\tag{W-height}

这里第一式的 `O` 只表达实数相对误差的指数尺度；证明来自

\[
\sqrt{1-t}=1+O(t)
\qquad(t\to0^+).
\]

---

## 5. discriminant carrier 的第二坐标只有 `3S`

上一文件定义

\[
\Omega=Q(a_2b_1)(\kappa+G).
\]

由 `(1.3)`、`(1.4)`、`(2.2)`：

\[
\boxed{
\log\Omega=3S+o(S).
}
\tag{5.1}

于是

\[
\boxed{
\log\frac W\Omega=4.5S+o(S).
}
\tag{5.2}

也就是说，在实平面上 `W+iOmega` 极度接近 real axis；其 slope 只有

\[
\frac\Omega W=10^{-4.5S+o(S)}.
\]

---

## 6. sphere carrier 的 slope 恰好朝相反尺度

因为

\[
y_i=a_i\frac q{b_i},
\]

公共 `q` 消去：

\[
\frac{y_2}{y_3}
=\frac{a_2/b_2}{a_3/b_3}.
\tag{6.1}

由 digit lengths：

\[
\log\frac{a_2}{b_2}
=n_2-m_2+O(1)
=-S+o(S),
\]

而

\[
\log\frac{a_3}{b_3}
=n_3-m_3+O(1)
=d_3+O(1)
=3.5S+o(S).
\]

所以

\[
\boxed{
\log\frac{y_2}{y_3}
=-4.5S+o(S).
}
\tag{Sphere-slope}

即原 sphere carrier `y2+i y3` 极度接近 imaginary axis：

\[
\frac{y_2}{y_3}=10^{-4.5S+o(S)}.
\]

---

## 7. cross determinant 中小项比大项低 `9S`

结合 `(5.2)` 与 `(Sphere-slope)`：

\[
\begin{aligned}
\log\frac{\Omega y_2}{W y_3}
&=\log\frac\Omega W+\log\frac{y_2}{y_3}\\
&=-4.5S-4.5S+o(S).
\end{aligned}
\]

因此

\[
\boxed{
\rho_S
:=\frac{\Omega y_2}{W y_3}
=10^{-9S+o(S)}.
}
\tag{Cross-ratio}

特别地 sufficiently large frontier 上

\[
0<\rho_S<1.
\tag{7.1}

于是 same determinant

\[
\Theta_{\rm same}
=\Omega y_2-Wy_3
=-Wy_3(1-\rho_S)
\]

严格非零，并满足

\[
\boxed{
|\Theta_{\rm same}|
=Wy_3\bigl(1-10^{-9S+o(S)}\bigr).
}
\tag{Same-size}

所以前一文件留下的 exact slope escape

\[
\Theta_{\rm same}=0
\]

在 sufficiently large frontier 上完全排除：

\[
\boxed{
\Theta_{\rm same}\ne0.
}
\tag{Same-zero-closed}

同理

\[
\Theta_{\rm opp}
=\Omega y_2+Wy_3
=Wy_3(1+\rho_S),
\]

故

\[
\boxed{
\Theta_{\rm opp}
=Wy_3\bigl(1+10^{-9S+o(S)}\bigr)>0.
}
\tag{Opp-size}

---

## 8. raw cross determinant 没有 Archimedean saving

由 §7：

\[
\boxed{
\log|\Theta_{\rm same}|
=
\log\Theta_{\rm opp}
=
\log W+\log y_3+o(S).
}
\tag{8.1}

而每个 genuine main prime上，由上一文件的 primitive unit facts：

\[
p\nmid W,
\qquad
p\nmid y_3.
\]

第二条因为

\[
y_3=a_3(q/b_3),
\]

且 `p` 在 `b3` 已达到 lcm max depth、`p∤a3`。

因此 `C_G` 的 square-depth divisibility

\[
C_{\rm same}^2\mid\Theta_{\rm same},
\qquad
C_{\rm opp}^2\mid\Theta_{\rm opp}
\]

确实来自两个 p-adic units 的 deep cancellation；但在 Archimedean place，两个 terms 的大小差了 `9S`，完全没有相应 cancellation。

所以：

\[
\boxed{
\text{直接用 raw }\Theta_{\rm same/opp}\text{ 的绝对高度，}
\text{不会产生 genuine core 的 strict small-determinant bound。}
}
\tag{Raw-cross-nogo}

**状态：`失效/降级`，针对 raw determinant height 路线。**

---

## 9. 新 carrier 仍然留下什么

虽然 raw cross determinant 不短，上一文件的新 p-adic结构仍然真实：

\[
C_{\rm same}^2\mid\Theta_{\rm same}\ne0,
\qquad
C_{\rm opp}^2\mid\Theta_{\rm opp}>0.
\]

本文进一步说明这两条 divisibility 都发生在 **Archimedean-transverse** 情形：

\[
\frac{\Omega/W}{y_3/y_2}
=10^{-9S+o(S)}.
\]

因此若要利用它们，下一步只能寻找 `Theta_same/opp` 的 exact factorization / normalized quotient，证明主导的 `Wy3` 部分由已知 source factors抽掉后只剩短 cofactor。

若完整展开再次退回 primitive carrier determinants、projective source quotient或原 discriminant identity，则这个 discriminant carrier也只能作为 orientation reader保留，不能关闭 genuine branch。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`log Q=log G=S+o(S)`、`log kappa=2S+o(S)`、`log mathscr C=4.5S+o(S)`、`log N12=4S+o(S)`、`log W=7.5S+o(S)`、`log Omega=3S+o(S)`、sphere/discriminant slope asymptotics、`Cross-ratio=10^{-9S+o(S)}`、`Same-zero-closed`。
- **`失效/降级`**：用 raw `Theta_same/Theta_opp` Archimedean height直接关闭 genuine core。
- **`待证`**：两个 cross determinant 的 exact normalized factorization；是否能剥出短 cofactor；genuine-Gaussian closure；DD 全局空性。
