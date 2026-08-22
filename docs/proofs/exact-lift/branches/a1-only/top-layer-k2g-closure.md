# A1 top layer: complete closure of the `k=2g` boundary

> 日期：2026-08-22。
>
> 范围：
> \[
> d=2,\qquad r=s=1,\qquad g\ge1,\qquad k=2g.
> \]

状态：**严格关闭。** 本文件只做 sector bookkeeping，不引入新局部引理。

`top-layer-minimal-offdiagonal-J-compression.md` 首先给
\[
\boxed{J=0.}
\]

随后：

1. `top-layer-k2g-gap-smallL-collapse.md` 用 primitive reducedness 把六类型压到 `(z,w)=(1,1),(1,3)`，并由 ultrathin gap 排除 `L=1,2`；
2. `top-layer-k2g-prime-shape-collapse.md` 排除 mixed-high、`L=2\cdot5^b` 与 pure-2 `L=2^a`，把唯一剩余 prime shape 压成
   \[
   L=5^b,\qquad b\ge2\text{ even};
   \]
3. `top-layer-k2g-pure5-real-phase-shell.md` 把 pure-5 tail 压进显式宽 `3/5` phase shell；
4. `top-layer-k2g-pure5-finite-collapse.md` 用 resultant finite-height reduction 与 exact phase/divisor certificate 关闭全部 pure-5 states。

因此所有 `L=2^a5^b` prime shapes 都已穷尽并排除，得到
\[
\boxed{
 d=2,\quad r=s=1,\quad k=2g
 \Longrightarrow\text{empty}.
}
