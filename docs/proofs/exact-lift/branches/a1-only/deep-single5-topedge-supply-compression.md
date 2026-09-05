# A1 minimal diagonal: single-5 top-edge supply compression

> 日期：2026-08-22。
>
> 依赖：`deep-single5-decimal-height-collapse.md`、`deep-denominator-ledger.md`、`global-terminal-bridge.md`。
>
> 范围：minimal diagonal `k=g>=32` 的 surviving single-5 top edge
> \[
> D_{\rm gap}=5^B,\qquad B>k,\qquad \lambda_2=2k-1.
> \]

状态：**本文各 reduction 已严格完成；top-edge 尚未整体关闭。**

---

## 1. 记号

令

\[
T=10^k,
\qquad
h=qs,
\qquad
Q=qv,
\qquad
b_1=us,
\]

其中 `q|Q`、`s|b1` 是 minimal-diagonal legal odd supply，并且 `s` 只能由 `b1` 中允许的 `1 mod 4` whole prime-power blocks 构成。

因此

\[
\boxed{s\equiv1\pmod4.}
\tag{1}
\]

令

\[
e=v_2(w)=v_2(b_1),
\qquad
b_1=2^eG_0,
\]

其中 `G0` 为奇数。因为 `h` 为奇数，

\[
M_c:=\frac{Qb_1}{h}=2^euv.
\]

---

## 2. `kappa` window 直接锁定 `h` 的大小

single-5 有

\[
\kappa=
\frac{5^BT^2M_c}{2^{\lambda_2}}.
\]

在 top edge `lambda2=2k-1` 中：

\[
\boxed{
\kappa=2^{e+1}5^{B+2k}uv.
}
\tag{2}
\]

另一方面

\[
Qb_1=2^e qv\,us=2^euvh.
\]

因此

\[
\boxed{
\frac{\kappa}{Qb_1}
=
\frac{2\,5^{B+2k}}h.
}
\tag{3}
\]

全局 tail-weight window 为

\[
Qb_1<\kappa\le10Qb_1.
\]

代入 (3) 得

\[
1<\frac{2\,5^{B+2k}}h\le10,
\]

也就是

\[
\boxed{
5^{B+2k-1}\le h<2\,5^{B+2k}.
}
\tag{4}
\]

因为 `B>=k+1`：

\[
h\ge5^{3k}.
\]

而

\[
Q<100T^2,
\qquad
b_1<10T^2.
\]

对 `k>=32`：

\[
\frac{5^{3k}}{100T^2}
=
\frac1{100}\left(\frac54\right)^k
>1.
\]

故

\[
\boxed{h>Q,\qquad h>b_1.}
\tag{5}
\]

由于 `h=qs`、`q<=Q`、`s<=b1`，(5) 立即推出

\[
\boxed{q>1,\qquad s>1.}
\tag{6}
\]

所以 top edge 强迫 odd supply 同时从 `Q` 与 `b1` 两侧取得 genuine nontrivial blocks。

---

## 3. exact high-sign 2-adic congruence

`deep-single5-decimal-height-collapse.md` 已证明：top edge 两个形式根的 reduced 2-denominator depths 精确为

\[
\{1,t_2-e\},
\qquad
 t_2=v_2(\kappa+2b_1).
\]

真实 third block 只能使用 high-denominator sign，并且其共同 decimal height `n` 满足

\[
\boxed{n=t_2-e.}
\tag{7}
\]

由 (2) 与 `b1=2^eG0=2^eus`：

\[
\begin{aligned}
\kappa+2b_1
&=2^{e+1}u\left(5^{B+2k}v+s\right).
\end{aligned}
\]

所以

\[
t_2=e+1+v_2\!\left(s+5^{B+2k}v\right).
\]

结合 (7)：

\[
\boxed{
 v_2\!\left(s+5^{B+2k}v\right)=n-1.
}
\tag{8}
\]

乘以奇数 `q` 并使用 `h=qs`,`Q=qv`：

\[
\boxed{
 v_2\!\left(h+5^{B+2k}Q\right)=n-1.
}
\tag{9}
\]

single-5 中

\[
v_5(L)=B+k,
\]

故 decimal-height synchronization 至少给

\[
n\ge B+k.
\]

