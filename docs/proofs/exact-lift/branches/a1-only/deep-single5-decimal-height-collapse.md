# A1 minimal diagonal: corrected single-5 reduction by decimal-height synchronization

> 日期：2026-08-22。
>
> 依赖：`deep-denominator-ledger.md`、`global-squarefree-terminal.md`、`decimal-height-synchronization.md`。
>
> 范围：minimal diagonal，`k=g>=32`，single-5 deep sector
> \[
> D_{\rm gap}=5^B,
> \qquad B>k.
> \]

状态：**已严格完成 reduction。** 本版替换此前把 `d_2=B+k` 过早写死的版本。正确结论是：低 `lambda_2` 只剩一个 fixed cell；顶部只剩 `lambda_2=2k-1` 的 exact sign-allocation terminal。single-5 尚未完全为空。

---

## 1. 正确的 decimal-height equation

写

\[
T=10^k,
\qquad
\lambda=2^{\lambda_2},
\qquad
\lambda_2=k+x\ge0.
\]

single-5 gap identity 为

\[
5^BT\rho=h2^{\lambda_2},
\qquad(h,10)=1.
\tag{1}
\]

把

\[
\rho=M/L,
\qquad(L,M)=1
\]

约到最低项：

\[
\boxed{\ell_5:=v_5(L)=B+k,}
\tag{2}
\]

\[
\boxed{\ell_2:=v_2(L)=(k-\lambda_2)_+.}
\tag{3}
\]

所以

\[
\ell_5>\ell_2.
\]

令形式根

\[
x_\sigma=u/v
\]

为最简分数，并记

\[
d_p=v_p(v),
\qquad p=2,5.
\]

`decimal-height-synchronization.md` 的正确条件是

\[
\boxed{
\max(d_2,\ell_2)=\max(d_5,\ell_5)=:n.
}
\tag{4}
\]

因为 `ell_5>ell_2`，(4) 首先给

\[
\boxed{d_2=n\ge B+k.}
\tag{5}
\]

但不能无条件把 `n` 写成 `B+k`：若 `d_5>B+k`，两个 completion heights 可以一起升高。后文始终使用 (4)-(5)。

---

## 2. `kappa` 的局部赋值

令 supply complement

\[
M_c:=QG/h.
\]

由 (1) 与全局 tail weight 得

