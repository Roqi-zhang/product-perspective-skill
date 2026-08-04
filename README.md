# Product Perspective Skill / 产品视角 Skill

Make engineering plans and delivery results understandable to designers and other non-engineering collaborators—without diluting the technical truth.

让设计师和其他非工程协作者能够清晰理解工程计划与交付结果，同时保留技术事实，不把复杂问题简单化。

This Skill adds product outcomes, benefits and tradeoffs, concrete risk decisions, strict change boundaries, reviewable acceptance paths, next-step recommendations, and approval-gated project progress recording.

这个 Skill 会补充产品效果、改动利弊、具象风险决策、严格改动边界、可执行的验收路径、下一步建议，以及需要用户批准后才写入的项目进度记录。

## What it changes / 它解决什么问题

| Situation / 场景 | Without this Skill / 使用前 | With this Skill / 使用后 |
| --- | --- | --- |
| Plan / 计划 | “Add a timeout state.”<br>“增加一个超时状态。” | Explains which user is blocked, the tradeoff, the risk control, and whether the change should proceed.<br>说明影响哪类用户、有哪些利弊、风险如何控制，以及是否建议继续。 |
| Acceptance / 验收 | “Tests pass.”<br>“测试通过。” | Explains the visible product result, how a designer can verify it, what remains unverified, and the next recommended action.<br>说明实际产品效果、设计师如何复核、哪些内容尚未验证，以及下一步建议。 |
| Scope / 范围 | “Also clean up adjacent code.”<br>“顺便清理相关代码。” | Keeps the requested change isolated and labels related work as out-of-scope advice.<br>只实现用户明确提出的内容，范围外问题只作为建议，不偷偷扩大改动。 |

## Core behavior / 核心能力

- **Product-facing plans / 产品侧计划**：describe product effect, scope, benefits, costs, alternatives, recommendation, and concrete risk cards.<br>说明产品效果、范围、利弊、替代方案、推荐结论和具象风险卡。
- **Designer-readable acceptance / 设计师可理解的验收**：describe completed changes, actual effect, review steps, verified and unverified items, and the next action.<br>说明完成的改动、实际效果、复核步骤、已验证与未验证项，以及下一步行动。
- **Strict scope control / 严格范围控制**：change only what the user explicitly requested.<br>只改动用户明确提出的内容。
- **Approval-gated progress / 用户批准后记录进度**：propose durable project-progress entries first and write them only after explicit approval.<br>先展示拟写入的长期项目进度，获得明确批准后才写入。

## Install in Codex / 在 Codex 中安装

Clone this repository directly into Codex's user Skill directory.

将仓库直接克隆到 Codex 的用户 Skill 目录：

```bash
git clone https://github.com/Roqi-zhang/product-perspective-skill.git \
  ~/.codex/skills/product-perspective
```

Restart or reload Codex if its Skill catalog is already open, then invoke it explicitly.

如果 Codex 已经打开 Skill 列表，请重启或重新加载，然后显式调用：

```text
$product-perspective Create an implementation plan for this workflow change.
```

Update with `git -C ~/.codex/skills/product-perspective pull --ff-only`. To remove it, delete only `~/.codex/skills/product-perspective`.

更新命令：`git -C ~/.codex/skills/product-perspective pull --ff-only`。卸载时只删除 `~/.codex/skills/product-perspective`。

## Use in another Agent / 在其他 Agent 中使用

Agents that can load a Markdown Skill can use the root [`SKILL.md`](SKILL.md) directly. Agents without native Skill discovery can copy [`adapters/generic-prompt.md`](adapters/generic-prompt.md) into their custom instructions, system prompt, or project rules.

能够加载 Markdown Skill 的 Agent 可以直接使用根目录的 [`SKILL.md`](SKILL.md)。不支持原生 Skill 发现机制的 Agent，可以把 [`adapters/generic-prompt.md`](adapters/generic-prompt.md) 复制到自定义指令、系统提示词或项目规则中。

| Support level / 支持级别 | Meaning / 含义 |
| --- | --- |
| Fully verified / 完整验证支持 | Codex, using `agents/openai.yaml` and explicit `$product-perspective` invocation.<br>Codex，通过 `agents/openai.yaml` 和显式 `$product-perspective` 调用。 |
| Rule-compatible / 规则兼容 | Any Agent that can load Markdown instructions and inspect/write local project files.<br>能够读取 Markdown 指令并检查或写入本地项目文件的 Agent。 |
| Read-only fallback / 只读降级 | The Agent explains the proposed project-progress entry but does not write files.<br>Agent 只展示拟写入的项目进度，不写入文件。 |

## Project progress behavior / 项目进度记录

For a writable local project, the first use locates the project root, creates `PROGRESS.md` only when absent, and adds one idempotent recording rule to root `AGENTS.md`. Later progress entries are always shown first and are written only after explicit user approval. Secrets, private data, and disposable logs are never recorded.

对于可写入的本地项目，首次使用时会定位项目根目录，仅在不存在时创建 `PROGRESS.md`，并在根目录 `AGENTS.md` 中加入幂等的记录规则。后续发现重要进度时，先展示拟写入内容，只有用户明确批准后才写入。不会记录凭据、私人数据或一次性过程日志。

## Quality and releases / 质量与版本

Run `python3 scripts/validate.py` before contributing. The repository validates metadata, explicit Codex invocation, adapter parity, required publication files, and obvious sensitive-value patterns on every pull request.

贡献前运行 `python3 scripts/validate.py`。仓库会在每个 Pull Request 中校验元数据、Codex 显式调用配置、适配文档一致性、发布必需文件和明显的敏感信息模式。

Use semantic version tags. Treat changes to `SKILL.md` behavior, output structure, or progress-recording rules as release-note-worthy changes.

使用语义化版本标签。凡是修改 `SKILL.md` 行为、输出结构或进度写入规则，都应在 Release Notes 中说明。

See [`examples/`](examples/) for expected behavior and [`tests/cases.md`](tests/cases.md) for the behavioral regression suite.

行为示例见 [`examples/`](examples/)，回归测试用例见 [`tests/cases.md`](tests/cases.md)。
