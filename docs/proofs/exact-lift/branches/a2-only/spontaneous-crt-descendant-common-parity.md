# A2 fully primitive descendant pair 的 canonical common-parity dichotomy

> **依赖：** `spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`、`spontaneous-crt-target-descent-global-gcd.md`、`spontaneous-crt-source-descent-depth.md`。
>
> **严格状态：**fully primitive positive descent产生 `Rstar_63,Dhat_63` 两个 odd descendant carriers。本文取它们的完整 common gcd，并把 mod-4 parity精确分配到 common part与互素 residuals。危险 orientation `Z=1 mod4` 中，若 common gcd为 `1 mod4`，两个 residual都是 `3 mod4` 并强迫两枚 distinct inert suppliers；若 common gcd为 `3 mod4`，双 parity被 common part吸收。另一 orientation `Z=3 mod4` 中，无论 common gcd orientation如何，总有且仅有一个 residual为 `3 mod4`。结合已完成的 target/source overlap audit，common parity若被吸收，只能由 fixed target `31/179`、受双短 carrier控制的 source-common overlap、或真正 external common kernel承担。本文尚未排除最后一类，因此不关闭 A2。

---

## 1. the descendant pair

fully primitive height descent为

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.}
\tag{1.1}
\]

已有

\[
\boxed{
\mathscr R_{63}^\star>0,
\qquad
\mathscr R_{63}^\star\equiv3\pmod4,}
\tag{1.2}
\]

\[
\boxed{
\widehat{\mathscr D}_{63}>0,
\qquad
\widehat{\mathscr D}_{63}\equiv3Z\pmod4,}
\tag{1.3}
\]

其中 `Z` 为 odd endpoint orientation，所以

\[
Z\equiv1\text{ or }3\pmod4.
\]

两个 carriers都是 positive odd integers。

---

## 2. canonical common gcd

定义完整 common gcd

\[
\boxed{
G_\Delta
:=\gcd(\mathscr R_{63}^\star,
          \widehat{\mathscr D}_{63}).}
\tag{2.1}
\]

以及 coprime residuals