因此 (8)-(9) 特别蕴含

\[
\boxed{
 s\equiv-5^{B+2k}v
 \pmod{2^{B+k-1}},
}
\tag{10}
\]

\[
\boxed{
 h\equiv-5^{B+2k}Q
 \pmod{2^{B+k-1}}.
}
\tag{11}
\]

---

## 4. Q-side complement orientation

因为 `B+k-1>=64`，(10) 当然可模 `4`。由 (1) 与

\[
5^{B+2k}\equiv1\pmod4
\]

得到

\[
1+v\equiv0\pmod4.
\]

故

\[
\boxed{v=Q/q\equiv3\pmod4.}
\tag{12}
\]

特别地

\[
\boxed{v>1,\qquad q<Q.}
\tag{13}
\]

结合 (6)，top edge 的 supply orientation 现在是

\[
\boxed{
1<q<Q,
\qquad
1<s<b_1,
\qquad
Q/q\equiv3\pmod4.
}
\tag{14}
\]

这不是 double-deep `strict-2` orientation 的沿用，而是由 top-edge decimal-height synchronization 独立推出的新结论。

---

## 5. first remainder 给 `B` 的线性高度上界

universal first complement remainder 为

\[
M_cD_{\rm gap}N_0
=1000\lambda T^3+R_1,
\]

\[
0<R_1<390100\lambda T.
\]

在 top edge：

\[
D_{\rm gap}=5^B,
\qquad
\lambda=2^{2k-1}.
\]

令

\[
\nu=v_5(N_0),
\qquad
Y=B+\nu.
\]

因为 `M_c` 为 5-unit：

\[
v_5(M_c5^BN_0)=Y.
\]

主项满足

\[
v_5(1000\,2^{2k-1}T^3)=3k+3.
\]

### 5.1 `Y>=3k+3` 不可能

若 `Y>=3k+3`，则

\[
5^{3k+3}\mid R_1.
\]

但

\[
R_1<390100\,2^{2k-1}T
=390100\,2^{3k-1}5^k.
\]

对 `k=32` 已有

\[
5^{3k+3}
>4\times10^{12}\cdot
390100\,2^{3k-1}5^k,
\]

且左/右之比每增加一个 `k` 再乘 `25/8>1`。故矛盾。因此

\[
\boxed{Y<3k+3.}
\tag{15}
\]

### 5.2 精确由 `R1` 承担 5-depth

由 (15)，左右主项 5-adic depths 不同，故

\[
\boxed{v_5(R_1)=Y.}
\tag{16}
\]

于是

\[
5^Y<R_1
<390100\,2^{3k-1}5^k.
\]

取 `log_5`：

\[
\boxed{
B+v_5(N_0)
<
\left(1+3\log_5 2\right)k
+\log_5(390100)-\log_5 2.
}
\tag{17}
\]

数值上

\[
1+3\log_5 2<2.293,
\]

\[
\log_5(390100)-\log_5 2<7.57.
\]

所以可安全写成

\[
\boxed{
B+v_5(N_0)<2.293k+7.57.
}
\tag{18}
\]

特别地

\[
\boxed{B<2.293k+7.57.}
\tag{19}
\]

所以 top edge 的 `B` 虽仍随 `k` 增长，但已经被压进一条显式窄线性带。

---

## 6. 当前 top-edge terminal

任意 surviving top-edge candidate 必须同时满足

\[
\boxed{
\begin{gathered}
 k\ge32,\qquad k<B<2.293k+7.57,\\
5^{B+2k-1}\le h<2\,5^{B+2k},\\
h=qs,\quad Q=qv,\quad b_1=us,\\
1<q<Q,\quad1<s<b_1,\quad v\equiv3\pmod4,\\
v_2(h+5^{B+2k}Q)=n-1,\quad n\ge B+k.
\end{gathered}}
\tag{20}
\]

并且同一个 high root sign 还必须通过 5-adic denominator allocation、finite-decimal recovery 与 odd-part coprimality。

后续最自然的攻击点是：把 (20) 的 genuine two-sided supply 与 Q-side contact square block lifting、`b1` whole-block structure 和 recovery-gap cyclotomic kernel联立，证明这些 odd blocks 无法全部支持同一个 root sign。
