# A1 top layer: complete `k=2g-1` boundary closure

> 日期：2026-08-22。
>
> 范围：
> \[
> d=2,\qquad r=s=1,\qquad g\ge2,\qquad k=2g-1.
> \]

状态：**严格关闭。**

---

## 1. moving prefix 已有限化

`top-layer-minimal-offdiagonal-J-compression.md` 给
\[
\boxed{J\in\{0,1,\dots,9\}.}
\]
并且 positive-excess identity进一步给超薄 third-tail gap
\[
\boxed{
0<(J+1)10^{g-1}-\rho<400\,10^{-2g}.
}
\]

---

## 2. `g=2,3`：full global-terminal certificate

`scripts/exact-lift/a1-only/research-checks/top-layer/check_a1_k2gm1_small_layers_full_terminal.py`

直接枚举全部 `2/5`-smooth `L` 与全部 divisor `M`，不使用 prime-shape reduction。

输出：
\[
\boxed{g=2:\ 236560\text{ tests},}
\]
\[
\boxed{g=3:\ 277270\text{ tests},}
\]
且 survivor 总数为
\[
\boxed0.
\]

所以小层完整为空。

---

## 3. `g>=4`：prime shapes 穷尽

对 `g>=4`，任意
\[
L=2^a5^b
\]
只有三类：

1. pure-2 `b=0`；
2. pure-5 `a=0`；
3. mixed `a,b>0`。

它们分别由：

- `top-layer-k2gm1-pure2-collapse.md`；
- `top-layer-k2gm1-pure5-collapse.md`；
- `top-layer-k2gm1-mixed-collapse.md`

严格关闭。

其中 pure-5 的大层 certificate

`scripts/exact-lift/a1-only/research-checks/top-layer/check_a1_k2gm1_pure5_phase_divisor_certificate.py`

在无因子分解的 finite box 中检查
\[
12420\text{ states}
\]
与
\[
1457\text{ exact gap-integer candidates},
\]
最终 divisor survivor 为 `0`。

pure-2 则由 phase-gap lower bound 与唯一 5-adic resonance 的正代表大小矛盾解析关闭；mixed shapes 由 local square parity 与 decimal-height mismatch 关闭。

---

## 4. theorem

因此对所有真正 off-diagonal 的 `g>=2`：
\[
\boxed{
 d=2,\quad r=s=1,\quad k=2g-1
 \Longrightarrow\text{empty}.
}

结合此前：

- minimal diagonal `k=g` 已关闭；
- far region `k>=2g+1` 已关闭；
- boundary `k=2g` 已关闭；

当前最小双 surplus `r=s=1` 只剩更内层窄楔
\[
\boxed{g<k\le2g-2.}
\]

下一层首先是
\[
\boxed{k=2g-2,}
\]
此时 `J` compression 给
\[
\boxed{0\le J\le108.}
\]
