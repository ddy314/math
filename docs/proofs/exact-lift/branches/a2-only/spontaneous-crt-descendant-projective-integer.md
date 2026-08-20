# A2 descendant-only external pool 的 canonical projective integer carrier

> **依赖：** `spontaneous-crt-pure-projective-carrier.md`、`spontaneous-crt-descendant-companion-separation.md`、deep-even primitive reduction。
>
> **严格状态：**generic descendant-only external support已经与 old `G_JB/Lambda_tail` companion pool严格分离，因此需要自己的 ordinary integer reader。本文直接把 dimensionless projective carrier `X_63^proj(u,v)` 代回真实整数 ratios `u=a_3/(TK)`、`v=Q^2N_0/(B^2K^2)`，清去统一 denominator，得到一个只含59个 composite monomials的 canonical integer `P_63`。其真实 endpoint值严格为正；完整二进 content为 `2^(16M+8m+58)`，positive primitive quotient恒为 `1 mod8`。于是 descendant-only external pool现在有了独立 natural carrier与 exact parity orientation，不再借用 `Lambda_tail`。本文尚未把 common-prime depth与该 carrier的 Archimedean height压成矛盾，因此不关闭 A2。

---

## 1. actual projective ratios

前一文件的 dimensionless variables可直接写成真实 integer blocks：

\[
\boxed{
u=\frac{a_3}{TK},}
\tag{1.1}
\]

\[
\boxed{
v=\frac{Q^2N_0}{B^2K^2}.}
\tag{1.2}
\]

这里

\[
N=10^M,
\qquad T=10^m,
\qquad B=b_2,
\qquad Q=B+2N,
\]

\[
K=9N+10A,
\qquad
N_0=(9B/2)^2+A^2.
\]

定义三个 positive blocks

\[
\boxed{R:=TK,\qquad X:=Q^2N_0,\qquad Y:=B^2K^2.}
\tag{1.3}
\]

于是

\[
u=a_3/R,
\qquad
v=X/Y.
\]

---

## 2. clear the projective carrier

`spontaneous-crt-pure-projective-carrier.md` 定义 primitive irreducible polynomial

