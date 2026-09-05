# A1 top layer: `k=2g` prime-shape collapse for `L`

> 日期：2026-08-22。
>
> 依赖：`top-layer-k2g-gap-smallL-collapse.md`、`decimal-height-synchronization.md`、global `kappa` square terminal。
>
> 范围：
> \[
> d=2,\quad r=s=1,\quad g\ge1,\quad k=2g,\quad J=0,
> \]
> primitive pruning 后只剩 `(z,w)=(1,1),(1,3)`。

状态：**已严格完成 reduction。** 本文关闭：

- mixed-high `2^a5^b` with `a>=2,b>=1`；
- `L=2*5^b`；
- pure-2 `L=2^a`。

所以 `k=2g,J=0` 若仍有候选，唯一可能的 decimal denominator 形状是
\[
\boxed{L=5^b.}
\]

---

## 1. boundary valuation table

令
\[
e_p:=v_p(\kappa),\qquad p=2,5.
\]

前文已证明
\[
v_p(10^gQG)=3g,
\qquad
v_p(K)=2g,
\qquad
v_p(N)=0,
\]
对 `p=2,5` 同时成立。

若
\[
L=2^a5^b,
\]
则按 `L=kappa/gcd(kappa,10^gQG)`：
\[
\boxed{
a=(e_2-3g)_+,\qquad b=(e_5-3g)_+.}
\tag{1}
\]

---

## 2. high 2-side

若 `a>=2`，则
\[
e_2=3g+a>3g+1.
\]

`kappa` square inner 中第二项严格更浅：
\[
v_2(\kappa K)=e_2+2g,
\qquad
v_2(2GD^2N)=5g+1.
\]

所以
\[
v_2(W)=\frac{e_2+5g+1}{2}.
\]
平方 parity 强迫
\[
\boxed{a\text{ 为奇数}.}
\tag{2}
\]

又
\[
v_2(\kappa+G)=g,
\qquad
v_2(\kappa+2G)=g+1.
\]
root numerator 中 `W` term 严格更浅，于是 reduced 2-denominator completion height 精确为
\[
\boxed{
H_2=2g+\frac{3a+1}{2}.
}
\tag{3}
\]

---

## 3. high 5-side

若 `b>=1`，则
\[
e_5=3g+b>3g.
\]
同理第二项严格更浅，得到
\[
v_5(W)=\frac{e_5+5g}{2}.
\]
平方 parity 强迫
\[
\boxed{b\text{ 为偶数}.}
\tag{4}
\]

并且
\[
\boxed{
H_5=2g+\frac{3b}{2}.
}
\tag{5}
\]

---

## 4. mixed-high 不可能

若同时
\[
a\ge2,\qquad b\ge1,
\]
则 exact decimal-height synchronization 要求 (3)=(5)：
\[
2g+\frac{3a+1}{2}
=
2g+\frac{3b}{2}.
\]
即
\[
3(a-b)+1=0,
\]
无整数解。

因此
\[
\boxed{a\ge2,\ b\ge1\Longrightarrow\text{empty}.}
\tag{6}
\]

---

## 5. `L=2*5^b` 也为空

现在取
\[
a=1,\qquad b\ge1.
\]

2-side 与 `top-layer-k2g-gap-smallL-collapse.md` 的 `L=2` 计算完全相同，因为 `e_2=3g+1`：
\[
\boxed{H_2=2g+2.}
\tag{7}
\]

而 5-side 是 high，(4) 给 `b` 为正偶数，所以 `b>=2`。由 (5)：
\[
H_5\ge2g+3.
\]
矛盾。因此
\[
\boxed{L=2\cdot5^b\Longrightarrow\text{empty}.}
\tag{8}
\]

---

# Pure-2 branch

以下假设
\[
\boxed{L=2^a,\qquad a\ge2.}
\]
由 (2) 实际
\[
\boxed{a\ge3\text{ 且为奇数}.}
\tag{9}
\]

## 6. 5-side 被强迫到唯一 low resonance

high 2-side height (3) 满足
\[
H_2>2g.
\]

5-side 现在 `b=0`，故 `e_5<=3g`。若 `e_5!=g`，则 `kappa+2G` 不发生低端 5-adic resonance；直接从 root numerator 得
\[
H_5\le2g.
\]
所以不可能同步。

因此任何 pure-2 candidate 必须满足
\[
\boxed{e_5=g.}
\tag{10}
\]

由于 base `10^gQG` 的 5-depth 为 `3g`，(10) 等价于
\[
\boxed{v_5(M)=2g.}
\tag{11}
\]

写
\[
\boxed{M=5^{2g}m,\qquad 5\nmid m.}
\tag{12}
\]

又 `(L,M)=1` 且 `L` 为 2-power，所以 `M,m` 为奇数。

---

## 7. ultrathin gap 强迫 `a` 很大

令
\[
A:=HL-M>0.
\]

因为
\[
v_5(HL)=g,
\qquad
v_5(M)=2g,
\]
所以
\[
\boxed{v_5(A)=g.}
\tag{13}
\]
特别地
\[
A\ge5^g.
\]

另一方面前文 ultrathin gap 给
\[
\frac AL=H-\rho<\frac{95}{H^2}.
\]
代入 `L=2^a,H=2^g5^g`：
\[
5^g
<
\frac{95\,2^a}{2^{2g}5^{2g}}.
\]
因此
\[
\boxed{
2^a>
\frac{2^{2g}5^{3g}}{95}.
}
\tag{14}
\]

---

## 8. high 5-resonance congruence

记
\[
B_1:=b_1=10^{4g+1}-w,
\qquad
Q_0:=10B_1+1.
\]