\[
\boxed{
\kappa
=\frac{5^BT^2M_c}{2^{\lambda_2}}.
}
\tag{6}

minimal diagonal 中

\[
e:=v_2(w)=v_2(G)\in\{0,1,2\},
\]

且 `Q,h` 为奇数，所以

\[
v_2(M_c)=e.
\]

因此

\[
\boxed{a:=v_2(\kappa)=2k+e-\lambda_2\ge0,}
\tag{7}
\]

故

\[
\boxed{\lambda_2\le2k+e.}
\tag{8}

5-adic 一侧则有

\[
\boxed{a_5:=v_5(\kappa)=B+2k.}
\tag{9}

同一 prefix 满足

\[
v_2(C)=0,
\qquad
v_2(K)=2e,
\qquad
v_2(D_c)=k,
\tag{10}
\]

其中 `D_c=TQ`，并记

\[
n_2=v_2(N)\in\{0,1\},
\qquad
n_5=v_5(N)\ge0.
\]

`w` 偶时 `n_2=0`。

---

## 3. 5-adic denominator allocation

全局 square 为

\[
W^2
=\kappa^2G^2C^2
-\kappa D_c^2N(\kappa+2G),
\tag{11}
\]

归一化根为

\[
x_\sigma
=\frac{X_\sigma}{Y},
\]

\[
X_\sigma
=\kappa G^2C+\sigma(\kappa+G)W,
\qquad
Y=\kappa^2(\kappa+2G).
\tag{12}
\]

在 5-adic 中 `G,C,Q` 都为单位，并且

\[
v_5(\kappa+G)=v_5(\kappa+2G)=0.
\]

### 3.1 `n_5<B`

(11) 中第二项严格更浅，故

\[
v_5(W)=2k+\frac{B+n_5}{2}<a_5.
\]

两个 signs 都无 cancellation，得到

\[
\boxed{
 d_5
=2k+\frac{3B-n_5}{2}.
}
\tag{13}

特别地

\[
d_5>B+k.
\tag{14}
\]

所以若这一 branch 真能恢复 decimal block，(4) 必须满足

\[
\boxed{d_2=d_5.}
\tag{15}

### 3.2 `n_5>B`

此时

\[
v_5(W)=a_5.
\]

两个共轭 signs 中：

- 一个保持完整 depth
  \[
  \boxed{d_5^{\rm full}=a_5=B+2k;}
  \tag{16}
  \]
- 另一个是 matching sign。若 `r=n_5-B<a_5`，则
  \[
  \boxed{
  d_5^{\rm match}=a_5-r
  =2B+2k-n_5;
  }
  \tag{17}
  \]
  若 `r>=a_5`，则 matching depth 只会进一步下降，统一可写为
  \[
  \boxed{
  d_5^{\rm match}
  =\max(0,2B+2k-n_5).
  }
  \tag{18}

因此 matching sign 的 required decimal height 是

\[
\boxed{
 n_{\rm match}
 =\max(B+k,d_5^{\rm match}).
}
\tag{19}

特别地

\[
n_5\ge B+k
\Longrightarrow
n_{\rm match}=B+k.
\tag{20}

### 3.3 resonance `n_5=B`

这里两项同深。无需猜测 cancellation：直接使用两个 root numerators 的乘积。

由 (12) 与 (11) 可化简

\[
X_+X_-
=-\kappa(\kappa+2G)
\left(
\kappa^2G^2C^2
-D_c^2N(\kappa+G)^2
\right).
\tag{21}

在 `n_5=B` 时：

- `v_5(kappa)=a_5`；
- `v_5(kappa+2G)=0`；
- (21) 中括号的第二项严格承担较浅 valuation `a_5`。

所以

\[
v_5(X_+X_-)=2a_5.
\]

另一方面 (12) 的两个 summands 都至少有 valuation `a_5`，故

\[
v_5(X_+),v_5(X_-)\ge a_5.
\]

两者之和恰为 `2a_5`，于是

\[
\boxed{
v_5(X_+)=v_5(X_-)=a_5.}
\]

因此 resonance 的两个 signs 都满足

\[
\boxed{d_5=a_5=B+2k.}
\tag{22}

若 resonance 恢复 decimal block，必须有

\[
\boxed{d_2=B+2k.}
\tag{23}

---

## 4. 2-adic low region `lambda_2<=2k-2`

此时

\[
a\ge e+2,
\]

所以

\[
v_2(\kappa+G)=e,
\qquad
v_2(\kappa+2G)=e+1.
\tag{24}

令

\[
E=v_2(\kappa K)=a+2e,
\qquad
F=v_2(2GD_c^2N)=2k+e+1+n_2.
\]

则

\[
E-F=2e-\lambda_2-1-n_2.
\tag{25}

### 4.1 `E<F`

此时

\[
v_2(W)=a+e.
\]

(12) 中两个 summands 除去 `2^{a+2e}` 后都是奇数。因此两个 signs 的和/差都至少再多一个 2：

\[
v_2(X_\sigma)\ge a+2e+1.
\]

raw denominator 有

\[
v_2(Y)=2a+e+1,
\]

所以

\[
\boxed{d_2\le2k-\lambda_2\le2k.}
\tag{26}

但 (5) 要求

\[
d_2\ge B+k>2k.
\]

矛盾。因此

\[
\boxed{E<F\text{ 全部为空}.}
\tag{27}

### 4.2 `E=F`

这里

\[
\lambda_2=2e-1-n_2.
\]

两边除去公共 2-power 后都是 odd units，因此 inner difference 至少多一个 2；平方 parity 又强迫 cancellation depth 为偶数，故实际至少多两个 2。于是 `W` term 比 `kappa G^2C` 更深，得到

\[
\boxed{d_2=2k-\lambda_2+1.}
\tag{28}

由 `d_2>=B+k>=2k+1` 只能有 `lambda_2=0`。但 resonance equation

\[
0=2e-1-n_2
\]

在六个 minimal-diagonal 类型中没有解：

- `e=0` 时右侧为负；
- `e=1,2` 时 `w` 偶，故 `n_2=0`，右侧分别为 `1,3`。

所以

\[
\boxed{E=F\text{ 全部为空}.}
\tag{29}

### 4.3 `E>F`

平方 parity 给

\[
\lambda_2\equiv1+n_2\pmod2,
\]

且较浅的 `W` term 唯一承担 numerator valuation，得到 exact

\[
\boxed{
 d_2
=2k+e+rac{1-n_2-3\lambda_2}{2}.
}
\tag{30}

因为 `E>F` 要求

\[
\lambda_2<2e-1-n_2,
\]

只需检查绝对小的 `e<=2,n_2<=1`：

- `e=0`：无此 branch；
- `e=1,n_2=0`：只可能 `lambda_2=0`，但 square parity 要求 `lambda_2` 奇，排除；
- `e=2,n_2=0`：只剩 `lambda_2=1`，并有
  \[
  d_2=2k+1.
  \]

由 (5) 强迫

\[
B=k+1.
\]

所以 low `lambda_2` 区唯一 survivor 是

\[
\boxed{
(z,w)=(1,4),
\quad\lambda_2=1,
\quad B=k+1.
}
\tag{31}

此时 `d_2=2k+1=B+k`，故 (4) 进一步要求

\[
d_5\le2k+1.
\]

由 §3：

- `n_5<B` 时 (13) 远大于 `2k+1`，排除；
- `n_5=B` 时 (22) 给 `d_5=3k+1`，排除；
- `n_5>B` 时只有 matching sign 可能，且 (18)-(20) 给必要条件
  \[
  \boxed{n_5\ge B+k=2k+1.}
  \]

因此唯一 low-edge cell 是

\[
\boxed{
(z,w)=(1,4),
\quad\lambda_2=1,
\quad B=k+1,
\quad v_5(N)\ge2k+1,
}
\tag{32}

并且只能使用 5-adic matching sign。

---

## 5. 2-adic top edge `lambda_2=2k-1`

现在

\[
a=e+1.
\]

写

\[
\kappa=2^{e+1}\kappa_0,
\qquad
G=2^eg,
\]

其中 `kappa_0,g` 为奇数，并定义

\[
\boxed{t_2:=v_2(\kappa+2G).}
\tag{33}

因为

\[
\kappa+2G=2^{e+1}(\kappa_0+g),
\]

有 `t_2>=e+2`。

从 (11) 得

\[
\boxed{v_2(W)=2e+1.}
\tag{34}

于是 (12) 的两个 summands 都恰从 `2^{3e+1}` 开始，故

\[
v_2(X_\sigma)\ge3e+2.
\]

为了精确分配两个 signs，再使用乘积恒等式 (21)。在 2-adic 中，(21) 括号第一项严格承担较浅 valuation

\[
4e+2.
\]

因此

\[
\boxed{
v_2(X_+X_-)=t_2+5e+3.}
\tag{35}

另一方面

\[
X_+-X_-=2(\kappa+G)W
\]

恰有 valuation

\[
\boxed{v_2(X_+-X_-)=3e+2.}
\tag{36}

由 (35)-(36)，两个 signs 的 valuations 不能相同，且精确为

\[
\boxed{
\{v_2(X_+),v_2(X_-)\}
=
\{3e+2,\ t_2+2e+1\}.
}
\tag{37}

raw denominator depth 是

\[
v_2(Y)=t_2+2e+2.
\]

所以两个 reduced 2-denominator depths 精确为

\[
\boxed{
\{d_2^{(+)},d_2^{(-)}\}
=
\{1,\ t_2-e\}.
}
\tag{38}

因为任何合法 single-5 block 都需要 `d_2>=B+k>1`，只有 high-denominator sign 可能存活，并且它必须满足

\[
\boxed{
 t_2-e
=
\max(B+k,d_5^{\rm high-sign}).
}
\tag{39}

这里 `d_5^{high-sign}` 由 §3 按该同一 sign 的 5-adic orientation 读取。于是 top-edge 已成为一个 exact sign-allocation terminal，而不是此前错误的固定 `B+k` equation。

---

## 6. `lambda_2>=2k` 全空

若 `lambda_2>=2k`，则

\[
a=2k+e-\lambda_2\le e.
\]

此时 `kappa` 在 2-adic 上不比 `G` 更深，`kappa+2G` 的 valuation 至多绝对常数级，raw denominator

\[
\kappa^2(\kappa+2G)
\]

的 2-depth 至多 `3e<=6`（`lambda_2=2k` 时直接由 `v_2(kappa)=e<v_2(2G)=e+1` 得到；更大的 `lambda_2` 只会更浅）。

所以

\[
d_2\le6<B+k
\]

对 `k>=32` 矛盾。故

\[
\boxed{\lambda_2\ge2k\Longrightarrow\text{empty}.}
\tag{40}

---

## 7. corrected single-5 frontier

整个 minimal-diagonal single-5 deep sector 现在严格只剩两类：

### Low-edge cell

\[
\boxed{
(z,w)=(1,4),
\quad\lambda_2=1,
\quad B=k+1,
\quad v_5(N)\ge2k+1,
}
\tag{41}

且只能使用 5-adic matching sign。

### Top-edge sign-allocation cell

\[
\boxed{\lambda_2=2k-1,}
\tag{42}

且两个 2-adic signs 中只有 depth `t_2-e` 的一个能存活，并满足 exact equation (39)。

所有其余 `lambda_2`、strict-low 以及 5-adic resonance 都已经排除。

下一步：

1. 对 low-edge `(1,4)` 使用
   \[
   N\equiv(10^k+N_0-1)^2+16\pmod{5^{2k+1}}
   \]
   把 `v_5(N)>=2k+1` 压成每层两个 Hensel residues；
2. 对 top-edge 把 (39) 与 supply complement `h=qs`、`M_c=(Q/q)(b_1/s)` 联用，做 exact 2-adic divisor congruence。
