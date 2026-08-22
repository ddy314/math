# A1 top layer: `k=2g-2` pure-2 collapse

> 日期：2026-08-22。
>
> 依赖：`top-layer-k2gm2-tail-center.md`、global `kappa` square、`decimal-height-synchronization.md`。
>
> 范围：
> \[
> d=2,\quad r=s=1,\quad g\ge3,\quad k=2g-2,
> \quad J\in\{0,\dots,108\}.
> \]

状态：**已严格关闭 pure-2 branch**
\[
\boxed{L=2^a.}
\]

`g>=5` 解析关闭；`g=3,4` 已由 full small-layer global-terminal certificate 整层归零。

---

## 1. phase gap

令
\[
H=10^g,
\qquad
\tau=10^{g-2}=H/100.
\]
`top-layer-k2gm2-tail-center.md` 给
\[
\boxed{
0<(J+1)\tau-\rho<4000/H^2.
}
\tag{1}

假设
\[
L=2^a.
\]
令
\[
A:=((J+1)\tau)L-M>0.
\]
则
\[
\boxed{0<AH^2<4000\,2^a.}
\tag{2}

---

## 2. `g>=5` 的 high-2 side

以下取 `g>=5`。记
\[
e=v_2(w).
\]
显式 prefix 给
\[
v_2(N)=2e,
\qquad
v_2(K)=2g-4+2e,
\]
且 base 2-depth 为
\[
3g-4+e.
\]

由 (2)、`A>=1`，`2^a>H^2/4000`，所以 `a` 已远高于 small resonance threshold。于是
\[
v_2(\kappa)=3g-4+e+a
\]
落在 generic high branch。

`kappa` square 内第二项严格更浅，并给
\[
v_2(W^2)=8g-9+4e+a.
\]
因此 square parity 强迫
\[
\boxed{a\text{ 为奇数}.}
\]
特别地
\[
\boxed{a>=5\text{ odd}.}
\tag{3}

root numerator / denominator valuation 给
\[
\boxed{
H_2=2g+\frac{3a-5}{2}.
}
\tag{4}

---

## 3. 5-side 只能落到唯一 low resonance

5-adic prefix 满足
\[
v_5(N)=0,
\qquad
v_5(K)=2g-4,
\]
base 5-depth为
\[
3g-4.
\]

若 `v5(kappa)` 不等于 `g-2`，直接 local valuation 给
\[
H_5\le2g-2,
\]
无法追上 (4)。因此唯一可能是
\[
\boxed{v_5(\kappa)=g-2.}
\tag{5}

故
\[
\boxed{v_5(M)=2g-2.}
\tag{6}

写
\[
\boxed{M=5^{2g-2}m,}
\qquad (m,10)=1,
\qquad m\mid b_1Q_0.
\tag{7}

从 `kappa+2G` exact factorization得到
\[
v_5(\kappa+2G)
=g-2+v_5(m+2^{2g-3+a}Q_0).
\]
共轭 roots 的 5-denominator depths为
\[
\{0,\ v_5(m+2^{2g-3+a}Q_0)\}.
\]
因此 synchronization 与 (4) 强迫
\[
\boxed{
v_5(m+2^{2g-3+a}Q_0)
=2g+\frac{3a-5}{2}.
}
\tag{8}

记
\[
R:=2g+\frac{3a-5}{2}.
\]
则
\[
\boxed{
m\equiv-2^{2g-3+a}Q_0\pmod{5^R}.}
\tag{9}

---

## 4. gap numerator 的 exact 5-depth

写
\[
J+1=5^\nu j,
\qquad
\nu=v_5(J+1)\in\{0,1,2\},
\qquad 5\nmid j.
\tag{10}

由 (7)：
\[
A
=(J+1)\tau2^a-5^{2g-2}m
=2^{a+g-2}5^{g-2+\nu}j-5^{2g-2}m.
\]
因 `g>=5,nu<=2`，两项 5-depth 不同，所以
\[
\boxed{v_5(A)=g-2+\nu.}
\tag{11}

写
\[
A=5^{g-2+\nu}a_0.
\]
则
\[
\boxed{
a_0
=2^{a+g-2}j-5^{g-\nu}m,
}
\tag{12}
并且
\[
\boxed{0<a_0<2^{a+g-2}j.}
\tag{13}

---

## 5. phase gap forces `a` large

由 (2),(11)：
\[
5^{g-2+\nu}H^2<4000\,2^a.
\]
所以
\[
2^a>
\frac{2^{2g}5^{3g-2+\nu}}{4000}.
\]
使用
\[
5>2^2,
\qquad
4000<2^{12},
\]
得到
\[
\boxed{a>8g-16+2\nu.}
\tag{14}

对 `g>=5`：
\[
8g-16+2\nu>5g-\frac32.
\]
故
\[
\boxed{2a>10g-3.}
\tag{15}

---

## 6. positive representative contradiction

把 (9) 代入 (12)：
\[
\boxed{
a_0\equiv B_0\pmod{5^{R+g-\nu}},}
\tag{16}
其中
\[
\boxed{
B_0
:=2^{a+g-2}j
+2^{a+2g-3}5^{g-\nu}Q_0.
}
\tag{17}

显然
\[
B_0>2^{a+g-2}j>a_0.
\tag{18}

第二项大于第一项，所以
\[
B_0<2^{a+2g-2}5^{g-\nu}Q_0.
\]
而当前
\[
Q_0=10^{4g-2}-(10w-1)<10^{4g-2},
\]
因此
\[
\boxed{
B_0<2^{a+6g-4}5^{5g-2-\nu}.
}
\tag{19}

模数是
\[
5^{R+g-\nu}
=5^{3g-\nu+(3a-5)/2}.
\]
由 (19)，只需证明
\[
2^{a+6g-4}
<5^{(3a-4g-1)/2}.
\tag{20}

由 `5>2^2`，右边大于
\[
2^{3a-4g-1}.
\]
而 (15) 正给
\[
3a-4g-1>a+6g-4.
\]
所以 (20) 成立：
\[
\boxed{B_0<5^{R+g-\nu}.}
\tag{21}

现在
\[
0<a_0<B_0<5^{R+g-\nu},
\]
但 (16) 要求二者模该模数同余，矛盾。

因此
\[
\boxed{g>=5\Longrightarrow L=2^a\text{ empty}.}
\tag{22}

---

## 7. small layers

`g=3,4` 已由

`scripts/exact-lift/a1-only/research-checks/top-layer/check_a1_k2gm2_small_layers_full_terminal.py`

对全部 smooth `L` 做 global-terminal exact enumeration，survivor 均为 `0`。

所以小层 pure-2 也为空。

---

## 8. closure

综上
\[
\boxed{
 d=2,\quad r=s=1,\quad k=2g-2,\quad L=2^a
 \Longrightarrow\text{empty}.
}
