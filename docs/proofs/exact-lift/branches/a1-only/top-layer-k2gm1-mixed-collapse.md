# A1 top layer: `k=2g-1` mixed denominator collapse

> 日期：2026-08-22。
>
> 依赖：`top-layer-k2gm1-pure2-collapse.md`、`top-layer-k2gm1-pure5-collapse.md`、global `kappa` square、`decimal-height-synchronization.md`。
>
> 范围：
> \[
> d=2,\qquad r=s=1,\qquad g\ge4,\qquad k=2g-1,
> \]
> 且
> \[
> L=2^a5^b,\qquad a,b>0.
> \]

状态：**已严格关闭全部 mixed prime shapes。**

---

## 1. common local table

令
\[
e:=v_2(w)\in\{0,1,2\}.
\]
对 `g>=4`，显式 prefix 给
\[
v_2(N)=2e,
\qquad
v_2(K)=2g-2+2e,
\]
\[
v_5(N)=0,
\qquad
v_5(K)=2g-2.
\tag{1}
\]

base integer 的 valuations 为
\[
v_2(10^gQG)=3g-2+e,
\qquad
v_5(10^gQG)=3g-2.
\tag{2}

若
\[
L=2^a5^b,
\qquad a,b>0,
\]
则 `(L,M)=1` 使两侧都真正超过 base：
\[
\boxed{v_2(\kappa)=3g-2+e+a,}
\qquad
\boxed{v_5(\kappa)=3g-2+b.}
\tag{3}

此外 off-diagonal phase gap 对任意 `L` 给
\[
L>H^2/400,
\qquad H=10^g.
\tag{4}
所以 `g>=4` 时极小的 `(a,b)` 组合本身也不可能承载整个 denominator。

---

## 2. generic 2-high side：`a>=3`

由 `kappa` square，2-side 两个 inner terms 的 depth 差为
\[
a-2.
\]
若
\[
a\ge3,
\]
则第二项严格更浅，得到
\[
v_2(W^2)=8g-4+4e+a.
\]
因此 square parity 强迫
\[
\boxed{a\text{ 为偶数}.}
\tag{5}
特别地
\[
\boxed{a\ge4.}
\]

root numerator / denominator 的 exact valuation 给
\[
\boxed{
H_2=2g-1+\frac{3a}{2}.
}
\tag{6}

---

## 3. generic 5-high side：`b>=2`

5-side 两个 square-inner terms 的 depth 差为
\[
b-1.
\]
若
\[
b\ge2,
\]
第二项严格更浅：
\[
v_5(W^2)=8g-5+b.
\]
所以 square parity 强迫
\[
\boxed{b\text{ 为奇数}.}
\tag{7}
即
\[
\boxed{b\ge3.}
\]

此时 exact completion height 为
\[
\boxed{
H_5=2g+\frac{3b-3}{2}.
}
\tag{8}

---

## 4. mixed-high `a>=3,b>=2` 不可能

由 (5),(7)，实际
\[
a\ge4\text{ even},
\qquad
b\ge3\text{ odd}.
\]

exact decimal-height synchronization 要求 (6)=(8)：
\[
2g-1+\frac{3a}{2}
=
2g+\frac{3b-3}{2}.
\]
整理为
\[
\boxed{3(a-b)=-1,}
\]
无整数解。

因此
\[
\boxed{a\ge3,\ b\ge2\Longrightarrow\text{empty}.}
\tag{9}

---

## 5. `a=1` 甚至不能通过 global square terminal

现在假设
\[
a=1.
\]

2-side 有
\[
v_2(\kappa)=3g-1+e.
\]
在 `W^2` 中第一项比第二项浅恰一层，所以若 `W` 真是整数平方根，则
\[
\boxed{v_2(W)=4g-2+2e.}
\tag{10}

两个 root numerator
\[
X_\pm=\kappa G^2C\pm(\kappa+G)W
\]
中的两项都有同一 exact depth
\[
B:=5g-3+3e,
\]
且除去 `2^B` 后两项均为 odd。
因此
\[
\boxed{v_2(X_+)\ge B+1,\qquad v_2(X_-)\ge B+1.}
\tag{11}

可是 exact conjugate product
\[
X_+X_-
=-\kappa(\kappa+2G)
\left(
\kappa^2G^2C^2-D^2N(\kappa+G)^2
\right)
\]
在当前 `a=1` 的 valuation 是
\[
\boxed{v_2(X_+X_-)=2B+1.}
\tag{12}

(11) 却要求左边至少有 depth `2B+2`，矛盾。

所以
\[
\boxed{a=1\Longrightarrow\text{empty}.}
\tag{13}

---

## 6. `a=2,b>=2` 不可能

取
\[
a=2.
\]
2-side square-inner 两项同深。除去公共 2-power 后是 odd-odd difference，所以至少额外消掉一层；总 square parity 又迫使额外 cancellation depth为偶数，故至少为 2。

于是 `W` term 比另一个 root-numerator term严格更深，两个 signs 都有 exact reduced 2-denominator completion height
\[
\boxed{H_2=2g+2.}
\tag{14}

另一方面若 `b>=2`，由 §3 实际 `b>=3` odd，因此
\[
H_5
=2g+\frac{3b-3}{2}
\ge2g+3.
\]
不能同步。

所以
\[
\boxed{a=2,\ b>=2\Longrightarrow\text{empty}.}
\tag{15}

---

## 7. 最后一条 strip：`b=1`

现在取
\[
b=1.
\]

若 `a>=3`，由 §2 实际 `a>=4` even，且
\[
H_2\ge2g+5.
\tag{16}

5-side 此时 square-inner 两项同深。除去 common 5-power 后发生 unit cancellation；square parity 使额外 cancellation depth至少为 2。结果 `W` term在两个 root numerators 中都比另一项更深，故 exact reduced 5-height为
\[
\boxed{H_5=2g.}
\tag{17}

(16),(17) 不可能同步。

剩余 `(a,b)=(1,1),(2,1)` 已由 (4) 直接排除：
\[
L\le20
\]
而 `g>=4` 时
\[
H^2/400\ge250000.
\]

因此
\[
\boxed{b=1\Longrightarrow\text{empty}.}
\tag{18}

---

## 8. closure

mixed branch 的全部可能性已被 (9),(13),(15),(18) 穷尽。

所以
\[
\boxed{
 d=2,\quad r=s=1,\quad g>=4,\quad k=2g-1,
 \quad a,b>0
 \Longrightarrow\text{empty}.
}
\tag{19}

结合 pure-2、pure-5 closure 与 `g=2,3` full small-layer certificate，整个 `k=2g-1` boundary 已无剩余 prime shape。
