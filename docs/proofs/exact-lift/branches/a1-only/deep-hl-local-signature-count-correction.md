# A1 moderate HL: correction to the local-signature count

> 日期：2026-08-27。依赖 `deep-double-2high-master.md`、`deep-2high-mod8-lock.md` 与现有审计脚本 `check_a1_deep_hl_local_signatures.cpp`。
>
> 本文只修正一个旧 finite-certificate 计数错误，不改变其余 local conditions，也不宣称关闭 moderate HL。

状态：**严格审计完成；旧总数 `3,019,293` 应替换为 `2,603,440`。**

---

## 1. 发现的 certificate inconsistency

旧文档 `deep-hl-local-signature-count` 记录六类型 surviving `r` counts

\[
579692,383278,328609,201854,863426,662434,
\]

总计

\[
3,019,293.
\]

对应 checker 同时写有 proved parity filter

```cpp
if ((tp.w&1)==0) { if (apar) continue; }
```

即 even `w=2,4` 时只允许

\[
a_2=v_2(r)\equiv0\pmod2.
\]

但 checker 中硬编码的 expected counts 实际来自**删去这一行**后的旧运行结果。因此原脚本逐字编译执行会在 `(z,w)=(1,2)` 处得到

\[
255519\ne383278
\]

并以 `COUNT MISMATCH` 退出。

---

## 2. parity filter 确实必须保留

full 2-high master 写

\[
A=2k+3+\eta.
\]

对 even `w=2,4`，strict 2-deep parity 已严格给出

\[
A\equiv1\pmod2.
\]

因此

\[
\boxed{\eta\equiv0\pmod2.}
\tag{1}
\]

moderate HL 中

\[
\eta=-v_2(r)=-a_2,
\]

故

\[
\boxed{w\in\{2,4\}\Longrightarrow a_2\equiv0\pmod2.}
\tag{2}
\]

所以 checker 中的 even-`w` parity line 是正确的 necessary condition；需要修的是 expected counts，而不是删除该 filter。

---

## 3. corrected exact counts

保留原 checker 的全部条件：

1. typewise `r` window；
2. `5|r`；
3. moderate `nu_5,B` cells；
4. master `eta` parity，包括 (2)；
5. unified mod-8 lock；
6. mod-5 Legendre lock；
7. odd-`w` whole-block partition witness；
8. `N_0 mod 16*5^6` safe local cover。

重新逐字编译执行后得到

\[
\boxed{
\begin{array}{c|r}
(z,w)&\text{locally compatible }r\\ \hline
(1,1)&579692\\
(1,2)&255519\\
(1,3)&328609\\
(1,4)&134570\\
(3,1)&863426\\
(3,2)&441624
\end{array}}
\tag{3}
\]

总计

\[
\boxed{2,603,440.}
\tag{4}
\]

初始 `5|r` 总数仍为

\[
11,051,041.
\]

所以 safe local filters 实际删除约

\[
1-\frac{2,603,440}{11,051,041}\approx76.44\%
\]

的初始 `r` set，比旧文档声称的约 `72.7%` 更强。

---

## 4. 为什么旧数恰好重现

作为反向审计，把 checker 中 only-even parity line 暂时删除，同时保持其它代码完全不变，就精确恢复

\[
383278,201854,662434
\]

三个 even-`w` 旧数，以及总计

\[
3,019,293.
\]

因此 discrepancy 的来源已被唯一定位：旧 expected table 是在 even-`w` parity filter 加入代码之前生成的，之后只更新了代码，没有同步 expected constants / 文档。

---

## 5. 当前接口

后续任何 moderate HL finite-coefficient certificate 应使用

\[
\boxed{2,603,440}
\]

作为 local-compatible `r` 上集的基数。

修正后的

`scripts/exact-lift/a1-only/research-checks/deep-denominator/check_a1_deep_hl_local_signatures.cpp`

现在能够实际运行到

```text
CERTIFICATE OK: moderate HL local r signatures reduced to 2,603,440.
```

旧 ledger / README 中出现的 `3,019,293` 属于历史 stale count；在下一次集中导航同步时应统一替换。