# A2 pure-spontaneous / descendant common branch 的 canonical defect residue

> **依赖：** `spontaneous-prefix-branch-audit.md`、`spontaneous-sphere-roots.md`、`spontaneous-crt-height-primitive-remainder.md`。
>
> **严格状态：**genuine alpha-free noncentral spontaneous common prime精确选择 `Q_1,Q_2` 中一个 branch；相应 third numerator由显式 sphere root `z_i(x,y)` 唯一恢复。本文把该 branch root代入 descended quotient，证明 top finite defect `delta=C/D` 也随之被唯一恢复。两 branch要求的 real defect都严格为负，而真实 endpoint defect严格为正，因此所有 pure-spontaneous/descendant common roots都必须依赖 p-adic wrapping。本文减少一个 local coordinate，但不排除 modular wrapping，因此不关闭 A2。

---

## 1. unique pure-spontaneous branch

沿用

\[
\tau=10^{-M},
\qquad
x=B/N,
\qquad
y=10A/N,
\]
并记

\[
\boxed{s:=9+y.}
\tag{1.1}

在 genuine pure-spontaneous noncentral sector：

\[
p\nmid\alpha(2K-9),
\]
且排除既有 source/denominator/prefix boundaries。

`spontaneous-prefix-branch-audit.md` 已证明此时恰有唯一

\[
i\in\{1,2\}
\]
满足

\[
\boxed{\mathcal Q_i(\tau;x,y)\equiv0\pmod p.}
\tag{1.2}

`spontaneous-sphere-roots.md` 把两支恢复成显式 normalized third numerator

\[
\boxed{
\bar\zeta=z_i(x,y),}
\tag{1.3}

其中

\[
\bar\zeta:=\frac{a_3}{TN}.
\]

所以在该 branch：

\[
\boxed{
K=\frac{s}{\tau},
\qquad
\zeta:=\frac{a_3}{T}=\frac{z_i}{\tau}.}
\tag{1.4}

---

## 2. universal descendant defect equation

fully primitive descended quotient可写成

\[
\widehat{\mathscr D}_{63}=c_u^2\mathscr F_{63},
\]

\[
\mathscr F_{63}
=(2K-9)\{g((2K-9)T-a_3)-H_0\}
-\frac{63}{16}gTK^2.
\tag{2.1}

finite-defect height identity为

\[
\boxed{
\frac{H_0}{gT}
=3+\zeta-\delta,
\qquad
\delta:=C/D.}
\tag{2.2}

所以除以 positive/genuine unit `gT`：

\[
\frac{\mathscr F_{63}}{gT}
=(2K-9)(2K-12-2\zeta+\delta)
-\frac{63}{16}K^2.
\tag{2.3}

若 prime进入 descendant common support，`F63=0 mod p`。在 noncentral sector `2K-9` 为 unit，故

\[
\boxed{
\delta
\equiv
12+2\zeta-2K
+\frac{63K^2}{16(2K-9)}
\pmod p.}
\tag{2.4}

因此 descendant condition本身已唯一固定 top defect first digit。

---

## 3. substitute the unique sphere branch

代入 (1.4)：

\[
\delta_i
=
12+rac{2z_i-2s}{\tau}
+rac{63s^2}{16\tau(2s-9\tau)}.
\]

统一清成一个分式：

\[
\boxed{
\delta_i
\equiv
\frac{
-s^2+672s\tau+64sz_i
-1728\tau^2-288\tau z_i
}
{16\tau(2s-9\tau)}
\pmod p.}
\tag{3.1}

所以两个 quadratic branches不再携带一个额外独立的 finite-defect parameter：

\[
\boxed{
(x,y,\tau,i)
\Longrightarrow
z_i
\Longrightarrow
\delta_i\pmod p}
\tag{3.2}

是 canonical chain。

这与 omega-content branch的 defect map同型，但此处不使用 `alpha=0` 或 source triangle。

---

## 4. both real branch defects are strictly negative

真实 dangerous endpoint满足

\[
\frac{249}{250}<y<1,
\qquad
s=9+y>\frac{2499}{250},
\]

\[
0<\tau\le10^{-11}.
\]

`spontaneous-sphere-roots.md` 已证明两支都满足

\[
\boxed{z_i<-4.778.}
\tag{4.1}

分母

\[
16\tau(2s-9\tau)>0.
\]

看 numerator

\[
N_i
=-s^2+672s\tau
+z_i(64s-288\tau)
-1728\tau^2.
\tag{4.2}

这里

\[
64s-288\tau
>64\frac{2499}{250}-288\cdot10^{-11}>639,
\]
所以由 `z_i<-4.778`：

\[
z_i(64s-288\tau)<-4.778\cdot639<-3052.
\]

而唯一正项满足

\[
672s\tau<6720\cdot10^{-11}<10^{-7}.
\]

其余两项 `-s^2,-1728tau^2` 非正。因此

\[
\boxed{N_i<0.}
\tag{4.3}

故两支 required real defect均满足

\[
\boxed{\delta_i<0.}
\tag{4.4}

---

## 5. opposite to the actual finite-defect endpoint

真实 rational-root state为

\[
J_{def}=3-C/D
\]
且 endpoint shell已给

\[
\boxed{0<\delta=C/D<3/250.}
\tag{5.1}

与 (4.4) 比较：

\[
\boxed{
\delta_{actual}>0,
\qquad
\delta_i^{real}<0
\quad(i=1,2).}
\tag{5.2}

所以不存在 real-nearby pure-spontaneous/descendant intersection。任何 modular common prime都必须让 branch root跨过一个固定符号间隔，通过 genuine p-adic wrapping匹配真实 positive defect。

这不是单独的矛盾：模 p 的同余不要求实数接近。它的严格新增作用是把 descendant common branch从

\[
\text{prefix branch}+\text{free }C/D
\]
压成

\[
\boxed{\text{prefix branch}+\text{canonical }C/D\text{ residue}.}
\tag{5.3}

---

## 6. revised pure-spontaneous external kernel

在 alpha-free、noncentral、source/denominator-separated sector，真正 remaining descendant common prime现在必须同时满足：

1. 唯一 `Q_i` decimal branch；
2. sphere root `z_i(x,y)`；
3. canonical defect residue (3.1);
4. actual decimal orbit `tau=10^{-M}`。

所以 local freedom只剩 prefix decimal orbit本身；third numerator与 finite defect都已被 branch唯一恢复。

下一步最自然的是把 (3.1) 与 `C` 的 centered Hensel representative `(z_E,chi_E)` 联立，或清分母得到 branch-specific natural integer并对其 required p-depth做 height comparison。ordinary discriminant stacking仍不会新增 obstruction。

A2 仍为 `待证`。
