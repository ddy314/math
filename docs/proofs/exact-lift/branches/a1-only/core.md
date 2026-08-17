# `A_1`-only 分支

本文件对应原总稿 §§28–31。它包含薄环约束、尾商斜率锁、saturated `L = 1` 支、denominator-only 尾长界和 saturated 支的奇素数约束。

> 迁移说明：以下 §§28–31 由原始总稿机械拆分；§§32–33 记录 2026-08-16 的 A1 独立重建与新证明树；§34 记录 2026-08-17 的 moving-prefix 继续压缩。

# 28. \(A_1\)-only 分支

\(A_1\)-only 满足

\[
s_3\le0,
\qquad
s_2+s_3>0.
\]

统一记

\[
\boxed{g=-s_3\ge0,}
\qquad
\boxed{k_{12}=s_2+s_3\ge1.}
\]

有效第三尾长为

\[
\boxed{\ell=m_3-g.}
\]

定义

\[
U=H-y_3,
\qquad
\mathcal S_{12}=y_1^2+y_2^2.
\]

经过第三块正规化，同样有

\[
\boxed{U=La,\qquad La\mid\mathcal S_{12}.}
\]

并且

\[
H=\frac12\left(La+\frac{\mathcal S_{12}}{La}\right),
\qquad
y_3=\frac12\left(\frac{\mathcal S_{12}}{La}-La\right).
\]

---

## 28.1 薄环约束

由第一坐标 carrier 及球面条件可得到 \(La\) 必须处在一个很薄的实数区间：

\[
\boxed{
10^{k_{12}}y_1-
\sqrt{(10^{2k_{12}}-1)y_1^2-y_2^2}
<La<\sqrt{\mathcal S_{12}}.
}
\]

---

## 28.2 尾商斜率锁

第三分母正规化进一步给出

\[
\boxed{10^{g-1}\le\frac{\tau}{L}<10^g.}
\]

---

# 29. \(A_1\) 的 saturated 支 \(L=1\)

真正特殊的是

\[
\boxed{L=1.}
\]

旧思路曾希望在这里继续 Gaussian descent，但严格检查发现：

\[
\boxed{L=1\text{ 时 Gaussian flip 只是 projective identity}.}
\]

所以 saturated 支必须采用独立机制。

---

# 30. \(A_1\) saturated 的 denominator-only 尾长界

旧基线给出

\[
\boxed{
\ell\le\left\lfloor\log_5((10Q+2)G)\right\rfloor
}
\]

以及粗化

\[
\boxed{\ell\le3(m_1+m_2)+1.}
\]

---

# 31. \(A_1\) saturated 的奇素数约束

令

\[
d_*=\gcd(\tau,10^gQ),
\qquad
h=\frac{\tau}{d_*}.
\]

旧基线记录

\[
\boxed{\gcd(U,h)=1,\qquad h\mid G,}
\]

并进一步限制 `h` 的奇素因子及其来源。

这些旧结论保留为迁移基线；涉及第三分子正规化的推导必须按 §33 的审计边界重新核验。

---

# 32. 2026-08-16 A1 独立重建入口

A1 现已增加一套直接从原始拼接恒等式重建、且不依赖 Gaussian flip 的证明链：

1. [`rational-contact.md`](rational-contact.md) 汇总直接重建、universal denominator funnel、resonance 和 cross-corridor 收缩：
   - 严格证明 \(\ell=n_3\)，得到 \(0\le g\le\min(s_2-1,s_1+1)\)，并建立
     \[
     R=\frac{P+\theta r_3}{1+\theta},
     \qquad
     \frac1{10Q}\le\theta<\frac1Q;
     \]
   - 推出 A1 universal rational-contact quadratic、判别平方和 saturated 支的整数平方证书；
   - 推出
     \[
     W^2=T^2K-2Tb_3DN,
     \qquad b_3\mid10^{2m_3}Q^2G;
     \]
   - 对 \(b_3=h2^u5^v\)、\(\gcd(h,10)=1\) 得到 \(h\mid Q^2G\)，并以 \(x=u-\ell,y=v-\ell\) 完成 resonance/cross-corridor 的 fixed-prefix finite 归约。

2. [`rational-contact.md`](rational-contact.md) 还保留 cross-corridor 的 universal factor-pair identity
   \[
   (TGC-W)(TGC+W)=TDN(TD+2b_3),
   \]
   以及使用 \(\gcd(a_3,b_3)=1\) 得到的两条交叉走廊上界；这部分只证明 fixed-prefix finite，不关闭 moving-prefix。

3. [`rational-contact.md`](rational-contact.md) 的最后一段
   - 重新接回整数球面；
   - 定义
     \[
     E=Cq-DH,\qquad U=H-y_3;
     \]
   - 严格推出
     \[
     10^\ell E=b_3U;
     \]
   - 若
     \[
     \delta=\gcd(10^\ell,b_3),\quad
     L=10^\ell/\delta,\quad
     \tau=b_3/\delta,
     \]
     则存在正整数 gap 参数 `A` 满足
     \[
     \boxed{U=LA,\qquad E=\tau A};
     \]
   - 从而安全恢复
     \[
     LA(H+y_3)=y_1^2+y_2^2.
     \]

---

# 33. 当前严格状态与审计边界

## 33.1 已严格完成

当前新框架已经证明：

\[
\boxed{
\text{对任意固定前两块 }(a_1,b_1,a_2,b_2),
\text{ A1 第三块候选集合有限。}
}
\]

