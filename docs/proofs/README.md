# 证明资料

当前唯一的主研究树是 [三块十进制拼接 Exact Lift](exact-lift/README.md)。

证明资料采用以下层次：

```text
proofs/
└── exact-lift/
    ├── problem-and-carrier.md     # 原问题、统一符号、carrier 分支
    ├── global-framework.md        # 整数球面、尾正规化、统一判别式
    ├── branches/
    │   ├── a2-only/               # A2 主干与按依赖合并的专题文件
    │   ├── double-deficit/        # DD 主干与统一 frontier 文件
    │   └── a1-only/               # A1 框架、top layer 与 diagonal
    ├── status.md                  # 严格状态、剩余核心、优先级
    ├── notation.md                # 统一符号和旧符号映射
    ├── dependency-map.md          # 公式依赖图
    ├── conclusion.md              # 当前研究结论
    └── archive/                   # 原始总稿快照
```

树中的章节文件是日常阅读和修改入口；三个分支目录中的 `README.md` 给出各自的唯一阅读路线；`archive/` 只用于历史对照。任何新增结果都应落到最具体的专题文件，并回写分支 README、状态索引和依赖图。
