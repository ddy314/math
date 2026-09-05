# DD post-deflation structural reduction（curated import）

来源：`dongxuelian2/three-term-decimal-concatenation-square-sum@2cfa389f1d4ced90653101e6c92ee8dfe85b5535`，原稿 `strict_layer_DD_post_deflation_campaign.md`。

来源证据等级：`SGR-5D — STRUCTURAL REDUCTION`。**本仓库仅把它作为 frozen top-DD 历史中间件；来源后续的全局 DD closure 不被本仓库采纳。**

从
\[
\varepsilon M^2-E=\varepsilon Y^2,\qquad J=M-Y\ge1,
\]
及 top-DD double resonance
\[
v_p(M-Y)=v_p(M+Y)=j_p\quad(p=2,5),
\]
定义
\[
D_0=2^{j_2}5^{j_5},\qquad J^\sharp=(M-Y)/D_0,\qquad K^\sharp=(M+Y)/D_0.
\]
则
\[
\gcd(J^\sharp K^\sharp,10)=1,
\]
\[
H^\sharp=J^\sharp+K^\sharp=2M/D_0,
\]
\[
N^\sharp=J^\sharp K^\sharp=E/(\varepsilon D_0^2),
\]
从而
\[
\boxed{(J^\sharp)^2-H^\sharp J^\sharp+N^\sharp=0}.
\]

以 `n^{<10>}` 表示 prime-to-10 part，定义 residual supply
\[
\boxed{\Omega_{DD}=(Q_{12}\mathcal N_{12}\mathscr T)^{\langle10\rangle}},
\qquad
\mathscr T=\kappa^2(\kappa+2G)/10^{m_3}.
\]
关键 divisor result 为
\[
\boxed{J^\sharp\mid\Omega_{DD}^2}.
\]
因此 deflated small factor 的 residual odd prime powers 必须由 prefix `Q12`、`N12` 或 tail residual `mathscr T` 供应。

Residual local phase 可写成
\[
(J^\sharp)^2\equiv-N^\sharp\pmod{p^{R_p^\sharp}},
\qquad R_p^\sharp=v_p(H^\sharp),\quad p=2,5.
\]
Archimedean exact formula 为
\[
J^\sharp=\frac{M\rho}{D_0(1+\sqrt{1-\rho})},\qquad \rho=E/(\varepsilon M^2),
\]
故
\[
\frac{M\rho}{2D_0}\le J^\sharp\le\frac{M\rho}{D_0}.
\]
在来源 frozen top-DD inequalities 下得到高度相关上界
\[
\boxed{J^\sharp<14443\cdot10^{3S_{12}-10}}.
\]

该阶段没有 height-independent `J^sharp` bound；moving prefix supply 是真实瓶颈。后续 supply/phase audit 又证明 projected phase 本身是 endogenous，因此不能把它当独立 Hensel obstruction 重复收费。
