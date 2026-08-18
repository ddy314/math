# A2 source–external length resultant

> **依赖：** `source-spontaneous-bridge.md`、`hensel.md`、`decimal-discriminant.md`。
>
> **严格状态：**本文继续处理 moving external double-root 与 source excess 的可能交集。把 source prefix contact `D_src`、linear prefix root `36P-11` 与固定 quartic `R_SW` 联立后，所有 `a_2,b_2,x,r` 都可消去，只剩 `s=36·10^{M-1}` 的固定四次 length polynomial。其 genuine inert repeated-root gate 最终只剩 `p=19`，并进一步强迫 `M mod 18` 只取两类。本文仍**不宣称 A2 全局关闭**。

---

## 1. `D_src` 与 double-root prefix 的纯 decimal 合并

当前 endpoint 固定 `a_1=9`。令

\[
S:=10^{M-1},
\qquad
A_0=9S,
\qquad
P=A_0+a_2,
\qquad
C_0=\frac{9b_2}{2}.
\]

source prefix contact 为

\[
D_{\rm src}=C_0^2-A_0a_2.
\tag{1.1}
\]

moving external double-root 已由 `decimal-discriminant.md` / `decimal-prefix-bridge.md` 强迫

\[
36P-11\equiv0\pmod p.
\tag{1.2}
\]

把 `a_2=P-9S` 代入 `4D_src`：

\[
4D_{\rm src}
=81b_2^2-36Sa_2
=81b_2^2-36SP+324S^2.
\]

在 (1.2) 下得到新的纯 denominator/length contact：

\[
\boxed{
 p\mid D_{\rm src},\ p\mid36P-11
\Longrightarrow
p\mid81b_2^2+324S^2-11S.
}
\tag{1.3}
\]

现在写

\[
x=\frac{b_2}{10^M}=\frac{b_2}{10S},
\qquad
s:=36S.
\tag{1.4}
\]

因为 genuine external prime 不整除 `2·3·5S`，(1.3) 等价于

\[
\boxed{
225s x^2+9s-11\equiv0\pmod p.
}
\tag{1.5}
\]

---

## 2. `已严格完成`：消去 `x` 得到固定 length polynomial

`source-spontaneous-bridge.md` 已证明 source/external overlap 必满足

\[
\boxed{
\mathcal R_{SW}(x)
=-480029x^4+40568x^3+4496x^2+7040x+3520
\equiv0\pmod p.
}
\tag{2.1}
\]

将 (2.1) 与 (1.5) 对 `x` 求 resultant，得到只含 `s` 的固定 quartic：

\[
\boxed{
\begin{aligned}
\mathcal L_{SW}(s):={}&
19964008847990601s^4
+26176176015770484s^3\\
&-6142888878869754s^2
-12826705293056556s\\
&+3373694017753081.
\end{aligned}}
\tag{2.2}
\]

因此若 moving external double-root 同时承担 source excess，则

\[
\boxed{
\mathcal L_{SW}(36\cdot10^{M-1})\equiv0\pmod p.
}
\tag{2.3}
\]

这一步把 `(x,r,a_2,b_2)` 全部消掉；source/external overlap 已经变成一个**纯 decimal length Hensel condition**。

---

## 3. `已严格完成`：length polynomial 的 repeated-root gate 是固定有限集

(2.2) 的整数判别式因子分解为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(\mathcal L_{SW})
={}&-2^{48}3^{29}5^{28}7^6 11^{18}19^2\\
&\cdot101^4\cdot748057\cdot45503^2.
\end{aligned}}
\tag{3.1}
\]

其中

\[
748057\equiv1\pmod4,
\qquad
101\equiv1\pmod4,
\]

且 `748057` 与 `45503` 都是素数，而

\[
45503\equiv3\pmod4.
\tag{3.2}
\]

对 genuine non-`3` external inert prime：

