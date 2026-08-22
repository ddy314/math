# A1 minimal diagonal: top-edge 2-adic resonance certificate

> 日期：2026-08-22。
>
> 依赖：`deep-single5-topedge-finite-height.md`、`deep-single5-topedge-phase-shell.md`、`deep-single5-decimal-height-collapse.md`。
>
> 可复核脚本：
> `scripts/exact-lift/a1-only/research-checks/topedge-phase-resonance/check_topedge_2resonance.py`。

状态：**严格有限证书。** 本文关闭 single-5 top edge 中同时满足 `v5(N)>B` 与 phase 的两个 2-adic resonance classes；不声称 top edge 已整体关闭。

---

## 1. finite-height input

`deep-single5-topedge-finite-height.md` 已证明 top edge 只能满足

\[
32\le k\le k_{\max}(z,w),
\]

其中

\[
(k_{\max})=(77,75,74,72,74,73)
\]

按

\[
(z,w)=(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)
\]

排列。

另外 `deep-single5-topedge-supply-compression.md` 给严格整数上界

\[
B<2.293k+7.57.
\]

脚本使用等价整数条件

\[
1000B<2293k+7570.
\]

因此本证书检查的是一个先由定理严格推出的有限盒子。

---

## 2. 2-adic resonance classes

phase integer 写成

\[
A_{z,w}=
\begin{cases}
14N_0+(339-40w)T,&z=1,\\
12N_0+(237-20w)T,&z=3.
\end{cases}
\]

因为 `v2(T)=k` 且 T 项系数为奇数，唯一可能发生同-depth 2-adic resonance 的 prefix classes 是

\[
\boxed{z=1:\quad v_2(N_0)=k-1,}
\tag{1}
\]

\[
\boxed{z=3:\quad v_2(N_0)=k-2.}
\tag{2}
\]

写

\[
N_0=2^r m,
\qquad m\text{ odd},
\]

其中 `r=k-1` 或 `k-2`。

---

## 3. `v5(N)>B` 只有两个 Hensel roots

minimal diagonal prefix norm 为

\[
N=a_1^2+(a_2b_1)^2.
\]

对固定 `(k,z,w)`，写

\[
a_1=A_0+N_0,
\]

\[
A_0=100T^3+(10(5-z-w)+1)T-1,
\]

\[
C_0=(10T^2-z)(10T^2-w).
\]

于是

\[
\boxed{N=(A_0+N_0)^2+C_0^2.}
\tag{3}
\]

若 `v5(N)>B`，则

\[
N\equiv0\pmod{5^{B+1}}.
\]

因为 `-1` 在 `Z/5^m Z` 中恰有两个 simple square roots，所以令

\[
i^2\equiv-1\pmod{5^{B+1}},
\]

有且仅有两个 prefix residue classes：

\[
\boxed{
N_0\equiv-A_0\pm C_0i
\pmod{5^{B+1}}.
}
\tag{4}

将 (1) 或 (2) 的固定 2-power 除去，由于它与 `5^(B+1)` 互素，得到 `m` 的两个 residue classes。

而十进制窗口给：

- `z=1,r=k-1` 时
  \[
  m<2\cdot5^k;
  \]
- `z=3,r=k-2` 时
  \[
  m<4\cdot5^k.
  \]

另一方面 `B>=k+1`，所以

\[
5^{B+1}\ge25\cdot5^k.
\]

因此每个 Hensel root 在合法 `m` 区间中至多给一个整数候选。不存在隐藏的长 arithmetic progression。

---

## 4. exact scan 的第一阶段

脚本对 §1 的全部有限 `(z,w,k,B)`：

1. 纯整数 Hensel lift 两个 `i^2=-1 mod 5^(B+1)` roots；
2. 用 (4) 恢复两个 `m` residues；
3. 检查十进制窗口、`m` 奇性与 exact `v5(N)>B`。

完整结果：

\[
\boxed{33}
\]

个 Hensel/high-5 2-resonance states。

这里 `33` 是全部状态，不是抽样。

---

## 5. phase-residue 把 33 个状态全部排除

`deep-single5-topedge-phase-shell.md` 给

\[
E=5^{B-k}A_{z,w}-10\,2^k\gamma,
\qquad \gamma\in\mathbb Z,
\]

以及严格实窗口

\[
\boxed{0<E<30\,5^{B-k}.}
\tag{5}
\]

因此对固定 `(z,w,k,B,N0)`，`E` 必须同时满足

\[
\boxed{
E\equiv5^{B-k}A_{z,w}
\pmod{10\,2^k}
}
\tag{6}
\]

与 (5)。

脚本对 §4 的 33 个状态逐个计算 (6) 的最小正代表。结果：没有一个最小正代表落入 (5)。即

\[
\boxed{\text{phase-residue survivors}=0.}
\tag{7}

所以：

\[
\boxed{
\begin{gathered}
\lambda_2=2k-1,\quad v_5(N)>B,\\
z=1,\ v_2(N_0)=k-1
\end{gathered}
\Longrightarrow\text{empty},
}
\]

以及

\[
\boxed{
\begin{gathered}
\lambda_2=2k-1,\quad v_5(N)>B,\\
z=3,\ v_2(N_0)=k-2
\end{gathered}
\Longrightarrow\text{empty}.
}

这关闭的是 high-5 branch 中 phase 的两个 2-adic resonance classes；non-resonant high-5 与其他 5-adic allocation 仍须继续处理。