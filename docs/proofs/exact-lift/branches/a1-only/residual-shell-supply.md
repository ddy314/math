# A1 minimal diagonal regular residual-shell supply

> 日期：2026-08-19。本文把 `boundary-decimal-supply.md` 从 `ell=k-1` 推广到任意 residual shell。
> 仍处于
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge6.
> \]

由 `positive-tail-residual.md`，定义

\[
N_0=j-10^k+1,
\qquad
 t=(N_0-\rho)10^\ell
=N_0 10^\ell-b_3\in\mathbf Z_{>0}.
\]

并有

\[
5.09\,10^{\ell-k}<t<50.45\,10^{\ell-k}.
\tag{1}
\]

本文证明：只要

\[
\boxed{
v_2(t)<\ell,
\qquad
v_5(t)<\ell,}
\tag{2}
\]

则令

\[
a_t=2^{v_2(t)}5^{v_5(t)},
\qquad
\widehat t=t/a_t,
\]

必有

\[
\boxed{b_3=a_t h,}
\tag{3}
\]

其中 `h` 属于 minimal-diagonal 的有限 odd-prime supply，并且

\[
\boxed{
\frac{10^\ell}{a_t}\mid h+\widehat t,
}
\tag{4}
\]

\[
\boxed{
N_0=\frac{a_t(h+\widehat t)}{10^\ell}.
}
\tag{5}
\]

因此每个满足 (2) 的 residual shell 都自动变成有限 divisor-congruence problem。

特别地，对全部 `k>=6` 的 `ell=k` shell，(1) 给

\[
\boxed{t\in\{6,7,\ldots,50\},}
\tag{6}
\]

而这些整数统一满足 (2)，所以 `ell=k` 整层都可以只枚举有限 `h` supply。

状态：**已严格完成。**

---

## 1. 赋值比较

由 residual 定义

\[
b_3=N_0 10^\ell-t.
\tag{7}
\]

第一项同时至少被

\[
2^\ell,
\qquad
5^\ell
\]

整除。

若 (2) 成立，则在 `p=2,5` 两个素数上，右侧两项赋值严格不同，因此低赋值项由 `t` 唯一承担：

\[
\boxed{v_2(b_3)=v_2(t),}
\tag{8}
\]

\[
\boxed{v_5(b_3)=v_5(t).}
\tag{9}
\]

所以提出完整 `2/5` 部分后

\[
b_3=a_t h,
\qquad \gcd(h,10)=1.
\]

这就是 (3)。

---

## 2. odd-prime supply 不随 `ell` 改变

minimal diagonal odd-prime theorem 已给出

\[
\boxed{h=q\,s,}
\]

其中

\[
q\mid Q,
\]

而 `s` 是 `b_1` 中 `1 mod4` odd prime-power blocks 的 whole-block selector。

因此对固定 `(k,w)`，可能的 `h` 始终属于同一个有限集合

\[
\mathcal H_{k,w},
\]

与 `ell,t,N_0` 无关。

---

## 3. 任意 regular shell 的十进制同余

写

\[
t=a_t\widehat t.
\]

把 (3) 代入 (7)：

\[
a_t h=N_0 10^\ell-a_t\widehat t.
\]

所以

\[
a_t(h+\widehat t)=N_0 10^\ell.
\]

因为 `a_t|10^ell`，得到

\[
\boxed{
\frac{10^\ell}{a_t}\mid h+\widehat t.
}
\]

并唯一恢复

\[
\boxed{
N_0=\frac{a_t(h+\widehat t)}{10^\ell}.
}
\]

这说明：对 regular residual，搜索变量应为 `(h,t)`，而不应扫描 `N_0` 或 `(x,y)`。

---

## 4. `ell=k` 自动全部 regular

取

\[
\ell=k.
\]

由 (1)：

\[
5.09<t<50.45,
\]

所以

\[
6\le t\le50.
\]

在该区间中

\[
v_2(t)\le5,
\qquad
v_5(t)\le2.
\]

而当前

\[
k=\ell\ge6.
\]

故

\[
v_2(t),v_5(t)<\ell
\]

对全部 `t=6,...,50` 自动成立。

所以

\[
\boxed{
\ell=k\text{ shell 完全属于 regular divisor-congruence regime.}
}
\tag{10}
\]

---

## 5. 后续 shell 的 exceptional residual

当 `ell-k` 增大时，(1) 中的 `t` 窗也按十倍增长；此时可能出现

\[
v_2(t)\ge\ell
\quad\text{或}\quad
v_5(t)\ge\ell.
\]

这些 residual 不能直接使用 (8)–(9)，因为 `N_0 10^ell` 与 `t` 可能在相同或更深的 `2/5` 层发生 cancellation。

因此长尾自然分成：

1. **regular residuals**：满足 (2)，直接使用有限 `h` congruence；
2. **deep-2/5 residuals**：至少一个赋值达到 `ell`，需要单独做 resonance/cancellation 分析。

这给 `ell>=k` 的 genuinely-long tail 一个新的、比旧 `(x,y)` 平面更细的分层。