\[
\boxed{
\mathscr X_{63}^{\rm proj}(u,v)
=\sum c_{ij}u^iv^j,}
\tag{2.1}

满足

\[
\deg_u=\deg_v=8,
\qquad
\deg_{\rm total}=11,
\qquad
\#\operatorname{supp}=59.
\]

定义 ordinary integer clearing

\[
\boxed{
\mathscr P_{63}
:=R^8Y^8
\mathscr X_{63}^{\rm proj}(a_3/R,X/Y).}
\tag{2.2}

展开仍只有同样59个 composite terms：

\[
\boxed{
\mathscr P_{63}
=\sum c_{ij}
 a_3^iR^{8-i}X^jY^{8-j}.}
\tag{2.3}

对于 genuine descendant-only external prime，`p` 与 `RY` 以及 fixed content `5^7 11^7` 分离，因此

\[
\boxed{p\mid\mathscr P_{63}.}
\tag{2.4}

这给新 external pool一个无需 branch-specific sphere denominator的 canonical integer reader。

---

## 3. real endpoint lies in a tiny positive projective box

已有 exact window

\[
\boxed{
\frac{937}{1000}<v<\frac{939}{1000}.}
\tag{3.1}

对 `u`，第三块 endpoint给

\[
1<\frac{a_3}{T}<\frac{251}{250},
\]
而

\[
K/N=9+y>\frac{2499}{250},
\qquad
N\ge10^{11}.
\]

所以

\[
0<u
<\frac{251}{2499}\,10^{-11}
<\frac1{1000}.
\tag{3.2}

因此真实 point 位于 rational rectangle

\[
\boxed{
\mathcal R_{\rm act}
=[0,1/1000]\times[937/1000,939/1000].}
\tag{3.3}

---

## 4. exact positivity of the projective carrier

将 `X_63^proj` 仿射搬到 unit square对应 (3.3)，再转成 bidegree `(8,8)` tensor Bernstein basis。

checker逐一验证全部81个 exact rational Bernstein coefficients严格为正。最小 coefficient仍为

\[
\boxed{
\frac{170202247140227961698711469574928714478754971}
{9313225746154785156250}>0.}
\tag{4.1}

所以 Bernstein convex-hull property给

\[
\boxed{
\mathscr X_{63}^{\rm proj}(u,v)>0
\qquad((u,v)\in\mathcal R_{\rm act}).}
\tag{4.2}

因为 `R,Y>0`，真实 dangerous endpoint上

\[
\boxed{\mathscr P_{63}>0.}
\tag{4.3}

---

## 5. exact binary depths of the blocks

当前 deep-even normal form给：

\[
\boxed{a_3\text{ odd},}
\tag{5.1}

因为 `b_3` 为偶且 `(a_3,b_3)=1`。

另外

\[
\boxed{v_2(R)=v_2(TK)=m+1,}
\tag{5.2}

因为 `v_2(T)=m`、`v_2(K)=1`。

对 `X`：

\[
Q=2^{M+1}Q_0,
\qquad Q_0,N_0\text{ odd},
\]
所以

\[
\boxed{v_2(X)=2M+2.}
\tag{5.3}

对 `Y`：

\[
v_2(B)=M+m+t,
\qquad v_2(K)=1,
\]
故

\[
\boxed{v_2(Y)=2M+2m+2t+2.}
\tag{5.4}

记

\[
\delta:=v_2(Y)-v_2(X)=2m+2t\ge16.
\tag{5.5}

---

## 6. unique lowest monomial

对 projective carrier coefficients做 exact audit。最高 `v` 次只有一个 monomial

\[
\boxed{c_{0,8}v^8,}
\]
其中

\[
\boxed{c_{0,8}=2^{34}3^{24}13^2.}
\tag{6.1}

对任意 support monomial `(i,j)`，(2.3) 的二进深度为

\[
v_2(c_{ij})
+(8-i)(m+1)
+j(2M+2)
+(8-j)(2M+2m+2t+2).
\]

抽出公共项

\[
8(m+1)+8(2M+2),
\]
剩余 extra depth 为

\[
\boxed{
\epsilon_{ij}
=v_2(c_{ij})-i(m+1)+(8-j)(2m+2t).}
\tag{6.2}

checker对全部59项验证：

1. `16-i-2j>=0`，所以 `epsilon_ij` 对 `m>=5` 不会下降；
2. `16-2j>=0`，所以对 `t>=3` 也不会下降；
3. 在最小 `(m,t)=(5,3)` 上，唯一 minimum 是
   \[
   \boxed{\epsilon_{0,8}=34,}
   \]
   第二浅层至少为
   \[
   \boxed{39.}
   \]

因此不存在 lowest-layer cancellation。

---

## 7. exact primitive orientation

由 §6：

\[
\boxed{
 v_2(\mathscr P_{63})
=8(m+1)+8(2M+2)+34
=16M+8m+58.}
\tag{7.1}

除去该完整二进 content，模 `8` 只剩 `(i,j)=(0,8)` 项：

\[
\frac{\mathscr P_{63}}{2^{16M+8m+58}}
\equiv
\frac{c_{0,8}}{2^{34}}
\left(\frac R{2^{m+1}}\right)^8
\left(\frac X{2^{2M+2}}\right)^8
\pmod8.
\]

三个括号均为 odd units，且 odd eighth power恒为 `1 mod8`。又

\[
\frac{c_{0,8}}{2^{34}}
=3^{24}13^2
\equiv1\pmod8.
\]

故

\[
\boxed{
\frac{\mathscr P_{63}}{2^{16M+8m+58}}
\equiv1\pmod8.}
\tag{7.2}

结合 (4.3)，这是 positive primitive `1 mod8` orientation。

---

## 8. parity role

`P_63` 的 positive primitive part为 `1 mod4`，所以其全部 `3 mod4` prime valuation总 parity为偶数。

这与 coefficient-singular low branch

\[
H_{V4}^\circ\equiv7\pmod8
\]
形成明确对照：

- generic descendant-only external natural carrier：`1 mod8`，parity-neutral；
- `H_4` coefficient singular escape：`7 mod8`，额外 odd-inert surcharge；
- `H_24` coefficient singular escape：`5 mod8`，total inert parity even。

所以 generic pool现在已有自己的 canonical reader与 exact orientation，但这仍没有证明某个 particular inert common prime不能整除 `P_63`。

---

## 9. updated frontier

`spontaneous-crt-descendant-companion-separation.md` 已证明 generic descendant-only external support不能借 `Lambda_tail` 付账。本文补上其独立 reader：

\[
\boxed{
\mathscr P_{63}>0,
\qquad
v_2(\mathscr P_{63})=16M+8m+58,
\qquad
\mathscr P_{63}^{\circ}\equiv1\pmod8.}
\]

下一步应把 `G_Delta` 的 actual external common depth与 `P_63` 的 valuation做 exact comparison；若能证明 `v_p(P_63)`只读取 first-layer/simple depth，而 `G_Delta` 需要 odd excess，就可能关闭 generic common-parity escape。

A2 仍为 `待证`。
