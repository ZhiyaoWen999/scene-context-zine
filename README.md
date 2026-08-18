# 场景语境纸刊 · Scene Context Zine

**Context-first reconstruction and maintenance: zhiyaowen**

这是对 [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) 的一次 **context-first 重构**。它保留人物切出、非规则裁切、分割、撕纸、跨边界延伸和纸张触感，同时把原先较固定的奶油纸、大片留白、高纯度单色、强制极简和固定 3:5，改成由照片本身决定的可选模块。

核心变化只有一句话：

> 先锁定不可丢失的场景 DNA，再选择设计语言。

这次重构只聚焦原项目的“实景拼贴”路径；`scene-distillation-zine-v1-3` 本来就以脱离原照片、重新创作为目标，因此没有被并入。新 Skill 名称不同，可与原有两个 Skill 并存，不会覆盖旧版。

## 这版解决什么

- 白墙、木墙、咖啡色室内不再自动变成同一张米色纸。
- 背景不再只按“复杂不复杂”决定删除，而按“是否承载地点与记忆”决定。
- 默认使用原生色盘；高饱和对比色降为可选模式。
- 默认轻度抽象；不再自动删除 60–80% 细节。
- RISO、Xerox、撕纸和纸纤维变成局部材料，而不是全局滤镜。
- 地点、日期、时间、菜单、票据与地图可作为真实记忆线索，不再一律排除。

## 架构

```text
SCENE CORE（强制）
├── identity anchors
├── spatial invariants
├── context-bearing regions
├── environmental palette
├── light / material / density
└── memory cues + semantic detail map
          ↓
PRIMARY ROUTE（四选一）
├── Documentary Editorial
├── Multi-frame Joiner
├── Graphic Scene Poster
└── Gathered Collage
          ↓
INDEPENDENT MODULES
├── field tone
├── palette
├── abstraction
├── material / print
└── typography / memory layer
```

## 四条路线

| 路线 | 适合 | 照片保留 | 主要变化 |
| --- | --- | ---: | --- |
| Documentary Editorial | 咖啡馆、室内、白色空间、细腻光线 | 65–100% | 网格、留边、轻裁切、小字 |
| Multi-frame Joiner | 旅行、街道、复杂背景、动作 | 55–100% | 多个源照片片段、重叠、时间/视角变化 |
| Graphic Scene Poster | 建筑、风景、地标、招牌 | 40–80% | 尺度变化、源自现场的图形平面、明确层级 |
| Gathered Collage | 想保留原来的手撕纸刊气质 | 25–60% | 人物切出、非规则撕边、插画续接、选择性印刷 |

## 安装

将下面这个目录复制到 Codex 的用户级 skills 目录：

```text
.agents/skills/scene-context-zine
```

Windows PowerShell 示例：

```powershell
Copy-Item -Recurse -LiteralPath '.\.agents\skills\scene-context-zine' -Destination "$env:USERPROFILE\.agents\skills\scene-context-zine"
```

macOS / Linux 示例：

```bash
cp -R ./.agents/skills/scene-context-zine ~/.agents/skills/
```

如 Skill 没有立即出现，请重启 Codex。

## 使用

直接生成：

```text
用 $scene-context-zine 重构这张咖啡馆照片。保留木墙、白桌、暖灯和窗外冷光，路线由你选择。
```

先比较路线：

```text
用 $scene-context-zine 给这张旅行照片做四条 route preview，先不要生成。
```

指定路线：

```text
用 $scene-context-zine 的 Multi-frame Joiner 路线处理这张街景；保留店招、路面颜色和人物方向。
```

只输出 Prompt / Scene Contract：

```text
用 $scene-context-zine 分析这张照片，输出 Scene Contract 和最终生图提示词，不要生成图片。
```

## 结构

```text
scene-context-zine/
├── LICENSE
├── README.md
├── .agents/
│   └── skills/
│       └── scene-context-zine/
│           ├── SKILL.md
│           ├── agents/openai.yaml
│           ├── references/
│           └── scripts/
└── tests/
    └── fixtures/
```

## A/B 测试建议

选 5–10 张曾经暴露问题的照片，固定原图与文字，分别运行：

1. Documentary Editorial；
2. Multi-frame Joiner；
3. Graphic Scene Poster；
4. Gathered Collage。

只评价五件事：地点是否还在、背景色是否正确、光线是否正确、语义物件是否保留、四条路线是否真的不同。不要先用“好不好看”掩盖场景身份的丢失。

## 结构校验

项目附带四份有效 Scene Plan 和一份故意失败的回归样例。可用标准 Python 运行：

```bash
python ./.agents/skills/scene-context-zine/scripts/lint_scene_plan.py \
  ./tests/fixtures/01-cafe-documentary.json \
  ./tests/fixtures/02-city-joiner.json \
  ./tests/fixtures/03-mountain-poster.json \
  ./tests/fixtures/04-gathered-collage.json
```

校验器会检查 Scene Core 是否完整、是否真的引用原图、照片占比是否落在路线护栏内、是否凭空增加颜色，以及最终提示词是否用艺术家姓名代替可见形式描述。

## 来源与修改声明

- 原项目与视觉 Skill 作者：**Zeejay0**。
- 原项目：[github.com/Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill)。
- 重构基线：commit `eae9a62e20cb570c0adabc94cb189b1c91b7be99`（2026-08-17）。
- Context-first 重构与维护：**zhiyaowen**。
- 本项目中的 `scene-context-zine`、测试与本 README 均为 2026-08-18 的修改版本，不是官方上游版本。
- 原作者网站：[zeejayzine.com](https://zeejayzine.com/)。

## License

沿用原项目的 **个人、非商业许可证**。许可证原文保存在 [LICENSE](LICENSE)；商业使用、客户项目、收费生成、SaaS/API、培训或其他商业化用途均需先获得 Zeejay0 的书面许可。
