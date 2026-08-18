# A2 spontaneous angle 的 primitive `3 mod 4` carrier

> **依赖：** `spontaneous-prefix-eliminant.md`、`spontaneous-angle.md`、`primitive-reduction.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文把 `Omega_sp` 的原始 integer numerator 做精确 `2`-进本原化。结论是它与 `Theta_dec` 具有完全相同的 `2`-adic depth `2M+m+2`，并且两者除去该尺度后都严格为 `3 mod 4` 的正奇整数。因此 spontaneous angle 侧自身也携带一个全局 odd-inert parity excess。本文只建立 parity carrier 与后续 gcd dichotomy，不宣称这已经关闭 spontaneous common-prime channel，也不宣称 A2 全局关闭。

---

## 1. `Omega_sp` 的原始整数 numerator

沿用

\[
N=10^M,
\qquad A=a_2,
\qquad B=b_2,
\]

\[
Q=2N+B,
\qquad T=10^m.
\]

`spontaneous-prefix-eliminant.md` 定义

\[
\boxed{
\mathcal U_\Omega
=(45B^2-2AN)^2-A^2B(99B-4N).
}
\tag{1.1}
\]

并证明

\[
\boxed{
\Omega_{\rm sp}
=\frac{100B}{b_3N^4}
\left(T\mathcal U_\Omega+2A^2Qb_3\right).
}
\tag{1.2}
\]

因此定义

\[
\boxed{
\mathcal O_{\rm sp}
:=T\mathcal U_\Omega+2A^2Qb_3.
}
\tag{1.3}
\]

在真实 endpoint 中 `Omega_sp>0`，而 (1.2) 的 prefactor 为正，所以

\[
\boxed{\mathcal O_{\rm sp}>0.}
\tag{1.4}
\]

对 genuine odd spontaneous prime `p∤10Bb_3`，`p`-adic valuation 也无损：

\[
\boxed{
v_p(\Omega_{\rm sp})=v_p(\mathcal O_{\rm sp}).}
\tag{1.5}
\]

---

## 2. deep-even 的精确 `2`-进尺度

已有

\[
B=2^{M+m+1}c_ug,
\tag{2.1}
\]

\[
Q=2^{M+1}Q_0,
\qquad Q_0=c_Qq\ \text{odd},
\tag{2.2}
\]

\[
b_3=2^{M+m+1}5^dc_Qc_u.
\tag{2.3}
\]

把 odd parts 记为

\[
b_0:=c_ug,
\qquad
b_{30}:=5^dc_Qc_u.
\]

所以

\[
B=2^{M+m+1}b_0,
\qquad
b_3=2^{M+m+1}b_{30},
\]
且 `b_0,b_30,Q_0` 均为奇数。

又因 `(A,B)=1` 且 `B` 偶，故

\[
\boxed{A\text{ odd}.}
\tag{2.4}
\]

---

## 3. `U_Omega` 的 primitive quotient 恒为 `1 mod 4`

先处理第一平方项。因为

\[
N=2^M5^M,
\]
有

\[
\frac{45B^2-2AN}{2^{M+1}}
=45\,2^{M+2m+1}b_0^2-A5^M.
\tag{3.1}
\]

第一项被 `4` 整除，第二项为奇数，所以 (3.1) 是奇数；其平方满足

\[
\left(
\frac{45B^2-2AN}{2^{M+1}}
\right)^2
\equiv1\pmod8.
\tag{3.2}
\]

另一方面

\[
99B-4N
=2^{M+2}
\left(99\,2^{m-1}b_0-5^M\right),
\]
所以

\[
\boxed{
\frac{B(99B-4N)}{2^{2M+2}}
=2^{m+1}b_0
\left(99\,2^{m-1}b_0-5^M\right).
}
\tag{3.3}
\]

因为 `m>=1`，右边被 `4` 整除。于是

\[
\boxed{
\mathcal U_\Omega^
sharp
:=\frac{\mathcal U_\Omega}{2^{2M+2}}
\in\mathbf Z,
\qquad
\mathcal U_\Omega^\sharp\equiv1\pmod4.
}
\tag{3.4}
\]

特别地

\[
\boxed{v_2(\mathcal U_\Omega)=2M+2.}
\tag{3.5}
\]

---

## 4. `已严格完成`：`O_sp` 与 `Theta_dec` 有同一 `2`-adic depth

将 (3.4) 代入 (1.3)，除去

\[
2^{2M+m+2}.
\]

第一项给

\[
\frac{T\mathcal U_\Omega}{2^{2M+m+2}}
=5^m\mathcal U_\Omega^\sharp.
\tag{4.1}
\]

第二项利用 (2.2)–(2.3)：

\[
\frac{2A^2Qb_3}{2^{2M+m+2}}
=2A^2Q_0b_{30}.
\tag{4.2}
\]

因此定义

\[
\boxed{
\widehat{\mathcal O}_{\rm sp}
:=\frac{\mathcal O_{\rm sp}}{2^{2M+m+2}}
=5^m\mathcal U_\Omega^\sharp
+2A^2Q_0b_{30}.
}
\tag{4.3}
\]

第一项模 `4` 为 `1`，第二项因 `A,Q_0,b_30` 都奇而模 `4` 为 `2`。故

\[
\boxed{
\widehat{\mathcal O}_{\rm sp}
\equiv3\pmod4.
}
\tag{4.4}
\]

所以它是奇数，并且

\[
\boxed{
v_2(\mathcal O_{\rm sp})=2M+m+2.}
\tag{4.5}
\]

另一方面已有

\[
\Theta_{\rm dec}
=2^{2M+m+2}\widehat{\mathcal T}_2,
\qquad
\widehat{\mathcal T}_2\equiv3\pmod4.
\tag{4.6}
\]

综上：

\[
\boxed{
\begin{array}{c|c|c}
&v_2&\text{primitive mod }4\\ \hline
\mathcal O_{\rm sp}&2M+m+2&3\\
\Theta_{\rm dec}&2M+m+2&3
\end{array}}
\tag{4.7}
\]

这两个此前来自完全不同推导的对象，在 `2`-adic orientation 上精确对齐。

---

## 5. 两侧都存在 odd inert parity excess

由 (1.4)、(4.4)：

\[
\widehat{\mathcal O}_{\rm sp}>0,
\qquad
\widehat{\mathcal O}_{\rm sp}\equiv3\pmod4.
\]
所以

\[
\boxed{
\sum_{p\equiv3\ (4)}
v_p(\widehat{\mathcal O}_{\rm sp})
\equiv1\pmod2.
}
\tag{5.1}
\]

旧 additive cofactor 同样满足

\[
\boxed{
\sum_{p\equiv3\ (4)}
v_p(\widehat{\mathcal T}_2)
\equiv1\pmod2.
}
\tag{5.2}
\]

因此 spontaneous angle side 与 additive side 各自都强迫一份 odd inert excess，而真正 common spontaneous carrier 属于

\[
\gcd(\widehat{\mathcal O}_{\rm sp},\widehat{\mathcal T}_2).
\]

---

## 6. `已严格完成`：common-gcd 的 mod-4 parity dichotomy

令

\[
G_{\rm sp}:=\gcd(
\widehat{\mathcal O}_{\rm sp},
\widehat{\mathcal T}_2
),
\]
并写

\[
\widehat{\mathcal O}_{\rm sp}=G_{\rm sp}U,
\qquad
\widehat{\mathcal T}_2=G_{\rm sp}V,
\qquad
\gcd(U,V)=1.
\]

三个量都为正奇数。因为两侧都 `3 mod4`：

- 若 `G_sp≡3 mod4`，则 `U≡V≡1 mod4`；common gcd 本身携带 odd inert parity；
- 若 `G_sp≡1 mod4`，则 `U≡V≡3 mod4`；两侧各自仍需一份**互不相同**的 residual odd inert excess。

即

\[
\boxed{
\begin{array}{c|c}
G_{\rm sp}\bmod4&\text{forced parity allocation}\\ \hline
3&\text{common spontaneous gcd carries odd inert parity}\\
1&\text{both coprime quotients carry separate odd inert parity.}
\end{array}}
\tag{6.1}
\]

这不是 closure，但把“是否存在共同 spontaneous excess”升级成一个全局 parity dichotomy；后续 prime-source 分类可分别攻击 `G_sp≡3` 与 `G_sp≡1` 两支。

---

## 7. 更新后的开放方向

本文件新增的不是又一个 Legendre symbol，而是一份真正的全局 primitive integer：

\[
\boxed{
\widehat{\mathcal O}_{\rm sp}>0,
\qquad
\widehat{\mathcal O}_{\rm sp}\equiv3\pmod4.
}
\]

下一步最值得做的是把已知 source/q/f overlap resultants 用在 (6.1) 的 residual quotients 上：如果能证明 `U` 或 `V` 的 non-`3` inert odd factors只能来自已经排除/固定的 denominator-source pools，就会强迫 `G_sp≡3 mod4`，从而得到真正的 common spontaneous inert carrier，而不再只是“某一侧必有一个 inert prime”。
