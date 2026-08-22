# A1 top layer: stable inner-wedge closure for `r=s=1`

> 日期：2026-08-22。
>
> 范围：
> \[
> d=2,\qquad r=s=1,
> \]
> 真正 off-diagonal 且
> \[
> \boxed{k-g\ge3.}
> \]

状态：**严格关闭。**

---

## 1. coordinates

令
\[
u:=2g-k.
\]
则
\[
g-u=k-g.
\]
所以当前范围正是
\[
\boxed{g-u\ge3.}
\]

`top-layer-inner-wedge-uniform-phase.md` 与 `top-layer-inner-wedge-digit-lock.md` 给统一 phase structure
\[
10^{u-1}<J+1\le10^u,
\]
\[
0<(J+1)10^{g-u}-\rho<40\,10^{u-2g}.
\]

---

## 2. denominator prime-shape exhaustion

任意 normalized denominator
\[
L=2^a5^b
\]
只有三类：

1. mixed: `a,b>0`；
2. pure-2: `b=0`；
3. pure-5: `a=0`。

它们分别由以下 theorem 严格关闭：

- `top-layer-inner-wedge-mixed-collapse.md`；
- `top-layer-inner-wedge-pure2-collapse.md`；
- `top-layer-inner-wedge-pure5-collapse.md`。

因此不存在任何 denominator shape。

---

## 3. theorem

所以
\[
\boxed{
 d=2,\quad r=s=1,\quad k-g\ge3
 \Longrightarrow\text{empty}.
}

结合此前：

- minimal diagonal `k=g` 已由 `minimal-diagonal-closure.md` 关闭；
- `k=2g`、`k=2g-1`、`k=2g-2` 已各自关闭；
- far region `k>=2g+1` 已关闭。

当前 `d=2,r=s=1` 的唯一尚未统一处理的 off-diagonal corridors 是
\[
\boxed{k=g+1}
\qquad\text{与}\qquad
\boxed{k=g+2}.
\]

这两条 corridor 的 `tau=10,100`，不满足 stable prefix 假设 `tau>=1000`，需要单独做 local valuation audit。
