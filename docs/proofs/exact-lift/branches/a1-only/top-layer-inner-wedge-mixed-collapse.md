# A1 top layer: uniform mixed-denominator collapse in the stable inner wedge

> 日期：2026-08-22。
>
> 依赖：`top-layer-inner-wedge-uniform-phase.md`、global `kappa` square、`decimal-height-synchronization.md`。
>
> 范围：
> \[
> d=2,\qquad r=s=1,
> \]
> 定义
> \[
> u:=2g-k,
> \qquad 1\le u\le g-1,
> \]
> 并假设稳定 prefix 条件
> \[
> \boxed{g-u\ge3}
> \]
>（等价于 `k-g>=3`）。

状态：**全部 mixed denominator shapes 严格为空。**

即若
\[
L=2^a5^b,
\qquad a,b>0,
\]
则不存在 candidate。

---

## 1. known generic high formulas

`top-layer-inner-wedge-uniform-phase.md` 已证明：

若
\[
a>u+1,
\]
则
\[
\boxed{
a\equiv u-1\pmod2,}
\qquad
\boxed{
H_2=2g+\frac{3(a-u)+1}{2}.
}
\tag{1}

因此真正 generic high 的最小 offset不是 `a-u=2`，而是
\[
\boxed{a-u\ge3,}
\]
从而
\[
\boxed{H_2\ge2g+5.}
\tag{2}

若
\[
b>u,
\]
则
\[
\boxed{b\equiv u\pmod2,}
\qquad
\boxed{
H_5=2g+\frac{3(b-u)}2.
}
\tag{3}

正的 parity-compatible offset至少为 2，所以
\[
\boxed{H_5\ge2g+3.}
\tag{4}

若两侧都 generic high，则 synchronization 给
\[
3(a-b)+1=0,
\]
已知无解。

下面只需处理 small strips。

---

# Part I. small 2-side

## 2. `1<=a<u`

固定
\[
1\le a<u.
\]
记
\[
e=v_2(w).
\]

因为 `a<u+1`，`kappa` square 的第一项严格更浅。直接 valuation 给
\[
v_2(W)=4g-3u+2e+a.
\]

两个 root-numerator terms 都从同一 depth
\[
B:=5g-4u+3e+a
\]
开始，并且除去 `2^B` 后均为 odd units。

exact conjugate product 的 depth 为
\[
\boxed{
v_2(X_+X_-)=2B+(u+1-a),
}
\tag{5}
而 difference 满足
\[
\boxed{
v_2(X_+-X_-)=B+1.}
\tag{6}

若 `a<=u-1`，(5)-(6) 给共轭 numerator depths
\[
\boxed{
\{v_2(X_+),v_2(X_-)\}
=\{B+1,\ B+u-a\}.
}
\tag{7}

raw denominator depth 为
\[
v_2(Y)=7g-5u+1+3e+2a.
\]
所以较大的 2-completion height恰为
\[
\boxed{
H_2^{\max}=2g-u+a\le2g-1.
}
\tag{8}

`L` 自身的 exponent `a` 更小，不改变该上界。

---

## 3. `a=u` 不可能

若
\[
a=u,
\]
则 (5) 变成
\[
v_2(X_+X_-)=2B+1.
\]
可是两个 numerator terms 仍都是 `2^B * odd` 的和/差，所以
\[
v_2(X_+)\ge B+1,
\qquad
v_2(X_-)\ge B+1.
\]
于是 product depth至少 `2B+2`，矛盾。

因此
\[
\boxed{a=u\Longrightarrow\text{empty}.}
\tag{9}

---

## 4. `a=u+1` resonance

此时 2-side square-inner 两项同深。unit cancellation至少一层，而 square parity强迫 extra depth为正偶数，所以至少为 2。

于是 root numerator 中非-`W` 项严格更浅，得到
\[
\boxed{H_2=2g+2.}
\tag{10}

综上 small 2-side 只有两种可能高度：
\[
\boxed{
1\le a\le u-1\Rightarrow H_2\le2g-1,
}
\]
\[
\boxed{
a=u+1\Rightarrow H_2=2g+2,
}
\]
而 `a=u` 已空。

---

# Part II. small 5-side

## 5. `1<=b<u`

若
\[
1\le b<u,
\]
5-side square 的第一项严格更浅。令 root numerator common depth
\[
B_5:=5g-4u+b.
\]

因为 `2` 是 5-adic unit，difference 本身已有 exact depth `B5`。conjugate product 给
\[
v_5(X_+X_-)=2B_5+(u-b).
\]
所以两个 depths 是
\[
\boxed{
\{B_5,\ B_5+u-b\}.
}
\tag{11}

raw denominator depth 为
\[
7g-5u+2b.
\]
因此较大的 5-completion height为
\[
\boxed{
H_5^{\max}=2g-u+b\le2g-1.
}
\tag{12}

---

## 6. `b=u` resonance

若
\[
b=u,
\]
square-inner 两项同深。unit cancellation与 square parity使 `W` term严格更深，root numerator 的另一项保持原 depth。于是
\[
\boxed{H_5=2g.}
\tag{13}

所以 small 5-side统一满足
\[
\boxed{b\le u\Longrightarrow H_5\le2g.}
\tag{14}

---

# Part III. all mixed shapes die

## 7. small-2 + high-5

若
\[
a\le u+1,
\qquad b>u,
\]
则：

- `a=u` 已由 (9) 排除；
- `a<=u-1` 时 `H2<=2g-1`；
- `a=u+1` 时 `H2=2g+2`。

而 generic high 5-side由 parity有
\[
H_5\ge2g+3.
\]
全部不能同步。

因此
\[
\boxed{a\le u+1,\ b>u\Longrightarrow\text{empty}.}
\tag{15}

---

## 8. high-2 + small-5

若
\[
a>u+1,
\qquad b\le u,
\]
则 generic high 2-side满足
\[
H_2\ge2g+5,
\]
而 (14) 给
\[
H_5\le2g.
\]
矛盾。

所以
\[
\boxed{a>u+1,\ b\le u\Longrightarrow\text{empty}.}
\tag{16}

---

## 9. small-small 由 real gap 排除

最后若
\[
a\le u+1,
\qquad b\le u,
\]
则
\[
L=2^a5^b
\le2^{u+1}5^u
=2\cdot10^u.
\tag{17}

另一方面 uniform phase theorem 给
\[
L>\frac{H^2}{40\cdot10^u}.
\tag{18}

因 `g-u>=3`：
\[
H=10^g\ge10^{u+3},
\]
所以
\[
\frac{H^2}{40\cdot10^u}
\ge\frac{10^{u+6}}{40}
>2\cdot10^u,
\]
与 (17) 矛盾。

所以 small-small 也空。

---

## 10. theorem

(15),(16)、generic high-high obstruction 与 §9 穷尽全部 `a,b>0`。

因此
\[
\boxed{
 d=2,\quad r=s=1,\quad g-u>=3,
 \quad L=2^a5^b,\ a,b>0
 \Longrightarrow\text{empty}.
}
\tag{19}

所以稳定 inner wedge 中只需继续处理两条坐标轴：
\[
\boxed{L=2^a}
\qquad\text{或}\qquad
\boxed{L=5^b}.
\]
