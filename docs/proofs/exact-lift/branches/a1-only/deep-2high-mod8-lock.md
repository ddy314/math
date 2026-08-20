# A1 minimal diagonal: unified 2-high mod-8 block lock

> 日期：2026-08-20。依赖 `deep-double-2high-master.md` 与 `deep-gap-unit-square.md`。

本文把此前 HL 的 mod-4 orientation 提升成一个对**全部剩余 double-deep 2-high / 5-low branch** 都成立的 mod-8 公式。它同时覆盖 moderate HL 与 2-extreme `E_2`。

状态：**已严格完成。**

---

## 1. 输入

沿用 master branch：

\[
a=2^{k+1}5^Y\alpha,
\qquad
b=2^{k+2}5^Y\beta,
\qquad
\alpha\beta=r_{10},
\]

且

\[
\beta q-5\alpha s=2^c n_0.
\]

当前 `k>=32`，而所有 surviving 2-high branch 都有 `c>=3`，所以模 8：

\[
\boxed{\beta q\equiv5\alpha s\pmod8.}
\tag{1}

whole-block selector `s` 只含 `1 mod 4` prime-power blocks，因此

\[
s\equiv1\text{ or }5\pmod8,
\qquad s^2\equiv1\pmod8.
\tag{2}

---

## 2. strict-2 unit square

`deep-gap-unit-square.md` 给

\[
\gamma QN_2 5^B\equiv1\pmod8,
\qquad N_2=N/2^{v_2(N)}.
\]

在 double-deep 中

\[
\gamma\equiv-h\pmod8,
\qquad h=qs.
\]

所以

\[
\boxed{hQN_2 5^B\equiv-1\pmod8.}
\tag{3}

另一方面由 (1)：

\[
q\equiv5\alpha s\beta^{-1}\pmod8.
\]

乘以 `s` 并用 `s^2=1 mod 8`：

\[
\boxed{h=qs\equiv5\alpha\beta^{-1}\pmod8.}
\tag{4}

把 (4) 代入 (3)：

\[
5^{B+1}\alpha QN_2\beta^{-1}\equiv-1\pmod8.
\]

因此

\[
\boxed{
\beta
\equiv
-5^{B+1}QN_2\,\alpha
\pmod8.}
\tag{5}

由于任意 odd `alpha` 都满足 `alpha^2=1 mod 8`，再乘 `alpha`：

\[
\boxed{
r_{10}
\equiv
-5^{B+1}QN_2
\pmod8.}
\tag{6}

这是主结论。

---

## 3. even `w` 的显式版本

已有：

- `w=2`：`QN_2=1 mod 8`；
- `w=4`：`QN_2=1 mod 8`。

所以统一：

\[
\boxed{
r_{10}\equiv-5^{B+1}\pmod8
\qquad(w=2,4).}
\tag{7}

等价于

\[
\boxed{
B\text{ even}\Longrightarrow r_{10}\equiv3\pmod8,}
\]

\[
\boxed{
B\text{ odd}\Longrightarrow r_{10}\equiv7\pmod8.}
\tag{8}

在 moderate HL 中 `B+2nu_5=v_5(r)`，所以 `B` parity 就是 `v_5(r)` parity。故对 fixed `r`，(8) 是立即可检查的 local filter。

它比旧的

\[
r_{10}\equiv3\pmod4
\]

严格强一位。

---

## 4. odd `w` 的显式版本

对 `w=1,3`，`QN_2 mod 8` 由 prefix `N_0 mod 16` 决定，但始终只取 `3` 或 `7`。

因此 (6) 说明：

\[
\boxed{r_{10}\equiv1\text{ or }5\pmod8,}
\tag{9}

与旧 `r_10=1 mod 4` 一致，但现在具体的 `1/5 mod 8` 类会反向锁定 `QN_2`，从而锁定 `N_0 mod 16` 的一半 classes。

例如当 `QN_2=7 mod 8`：

\[
B\text{ even}\Rightarrow r_{10}\equiv5\pmod8,
\qquad
B\text{ odd}\Rightarrow r_{10}\equiv1\pmod8;
\]

当 `QN_2=3 mod 8` 时两者交换。

---

## 5. 与 `eta` parity 联立

`deep-double-2high-master.md` 已给：

- even `w`：`eta` 必为偶数；
- odd `w`：`eta mod 2=v_2(N) mod 2`，等价地锁定 `N_0` parity。

所以 (6) 与 `eta` parity 合并后，剩余 2-high branch 的 2-adic局部数据不再只有 `q mod 4`：

\[
\boxed{
(\eta\bmod2,\ B\bmod2,\ r_{10}\bmod8,\ N_0\bmod16)
}
\]

之间存在显式有限兼容表。

这套表可直接用于后续 finite modular exhaustion；尤其 even-`w` moderate HL 的 `r` 候选在 `v_2(r)` parity 与 (8) 两层过滤后会显著减少。
