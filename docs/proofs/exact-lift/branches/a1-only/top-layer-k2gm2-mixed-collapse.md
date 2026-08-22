# A1 top layer: `k=2g-2` mixed denominator collapse

> 日期：2026-08-22。
>
> 依赖：`top-layer-k2gm2-tail-center.md`、global `kappa` square、`decimal-height-synchronization.md`。
>
> 范围：
> \[
> d=2,\quad r=s=1,\quad g\ge5,\quad k=2g-2,
> \]
> 且
> \[
> L=2^a5^b,\qquad a,b>0.
> \]

状态：**已严格关闭全部 mixed shapes。**

---

## 1. local valuation table

令
\[
e=v_2(w).
\]
对 `g>=5`：
\[
v_2(N)=2e,
\qquad
v_2(K)=2g-4+2e,
\]
\[
v_5(N)=0,
\qquad
v_5(K)=2g-4.
\]
base depths 为
\[
v_2(10^gQG)=3g-4+e,
\qquad
v_5(10^gQG)=3g-4.
\]

mixed `L` 与 `(L,M)=1` 给
\[
v_2(\kappa)=3g-4+e+a,
\qquad
v_5(\kappa)=3g-4+b.
\tag{1}

phase gap 还统一给
\[
\boxed{L>H^2/4000.}
\tag{2}

---

## 2. generic high sides

### 2-side: `a>=4`

`kappa` square inner 两项的 2-depth 差为
\[
a-3.
\]
所以 `a>=4` 时第二项严格更浅：
\[
v_2(W^2)=8g-9+4e+a.
\]
square parity 强迫
\[
\boxed{a\text{ 为奇数},}
\qquad
\boxed{a>=5.}
\tag{3}

completion height 为
\[
\boxed{
H_2=2g+\frac{3a-5}{2}.
}
\tag{4}

### 5-side: `b>=3`

两项 5-depth 差为
\[
b-2.
\]
所以 `b>=3` 时第二项严格更浅：
\[
v_5(W^2)=8g-10+b.
\]
square parity 强迫
\[
\boxed{b\text{ 为偶数},}
\qquad
\boxed{b>=4.}
\tag{5}

completion height 为
\[
\boxed{
H_5=2g-3+\frac{3b}{2}.
}
\tag{6}

若同时 `a>=4,b>=3`，同步 (4)=(6) 给
\[
3(a-b)=-1,
\]
无整数解。因此 generic mixed-high 全空。

---

## 3. small `a` strips

### `a=1`

2-side square 的第一项比第二项浅两层。若 `W` 为整数平方根，两个 root numerators 的 exact 2-depth都为
\[
5g-6+3e,
\]
从而 reduced 2-height 是
\[
\boxed{H_2=2g-1.}
\tag{7}

若 `b>=3`，由 §2 实际 `b>=4`，于是
\[
H_5>=2g+3,
\]
不能同步。

### `a=2`

此时 square 第一项只浅一层。两个 root-numerator terms 在相同 2-depth 上都是 odd units，所以 `X_+`、`X_-` 都必须再多一个 2；但 exact conjugate product 的总 2-depth只允许其中总共多一层。矛盾。

故
\[
\boxed{a=2\Longrightarrow\text{empty}.}
\tag{8}

### `a=3`

square-inner 两项同深。unit cancellation 加 square parity 使额外深度至少为 2，root numerator 的另一项因此严格更深，得到
\[
\boxed{H_2=2g+2.}
\tag{9}

若 `b>=3`，则 `H5>=2g+3`，仍不可能同步。

所以所有 `b>=3` mixed states 已空。

---

## 4. small `b` strips

### `b=1`

5-side square 第一项比第二项浅一层。共轭 product 与 difference 给两个 5-denominator depths为
\[
\{2g-2,\ 2g-1\}.
\]
因此
\[
\boxed{H_5=2g-1.}
\tag{10}

若 `a>=4`，由 §2 实际 `a>=5`，故
\[
H_2>=2g+5.
\]
不能同步。

剩余 `a=1,2,3` 与 `b=1` 中：`a=2` 已由 (8) 排除；`a=1,3` 的 `L<=40`，与 (2) 矛盾。

### `b=2`

5-side square-inner 两项同深。unit cancellation 加 square parity使 extra depth至少 2，因此
\[
\boxed{H_5=2g.}
\tag{11}

若 `a>=4`，`H2>=2g+5`；若 `a=2` 已死；若 `a=1,3`，则 `L<=200`，仍与 (2) 矛盾。

### `b=3`

已进入 generic 5-high，但 (5) 要求 `b` 为偶数，所以直接不可能。

---

## 5. closure

以上穷尽全部 `a,b>0`。

所以
\[
\boxed{
 d=2,\quad r=s=1,\quad g>=5,\quad k=2g-2,
 \quad a,b>0
 \Longrightarrow\text{empty}.
}
\tag{12}

`g=3,4` 已由 full small-layer certificate 对全部 smooth `L` 整层关闭。
