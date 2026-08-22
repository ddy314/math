# DD frontier: secondary Gaussian orientation 的全局 quadratic reciprocity constraint

> 日期：2026-08-22
>
> 作用域：假想 corrected
> \[
> n/S\to6.308883577618\ldots
> \]
> 的 terminal one-channel frontier。
>
> **状态：已严格完成（frontier 条件蕴含；非 closure）。**
>
> 本文不把 Gaussian congruence取 norm，而是只降到每个 main split prime 的一次 Legendre character。这样虽然丢掉 chosen `pi/bar pi` orientation，却保留了 `q_c` 本身而不是 `q_c^2`。结果是一个覆盖 rational / genuine 两支的统一 prime-support condition。

## 1. secondary orientation

terminal secondary Gaussian line为

\[
\boxed{
A_*2^{m-2}q_c-iB_*5^{2T-m}
=\Pi\Delta_1,
}
\tag{1.1}
\]

其中

\[
A_*=g_0a_2\theta s,
\qquad
B_*=\widetilde rR_0,
\qquad
N(\Pi)=C_L.
\]

固定 main rational prime

\[
p^h\Vert C_L,
\qquad p\equiv1\pmod4,
\]

并取 chosen Gaussian prime

\[
\pi^h\Vert\Pi,
\qquad p=\pi\bar\pi.
\]

删去 coefficient exceptional core后

\[
p\nmid10A_*B_*q_c.
\tag{1.2}
\]

在

\[
\mathbf Z[i]/(\pi)\simeq\mathbf F_p
\]

中令 `i` 的像为 `j_p`。则

\[
\boxed{j_p^2=-1\pmod p.}
\tag{1.3}
\]

由 `(1.1)`：

