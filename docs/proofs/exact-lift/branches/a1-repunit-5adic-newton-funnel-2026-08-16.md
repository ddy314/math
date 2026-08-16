# A1 second-repunit 5-adic Newton funnel — 2026-08-16

本文继续 `a1-repunit-5adic-saturation-dichotomy-2026-08-16.md`，专门处理其中的 5-unsaturated side。

当前参数：

\[
 g=0,
\quad n_2=2k,
\quad a_2=10^{2k}-1,
\quad b_2=10^{k-1},
\]

\[
 s=\ell-2k>0,
\qquad
 b_3=10^{\ell-1}+f,
\qquad
 f>0,
\]

且 5-unsaturated 已严格给出

\[
\boxed{v_5(d)=k-1,}
\qquad
b_1=10^{m_1}-d.
\]

令

\[
\boxed{q=v_5(f).}
\]

本文从 exact-lift 多项式的 5-adic Newton ledger 得到两个 resonance wall 与一个完整空区。

---

## 1. 三个竞争深度

令

\[
x=10^k,
\qquad
R=10^{m_1-4k},
\qquad
S=10^s.
\]

第一块写成

\[
b_1=Rx^4-d,
\qquad
 a_1=10Rx^4+e.
\]

第三块写成

\[
b_3=\frac{Sx^2}{10}+f,
\qquad
 a_3=Sx^2-h.
\]

将 exact lift 平方清分母，得到整数多项式 `\Phi`。

其 Newton ledger 中真正可能成为最低层的三种深度为

\[
\boxed{L_{\rm low}=2k+4q+4,}
\tag{1}
\]

\[
\boxed{L_{\rm mid}=7k+s+q+1,}
\tag{2}
\]

\[
\boxed{L_{\rm up}=9k+2s.}
\tag{3}
\]

其中 `L_low` 由两个 monomial 共同承担：

\[
-10^6d^2f^4,
\qquad
-10^4x^2e^2f^4;
\]

`L_mid` 的核心 monomial 为

\[
-2000x^5Sd^2h^2f;
\]

`L_up` 的核心 monomial 为

\[
-200x^7S^2d^2h^2.
\]

有限符号 ledger 审计见
`scripts/check_a1_repunit_5adic_newton_funnel.py`。

---

## 2. 两条 resonance wall

比较 (1)、(2)：

\[
L_{\rm low}=L_{\rm mid}
\Longleftrightarrow
\boxed{3q=5k+s-3.}
\tag{4}
\]

比较 (2)、(3)：

\[
L_{\rm mid}=L_{\rm up}
\Longleftrightarrow
\boxed{q=2k+s-1=\ell-1.}
\tag{5}
\]

所以 Newton 图只有两条真正的 resonance wall。

---

## 3. 中间开区间完全为空

若

\[
\boxed{
\frac{5k+s-3}{3}<q<2k+s-1,
}
\tag{6}
\]

则符号 ledger 逐项比较证明：

\[
-2000x^5Sd^2h^2f
\]

是唯一取得最小 5-adic 赋值的 monomial。

这里 `q>0`，所以 `5\mid b_3`；第三分数既约强迫

\[
v_5(h)=0,
\]

故该核心项不会因 `h` 增加额外五进深度。

唯一最浅项无法在整数和中相消，因此

\[
\boxed{
\frac{5k+s-3}{3}<q<\ell-1
\Longrightarrow
\text{无 exact lift}.}
\tag{7}
\]

---

## 4. `q>\ell-1` 同样为空

如果

\[
q>\ell-1=2k+s-1,
\]

则 `L_up` 严格低于所有其他 monomial 深度，故

\[
-200x^7S^2d^2h^2
\]

成为唯一最浅项。

因此

\[
\boxed{q>\ell-1\Longrightarrow\text{无 exact lift}.}
\tag{8}

于是 5-unsaturated 候选只可能满足

\[
\boxed{
q\le\frac{5k+s-3}{3}
\quad\text{或}\quad
q=\ell-1.
}
\tag{9}

---

## 5. Upper resonance 本身已经要求巨大第三尾

若

\[
q=\ell-1,
\]

则

\[
f\ge5^{\ell-1}.
\]

结合端点上界

\[
f<\frac18 10^s
\]

得到与 5-saturated side 相同的斜率约束：

\[
\boxed{
 s>2\log_2 5\,k+3-\log_2 5
}
\]

即

\[
\boxed{
\ell>6.643856189\ldots k+0.678071905\ldots.
}
\tag{10}

所以在 moderate-tail 区域中，只需研究 lower Newton side。

---

## 6. 严格 lower side 强迫第一分子 excess 为 5-unit

现在假设

\[
\boxed{3q<5k+s-3.}
\tag{11}

此时最低层只能由两个 `L_low` monomial 承担。

若

\[
5\mid e,
\]

第二项

\[
-10^4x^2e^2f^4
\]

会变得更深，只剩

\[
-10^6d^2f^4
\]

唯一最浅，矛盾。

所以

\[
\boxed{v_5(e)=0.}
\tag{12}

令

\[
d=5^{k-1}d_0,
\qquad
f=5^qf_0,
\]

其中 `d_0,f_0` 都是 5-unit。

约掉共同最小五进幂后，两个最低项模 `5` 的和必须为零。利用

\[
f_0^4\equiv1\pmod5,
\qquad
2^{2k}\equiv(-1)^k\pmod5,
\]

得到

\[
\boxed{
d_0^2+(-1)^{k+1}e^2\equiv0\pmod5.}
\tag{13}

所以：

### `k` 偶

\[
\boxed{e\equiv\pm d_0\pmod5;}
\tag{14}

### `k` 奇

\[
\boxed{e\equiv\pm2d_0\pmod5.}
\tag{15}

这是一条随 `k` 奇偶切换的固定 prefix phase lock。

---

## 7. Lower resonance

若恰有

\[
\boxed{3q=5k+s-3,}
\tag{16}

则两个 `L_low` monomial 与 `L_mid` monomial 三者同时达到最低层。

这是一条真正的 5-adic resonance family，而不是空区。后续可以继续保留三项模 `5` 相消条件，而无需再处理全部多项式。

---

## 8. 当前 second-repunit 的 5-adic 图

5-unsaturated side 现已化成：

1. **strict lower**
   \[
   3q<5k+s-3,
   \]
   带 `v_5(e)=0` 与 (13) 的 prefix phase lock；
2. **lower resonance**
   \[
   3q=5k+s-3;
   \]
3. **中间开区间**：空；
4. **upper resonance**
   \[
   q=\ell-1,
   \]
   但自动进入 slope `6.64` 以上的巨大 tail；
5. **upper side**：空。

因此 moderate-tail 的真正 5-adic moving core 已经只剩 strict lower 与单一 lower-resonance wall。