- `p=7,11` 已由 `D_dec=55T^2Q^2-49b_3^2` 的单位性直接排除；
- `p=5,101,748057` 不是 `3 mod 4` inert gate；
- 因而判别式中只需继续检查 `19,45503`。

---

## 4. `已严格完成`：`45503` 与 discriminant-zero character 不相容

external discriminant-zero 条件

\[
55T^2Q^2\equiv49b_3^2\pmod p
\]
且 `p\nmid Tb_3Q` 强迫

\[
\boxed{\left(\frac{55}{p}\right)=1.}
\tag{4.1}
\]

对 `p=45503`：

\[
45503\equiv3\pmod5,
\qquad
45503\equiv7\pmod{11},
\qquad
45503\equiv3\pmod4.
\]

直接用二次互反律得到

\[
\boxed{
\left(\frac{55}{45503}\right)=-1.
}
\tag{4.2}
\]

因此

\[
\boxed{p=45503\text{ 不可能进入 genuine external double-root}.}
\tag{4.3}
\]

所以 source/external length polynomial 的 genuine inert repeated-root gate 最终只剩

\[
\boxed{p=19.}
\tag{4.4}
\]

对所有其他 non-`3` inert external primes，`L_SW` 的 length root 都是 simple root，后续 `M`-方向只有唯一 Hensel lift。

---

## 5. `已严格完成`：固定 `19` 只允许两个 `M mod 18` 类

模 `19` 化简 (2.2)，高次 content 自动消去，得到

\[
\boxed{
\mathcal L_{SW}(s)
\equiv(s-2)(s-8)\pmod{19}.
}
\tag{5.1}
\]

因此 `p=19` 的 source/external overlap 强迫

\[
s=36\cdot10^{M-1}\equiv2\text{ 或 }8\pmod{19}.
\tag{5.2}
\]

又

\[
\operatorname{ord}_{19}(10)=18,
\qquad36\equiv-2\pmod{19}.
\]

逐一解出：

\[
36\cdot10^n\equiv2\pmod{19}
\iff n\equiv9\pmod{18},
\]

\[
36\cdot10^n\equiv8\pmod{19}
\iff n\equiv7\pmod{18}.
\]

令 `n=M-1`，得到

\[
\boxed{
M\equiv8\text{ 或 }10\pmod{18}.
}
\tag{5.3}
\]

所以唯一 remaining repeated-length inert gate `19` 也已经被压成两个固定十进制长度类。

还可恢复对应 source prefix roots：

\[
\begin{array}{c|c}
s\pmod{19}&x=b_2/10^M\pmod{19}\\ \hline
2&13\\
8&15.
\end{array}
\tag{5.4}
\]

在两类上，source ratio (2.3) 都选择 external orientation

\[
\boxed{z/c_u\equiv2\pmod{19},}
\tag{5.5}
\]

故 `f=z+2c_u\equiv4c_u\not\equiv0 (mod 19)`，与 external 定义一致；另一根 `z/c_u=-2` 正是 f-side，已被排除在 moving external channel 之外。

---

## 6. 更新后的 source/external 开放核

若 moving external double-root 还想同时承担 source excess，现在必须经过以下链：

\[
\boxed{
\begin{array}{c}
p^s\mid D_{\rm src},\\
p\mid\mathscr R_{SW},\\
p\mid\mathcal L_{SW}(36\cdot10^{M-1}).
\end{array}}
\tag{6.1}
\]

其中：

1. `R_SW` 对所有 genuine inert external primes 都是 simple-root；
2. `L_SW` 也对所有这些 primes 都是 simple-length root，唯一 fixed exception `19` 只允许
   \[
   M\equiv8,10\pmod{18};
   \]
3. 因此 source/external overlap 已不再有二维 source Hensel phase，也没有移动 repeated-length branch。

这仍未证明交集为空。下一步若继续 source 线，应研究 simple root `L_SW(36·10^{M-1})` 与 `10` 的乘法轨道是否能和 `D_src` 的完整 `p^s` 深度长期同步；固定 `19` 则可以直接做 `19`-进二阶提升。