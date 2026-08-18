# A2 residual parity doubling after removing height/content

> **依赖：** `spontaneous-height-parity-ledger.md`、`spontaneous-angle-parity.md`、`spontaneous-omega-content-common.md`、`primitive-reduction.md`。
>
> **严格状态：**本文把 additive carrier 与其 pure-decimal height companion `J_H` 的 primitive relation完全除去 2-adic scale，并同时记录 angle actual/conjugate sheets 的 primitive difference。结论是：去掉共同 height part 后，additive residual 与 `J_H` residual若再次共享 odd prime，该 prime只能来自 central factor `2K-9` 或 concatenated content `omega`；angle actual/conjugate residual的共同 odd prime则只能来自 numerator/denominator prefix content。于是 generic alpha-free、noncentral、denominator-free external sector中的 odd-inert parity不能在 companion sheets之间复用同一 prime。本文是 global parity allocation lemma，不证明 residual primes不存在，也不宣称 A2 closure。

---

## 1. 记号

固定 reflection endpoint：

\[
N=10^M,
\qquad T=10^m,
\qquad A=a_2,
\qquad B=b_2,
\]

\[
Q=B+2N,
\qquad K=9N+10A.
\]

由 deep-even denominator normal form：

\[
\boxed{B=2^{M+m+1}c_ug.}
\tag{1.1}
\]

记

\[
B_0:=c_ug,
\]
所以 `B_0` 为奇数。

已有 primitive height/reduced numerator：

\[
\boxed{
\alpha=TK+a_3=\omega W_q,
\qquad H_0=c_uW_q.
}
\tag{1.2}
\]

并且

\[
\gcd(W_q,10c_ug c_Q)=1.
\tag{1.3}
\]

---

# additive pair

## 2. `T_hat` 与 `J_H` 的 exact primitive identity

`spontaneous-height-parity-ledger.md` 定义

\[
\mathcal J_H
=B^2(5K^2-36K+55)-Q^2N_0
\]
并证明

\[
\boxed{
\Theta_{\rm dec}
=T\mathcal J_H
-2B^2(2K-9)\omega W_q.
}
\tag{2.1}
\]

同时

\[
\Theta_{\rm dec}
=2^{2M+m+2}\widehat{\mathcal T}_2,
\]

\[
\mathcal J_H
=2^{2M+2}\widehat{\mathcal J}_H,
\]

且

\[
\boxed{
\widehat{\mathcal T}_2>0,
\quad
\widehat{\mathcal J}_H>0,
\quad
\widehat{\mathcal T}_2\equiv
\widehat{\mathcal J}_H\equiv3\pmod4.
}
\tag{2.2}
\]

利用

\[
T=2^m5^m,
\qquad
B=2^{M+m+1}B_0,
\]
把 (2.1) 除以 `2^{2M+m+2}`，得到本文第一条核心恒等式：

\[
\boxed{
\widehat{\mathcal T}_2
=5^m\widehat{\mathcal J}_H
-2^{m+1}B_0^2(2K-9)\omega W_q.
}
\tag{2.3}
\]

这里没有 rational normalization；所有量都是整数。

---

## 3. 共同 height part完全相同

因为 `W_q` 为 odd 且 `5\nmid W_q`，(2.3) 模 `W_q` 给

\[
\widehat{\mathcal T}_2
\equiv5^m\widehat{\mathcal J}_H
\pmod{W_q}.
\]

故有全局 gcd identity

\[
\boxed{
D_H
:=\gcd(\widehat{\mathcal T}_2,W_q)
=
\gcd(\widehat{\mathcal J}_H,W_q).
}
\tag{3.1}
\]

定义 height-free quotients

\[
\boxed{
T^\circ:=\frac{\widehat{\mathcal T}_2}{D_H},
\qquad
J^\circ:=\frac{\widehat{\mathcal J}_H}{D_H},
\qquad
W^\circ:=\frac{W_q}{D_H}.
}
\tag{3.2}
\]

