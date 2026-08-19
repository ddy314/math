# A2 serial-first pool 对 `B_W` inert parity 的中性化

> **依赖：** `source-discriminant.md`、`spontaneous-height-equal-depth-serial-gcd-selectors.md`。
>
> **严格状态：**source cofactor `B_W` 是 positive `7 mod 8` integer，因此其 `3 mod 4` prime总赋值 parity为奇。本文观察到所有 genuine `Sigma_first` primes均满足 `r_B=h`，故在 `B_W` 中的 exponent 恰为 `2h`，对 inert parity贡献恒为偶。于是 serial-first pool（更包括其子池 `Sigma_double`）不可能承担 `B_W` 的全局奇 parity；必存在至少一枚 `3 mod 4` 的 complement prime在 `B_W` 中具有奇赋值。本文只给 parity allocation，不证明该 complement prime与其它 companion supplier必须不同，因此不关闭 A2。

---

## 1. global source parity

`source-discriminant.md` 已证明

\[
\boxed{\mathscr B_W\equiv7\pmod8.}
\tag{1.1}
\]

因此 `B_W` 为 positive odd `3 mod 4` integer，并有

\[
\boxed{
\sum_{\substack{r\equiv3\ (4)}}
v_r(\mathscr B_W)
\equiv1\pmod2.}
\tag{1.2}
\]

这里求和遍历 `B_W` 的全部 odd inert prime divisors，包括 fixed 与 moving sources。

---

## 2. every serial-first target has even `B_W` exponent

固定 genuine prime由 `Sigma_first` 选择。serial gcd selector theorem给

\[
\boxed{r_B=h,}
\tag{2.1}
\]

其中定义

\[
v_p(\mathscr B_W)=h+r_B.
\]

所以

\[
\boxed{v_p(\mathscr B_W)=2h.}
\tag{2.2}
\]

当前 genuine target primes满足

\[
p\equiv7\text{ or }11\pmod{24},
\]
特别地

\[
p\equiv3\pmod4.
\]

因此每一个 serial-first target虽然本身是 inert prime，但它对 (1.2) 的 parity贡献为

\[
\boxed{2h\equiv0\pmod2.}
\tag{2.3}
\]

---

## 3. the whole serial-first pool is parity-neutral

令 `E_first` 表示 genuine `Sigma_first` target prime集合。则由 (2.2)：

\[
\boxed{
\sum_{p\in E_{\rm first}}v_p(\mathscr B_W)
=2\sum_{p\in E_{\rm first}}h_p
\equiv0\pmod2.}
\tag{3.1}
\]

所以从 global parity ledger (1.2) 中删去整个 serial-first pool后，剩余 complement仍必须保持奇 parity：

\[
\boxed{
\sum_{\substack{r\equiv3\ (4)\\r\notin E_{\rm first}}}
v_r(\mathscr B_W)
\equiv1\pmod2.}
\tag{3.2}
\]

特别地，存在至少一枚 odd prime

\[
\boxed{r\equiv3\pmod4,\qquad r\notin E_{\rm first}}
\tag{3.3}
\]
满足

\[
\boxed{v_r(\mathscr B_W)\text{ 为奇数}.}
\tag{3.4}
\]

这是严格的存在性，不依赖 factorization certificate。

---

## 4. double-serial pool is also neutral

已有

\[
\Sigma_{\rm double}\mid\Sigma_{\rm first}
\]
在 support意义上成立，因为

\[
\Sigma_{\rm double}=\gcd(\Sigma_{\rm first},\Sigma_{\rm second}).
\]

所以 genuine double-serial prime同样满足 (2.2)。令 `E_dbl` 为 genuine double-serial prime集合，则

\[
\boxed{
\sum_{p\in E_{\rm dbl}}v_p(\mathscr B_W)
\equiv0\pmod2.}
\tag{4.1}
\]

因此 `Sigma_double` 即使非空，也不可能自己解释 `B_W≡7 mod8` 的奇 inert parity。

---

## 5. correct allocation consequence

本文并没有证明 (3.3) 的 complement prime属于哪个旧 source label。严格结论只有：

\[
\boxed{
B_W\text{ 的必需 odd inert parity必须由 serial-first pool之外的 support承担}.}
\tag{5.1}
\]

所以后续若能结合已有 residual parity doubling / support separation证明：

- complement prime不能回到 fixed denominator/content support；
- 或 companion residual parity不能复用这枚 complement prime；

就会被迫生成第二枚独立 inert prime并产生新的 product-height surcharge。

不能仅凭 (5.1) 宣称 contradiction。

---

## 6. current role

serial hierarchy现在同时具有：

1. canonical selectors `Sigma_first`, `Sigma_second`, `Sigma_double`；
2. double-serial weighted budget `G_dbl^3 rad(G_dbl)^2`；
3. 本文的 source parity neutrality。

所以 double/first serial pools一方面昂贵，另一方面又不能承担 `B_W` 的全局 odd-inert parity。下一步最有价值的是把强制存在的 complement inert prime送入已有 residual-parity support ledger，尝试证明它与 serial pool及 companion parity supplier三者两两分离。

A2 仍为 `待证`。
