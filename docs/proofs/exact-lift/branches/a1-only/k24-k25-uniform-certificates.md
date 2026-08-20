# A1 minimal diagonal: uniform certificates for `k=24,25`

> 日期：2026-08-19。本文继续 `uniform-layer-finite-box.md`。

固定层统一证书继续关闭

\[
\boxed{k=g=24,25.}
\]

因此结合此前 `k=1,...,23`：

\[
\boxed{
1\le k=g\le25
\Longrightarrow
\text{minimal diagonal empty}.
}
\tag{1}
\]

状态：**已由 exact integer/rational certificate 严格复核。**

---

## 1. `k=24`

完整 odd-prime supply 数量按 `w=1,2,3,4` 为

\[
\boxed{(256,256,32,64).}
\]

5-adic/root-lifting 与 2-adic floor 给出

\[
\underline x_*=-26,
\qquad
\underline y_*=-59.
\]

cross-corridor + decade 推出的 theorem-derived exponent box 为

\[
\boxed{
-298\le x\le216,
\qquad
-114\le y\le45.
}
\]

完整 decade state 数为

\[
\boxed{188712.}
\]

在旧的更宽窗口

\[
5.09<10^{24}(\lceil\rho\rceil-\rho)<50.45
\]

中命中数为

\[
\boxed{0.}
\]

因此当然也没有状态落入新 sharpened window

\[
15.09<10^{24}(\lceil\rho\rceil-\rho)<39.003.
\]

---

## 2. `k=25`

完整 odd-prime supply 数量为

\[
\boxed{(2048,48,16,512).}
\]

valuation floors：

\[
\underline x_*=-27,
\qquad
\underline y_*=-61.
\]

exponent box：

\[
\boxed{
-316\le x\le224,
\qquad
-122\le y\le47.
}
\]

完整 decade state 数为

\[
\boxed{796197.}
\]

同样在旧宽窗口中

\[
\boxed{\text{gap hits}=0.}
\]

所以 `k=g=25` 为空。

---

## 3. 新前沿

当前 minimal diagonal 已严格关闭

\[
\boxed{1\le k=g\le25.}
\]

因此首个未关闭固定层推进到

\[
\boxed{k=g\ge26.}
\]

但从证明结构上看，下一步优先级已经不再是继续逐层 factor `b_1,Q`。`sharp-positive-tail-window.md` 与 `gap-denominator-normal-form.md` 已把统一 gap-desert 问题压成：

1. central denominator 的 24 个固定整数 `Gamma=16,...,39`；
2. `a>k` 或 `b>k` 的 deep-denominator sector。

其中 central sector 已完全消去自由 exponent pair，是下一步最值得优先攻击的统一算术核心。

---

## 4. 可复核脚本

脚本：

`check_a1_top_diag_uniform_layers_24_25.py`

它复用 `check_a1_top_diag_uniform_layers.py` 的完整 fixed-layer machinery，并刻意检查旧的更宽 gap window；因此 `0` 命中对 sharpened window 是更强的有限证书。