# A1 minimal diagonal: moderate HL forces a genuine contact Q-side lift

> 日期：2026-08-20。依赖 `deep-hl-one-exponent-divisor-family.md`、`deep-complement-height.md`、`deep-contact-q-resultant-loss.md`。当前 fixed frontier 为 `k>=32`。

`deep-contact-q-resultant-loss.md` 证明 contact square 的 ideal `q^2` lifting 最多损失

\[
g:=\gcd(q,C)<1599T.
\]

本文证明在 moderate HL 中

\[
\boxed{q>1683T>g.}
\]

因此异常 resultant 不可能吞掉整个 Q-side supply：至少有一个 selected Q-primary block 在 contact factor 中发生**严格 exponent amplification**。

状态：**已严格完成。**

---

## 1. complement divisor `v` 的上界

moderate HL 的 stripped complement equation：

\[
2\beta u-\alpha v=5^d>0,
\]

所以

\[
\boxed{\alpha v<2\beta u.}
\tag{1}

乘以 `v`，并用

\[
M=uv:
\]

\[
\alpha v^2<2\beta M.
\]

因此

\[
\boxed{v^2<\frac{2\beta}{\alpha}M.}
\tag{2}

`deep-complement-height.md` 给

\[
\mu:=\frac{MD}{T^2}<10001.
\]

所以

\[
M<10001\frac{T^2}{D}.
\]

代入 (2)：

\[
\boxed{
v<T\sqrt{\frac{20002\beta}{\alpha D}}.}
\tag{3}

---

## 2. 转成 `q=Q/v` 的下界

minimal diagonal

\[
Q=100T^2-(10w-1).
\]

当前 `T>=10^32`，当然有安全界

\[
\boxed{Q>99T^2.}
\tag{4}

因此由 (3)：

\[
\boxed{
q=\frac Qv
>99T\sqrt{\frac{\alpha D}{20002\beta}}.}
\tag{5}

---

## 3. uniform moderate HL 输入

HL 中

\[
A=2k+3-v_2(r).
\]

全部 typewise `r` windows 均有

\[
r<15,214,000,
\]

所以

\[
\boxed{v_2(r)\le23.}
\]

又 double-deep 要求

\[
B\ge1.
\]

故

\[
\boxed{
D=2^A5^B
\ge5\cdot2^{2k+3-23}
=5\cdot2^{2k-20}.}
\tag{6}

同时

\[
\alpha\ge1,
\qquad
\beta\le r_{10}<15,214,000.
\tag{7}

把 (6)-(7) 代入 (5)：

\[
q
>99T
\sqrt{
\frac{5\cdot2^{2k-20}}
{20002\cdot15,214,000}
}.
\tag{8}

右侧除 `T` 外每增加一个 `k` 会额外乘 2。因此最弱层就是当前首个未关闭 fixed layer `k=32`。

直接计算安全常数：

\[
99\sqrt{
\frac{5\cdot2^{44}}
{20002\cdot15,214,000}
}
>1683.
\]

所以

\[
\boxed{q>1683T.}
\tag{9}

---

## 4. resultant exceptional part 不可能覆盖整个 `q`

contact resultant theorem 给

\[
\boxed{g:=\gcd(q,C)<1599T.}
\tag{10}

结合 (9)：

\[
\boxed{q>g.}
\tag{11}

写

\[
q=\prod p^{e_p},
\qquad
g=\prod p^{c_p},
\qquad c_p=\min(e_p,v_p(C)).
\]

若每个 selected block 都有

\[
e_p\le v_p(C),
\]

则 `c_p=e_p` 对全部 p，意味着 `g=q`，与 (11) 矛盾。

因此至少存在一个

\[
\boxed{p^e\Vert q}
\]

满足

\[
\boxed{e>v_p(C).}
\tag{12}

---

## 5. contact factor 中出现严格 exponent amplification

`deep-contact-q-resultant-loss.md` 已证明，对 `p^e||q`，某个 contact factor

\[
L_\pm=Db_1C\pm Z
\]

至少含

\[
p^{2e-\min(e,v_p(C))}.
\]

在 (12) 的 block 上：

\[
\min(e,v_p(C))=v_p(C)<e.
\]

因此

\[
\boxed{
2e-v_p(C)>e,}
\]

且

\[
\boxed{
p^{2e-v_p(C)}\mid L_-
\quad\text{or}\quad
p^{2e-v_p(C)}\mid L_+.}
\tag{13}

所以 moderate HL 中至少一个 Q-side selected prime block一定发生真正的 exponent amplification；不能全部只以原 exponent `e` 穿过 contact square。

---

## 6. 当前意义

moderate HL 的剩余 arithmetic 现在同时满足：

1. finite `r` signatures + one-exponent divisor family；
2. Q-side supply `q` 超线性：`q>1683T`；
3. exceptional contact gcd 仅 `O(T)`；
4. 因而至少一个 Q-primary block必须在 contact factor中被提升到严格大于原 `q` exponent。

下一步应针对这个 forced lifted block研究：

- 与 `q|Q=10^(2k+2)-(10w-1)` 的 p-adic exponent；
- 与 contact factor `L_+-L_-=2Z` 的 gcd；
- 与 complementary divisor `v=Q/q=O(T/sqrt D)` 的小尺度结构。

这已经把 contact square 从“额外必要条件”变成了 moderate HL 中必然出现的具体 prime-power event。