按 gcd 的定义：

\[
\boxed{
\gcd(T^\circ,W^\circ)
=
\gcd(J^\circ,W^\circ)=1.
}
\tag{3.3}
\]

将 (2.3) 再除以 `D_H`：

\[
\boxed{
T^\circ-5^mJ^\circ
=-2^{m+1}B_0^2(2K-9)\omega W^\circ.
}
\tag{3.4}
\]

---

## 4. `已严格完成`：height-free additive companions只能在 central/content 上再次共享 prime

令奇素数 `p` 同时满足

\[
p\mid T^\circ,
\qquad
p\mid J^\circ.
\]

由 (3.4)：

\[
p\mid B_0^2(2K-9)\omega W^\circ.
\]

但 (3.3) 给 `p\nmid W^circ`；又

\[
\gcd(\widehat{\mathcal T}_2,10c_ug)=1
\]
而 `T^circ|widehat(T)_2`，所以

\[
p\nmid B_0=c_ug.
\]

因此：

\[
\boxed{
 p\mid T^\circ,\ p\mid J^\circ
\Longrightarrow
p\mid(2K-9)\omega.
}
\tag{4.1}
\]

换句话说，在

\[
p\nmid(2K-9)\omega
\]
的 alpha-free、noncentral sector，两个 height-free additive companions不能复用同一个 odd prime。

定义

\[
E_H:=\gcd(T^\circ,J^\circ).
\]
则逐 prime 由 (4.1) 得

\[
\boxed{
\operatorname{Supp}_{odd}(E_H)
\subseteq
\operatorname{Supp}((2K-9)\omega).
}
\tag{4.2}
\]

这不是说右端 prime一定进入 `E_H`；只是所有再次 overlap 都被压回 central/content support。

---

## 5. additive residual parity复制

由 (2.2)，`D_H` 为 odd，所以

\[
T^\circ\equiv J^\circ
\equiv3D_H^{-1}\pmod4.
\tag{5.1}
\]

因此

\[
\boxed{
T^\circ\equiv J^\circ\pmod4.
}
\tag{5.2}
\]

具体地：

\[
\boxed{
D_H\equiv1\pmod4
\Longrightarrow
T^\circ\equiv J^\circ\equiv3\pmod4,
}
\tag{5.3}
\]

\[
\boxed{
D_H\equiv3\pmod4
\Longrightarrow
T^\circ\equiv J^\circ\equiv1\pmod4.
}
\tag{5.4}
\]

所以当 height common part本身为 `1 mod 4` 时，additive actual residual和 `J_H` residual **各自**都必须携带 odd total inert parity。由 §4，generic alpha-free noncentral部分不能由同一 prime同时承担这两份 parity。

---

# angle pair

## 6. actual/conjugate angle primitive difference

沿用 height ledger 的

\[
\mathcal O_\pm
=T\mathcal U_\Omega
\pm2A^2Qb_3,
\]

\[
\widehat{\mathcal O}_\pm
:=\frac{\mathcal O_\pm}{2^{2M+m+2}}.
\]

已有

\[
\boxed{
\widehat{\mathcal O}_+>0,
\quad
\widehat{\mathcal O}_->0,
\quad
\widehat{\mathcal O}_+\equiv
\widehat{\mathcal O}_-\equiv3\pmod4.
}
\tag{6.1}
\]

写

\[
Q=2^{M+1}Q_0,
\]
以及

\[
b_3=2^{M+m+1}5^dc_Qc_u.
\]

由

\[
\mathcal O_+-\mathcal O_-=4A^2Qb_3
\]
精确除去 primitive 2-power：

\[
\boxed{
\widehat{\mathcal O}_+
-
\widehat{\mathcal O}_-
=4A^2Q_0\,5^dc_Qc_u.
}
\tag{6.2}
\]

定义