\[
\boxed{
A_*2^{m-2}q_c
\equiv
j_pB_*5^{2T-m}
\pmod p.
}
\tag{1.4}

## 2. `sqrt(-1)` 的 Legendre symbol

因为 `p == 1 mod 4`，

\[
\left(\frac{j_p}{p}\right)
=j_p^{(p-1)/2}
=(j_p^2)^{(p-1)/4}
=(-1)^{(p-1)/4}.
\]

而对 `p == 1 mod 4`，二次补充律给

\[
\left(\frac2p\right)
=(-1)^{(p^2-1)/8}
=(-1)^{(p-1)/4}.
\]

故

\[
\boxed{
\left(\frac{j_p}{p}\right)
=\left(\frac2p\right).
}
\tag{2.1}

注意把 `j_p` 换成 `-j_p` 不改变此式，因为

\[
\left(\frac{-1}{p}\right)=1.
\]

所以本节结论不依赖 chosen Gaussian orientation 的正负号；rational / genuine 两支统一适用。

## 3. source character formula

对 `(1.4)` 取 Legendre symbol。逆元与原数有相同 Legendre symbol，因此

\[
\begin{aligned}
\left(\frac{q_c}{p}\right)
={}&
\left(\frac{j_p}{p}\right)
\left(\frac{A_*B_*}{p}\right)
\left(\frac2p\right)^{m-2}
\left(\frac5p\right)^{2T-m}.
\end{aligned}
\tag{3.1}

使用 `(2.1)`，且

\[
2T-m\equiv m\pmod2,
\]

得到

\[
\begin{aligned}
\left(\frac{q_c}{p}\right)
&=
\left(\frac{A_*B_*}{p}\right)
\left(\frac2p\right)^{m-1}
\left(\frac5p\right)^m\\
&=
\boxed{
\left(\frac{5A_*B_*10^{m-1}}p\right).
}
\end{aligned}
\tag{Source-character}

等价地，定义

\[
\boxed{
D_{\rm sec}:=5A_*B_*10^{m-1}q_c,
}
\tag{3.2}

则每个 main `C_L` prime满足

\[
\boxed{
\left(\frac{D_{\rm sec}}p\right)=1.
}
\tag{Secondary-splitting}

所以 main moving core同时具有两层 splitting：

1. `p == 1 mod 4`，即在 `Q(i)` 中 split；
2. `D_sec` 是模 `p` 的平方，即 `p` 也 split 于由 `sqf(D_sec)` 定义的 moving quadratic field。

## 4. global Jacobi form

令 `C_L^sharp` 为从 `C_L` 删除所有与

\[
10A_*B_*q_c
\]

有公共 prime 的 exceptional prime-power 后所得 main core。其高度仍为

\[
\log C_L^\sharp=S-o(S)
\]

只要上述 coefficient overlap本身为 `10^{o(S)}`；在 terminal coefficient normalization 下正是如此。

逐 prime-power 相乘 `(Source-character)`：

\[
\boxed{
\left(\frac{q_c}{C_L^\sharp}\right)
=
\left(\frac{5A_*B_*10^{m-1}}{C_L^\sharp}\right).
}
\tag{Jacobi-global}

由于 `C_L^sharp` 的每个 prime都 `1 mod 4`，有

\[
C_L^\sharp\equiv1\pmod4.
\]

因此对任意与其互素的 odd source core `q_c^o`，quadratic reciprocity没有 sign defect：

\[
\boxed{
\left(\frac{q_c^\circ}{C_L^\sharp}\right)
=
\left(\frac{C_L^\sharp}{q_c^\circ}\right).
}
\tag{Reciprocity-clean}

这把 secondary Gaussian orientation 的 local source condition转换成了一个 global reciprocity compatibility。

## 5. 与 denominator prefix 的接口

one-channel 中 main `C_L` 进入第二 denominator block。写

\[
b_2=C_L^\sharp\,\beta,
\tag{5.1}
\]

其中删除 main core后的 `beta` 只有 `10^{o(S)}` height。

denominator concat

\[
Q=b_1 10^{m_2}+b_2
\]

同时满足

\[
Q=Uq,
\qquad q=J\theta q_c.
\]

对 clean source core `q_c^o` 取模；删除 `(beta,q_c^o)` 与 `J theta` 的 slow overlap后：

\[
\boxed{
C_L^\sharp\beta
\equiv-b_1 10^{m_2}
\pmod{q_c^\circ}.
}
\tag{Prefix-source-residue}

因此

\[
\boxed{
\left(\frac{C_L^\sharp}{q_c^\circ}\right)
=
\left(\frac{-b_1\beta\,10^{m_2}}{q_c^\circ}\right)
}
\tag{Prefix-character}

在相应 clean Jacobi sense 下成立（inverse `beta^{-1}` 可替换为 `beta`，因为二次字符只取 `+/-1`）。

将 `(Reciprocity-clean)`、`(Jacobi-global)` 与 `(Prefix-character)` 合并，就得到一个完全跨越两套 parent family 的 global character compatibility：

\[
\boxed{
\left(\frac{-b_1\beta\,10^{m_2}}{q_c^\circ}\right)
=
\left(\frac{5A_*B_*10^{m-1}}{C_L^\sharp}\right)
}
\tag{Cross-reciprocity}

删去的 factors全属于 terminal slow/exceptional data；两边的 main moving moduli分别是 `q_c` 与 `C_L`。

## 6. 为什么这还不是 strict gap

`Secondary-splitting` 是一条真实的新 global support restriction，但 ordinary quadratic character只有有限值 `+/-1`。即使所有 main `C_L` primes都被要求 split 于一个额外 moving quadratic field，这类 prime仍有正密度；单靠这一条件无法给出 `exp(-epsilon*S)` 级的 height saving。

同样，`Cross-reciprocity` 是一个 exact sign compatibility，而 terminal slow coefficients的 Jacobi symbols仍可能吸收一个有限 sign condition。

所以本文不宣称 frontier closure。

它的价值是把下一步 quartic 任务精确定位：ordinary norm把 `q_c` 变成 `q_c^2` 后完全丢失 source character；本文恢复了一次 quadratic source character。若要继续获得 orientation-sensitive information，必须保留 chosen `pi`，进入 Gaussian **quartic residue symbol** 或等价的 global orientation invariant，而不能再只对 `(1.1)` 取 rational norm。

## 7. 下一目标

下一步可定义 primary associate `pi_p` 并研究

\[
\left(\frac{q_c}{\pi_p}\right)_4
\]

由 `(1.4)` 给出的显式值，然后对

\[
\Pi=\prod\pi_p^h
\]

使用 quartic reciprocity。

成功标准不是再得到一个普通 `+/-1` density condition，而是把 product orientation与 `(Prefix-source-residue)` 或 terminal global tail sign相连，形成无法由 `10^{o(S)}` coefficient choices吸收的 compatibility。
