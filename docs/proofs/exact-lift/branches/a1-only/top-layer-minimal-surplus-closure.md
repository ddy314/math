# A1 top layer: complete minimal-surplus closure

> 日期：2026-08-22。
>
> 范围：A1 最高层
> \[
> d=s_1-g=2
> \]
> 的最小双 surplus
> \[
> r=m_1-2k=1,
> \qquad
> s=m_2+g-k=1.
> \]

状态：**严格关闭。** 本文件只做 sector exhaustion；所有局部关闭均由下列已完成 theorem / exact certificate 提供。

最终结论：
\[
\boxed{
 d=2,\qquad r=s=1
 \Longrightarrow\text{empty}.
}
\tag{1}

---

## 1. parameter range is already `1<=g<=k`

`top-layer.md` 的 minimal-surplus kernel 在 `r=s=1` 上已经严格得到
\[
\boxed{1\le g\le k.}
\tag{2}
\]
因此不存在额外 `g=0` corridor，也不存在 `k<g` corridor。

所以只需穷尽 `1<=g<=k`。

---

## 2. diagonal `k=g`

`minimal-diagonal-closure.md` 已证明
\[
\boxed{k=g\Longrightarrow\text{empty}}
\tag{3}
\]
对全部 `g>=1` 成立。

---

## 3. far off-diagonal `k>=2g+1`

`top-layer-minimal-offdiagonal-far-collapse.md` 已证明
\[
\boxed{k\ge2g+1\Longrightarrow\text{empty}.}
\tag{4}

---

## 4. boundary `k=2g`

`top-layer-k2g-closure.md` 汇总该边界的 primitive pruning、ultrathin gap、prime-shape collapse 与 pure-5 exact certificate，得到
\[
\boxed{k=2g\Longrightarrow\text{empty}.}
\tag{5}

---

## 5. inner wedge `g<k<2g`

令
\[
c:=k-g\in\{1,2,\ldots,g-1\}.
\]

### 5.1 stable corridor `c>=3`

`top-layer-inner-wedge-stable-closure.md` 已由 uniform phase theorem、mixed collapse、pure-2 collapse 与 pure-5 collapse 得到
\[
\boxed{c\ge3\Longrightarrow\text{empty}.}
\tag{6}

### 5.2 final corridors `c=1,2`

`top-layer-final-corridor-reduction.md` 首先把 mixed shapes 解析关闭，并把 pure axes 压到七个小层。

`top-layer-final-corridor-certificate.md` 随后用 exact integer certificate 完整检查这些小层。certificate 的最终断言为

```text
phase_states=26
terminal_tests=37
survivors=0
```

因此
\[
\boxed{c\in\{1,2\}\Longrightarrow\text{empty}.}
\tag{7}

所以整个 inner wedge 为空。

---

## 6. exhaustion

由 (2)，任何 `r=s=1` candidate 必满足 `1<=g<=k`。互斥地：

1. `k=g`；
2. `g<k<2g`；
3. `k=2g`；
4. `k>=2g+1`。

(3)--(7) 分别关闭四类，没有剩余整数区域。因此得到 (1)：
\[
\boxed{
 d=2,\qquad r=s=1
 \Longrightarrow\varnothing.
}
\]

---

## 7. next frontier

这只关闭最高层的 **minimal-surplus** cell，不等价于关闭整个 `d=2`，更不等价于 A1 overall closure。

`top-layer.md` 对 `g>=1` 只先验给
\[
r\ge1,\qquad s\ge1.
\]
所以当前 `d=2` 真正剩余前沿是
\[
\boxed{r+s\ge3.}
\]
下一步应把 minimal-surplus 中成功的 coprime-residue / ultrathin-tail 机制推广到 `r>1` 或 `s>1`，而不是继续研究已关闭的 `r=s=1` cell。