\[
D_O:=\gcd(
\widehat{\mathcal O}_+,
\widehat{\mathcal O}_-
).
\tag{6.3}
\]

则任何 odd prime `p|D_O` 必满足

\[
\boxed{
p\mid A Q_0 5 c_Qc_u.}
\tag{6.4}
\]

而 angle primitive content lemma已有

\[
\gcd(\widehat{\mathcal O}_+,c_ug)=1.
\]

故对 non-`5` genuine inert common prime可进一步缩为

\[
\boxed{
 p\mid D_O,\ p\equiv3\pmod4,\ p\ne5
\Longrightarrow
p\mid A Q_0c_Q.
}
\tag{6.5}
\]

所以真正 prefix-content-free / denominator-free external prime不可能同时命中 actual 与 conjugate angle sheets。

---

## 7. angle residual parity也成对复制

令

\[
O_+^\circ
:=\frac{\widehat{\mathcal O}_+}{D_O},
\qquad
O_-^\circ
:=\frac{\widehat{\mathcal O}_-}{D_O}.
\]

则

\[
\gcd(O_+^\circ,O_-^\circ)=1
\]
且由 (6.1)：

\[
\boxed{
O_+^\circ\equiv O_-^\circ
\equiv3D_O^{-1}\pmod4.
}
\tag{7.1}
\]

所以：

\[
\boxed{
D_O\equiv1\pmod4
\Longrightarrow
O_+^\circ\equiv O_-^\circ\equiv3\pmod4.
}
\tag{7.2}
\]

此时两份 odd inert parity必须落在两个互素 residual integers中；由 (6.5)，generic external sector中不能用同一个 inert prime实现。

若

\[
D_O\equiv3\pmod4,
\]
则两个 residual均为 `1 mod 4`，odd parity已由共同 prefix-content部分 `D_O` 承担。

---

## 8. `global parity ledger` 的严格含义

现在 actual angle/additive 两个 `3 mod 4` carriers都有一个 companion：

\[
\widehat{\mathcal O}_+
\leftrightarrow
\widehat{\mathcal O}_-,
\]

\[
\widehat{\mathcal T}_2
\leftrightarrow
\widehat{\mathcal J}_H.
\]

并且：

1. angle pair 的 common support只能来自 `A Q_0 c_Q`（加固定 `5` / 已分离 content）；
2. additive pair在除去共同 height part以后，再次 common 的 support只能来自 `(2K-9)omega`；
3. 两个 pair 各自拥有相同的 mod-4 residual orientation；
4. 因而 generic alpha-free、noncentral、prefix-content-free external sector中的 odd inert parity具有 **doubling** 性质：若 actual residual需要一份 odd parity，它的 companion residual也需要一份，而两份不能由同一 generic prime复用。

这比单独知道

\[
\widehat{\mathcal O}_{sp}\equiv
\widehat{\mathcal T}_2\equiv3\pmod4
\]
更强，因为它明确限制 residual parity如何分配。

但这仍不是 closure：不同 generic external primes完全可能分别承担这些 parity。要最终关闭 `G_sp\equiv1 mod4` 分支，还需要证明这些分离 residual primes必须通过同一个 external prime-source / decimal orbit重新会合，或由 natural representative高度排除。

---

## 9. 后续接口

下一步最值得研究的是四个 primitive carriers之间的 **cross-pair** overlap：

\[
\gcd(O_+^\circ,J^\circ),
\qquad
\gcd(T^\circ,O_-^\circ).
\]

若能证明 cross-pair overlap也只能进入已知 `omega/source/denominator/central` fixed sheets，那么在 `G_sp\equiv1 mod4` 下就会被迫出现至少四份互不复用的 generic external odd parity。再结合最新 `spontaneous-pure-root-gap.md` 的全部 real roots `>1`，这会把剩余问题进一步压成纯 decimal multiplicative-orbit / height budget，而不再含局部几何自由度。
