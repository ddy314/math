# A2 fixed height/common 与 descendant gate 的横截性

> **依赖：** `primitive-reduction.md`、`fixed-prime-asymmetric-lifts.md`、`crt-descent-ledger.md` 中整合来源 `spontaneous-crt-f-descent-separation.md`、`spontaneous-crt-descendant-third-order-balance.md`。
>
> **严格状态：**本文把当前 canonical fixed-height center `2K-9=0` 与旧 descendant-height gate `G_D(K)=11K^2-240K+432` 直接做整数 Bézout 消元。结论是：二者的 non-`3` common support 只能是 `7`，而且共同深度最多一层；进一步代入本轮已经得到的两个 genuine fixed-`7` 二阶 angle/denominator continuation，二者都与 `G_D=0 mod 49` 横截。因此 `7` 不能作为 fixed denominator-height-angle pool 与 descendant recycling pool 的二阶复用标签。本文仍不单独宣称 A2 全局关闭。

---

## 1. exact central / descendant identity

定义

\[
\boxed{L_{23}:=2K-9,}
\tag{1.1}
\]

以及旧 descendant-height gate

\[
\boxed{G_D(K):=11K^2-240K+432.}
\tag{1.2}
\]

直接以 `K=(L_{23}+9)/2` 消元，得到整数恒等式

\[
\boxed{
4G_D(K)=11L_{23}^2-282L_{23}-1701.}
\tag{1.3}
\]

而

\[
\boxed{1701=3^5\cdot7.}
\tag{1.4}
\]

因此若 odd prime `p` 同时满足

\[
p^t\mid L_{23},
\qquad
p^t\mid G_D(K),
\tag{1.5}
\]

则 (1.3) 立即给

\[
p^t\mid1701.
\tag{1.6}
\]

对 non-`3` inert prime：

\[
\boxed{p=7,\qquad t\le1.}
\tag{1.7}
\]

所以 central height/saturation sheet 与 descendant `G_D` sheet 不存在共同二阶深接触。

---

## 2. exact center value解释 fixed `7`

在 height center

\[
K=\frac92
\]
上：

\[
\boxed{
G_D\!\left(\frac92\right)
=-\frac{1701}{4}
=-\frac{3^5\cdot7}{4}.}
\tag{2.1}
\]

故 `23,43` 两个其它 denominator-height fixed labels在第一层已经与 `G_D` 分离；上一轮发现的 angle-only `199` 同样不可能由这个 center进入 `G_D`。

这也重新解释了旧 `spontaneous-crt-f-descent-separation.md` 为什么在 f-denominator / descendant overlap 中只留下 inert label `7`：它正是 central/descendant resultant 的唯一 non-`3` 素因子。

---

## 3. `7` 的二阶 Hensel roots互相错开

模 `7`：

\[
G_D(K)=0
\]

有两个 roots

\[
K\equiv1,3\pmod7.
\tag{3.1}
\]

它们唯一提升到模 `49`：

\[
\boxed{K\equiv8,45\pmod{49}.}
\tag{3.2}
\]

而 central line

\[
2K-9\equiv0\pmod{49}
\]
的唯一 root 是

\[
\boxed{K\equiv29\pmod{49}.}
\tag{3.3}
\]

所以 central 与 descendant roots在第二层已经完全分离。

---

## 4. 加入 genuine fixed-`7` angle/common continuation 后仍无二阶复用

`fixed-prime-asymmetric-lifts.md` 已严格得到 `p=7` 的两条 genuine 二阶 continuation：

\[
(x,y,\tau)=(39,48,29),
\tag{4.1H}
\]

\[
(x,y,\tau)=(25,34,22)
\pmod{49}.
\tag{4.1A}
\]

由于

\[
K=\frac{y+9}{\tau}
\pmod{49},
\tag{4.2}
\]

两条分别给

\[
\boxed{K\equiv29,22\pmod{49}.}
\tag{4.3}
\]

直接代 `G_D`：

\[
G_D(29)\equiv28\not\equiv0\pmod{49},
\]

\[
G_D(22)\equiv35\not\equiv0\pmod{49}.
\tag{4.4}
\]

因此无论 fixed-`7` continuation选择 height-deep 还是 additive-deep：

\[
\boxed{
7^2\nmid G_D(K).}
\tag{4.5}
\]

尤其是 height-deep branch 的 `K=29` 恰落在 central `7^2` root，但 `G_D` 此时只有精确一层 `7`；additive-deep branch 连 central root本身都已退出。

---

## 5. 对 terminal recycling ledger 的意义

旧 quartic descendant hierarchy 把 `G_D(K)` 作为 strict third-order overdepth resultant中的旧 fixed sheet之一。本文说明 fixed denominator-height-angle pool 与该 sheet 的交集已经完全横截化：

\[
\boxed{
\text{fixed height/common}\cap G_D
\subseteq\{7\},
\qquad
v_7(\text{common support})=1.}
\tag{5.1}
\]

所以 terminal parity spill 若需要一枚 old fixed label进入 `G_D` 并继续承担第二层以上 recycling，不能使用 `7,23,43` 这组 denominator-height labels；`7` 只允许一次浅层 correction，`23,43` 第一层即分离。

这还没有排掉所有 terminal external suppliers，但已经删除了一种此前仍可想象的 fixed-prime 深复用机制。后续应把同样的“spill carrier vs old pool”横截审计继续用于 fixed `3`、source/target 与真正 external pool。

### 验证

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_fixed_prime_descendant_transversality.py
```
