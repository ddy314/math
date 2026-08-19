# A2 equal-depth minimum ties 的 serial tropical bridge

> **依赖：** `spontaneous-height-equal-depth-decimal-tropical-identity.md`、`spontaneous-height-equal-depth-three-cancellation-readers.md`。
>
> **严格状态：**此前 `E_+` 的 strict-extra 只能来自 `min(r_B,h,rho_p)` 的三类 pair tie 或 triple tie。本文引入一个新的纯 decimal 中间 carrier `C_BE=F_dec P-2K^2 beta`，证明原三项 tropical identity 精确分解成两条二项 bridge。第一节点只比较 `r_B` 与 `h`，第二节点只比较新的中间深度 `c_p` 与 `rho_p`。因此四种旧 tie 被压成两个串联 cancellation nodes；特别地，triple tie 若要 `E_+` strict-extra，第一节点反而必须精确停在 baseline，不能同时 extra。本文不排除第二节点的 higher cancellation，因此不关闭 A2。

---

## 1. notation

沿用

\[
P:=6K^2-36K+55,
\qquad
F_{\rm dec}:=TQ+2b_3,
\]

\[
\alpha=TK+a_3,
\qquad
\beta=TQ+b_3,
\]

以及三个 decimal readers

\[
B_{\rm dec}
=b_3^2(P-K^2)+T^2Q^2K^2,
\]

\[
E_+=P\beta-KQ\alpha,
\]

\[
\Lambda_{\rm dec}
=2K\beta^2-QF_{\rm dec}\alpha.
\]

固定 genuine deep equal-depth target prime `p`：

\[
v_p(P)=v_p(\beta)=h\ge1,
\qquad
v_p(\alpha)=2h,
\]

\[
v_p(B_{\rm dec})=h+r_B,
\qquad
v_p(\Lambda_{\rm dec})=2h+\rho_p,
\]

\[
v_p(E_+)=2h+r_+,
\qquad
r_B,\rho_p,r_+\ge1.
\]

当前 genuine separation 给

\[
p\nmid b_3TQKF_{\rm dec}.
\]

---

## 2. middle decimal carrier

定义

\[
\boxed{
C_{BE}:=F_{\rm dec}P-2K^2\beta.}
\tag{2.1}
\]

它完全由真实 prefix/decimal integers 构成。

### 2.1 first exact bridge

由

\[
B_{\rm dec}
=b_3^2P+K^2(TQ-b_3)\beta
\]
直接计算：

\[
\begin{aligned}
F_{\rm dec}B_{\rm dec}-TQK^2\beta^2
={}&b_3^2F_{\rm dec}P\\
&+K^2\beta\left[F_{\rm dec}(TQ-b_3)-TQ\beta\right].
\end{aligned}
\]

因为

\[
F_{\rm dec}(TQ-b_3)-TQ\beta
=(TQ+2b_3)(TQ-b_3)-TQ(TQ+b_3)
=-2b_3^2,
\]
所以

\[
\boxed{
F_{\rm dec}B_{\rm dec}
-TQK^2\beta^2
=b_3^2C_{BE}.}
\tag{2.2}
\]

### 2.2 second exact bridge

另一方面

\[
\begin{aligned}
F_{\rm dec}E_+-K\Lambda_{\rm dec}
={}&F_{\rm dec}(P\beta-KQ\alpha)\\
&-K(2K\beta^2-QF_{\rm dec}\alpha)\\
={}&\beta(F_{\rm dec}P-2K^2\beta).
\end{aligned}
\]

故

\[
\boxed{
F_{\rm dec}E_+
-K\Lambda_{\rm dec}
=\beta C_{BE}.}
\tag{2.3}
\]

原三项 tropical identity因此不是一个不可分的三项式，而是 (2.2) 与 (2.3) 两个串联二项节点。

---

## 3. `C_BE` 的 short positive window

写

\[
s:=K/N,
\qquad q:=Q/N,
\qquad w:=b_3/T.
\]

endpoint 给

\[
\frac{2499}{250}<s<10,
\qquad
\frac{21}{10}<q<\frac{40}{19},
\qquad
0<w<\frac{843}{1000},
\qquad
N\ge10^{11}.
\]

由定义

\[
\frac{C_{BE}}{TN^3}
=
q\left(4s^2-\frac{36s}{N}+\frac{55}{N^2}\right)
+\frac{2w}{N}
\left(5s^2-\frac{36s}{N}+\frac{55}{N^2}\right).
\tag{3.1}
\]

第二项为正。用 `q>21/10,s>2499/250,s<10,N>=10^11`：

\[
\frac{C_{BE}}{TN^3}
>
\frac{21}{10}
\left[
4\left(\frac{2499}{250}\right)^2
-\frac{360}{10^{11}}
\right]
>839.
\]

上界则丢掉所有负项并用 `q<40/19,s<10,w<843/1000`：

\[
\frac{C_{BE}}{TN^3}
<
\frac{40}{19}
\left(400+\frac{55}{10^{22}}\right)
+
\frac{2}{10^{11}}\frac{843}{1000}
\left(500+\frac{55}{10^{22}}\right)
<843.
\]

所以

\[
\boxed{
839TN^3<C_{BE}<843TN^3.}
\tag{3.2}
\]

特别地

\[
\boxed{C_{BE}>0}
\]
并且

\[
\boxed{C_{BE}\text{ 恰有 }m+3M+3\text{ 位}.}
\tag{3.3}
\]

它比 `E_+` 的 `m+3M+4` 位短一位十进制数字。

---

## 4. first-node valuation law