因为 `M` 是 `10^gQG=H^3B_1Q_0` 的 divisor，(12) 中的 `m` 整除 `B_1Q_0`。写
\[
C:=\frac{B_1Q_0}{m}\in\mathbf Z.
\]

于是
\[
\kappa
=\frac{H^3B_1Q_0\,2^a}{5^{2g}m}
=2^{3g+a}5^gC.
\]
而
\[
2G=2^{g+1}5^gB_1.
\]
所以
\[
\kappa+2G
=2^{g+1}5^g
\left(2^{2g+a-1}C+B_1\right).
\tag{15}
\]

若 5-side 要达到 high 2-side 的 completion height (3)，则必要地
\[
v_5(\kappa+2G)-g\ge H_2.
\]
因此
\[
\boxed{
5^{R}\mid
2^{2g+a-1}C+B_1,
\qquad
R:=2g+\frac{3a+1}{2}.
}
\tag{16}
\]

乘以 `m` 并约去 5-unit `B_1`：
\[
\boxed{
 m\equiv
 -2^{2g+a-1}Q_0
 \pmod{5^R}.
}
\tag{17}
\]

---

## 9. gap numerator 与 resonance 同余冲突

由 (13) 写
\[
A=5^g a_0,
\qquad a_0\in\mathbf Z_{>0}.
\]

而
\[
A=HL-M
=2^{a+g}5^g-5^{2g}m,
\]
所以
\[
\boxed{a_0=2^{a+g}-5^g m.}
\tag{18}
\]
特别地
\[
0<a_0<2^{a+g}.
\tag{19}
\]

把 (17) 代入 (18)：
\[
\boxed{
 a_0\equiv B_0
 \pmod{5^{R+g}},
}
\tag{20}
\]
其中
\[
\boxed{
B_0
:=2^{a+g}
+2^{2g+a-1}5^gQ_0
>2^{a+g}.
}
\tag{21}
\]

只要证明
\[
B_0<5^{R+g},
\tag{22}
\]
则 (19)-(21) 立即矛盾：`a_0,B_0` 都是模数内的正代表，却有 `a_0<B_0` 而二者同余。

---

## 10. `g>=2` 时 (22) 自动成立

有
\[
Q_0<2\cdot10^{4g+2}.
\]
所以
\[
B_0
<2^{6g+a+3}5^{5g+2}.
\tag{23}
\]

而
\[
5^{R+g}
=5^{3g+(3a+1)/2}.
\]

(23)<该模数的充分条件是
\[
2^{12g+2a+6}<5^{3a-4g-3}.
\tag{24}
\]

由 (14)、`5^{3g}>2^{6g}`、`95<2^7`：
\[
2^a>2^{8g-7},
\qquad
\boxed{a>8g-7.}
\tag{25}
\]

又 `a` 为奇数。

- `g>=4` 时，(25) 直接给 `a>5g+3`；
- `g=3` 时，`a>17` 且为奇数，所以 `a>=19>18=5g+3`。

若 `a>5g+3`，因为 `5>2^2`：
\[
5^{3a-4g-3}
>2^{6a-8g-6}
>2^{12g+2a+6},
\]
正是 (24)。

对 `g=2`，(14) 直接给 `a>=13`（并且为奇数）。在最小值 `a=13`：
\[
(24)\Longleftarrow 2^{56}<5^{28},
\]
而
\[
5^7=78125>65536=2^{16}
\]
的四次方给 `5^28>2^64>2^56`。更大的奇数 `a` 每增加 2，右/左比额外乘 `5^6/2^4>1`，所以 (24) 继续成立。

因此
\[
\boxed{g>=2\Longrightarrow\text{pure-2 empty}.}
\tag{26}

---

## 11. `g=1` 的两个小 `a` 也直接死于 (17)

`g=1` 时，对所有奇数 `a>=7`，(22) 已在 `a=7` 成立：充分不等式变成
\[
2^{32}<5^{14},
\]
由 `5^7>2^16` 平方即得；更大的奇 `a` 仍单调更强。

只需检查 `a=3,5`。

### `a=3`

slope 给
\[
8\le M<80.
\]
又 `M=25m`、`m` 为奇 5-unit，所以只可能
\[
m\in\{1,3\}.
\]

此时 `R=7`。对 `w=1,3`，(17) 的最小正 residue 分别为
\[
15769,\qquad16089
\pmod{5^7=78125},
\]
均不可能等于 `1` 或 `3`。

### `a=5`

slope 给
\[
32\le M<320,
\]
所以 `m<13`。此时 `R=10`，`w=1,3` 的最小正 residue 分别为
\[
4359951,\qquad4361231
\pmod{5^{10}},
\]
再次远大于所有可能 `m`。

故
\[
\boxed{g=1\Longrightarrow\text{pure-2 empty}.}
\tag{27}

综合 (26)-(27)：
\[
\boxed{L=2^a\Longrightarrow\text{empty}.}
\tag{28}

---

## 12. 当前唯一 prime shape

small `L=1,2` 已由前文关闭；(6)、(8)、(28) 又关闭 mixed-high、`2*5^b` 与 pure-2。

因此当前 `k=2g,J=0` 若存在 candidate，必有
\[
\boxed{
L=5^b,
\qquad b\ge1.
}
\tag{29}

由 high 5 square parity 实际
\[
\boxed{b\ge2\text{ 且为偶数}.}
\tag{30}

并且 ultrathin gap 继续要求
\[
\boxed{5^b>H^2/95.}
\]

下一步只需处理这个 pure-5 / 2-adic resonance terminal。