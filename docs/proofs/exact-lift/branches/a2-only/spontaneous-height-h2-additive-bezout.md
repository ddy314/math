# A2 moving height `H_2` / additive 的 exact Bézout depth bridge

> **依赖：** `spontaneous-height-parity-ledger.md`、`spontaneous-height-resultant-parity.md`、`spontaneous-height-h1-additive-bezout.md`、`spontaneous-height-angle-additive-norm-bridge.md`。
>
> **严格状态：**`H_1` orientation 已有 exact Bézout depth bridge；本文补齐第二张 pure-prefix sphere orientation `H_2`。首先把 `H_2` 精确分成一个整数平方与 `Q^2N_0` 项，随后与 additive-height carrier `J_H` 消去 `N_0`，得到新的 positive primitive `3 mod4` carrier `R_H2`。对 genuine external height prime，若 `H_2` 与 `B_W` 深度不等，`R_H2` 精确读取较浅者；equal-depth extra lift 则强迫 normalized `B_W/H_2` ratio 为 `-square`，即 non-square。它与 `H_1` bridge 的 square ratio形成严格互补。本文不宣称 equal-depth shell 已全部关闭。

---

## 1. notation

固定 reflection endpoint：

\[
N:=N_{\rm dec}=10^M,
\qquad A:=a_2,
\qquad B:=b_2,
\]

\[
Q:=B+2N,
\qquad K:=9N+10A,
\]

\[
N_0:=\left(\frac{9B}{2}\right)^2+A^2,
\]

\[
F_W(K):=(K-5)(5K-11)=5K^2-36K+55.
\tag{1.1}
\]

additive-height pure decimal carrier为