定义中间 residual depth

\[
\boxed{c_p:=v_p(C_{BE})-h.}
\tag{4.1}
\]

由 (2.2)，三项赋值为

\[
v_p(F_{\rm dec}B_{\rm dec})=h+r_B,
\]

\[
v_p(TQK^2\beta^2)=2h,
\]

\[
v_p(b_3^2C_{BE})=h+c_p.
\]

因此

\[
\boxed{c_p\ge\min(r_B,h).}
\tag{4.2}
\]

若

\[
r_B\ne h,
\]
左边差式中存在唯一最浅项，所以

\[
\boxed{c_p=\min(r_B,h).}
\tag{4.3}
\]

只有

\[
\boxed{r_B=h}
\tag{4.4}
\]
时，第一节点才能让 `C_BE` 比 `2h` 更深，即

\[
c_p>h.
\]

另外当前 `r_B,h>=1`，故无条件有

\[
\boxed{c_p\ge1,\qquad p^{h+1}\mid C_{BE}.}
\tag{4.5}
\]

---

## 5. second-node valuation law

由 (2.3)：

\[
F_{\rm dec}E_+=K\Lambda_{\rm dec}+\beta C_{BE}.
\]

三项赋值为

\[
v_p(F_{\rm dec}E_+)=2h+r_+,
\]

\[
v_p(K\Lambda_{\rm dec})=2h+\rho_p,
\]

\[
v_p(\beta C_{BE})=2h+c_p.
\]

所以

\[
\boxed{r_+\ge\min(\rho_p,c_p).}
\tag{5.1}
\]

若

\[
\rho_p\ne c_p,
\]
右边有唯一最浅项，因此

\[
\boxed{r_+=\min(\rho_p,c_p).}
\tag{5.2}
\]

所以 second-node strict cancellation只有在

\[
\boxed{\rho_p=c_p}
\tag{5.3}
\]
时才可能发生。

---

## 6. four old minimum ties collapse to two serial mechanisms

现在重新审计此前的四类 strict-extra frontier。

### 6.1 `r_B=h<rho_p`

假设

\[
r_+>h.
\]

若 `c_p=h`，则 `rho_p>c_p`，由 (5.2) 必有

\[
r_+=c_p=h,
\]
矛盾。因此

\[
\boxed{
r_B=h<\rho_p,\quad r_+>h
\Longrightarrow
c_p>h.}
\tag{6.1}
\]

所以这类 strict-extra 完全由**第一节点**的额外 cancellation产生：

\[
F_{\rm dec}B_{\rm dec}
\equiv TQK^2\beta^2
\pmod{p^{2h+1}}.
\]

特别地

\[
\boxed{p^{2h+1}\mid C_{BE}.}
\tag{6.2}
\]

### 6.2 `r_B=\rho_p<h`

由 `r_B<h`，(4.3) 给

\[
c_p=r_B=\rho_p.
\]

所以 strict-extra `r_+>r_B` 精确进入第二节点 tie：

\[
\boxed{c_p=\rho_p=r_B.}
\tag{6.3}
\]

### 6.3 `h=\rho_p<r_B`

由 `r_B>h`，(4.3) 给

\[
c_p=h=\rho_p.
\]

因此 strict-extra 同样只能来自第二节点：

\[
\boxed{c_p=\rho_p=h.}
\tag{6.4}
\]

### 6.4 triple tie `r_B=h=\rho_p`

第一节点只给

\[
c_p\ge h.
\]

若 `c_p>h`，则

\[
\rho_p=h<c_p,
\]
由 (5.2) 反而强迫

\[
r_+=h.
\]

所以若 triple tie 还要求 strict-extra

\[
r_+>h,
\]
就必须有

\[
\boxed{c_p=h.}
\tag{6.5}
\]

并且第二节点恰发生 tie：

\[
\boxed{c_p=\rho_p=h.}
\tag{6.6}
\]

这是重要的互斥：triple tie 中 `C_BE` 不能同时 extra；第一节点若继续深化，第二节点反而失去 tie，`E_+` 被锁回最低深度。

---

## 7. serial cancellation picture

四类旧 frontier因此被压成：

\[
\boxed{
\begin{array}{c|c}
\text{old tie}&\text{actual strict-extra mechanism}\\ \hline
r_B=h<\rho_p&\text{first node: }c_p>h\\
r_B=\rho_p<h&\text{second node: }c_p=\rho_p\\
h=\rho_p<r_B&\text{second node: }c_p=\rho_p\\
r_B=h=\rho_p&\text{second node: }c_p=\rho_p=h
\end{array}}
\tag{7.1}
\]

所以只有两个真正 remaining higher-cancellation problems：

1. first-node extra
   \[
   r_B=h<\rho_p,\qquad c_p>h;
   \]
2. second-node extra
   \[
   c_p=\rho_p,\qquad r_+>\rho_p.
   \]

后续无需继续分别维护三种 pair tie和 triple tie。

---

## 8. current frontier

`C_BE` 给出了一个新的 canonical short reader：

\[
\boxed{
C_{BE}=F_{\rm dec}P-2K^2\beta,
\qquad
839TN^3<C_{BE}<843TN^3.}
\]

完整 depth pipeline 变成

\[
\boxed{
(r_B,h)
\longrightarrow c_p
\longrightarrow(\rho_p,c_p)
\longrightarrow r_+.}
\tag{8.1}
\]

因此 equal-depth deep resonance 的局部无界机制已从四个 minimum-tie cases压成两个串联二项 cancellation nodes。

A2 仍为 `待证`。
