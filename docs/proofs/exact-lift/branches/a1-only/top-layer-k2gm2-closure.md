# A1 top layer: complete `k=2g-2` boundary closure

> 日期：2026-08-22。
>
> 范围：
> \[
> d=2,\qquad r=s=1,\qquad g\ge3,\qquad k=2g-2.
> \]

状态：**严格关闭。**

---

## 1. real phase reduction

`top-layer-k2gm2-tail-center.md` 证明
\[
\boxed{0\le J\le108}
\]
以及
\[
\boxed{
0<(J+1)10^{g-2}-\rho<4000\,10^{-2g}.
}
\]

所以 normalized denominator 总满足整数超薄 gap
\[
\boxed{0<A_J10^{2g}<4000L.}
\]

---

## 2. small layers `g=3,4`

`check_a1_k2gm2_small_layers_full_terminal.py` 不区分 prime shape，直接枚举全部 smooth `L` 与 divisor `M`，检查 global `kappa` square 与完整 decimal recovery。

输出：
\[
\boxed{g=3:\ 5,408,362\text{ tests},}
\]
\[
\boxed{g=4:\ 9,450,518\text{ tests},}
\]
且 survivor 总数为
\[
\boxed0.
\]

---

## 3. large layers `g>=5`

全部
\[
L=2^a5^b
\]
被三类穷尽：

1. pure-2：由 `top-layer-k2gm2-pure2-collapse.md` 解析关闭；
2. pure-5：由 `top-layer-k2gm2-pure5-collapse.md` 关闭；
3. mixed：由 `top-layer-k2gm2-mixed-collapse.md` 的 parity / height mismatch关闭。

pure-5 的无因子分解 certificate 检查
\[
328308\text{ states}
\]
与
\[
23554\text{ exact gap-integer candidates},
\]
最终 divisor survivor 为 `0`。

---

## 4. theorem

因此
\[
\boxed{
 d=2,\quad r=s=1,\quad k=2g-2
 \Longrightarrow\text{empty}.
}

结合此前 `k=2g` 与 `k=2g-1` closure，当前最小双 surplus 的 outer wedge 已推进到
\[
\boxed{g<k\le2g-3.}
\]
