# A1 top layer: `k=2g-1` pure-2 collapse

> 日期：2026-08-22。
>
> 依赖：`top-layer-minimal-offdiagonal-J-compression.md`、global `kappa` square、`decimal-height-synchronization.md`、`top-layer-k2gm1-pure5-collapse.md` 的同一 off-diagonal phase gap。
>
> 范围：
> \[
> d=2,\qquad r=s=1,\qquad g\ge2,\qquad k=2g-1,
> \qquad J\in\{0,\dots,9\}.
> \]

状态：**已严格关闭 pure-2 denominator branch**
\[
\boxed{L=2^a.}
\]

`g>=4` 解析关闭；`g=2,3` 已由 full small-layer global-terminal certificate 整层归零。

---

## 1. prefix 与 phase gap

令
\[
H:=10^g,
\qquad
\tau:=10^{g-1}=H/10,
\qquad
Q_0:=10b_1+1.
\]

沿用
\[
b_1=10^{4g-1}-w,
\qquad
Q=\tau Q_0,
\qquad
G=\tau b_1,
\qquad
D=H\tau Q_0.
\]

`J`-phase reduction 给
\[
\boxed{
0<(J+1)\tau-\rho<\frac{400}{H^2}.
}
\tag{1}

现在假设
\[
\boxed{L=2^a.}
\tag{2}

令
\[
A:=((J+1)\tau)L-M\in\mathbf Z_{>0}.
\]
由 (1)：
\[
\boxed{0<AH^2<400\,2^a.}
\tag{3}

仅由 `A>=1` 已有
\[
2^a>H^2/400.
\]
对 `g>=4` 特别说明 `a` 远大于所有 small-high resonance threshold；后文的更强界会直接给 `a>8g-11`。

---

## 2. `g>=4` 的 2-high completion height

以下假设
\[
\boxed{g\ge4.}
\]

记
\[
e:=v_2(w)\in\{0,1,2\}.
\]
显式 prefix 给
\[
\boxed{v_2(N)=2e,}
\qquad
\boxed{v_2(K)=2g-2+2e.}
\tag{4}

并且
\[
v_2(10^gQG)=3g-2+e.
\]
由 `L=2^a`：
\[
\boxed{v_2(\kappa)=3g-2+e+a.}
\tag{5}

因为 (3) 已使 `a>=3`，`kappa` square 内第二项严格更浅：
\[
v_2(\kappa K)=5g-4+3e+a,
\]
\[
v_2(2GD^2N)=5g-2+3e.
\]
故 square parity 强迫
\[
\boxed{a\text{ 为偶数}.}
\tag{6}

root numerator / denominator 的直接 valuation 给
\[
\boxed{
H_2=2g-1+\frac{3a}{2}.
}
\tag{7}

特别地
\[
H_2>2g-1.
\]

---

## 3. 5-side 只能落在唯一 low resonance

5-adic prefix 是统一的：
\[
v_5(G)=g-1,
\qquad
v_5(D)=2g-1,
\]
\[
\boxed{v_5(N)=0,}
\qquad
\boxed{v_5(K)=2g-2.}
\tag{8}

又 `L` 没有 5 因子，所以
\[
e_5:=v_5(\kappa)\le3g-2.
\]

若
\[
e_5<g-1,
\]
直接 valuation 给 reduced 5-denominator depth为 `0`。

若
\[
e_5>g-1,
\]
则 `kappa+G` 与 `kappa+2G` 都有 5-depth `g-1`；不论 root numerator 是否发生额外 cancellation，都有
\[
H_5\le e_5-g+1\le2g-1.
\]

这与 (7) 不可能同步。

所以唯一可能是
\[
\boxed{v_5(\kappa)=g-1.}
\tag{9}

base 5-depth 为 `3g-2`，故
\[
\boxed{v_5(M)=2g-1.}
\tag{10}

写
\[
\boxed{M=5^{2g-1}m,}
\qquad
(m,10)=1.
\tag{11}

且由 `M|10^gQG`：
\[
\boxed{m\mid b_1Q_0.}
\tag{12}

---

## 4. 5-adic resonance congruence

在 (9) 中，令
\[
c:=2^{2g-2+a}.
\]
从 `kappa+2G` 的 exact factorization：
\[
v_5(\kappa+2G)
=g-1+v_5(m+cQ_0).
\]

同一局部计算给两个共轭 normalized roots 的 5-denominator depths
\[
\{0,\ v_5(m+cQ_0)\}.
\]
因此 exact decimal-height synchronization 与 (7) 强迫
\[
\boxed{
v_5(m+2^{2g-2+a}Q_0)
=2g-1+\frac{3a}{2}.
}
\tag{13}

记
\[
R:=2g-1+\frac{3a}{2}.
\]
则
\[
\boxed{
m\equiv-2^{2g-2+a}Q_0\pmod{5^R}.}
\tag{14}

---

## 5. gap numerator 的精确 5-depth

写
\[
J+1=5^\nu j,
\qquad
\nu:=v_5(J+1)\in\{0,1\},
\qquad
5\nmid j.
\tag{15}

由 (11)：
\[
A
=(J+1)\tau2^a-5^{2g-1}m
=2^{a+g-1}5^{g-1+\nu}j-5^{2g-1}m.
\]

因为 `g>=4` 且 `nu<=1`，两项的 5-depth 不同，所以
\[
\boxed{v_5(A)=g-1+\nu.}
\tag{16}

写
\[
\boxed{A=5^{g-1+\nu}a_0,}
\qquad a_0\in\mathbf Z_{>0}.
\]
于是
\[
\boxed{
a_0
=2^{a+g-1}j-5^{g-\nu}m,
}
\tag{17}

特别地
\[
\boxed{0<a_0<2^{a+g-1}j.}
\tag{18}

---

## 6. phase gap 强迫 `a` 很大

由 (3),(16)：
\[
5^{g-1+\nu}H^2
\le AH^2
<400\,2^a.
\]
故
\[
2^a
>
\frac{2^{2g}5^{3g-1+\nu}}{400}.
\tag{19}

使用
\[
5>2^2,
\qquad
400<2^9,
\]
得到
\[
\boxed{
a>8g-11+2\nu.}
\tag{20}

对 `g>=4`：
\[
8g-11+2\nu>5g+\frac12.
\]
因此
\[
\boxed{2a>10g+1.}
\tag{21}

---

## 7. resonance 正代表与 gap 大小矛盾

把 (14) 代入 (17)：
\[
\boxed{
a_0\equiv B_0\pmod{5^{R+g-\nu}},}
\tag{22}

其中
\[
\boxed{
B_0
:=2^{a+g-1}j
+2^{a+2g-2}5^{g-\nu}Q_0.
}
\tag{23}

显然
\[
\boxed{B_0>2^{a+g-1}j>a_0.}
\tag{24}

下面证明 `B0` 本身仍小于模数。

第二项显然大于第一项（`g>=4,j<=9`），故
\[
B_0
<2^{a+2g-1}5^{g-\nu}Q_0.
\]
又
\[
Q_0=10^{4g}-(10w-1)<10^{4g},
\]
所以
\[
\boxed{
B_0<2^{a+6g-1}5^{5g-\nu}.
}
\tag{25}

另一方面
\[
5^{R+g-\nu}
=5^{3g-1-\nu+3a/2}.
\]
要由 (25) 得 `B0` 小于该模数，只需
\[
2^{a+6g-1}<5^{3a/2-2g-1}.
\tag{26}

由 `5>2^2`，右边严格大于
\[
2^{3a-4g-2}.
\]
而 (21) 正好给
\[
3a-4g-2>a+6g-1.
\]
因此 (26) 成立：
\[
\boxed{B_0<5^{R+g-\nu}.}
\tag{27}

现在 (18),(24),(27) 给
\[
0<a_0<B_0<5^{R+g-\nu},
\]
但 (22) 又要求 `a0` 与 `B0` 模该模数同余，矛盾。

所以
\[
\boxed{g>=4\Longrightarrow L=2^a\text{ empty}.}
\tag{28}

---

## 8. `g=2,3` 已由 full small-layer certificate 整层关闭

脚本

`scripts/exact-lift/a1-only/research-checks/top-layer/check_a1_k2gm1_small_layers_full_terminal.py`

不区分 prime shape，而是枚举全部
\[
L=2^a5^b,
\qquad (L,M)=1,
\]
满足 slope window 的 exact states，并检查 global `kappa` square 与完整 decimal recovery。

输出：
\[
\boxed{g=2:\ 236560\text{ terminal tests},}
\]
\[
\boxed{g=3:\ 277270\text{ terminal tests},}
\]
均有
\[
\boxed{0\text{ survivors}.}
\tag{29}

因此小层 pure-2 当然也为空。

---

## 9. closure

由 (28),(29)：
\[
\boxed{
 d=2,\quad r=s=1,\quad k=2g-1,\quad L=2^a
 \Longrightarrow\text{empty}.
}
\tag{30}

结合 `top-layer-k2gm1-pure5-collapse.md`，当前 `g>=4` 若还存在 `k=2g-1` candidate，只可能来自尚待单独审计的 mixed small-prime shapes。`g=2,3` 已由 (29) 整层关闭。
