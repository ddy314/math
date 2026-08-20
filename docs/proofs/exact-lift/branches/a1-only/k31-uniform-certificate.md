# A1 minimal diagonal: exact `k=g=31` uniform certificate

> 日期：2026-08-20。依赖 `uniform-layer-finite-box.md`。本证书继续使用旧的更宽 near-integer window，因此比当前 sharpened window 更强。

本文关闭

\[
\boxed{k=g=31.}
\]

状态：**已严格完成。**

---

## 1. 完整 factorization

令

\[
b_1=10^{63}-w,
\qquad
Q=10^{64}-(10w-1).
\]

四个 `w` 的完整 factorization 已全部获得并做素性确认。此前最后的缺口是 `w=4` 的 Q-side；现在有

\[
\boxed{
10^{64}-39
=7^2\cdot34673\cdot
7675984356934380436832851\cdot
766793494003346313676638849083843.
}
\tag{1}
\]

最后两个大因子均为素数。

由完整 odd-prime supply theorem 得到四个 `w` 的 `h` 数量

\[
\boxed{(|H_1|,|H_2|,|H_3|,|H_4|)=(16384,96,16,96).}
\tag{2}
\]

---

## 2. valuation floors 与 finite box

对六类型用 exact p-adic root lifting 计算 prefix `N` 的最大赋值：

\[
\begin{array}{c|cc}
(z,w)&\max v_2(N)&\max v_5(N)\\ \hline
(1,1)&1&45\\
(1,2)&3&44\\
(1,3)&1&44\\
(1,4)&5&45\\
(3,1)&1&44\\
(3,2)&3&47
\end{array}
\]

所以 global resonance floors 为

\[
\boxed{\underline x_*=-33,\qquad \underline y_*=-78.}
\tag{3}
\]

结合 decade 与 primitive cross-corridor，`uniform-layer-finite-box.md` 的一般公式给出

\[
\boxed{
-321\le x\le284,
\qquad
-120\le y\le58.
}
\tag{4}
\]

这是与 `ell` 无关的完整 finite search box。

---

## 3. exact decade scan

脚本

`check_a1_top_diag_uniform_layer_31.py`

枚举全部合法 `h`，对每个 `x` 精确恢复 decade 中至多两个 `y`，并应用两个 cross-corridor necessary conditions。

落入

\[
10^{30}\le\rho<10^{31}
\]

的状态数按 `w` 为

\[
\boxed{
\begin{array}{c|r}
w&\text{decade states}\\ \hline
1&6,066,806\\
2&36,304\\
3&6,277\\
4&37,285
\end{array}}
\]

总计

\[
\boxed{6,146,672.}
\tag{5}
\]

---

## 4. 仍检查旧的更宽 gap window

当前理论只要求排除

\[
15.09<10^{31}(\lceil\rho\rceil-\rho)<39.003.
\]

为保持与 `k=6..30` 保险证书一致，本层仍检查旧的更宽区间

\[
\boxed{
5.09<10^{31}(\lceil\rho\rceil-\rho)<50.45.
}
\tag{6}
\]

所有 `6,146,672` 个 decade states 中：

\[
\boxed{\text{near hits}=0.}
\tag{7}
\]

因此 sharpened window 当然也没有 candidate。

---

## 5. 结论

结合旧证书 `k<=30`：

\[
\boxed{1\le k=g\le31\Longrightarrow\text{empty}.}
\tag{8}
\]

所以 fixed-layer 保险线的首个未关闭层现在推进到

\[
\boxed{k=g=32.}
\]

这与统一 deep 理论独立：central 已对所有 `k>=26` 关闭，而 deep 统一证明仍继续处理 `k>=32` 的无限尾。