# 统一符号

本文件对应原总稿 §§40–41，作为跨章节符号索引。若新推导需要复用旧符号，先在这里登记对应关系，不要让同一字母重新承担多个全局含义。

## 2026-08-13 DD 新增符号

| 符号 | 含义 |
|---|---|
| (S,m,n,d) | DD 后续推导中的 (S_{12},m_3,n_3,d_3) 简写，仅限 §27.33 起 |
| (gamma,u,v) | (gamma=(kappa,G))、(kappa=gamma u)、(G=gamma v)，且 ((u,v)=1) |
| (U,V,H,T,Z) | 双 resonance S-unit phase：(5^TU+V=2^HZ) |
| (mathscr T) | 全局 tail quotient (kappa^2(kappa+2G)/10^{m_3}) |
| (g_*) | denominator overlap ((b_1,b_2)(\operatorname{lcm}(b_1,b_2),b_3)) |
| (D,H_0,q_0,C,E') | primitive exact-lift reduction 中的公共尺度、本原球面量、concat gcd 与本原 determinant |
| (	heta_{12},	heta_{13},	heta_{23}) | 三条 primitive carrier determinants |
| (Z_0) | stereographic/projective 参数的最低项分母 |
| (C_L,Pi) | frontier 上的 moving pair-max Gaussian core 及其有向 Gaussian 因子，(N(Pi)=C_L) |
| (q_c) | frontier 上与 (C_L) 渐近互素的 clean source core |
| (R_2) | denominator-only quotient ((5^T\widetilde r+s q_c\theta)/2^{m_2}) |
| (delta_*) | frontier 剩余 source entropy 常数 (0.007853581954\ldots) |

> 迁移说明：以下正文由原始总稿机械拆分，公式和证明状态不作数学改写。
# 40. 统一符号表

本文有意消除了旧工作稿中同一字母被多次复用的问题。

| 统一符号 | 含义 |
|---|---|
| \(a_i,b_i\) | 第 \(i\) 个既约有理数的分子、分母 |
| \(n_i,m_i\) | \(a_i,b_i\) 的十进制位数 |
| \(s_i=n_i-m_i\) | 第 \(i\) 块位数差 |
| \(\alpha,\beta\) | 三分子、三分母的十进制拼接 |
| \(\mathcal R\) | \(\sqrt{r_1^2+r_2^2+r_3^2}\) |
| \(B_i,w_i,\Lambda_i\) | 拼接位置权重、正权、carrier 放大因子 |
| \(q\) | \(\operatorname{lcm}(b_1,b_2,b_3)\) |
| \(y_i,H\) | 整数球面坐标与半径 |
| \(Q\) | \(b_1 10^{m_2}+b_2\) |
| \(G\) | \(b_1b_2\) |
| \(\mathcal N_{12}\) | \((a_1b_2)^2+(a_2b_1)^2\) |
| \(C,D\) | 三分支统一 coefficient pair |
| \(\ell\) | 有效第三尾长 |
| \(\delta_3\) | \(\gcd(10^\ell,b_3)\) |
| \(L\) | \(10^\ell/\delta_3\) |
| \(\tau\) | \(b_3/\delta_3\) |
| \(z_3\) | \(a_3/\delta_3\) |
| \(\kappa\) | 统一整数尾权 |
| \(K_{C,D}\) | 统一判别核 |
| \(W\) | 统一判别平方根 |
| \(G_0\) | primitive recovery gcd |
| \(S_{12}\) | \(m_1+m_2\)，前两分母位数尺度 |
| \(\mathcal S_{12}\) | \(y_1^2+y_2^2\)，前两 ghost 平方和 |
| \(d_3\) | DD 中 \(s_3\) |
| \(k_{12}\) | DD/A1 中 \(s_2+s_3\) |
| \(g\) | \(A_1\) 中 \(-s_3\) |
| \(A_{12}\) | \(a_1 10^{n_2}+a_2\) |
| \(\sigma_5\) | \(A_2\) deep-even 中 \(v_5(u)\) |
| \(E_5\) | \(\lambda+\sigma_5\) |
| \(Q_0,\mathcal N_0\) | \(A_2\) 去二后的前缀量 |
| \(c_Q,c_u,\rho\) | \(A_2\) source split |
| \(\Delta_{\rm pref}\) | \(A_2\) prefix defect |
| \(\Phi,\Psi_{a_1}\) | \(A_2\) source 双 Hensel 多项式 |

---

# 41. 旧记号到统一记号的主要对应

为了阅读此前工作稿，下面给出最容易冲突的旧记号对应。正文不再使用这些歧义写法。

| 旧用法 | 本文统一写法 |
|---|---|
| \(M=m_2,\ m=m_3\) | 直接使用 \(m_2,m_3\) |
| \(S=y_1^2+y_2^2\) | \(\mathcal S_{12}\) |
| \(S=m_1+m_2\) | \(S_{12}\) |
| DD 中 \(d=s_3\) | \(d_3\) |
| 多处 \(D\) 表 gcd / divisor / coefficient | gcd 用 \(\delta_3,d_*\)，统一系数保留 \(D\) |
| 第三分子本原根 \(z\) | \(z_3\) |
| \(A_2\) 判别平方根 \(z\) | \(Z\) |
| source normalized \(z\) | 只在 Hensel 小节局部使用 \(z\) |
| \(q\) 同时表示 lcm 与 source quotient | 全局 lcm 保留 \(q\)，source quotient 改为 \(q_Q\) |
| \(G\) 同时表示 gap / \(b_1b_2\) | 全局 \(G=b_1b_2\)，gap 改用 \(\mathcal G\) |
| \(N\) 的多个二平方范数 | 全局 \(\mathcal N_{12}\)，A2 去二后 \(\mathcal N_0\) |
| A1 saturated 的尾长 \(n\) | \(\ell=m_3-g\) |
| \(s=v_5(u)\) | \(\sigma_5\) |
| \(E=\lambda+s\) | \(E_5=\lambda+\sigma_5\) |

---