\[
\boxed{
\mathcal J_H:=B^2F_W(K)-Q^2N_0.}
\tag{1.2}

第二张 sphere orientation integer 是

\[
\boxed{
\begin{aligned}
\mathcal H_2={}&
404A^4B^2+16A^4BN+16A^4N^2
+1440A^3B^2N\\
&-16119A^2B^4+324A^2B^3N
+1620A^2B^2N^2\\
&-29160AB^4N+164025B^6.
\end{aligned}}
\tag{1.3}

---

## 2. `H_2` 有一个此前未显式记录的 exact square decomposition

定义

\[
\boxed{
\mathcal L_2:=20A^2+36AN-405B^2.}
\tag{2.1}

直接展开得到

\[
\boxed{
\mathcal H_2
=B^2\mathcal L_2^2+4A^2Q^2N_0.}
\tag{2.2}

这是纯整数恒等式。验证只需展开右端：

\[
B^2(20A^2+36AN-405B^2)^2
+4A^2(B+2N)^2
\left(\frac{81B^2}{4}+A^2\right),
\]
逐项即恢复 (1.3)。

这个形式还给 genuine external `H_2` prime 一个简单 unit audit。若

\[
p\mid\mathcal H_2,
\qquad p\nmid2AQN_0,
\]
而又 `p|L_2`，则 (2.2) 会迫使

\[
p\mid4A^2Q^2N_0,
\]
矛盾。因此

\[
\boxed{p\nmid\mathcal L_2}
\tag{2.3}

在 genuine `H_2` locus 自动成立。

---

## 3. exact Bézout identity

由 (1.2)：

\[
4A^2\mathcal J_H
=4A^2B^2F_W-4A^2Q^2N_0.
\]
与 (2.2) 相加，`Q^2N_0` 精确消失：

\[
\boxed{
4A^2\mathcal J_H+\mathcal H_2
=B^2\mathscr R_{H2},}
\tag{3.1}

其中定义

\[
\boxed{
\mathscr R_{H2}
:=\mathcal L_2^2+4A^2F_W(K).}
\tag{3.2}

这就是第二张 orientation 的 exact Bézout carrier。

---

## 4. `R_H2` 是 positive primitive `3 mod4` carrier

真实 endpoint中 `K>5`，所以

\[
F_W(K)=(K-5)(5K-11)>0.
\]
于是 (3.2) 为一个平方加一个严格正项：

\[
\boxed{\mathscr R_{H2}>0.}
\tag{4.1}

再看二进方向。reflection deep-even 中

\[
N=2^M5^M,
\qquad
B=2^{M+m+1}b_0,
\qquad A\text{ odd},
\]
且 `M>=11,m>=1`。

由 (2.1)，`20A^2` 的 2-adic depth恰为 `2`，其余两项深度严格大于 `2`，所以

\[
v_2(\mathcal L_2)=2.
\tag{4.2}

因此

\[
v_2(\mathcal L_2^2)=4.
\]
另一方面 `F_W(K)` 为 odd，所以

\[
v_2(4A^2F_W)=2.
\]
两项深度不同，故

\[
\boxed{v_2(\mathscr R_{H2})=2.}
\tag{4.3}

并且除以 `4` 后，平方项仍为偶数的平方、模 `4` 消失：

\[
\frac{\mathscr R_{H2}}4
\equiv A^2F_W(K)
\pmod4.
\]
当前 `K=2 mod4`，于是

\[
F_W(K)=(K-5)(5K-11)\equiv1\cdot3\equiv3\pmod4.
\]
而 `A^2=1 mod4`，所以

\[
\boxed{
\widehat{\mathscr R}_{H2}
:=\frac{\mathscr R_{H2}}4
>0,
\qquad
\widehat{\mathscr R}_{H2}\equiv3\pmod4.}
\tag{4.4}

因此 `R_H2` 和 `H_1` 文件中的 `R_H1`、universal `R_HO` 一样，提供一份真实 positive odd-inert parity carrier。

---

## 5. 送入 `W_q` height bridge

`spontaneous-height-resultant-parity.md` 已证明

\[
\boxed{
c_u^2\mathcal J_H
\equiv B^2\mathscr B_W
\pmod{W_q}.}
\tag{5.1}

把 (5.1) 代入 (3.1) 乘 `c_u^2` 的形式：

\[
\boxed{
B^2c_u^2\mathscr R_{H2}
\equiv
4A^2B^2\mathscr B_W
+c_u^2\mathcal H_2
\pmod{W_q}.}
\tag{5.2}

与 `H_1` bridge相比，这里的两个 depth-reader coefficients

\[
(2AB)^2,
\qquad c_u^2
\]
本身都是完整 squares。

---

## 6. genuine `H_2` height prime上的 coefficient audit

固定 endpoint-external non-`3` inert prime

\[
p^h\Vert W_q,
\qquad h\ge1,
\qquad p\equiv3\pmod4,
\qquad p\ne3,5,
\]
并假设它进入第二张 sphere orientation：

\[
p\mid\mathcal H_2.
\]

primitive/external separation给

\[
\boxed{p\nmid2ABc_u.}
\tag{6.1}

所以 (5.2) 中

\[
B^2c_u^2,
\qquad4A^2B^2,
\qquad c_u^2
\]
全是 `p`-adic units。由 §2 还知道 `L_2` 本身也是 unit，但后面的 depth law甚至不需要使用这一点。

---

## 7. unequal-depth law

写

\[
e_B:=v_p(\mathscr B_W),
\qquad
e_2:=v_p(\mathcal H_2),
\qquad
e_R:=v_p(\mathscr R_{H2}).
\]

在

\[
\min(e_B,e_2)<h
\]
范围内，(5.2) 是两个 unit-coefficient项之和。

若

\[
e_B<e_2,
\]
则第二项严格更深，不能取消第一项：

\[
\boxed{e_R=e_B.}
\tag{7.1}

若

\[
e_2<e_B,
\]
同理

\[
\boxed{e_R=e_2.}
\tag{7.2}

因此

\[
\boxed{
e_B\ne e_2,
\quad\min(e_B,e_2)<h
\Longrightarrow
v_p(\mathscr R_{H2})=\min(e_B,e_2).}
\tag{7.3}

第二张 orientation 的普通 unequal-depth区由此完全同步。

---

## 8. equal-depth extra lift强迫 `-square`

现在固定唯一危险层

\[
e_B=e_2=e<h.
\]

若 `R_H2` 比共同深度额外提升，则 (5.2) 除以 `p^e` 后必须满足

\[
4A^2B^2\frac{\mathscr B_W}{p^e}
+c_u^2\frac{\mathcal H_2}{p^e}
\equiv0\pmod p.
\]
因此

\[
\boxed{
\frac{\mathscr B_W/p^e}{\mathcal H_2/p^e}
\equiv
-\left(\frac{c_u}{2AB}\right)^2
\pmod p.}
\tag{8.1}

因为 `p=3 mod4`，`-1` 为 non-square，而括号中是 unit square，所以

\[
\boxed{
\left(
\frac{(\mathscr B_W/p^e)/(\mathcal H_2/p^e)}p
\right)=-1.}
\tag{8.2}

这与第一张 orientation 的结果严格互补。`spontaneous-height-h1-additive-bezout.md` 在 `H_1` equal-depth extra-lift shell得到

\[
\boxed{
(\mathscr B_W/p^e)/(\mathcal H_1/p^e)
\text{ 是 square},}
\tag{8.3}

而本文得到

\[
\boxed{
(\mathscr B_W/p^e)/(\mathcal H_2/p^e)
\text{ 是 non-square}.}
\tag{8.4}

因此 moving-height 两张 sphere orientations现在携带一个明确的 relative character label：

\[
\boxed{
H_1:\ +1,
\qquad
H_2:\ -1.}
\tag{8.5}

这个 label 来自 exact Bézout coefficients，不是另一次 singular-resultant audit。

---

## 9. 与 universal angle-norm bridge 的组合

`spontaneous-height-angle-additive-norm-bridge.md` 已证明，在 universal equal-depth extra-lift shell中

\[
\boxed{
(\mathscr B_W/p^e)/(\mathcal H_O/p^e)
\text{ 是 non-square},}
\tag{9.1}

且

\[
\mathcal H_1\mathcal H_2=4\mathcal H_O.
\tag{9.2}

因此在 companion orientation为 unit 的场合，可把 (8.3)–(8.4) 与 (9.1) 转成 companion character：

- `H_1` equal-depth extra lift若同时由 universal bridge读取，并且 `p∤H_2`，则
  \[
  \boxed{\left(\frac{\mathcal H_2}{p}\right)=-1;}
  \tag{9.3a}
  \]
- `H_2` equal-depth extra lift若同时由 universal bridge读取，并且 `p∤H_1`，则
  \[
  \boxed{\left(\frac{\mathcal H_1}{p}\right)=+1.}
  \tag{9.3b}
  
这是一个新的 cross-orientation character ledger。本文不假定两个 orientation在所有 prime上自动互斥，因此 (9.3) 明确保留 companion-unit 前提。

---

## 10. updated moving-height frontier

两张 moving sphere sheets 的 exact additive bridges现已对称完备：

\[
\boxed{
\begin{array}{c|c|c}
\text{orientation}&\text{new positive }3\bmod4\text{ carrier}&\text{equal-depth ratio}\\ \hline
H_1&\widehat{\mathscr R}_{H1}&\text{square}\\
H_2&\widehat{\mathscr R}_{H2}&\text{non-square}
\end{array}}
\tag{10.1}

加上 universal `H_O` bridge，所有 unequal-depth simple contacts都已有 exact depth reader；剩余 unsaturated kernel只在 equal-depth cancellation，并且现在带有 orientation-specific character。

下一步最有价值的目标不再是给 `H_2` 做新的 singular resultant，而是：

1. 审计 genuine external prime是否能同时进入 `H_1,H_2`；
2. 在 orientation互斥后，用 (9.3) 与 actual/conjugate angle sheet或 `W_q=alpha/omega` natural representative独立计算 companion character；
3. 若得到相反 character，即可关闭对应 equal-depth shell。