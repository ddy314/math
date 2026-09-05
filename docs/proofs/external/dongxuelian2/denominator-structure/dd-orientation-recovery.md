# DD source orientation recovery（curated import）

来源：`dongxuelian2/three-term-decimal-concatenation-square-sum@2cfa389f1d4ced90653101e6c92ee8dfe85b5535`，原稿 `strict_layer_DD_orientation_recovery_campaign.md`。

来源状态：`SGR-8B — ORIENTATION RECOVERY GATE`。**本仓库审计：只在来源冻结的 top-DD hypotheses 下保留；它是 `dd-top-quotient-overload.md` 的条件前置，不代表当前 DD 全局状态。**

对 frozen top-DD chamber，写
\[
Q=b_1 10^{m_2}+b_2,\quad G=b_1b_2,\quad
N=(a_1b_2)^2+(a_2b_1)^2,
\]
\[
A=a_1 10^{n_2}+a_2,\quad C=10^{d_3}A,\quad T=10^{m_3},
\]
\[
\kappa=TQG/b_3,\qquad QG<\kappa\le10QG.
\]

原六变量方程成为第三分子 `a=a3` 的二次式
\[
\kappa^3(\kappa+2G)a^2-2CG^2T\kappa^2a
+T^2[NQ^2(\kappa+G)^2-C^2G^2\kappa^2]=0.
\]
若 `t=G(R-r3)` 为 gap root，则恢复式
\[
\boxed{a(t)=\frac{TCG}{\kappa}-\frac{TQ(\kappa+G)}{\kappa^2}t}
\]
严格递减。Vieta involution 交换 gap quadratic 的两根，也交换 tail quadratic 的两根。

在来源 top-DD 数值区间内，若 `a3` 是合法 `n3` 位正根，则两根和满足
\[
\Sigma_a/a_3<2\cdot10^{-3},
\]
故共轭根
\[
\boxed{a_3^\vee<0}.
\]
因此合法 original candidate 选择唯一代数 orientation：gap root 是较小 Vieta root，并有
\[
\boxed{F_-<F_+}.
\]
若 post-deflation ordered roots 为 `J^sharp<K^sharp`，则
\[
\boxed{F_-=\Lambda D_0J^\sharp,\qquad F_+=\Lambda D_0K^\sharp}.
\]

令
\[
h=\gcd(\kappa,G),\quad A_\kappa=\kappa/h,\quad D=G/h,
\]
\[
B_\kappa=(\kappa+2G)/h=A_\kappa+2D.
\]
则
\[
\boxed{B_\kappa\mid F_-,\qquad A_\kappa\mid F_+},
\]
\[
\gcd(A_\kappa,B_\kappa)\in\{1,2\}.
\]
Denominator normalization 给 `A_kappa|TQ`。定义
\[
c=TQ/A_\kappa,\qquad b_3=cD,
\]
\[
u=F_-/B_\kappa,\qquad v=F_+/A_\kappa.
\]
得到 source-oriented quotient system
\[
\boxed{uv=Nc^2,\qquad v-u=2ha_3,\qquad b_3=cD},
\]
即
\[
\boxed{a_3=(v-u)/(2h)}.
\]

该系统与 third-block reducedness、top-DD double resonance 联立可推出本仓库保留的 frozen-top quotient-overload 矛盾；**任何超出 frozen top-DD 的使用都必须重新证明 coverage。**
