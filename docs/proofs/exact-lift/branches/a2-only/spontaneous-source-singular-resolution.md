# A2 source→common 唯一 singular projection 的 blow-up resolution

> **依赖：** `spontaneous-source-common-integer.md`、`spontaneous-source-equal-depth-nogo.md`。
>
> **严格状态：**`spontaneous-source-common-integer.md` 的 corrected carry audit证明：唯一 projected singular prime `p=1746991` 在 source half-depth `h>=2` 全部死亡，而 `h=1` 恰留下两个 normalized transverse templates `D=+-16651`。本文继续证明这两个模板在 blow-up 坐标 `(D,phi)` 上都是 nonsingular：angle 与 sphere 的二阶 normalized equations 具有非零 Jacobian determinant。等价地，消去 `phi` 后的 effective quadratic在两个根上 derivative均非零。因此 projected singularity经过一次 source transverse blow-up 后严格分裂成两条 simple Hensel branches；不会再产生 singular branching。本文不证明这两条 simple branch最终存在，也不宣称 A2 全局关闭。

---

## 1. corrected `h=1` exceptional equation

固定

\[
\boxed{p=1746991,}
\]

projected singular residue

\[
\boxed{x_0=1362653,\qquad \tau_0=807263.}
\tag{1.1}
\]

source half-depth `h=1` 写成

\[
d=pD,
\qquad
\Phi_s=p^2\phi.
\]

angle extra-lift的 normalized equation是

\[
\boxed{
F_{\rm ang}(D,\phi)
:=a_DD^2+b_\phi\phi=0,}
\tag{1.2}
\]

其中

\[
a_D
:=\frac{8(x_0+2)}{99x_0-4}
\equiv-8\pmod p,
\tag{1.3}
\]

\[
b_\phi:=-50625x_0^5
\equiv883946\pmod p.
\tag{1.4}
\]

所以

\[
\phi\equiv1007439D^2\pmod p.
\tag{1.5}
\]

corrected sphere二阶 equation为

\[
\boxed{
F_{\rm sph}(D,\phi)
:=572710+32070D^2-680549\phi=0.}
\tag{1.6}
\]

这里常数 `572710` 是旧纯 `F_p[eps]` checker 漏掉的 genuine `p`-adic carry。

---

## 2. 两个 transverse roots

将 (1.5) 代入 (1.6)：

\[
\boxed{
F_{\rm eff}(D)
:=572710+286982D^2=0\pmod p.}
\tag{2.1}
\]

于是

\[
D^2\equiv1231223\pmod p,
\]
且恰有两个 roots：

\[
\boxed{
D_+=16651,
\qquad
D_-=1730340=-16651\pmod p.}
\tag{2.2}
\]

因为只依赖 `D^2`，两支具有相同 angle correction：

\[
\boxed{\phi_+=\phi_-=987987\pmod p.}
\tag{2.3}
\]

---

## 3. `已严格完成`：effective root均为 simple

由 (2.1)：

\[
F_{\rm eff}'(D)=2\cdot286982D.
\tag{3.1}
\]

逐根计算：

\[
\boxed{
F_{\rm eff}'(D_+)
\equiv1033794\not\equiv0\pmod p,}
\tag{3.2+}
\]

\[
\boxed{
F_{\rm eff}'(D_-)
\equiv713197\not\equiv0\pmod p.}
\tag{3.2-}
\]

所以二阶 exceptional equation 在 blow-up 坐标 `D` 上已经完全非奇异：

\[
\boxed{
D_+,D_-\text{ are two simple roots of }F_{\rm eff}.}
\tag{3.3}
\]

特别地，如果后续 higher endpoint equations允许继续提升，每一支的 `D` correction都由普通一元 Hensel lemma唯一确定；不会再次分叉。

---

## 4. `已严格完成`：完整 `(D,phi)` Jacobian也非奇异

更直接地保留两条 normalized equation

\[
F_{\rm ang}=0,
\qquad
F_{\rm sph}=0.
\]

Jacobian为

\[
J(D,\phi)
=
\begin{pmatrix}
2a_DD&b_\phi\\
64140D&-680549
\end{pmatrix}.
\tag{4.1}
\]

在两个 roots上：

\[
\boxed{
\det J(D_+,\phi_+)
\equiv1475138\not\equiv0\pmod p,}
\tag{4.2+}
\]

\[
\boxed{
\det J(D_-,\phi_-)
\equiv271853\not\equiv0\pmod p.}
\tag{4.2-}
\]

所以不是只有消元后碰巧 simple；完整 angle+sphere 二元系统本身在 blow-up exceptional divisor 上就是 transversal intersection。

---

## 5. singularity 的正确几何解释

projected `(x,tau)` gate在 `p=1746991` 有 singular point：

\[
\mathcal C_{\rm src}
=\partial_x\mathcal C_{\rm src}
=\partial_\tau\mathcal C_{\rm src}=0\pmod p.
\]

但真实 source system还带一个 transverse coordinate

\[
d/p=D.
\]

corrected carry表明：

- `h>=2` 时 transverse correction来得太晚，projected `p^2` 主项无法取消，因此全部死亡；
- `h=1` 时 `D` 恰好在同一 `p^2` 层进入，并把 singular projection分裂成两点；
- 这两点的 Jacobian非零，所以 blow-up 后立刻 smooth。

因此真正的局部图景是

\[
\boxed{
\text{one projected singular point}
\xrightarrow{\text{source blow-up}}
\text{two simple }h=1\text{ branches}.}
\tag{5.1}
\]

这比“singular point无 lift”更精确，也解释了为什么旧 checker若忽略 `p`-adic carry会得到错误结论。

---

## 6. 更新后的 strict frontier

对于 source→common singular sector，现在已经没有继续做 discriminant/Jacobian 的理由：

\[
\boxed{
\begin{array}{c|c}
\text{source half-depth}&\text{status}\\ \hline
h\ge2&\text{严格为空}\\
h=1&D=16651,-16651\text{ 两条 simple branches}
\end{array}}
\tag{6.1}
\]

因此下一步若继续 fixed `1746991`，应把这两条 **simple** branch 与真实 decimal orbit / natural representative / endpoint defect `e` 同步，而不是再次做 singular-prime hunting。

generic source→common roots同理已经属于 simple-orbit问题。A2 仍保持 open。