更具体地，第三分母的非 `2,5` 部分由 `Q^2G` 控制，所有 `2/5` resonance、同向非 resonance、两条交叉非 resonance 都不能承载固定前缀下的无界尾族。

因此 A1 的研究核心已经从“第三尾是否无界”转移到“移动前缀本身是否可能”。

## 33.2 仍待证明

上面的 fixed-prefix finite theorem **不能**推出所有前缀的并集有限，也不能推出 A1 已全局为空。

剩余目标是：利用前缀对象

\[
C=a_1 10^{n_2}+a_2,
\quad
D=10^gQ,
\quad
G=b_1b_2,
\quad
N=(a_1b_2)^2+(a_2b_1)^2,
\]

以及

\[
K=G^2C^2-D^2N
\]

的 contact 必要条件，继续限制移动前缀，直到得到全局矛盾或真正 prefix-uniform 的有限盒。

## 33.3 旧统一正规化的审计警告

旧公共框架曾定义

\[
\delta=\gcd(10^\ell,b_3)
\]

后又使用类似 `a_3/\delta` 的第三分子整数化。由于原问题有

\[
\gcd(a_3,b_3)=1,
\]

而 `\delta\mid b_3`，故除 `\delta=1` 外不能无条件有 `\delta\mid a_3`。

因此当前 A1 主线只使用 §32 第 6 项中的安全 gap parameter `A`，不使用 `a_3/\delta` 作为整数 primitive numerator。

---

# 34. 2026-08-17 moving-prefix 继续压缩

2026-08-17 的继续工作已经把 A1 moving-prefix 从“泛型四层 + 两个低尺度角落”进一步压成一个无例外的全局四层系统，并开始关闭最高层 `d=2` 的边界自由度。

1. [`top-layer.md`](top-layer.md) 汇总 moving-prefix 四层压缩和最高层 endpoint kernel：
   - 新的统一无量纲结论：
     \[
     \boxed{R/(10^kr_1)>1/2};
     \]
   - 两个旧低尺度角落 `(g,k)=(0,1),(0,2)` 均被并入同一位数带；
   - 对整个 A1 无例外得到
     \[
     \boxed{s_1-g\in\{-1,0,1,2\}}.
     \]

   - 对最高层
     \[
     d:=s_1-g=2
     \]
     严格推出
     \[
     \boxed{m_1\ge2k};
     \]
   - 定义
     \[
     r=m_1-2k,\qquad s=m_2+g-k,
     \]
     得到 `r,s\ge0`；
   - 把四个大前缀整数压成端点 offset `(w,x,y,z)`；
   - 建立 compact determinant kernel；
   - 若 `g\ge1`，进一步有
     \[
     \boxed{r,s\ge1};
     \]
   - 若 `g=0`，至少 `(r,s)\ne(0,0)`。

   - 合并四个 offset 为两个正整数余量
     \[
     U_1=x+10^{g+1}w,
     \qquad
     U_2=z+10^{k+g+1}y;
     \]
   - 得到精确十进制中心分解
     \[
     \boxed{a_1=10^{g+1}b_1+U_1,}
     \qquad
     \boxed{a_2=10^{k+g+1}b_2-U_2};
     \]
   - 原既约性变成
     \[
     \boxed{(U_1,b_1)=(U_2,b_2)=1};
     \]
   - carrier determinant 精确化为
     \[
     \boxed{\Delta=10^kb_2U_1+b_1U_2}.
     \]

2. [`top-layer.md`](top-layer.md) 的 half-gap、positive-excess 和 minimal-surplus 章节继续给出：
   - 在 `d=2,g\ge1` 中，两个既约余量的总 carrier gap 被压入宽度 `17/500` 的半单位壳层：
     \[
     \boxed{
     \frac12
     <
     \frac{10^kU_1/b_1+U_2/b_2}{10^{g+1-k}}
     <
     \frac{267}{500};
     }
     \]
   - 最小第二 surplus `s=1` 时得到
     \[
     \boxed{y=0,\quad z\in\{1,3\}}.
     \]

   - 在最危险的 `r=s=1` 边界，进一步得到
     \[
     \boxed{
     (z,w)\in
     \{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\};
     }
     \]
   - 并有跨块绝对小差
     \[
     \boxed{a_2-b_1=w-z\in\{-2,-1,0,1,2,3\}}.
     \]

3. [`diagonal.md`](diagonal.md)
   - 澄清完整 contact 系统中
     \[
     \boxed{
     P^2-(1+2\theta)S
     =\bigl(r_3-\theta(R-r_3)\bigr)^2;
     }
     \]
   - 因而“判别平方”在完整 exact candidate 上是 contact + sphere 的整数化重写，不能重复当成独立方程；
   - 已有整数平方恒等式、赋值分层、denominator certificate 与 fixed-prefix finite 结论保持有效。

## 34.1 当前严格边界

截至本节，A1 仍未全局关闭。当前最小化后的 moving-prefix 结构为：

\[
\boxed{d=s_1-g\in\{-1,0,1,2\}.}
\]

其中最高层 `d=2` 已经进入 coprime-residue / half-gap kernel；`g\ge1` 的最小 surplus 边界 `r=s=1` 进一步只剩 6 个绝对类型。

下一阶段应：

- 继续关闭 `d=2` 的六类型边界与更高 `r,s`；
- 把 denominator prime graph 与 safe integer-gap identity 转写到 `(U_1,b_1;U_2,b_2)`；
- 随后对 `d=1,0,-1` 建立对应的 prefix kernel。

这些仍为 **待证**，不能把当前压缩误写为 A1 全局空性。