\[
\boxed{
R_\Delta^\circ
:=\frac{\mathscr R_{63}^\star}{G_\Delta},
\qquad
D_\Delta^\circ
:=\frac{\widehat{\mathscr D}_{63}}{G_\Delta}.}
\tag{2.2}

则

\[
\boxed{\gcd(R_\Delta^\circ,D_\Delta^\circ)=1.}
\tag{2.3}

`G_Delta` 为 odd，因此模 `4` 可逆。由 (1.2),(1.3)：

\[
\boxed{
R_\Delta^\circ
\equiv3G_\Delta^{-1}\pmod4,}
\tag{2.4}

\[
\boxed{
D_\Delta^\circ
\equiv3ZG_\Delta^{-1}\pmod4.}
\tag{2.5}

---

## 3. dangerous `Z=1`: either common parity or two distinct residual suppliers

固定

\[
\boxed{Z\equiv1\pmod4.}
\tag{3.1}

此时两个 parent 都是 `3 mod4`：

\[
\mathscr R_{63}^\star
\equiv
\widehat{\mathscr D}_{63}
\equiv3\pmod4.
\]

### common gcd `1 mod4`

若

\[
G_\Delta\equiv1\pmod4,
\]
由 (2.4),(2.5)：

\[
\boxed{
R_\Delta^\circ
\equiv
D_\Delta^\circ
\equiv3\pmod4.}
\tag{3.2}

两个 residual positive、odd、coprime，因此每个都必须含至少一枚 `3 mod4` prime到奇次，而且 suppliers不能相同：

\[
\boxed{
Z\equiv1,\quad G_\Delta\equiv1\pmod4
\Longrightarrow
\text{至少两枚 distinct residual inert primes}.}
\tag{3.3}

### common gcd `3 mod4`

若

\[
G_\Delta\equiv3\pmod4,
\]
则

\[
\boxed{
R_\Delta^\circ
\equiv
D_\Delta^\circ
\equiv1\pmod4.}
\tag{3.4}

此时两个 parent 的 odd-inert parity可以由 common gcd整体承担。由于

\[
G_\Delta\equiv3\pmod4,
\]
`G_Delta` 自身必含至少一枚 inert prime到奇次。

所以危险 orientation 的 strict dichotomy为

\[
\boxed{
Z\equiv1:
\quad
\begin{cases}
G_\Delta\equiv1:&\text{两个 distinct residual suppliers},\\
G_\Delta\equiv3:&\text{common gcd承担 odd parity}.
\end{cases}}
\tag{3.5}

---

## 4. `Z=3`: one residual parity always survives

现在固定

\[
\boxed{Z\equiv3\pmod4.}
\tag{4.1}

则

\[
\mathscr R_{63}^\star\equiv3,
\qquad
\widehat{\mathscr D}_{63}\equiv1
\pmod4.
\]

若 `G_Delta≡1`：

\[
R_\Delta^\circ\equiv3,
\qquad
D_\Delta^\circ\equiv1.
\]

若 `G_Delta≡3`，因为 `3^{-1}≡3 mod4`：

\[
R_\Delta^\circ\equiv1,
\qquad
D_\Delta^\circ\equiv3.
\]

所以无论 common gcd orientation如何：

\[
\boxed{
Z\equiv3\pmod4
\Longrightarrow
\text{恰有一个 coprime descendant residual为 }3\pmod4.}
\tag{4.2}

因此总有一枚 odd-inert supplier位于 common gcd之外：

\[
\boxed{
Z\equiv3
\Longrightarrow
\text{至少一份 non-common descendant inert parity}.}
\tag{4.3}

---

## 5. common parity can now be split by prime-source origin

危险 `Z=1,G_Delta≡3` 分支中真正需要解释的是 common gcd 的 odd parity。

此前两套 overlap audit已经给：

### target labels

若 common prime同时属于 equal-depth target pool，则 prime label只能是

\[
\boxed{31\text{ or }179.}
\tag{5.1}

与 target baseline 的 canonical common factor为 squarefree

\[
\boxed{G_{TD}\mid31\cdot179.}
\tag{5.2}

### source-common labels

若 common prime同时属于 source common gcd，则其三重 common depth `k_r` 必须通过

\[
H_{SD}
=
\prod r^{\lceil k_r/2\rceil}
\]
收费，且

\[
\boxed{
H_{SD}\mid18K-55,}
\tag{5.3}

\[
\boxed{
H_{SD}\mid
\mathscr H_{S63},}
\tag{5.4}

其中

\[
\mathscr H_{S63}
=102383gT-29952ga_3+14976C5^\lambda.
\]

此外 source common 与 target support完全分离。

因此 `G_Delta` 的 inert parity supplier若既不是 fixed `31/179`，也不是 source-common overlap，就必须进入一个真正的

\[
\boxed{\text{external descendant-common kernel}.}
\tag{5.5}

这给后续 closure一个明确对象，而不再把所有 common primes混在同一 gcd 中。

---

## 6. revised parity frontier

fully primitive descent现在提供如下全局分叉：

1. `Z=3`：自动有一份 non-common descendant inert parity；
2. `Z=1,G_Delta=1 mod4`：自动有两份 distinct non-common descendant inert parity；
3. `Z=1,G_Delta=3 mod4`：唯一逃逸方式是 common gcd自身含 odd inert parity；该 parity的 old-pool来源已被压成
   - fixed target `31/179`；
   - source-common double-short depth；
   - residual external common kernel。

所以下一步真正需要关闭的是第三项中的 external common parity，或者证明前两类 old-pool parity无法使整个 `G_Delta` 达到 `3 mod4`。ordinary resultant/Legendre路线此前已经审计为 no-go，因此应优先使用 height drop、natural representative或其它 prime-source ledger。

A2 仍为 `待证`。
