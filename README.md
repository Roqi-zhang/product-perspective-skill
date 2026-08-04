# Product Perspective Skill

Make engineering plans and delivery results understandable to designers and other non-engineering collaborators—without diluting the technical truth.

This Skill adds product outcomes, benefits and tradeoffs, concrete risk decisions, strict change boundaries, reviewable acceptance paths, next-step recommendations, and approval-gated project progress recording.

## What it changes

| Situation | Without this Skill | With this Skill |
| --- | --- | --- |
| Plan | "Add a timeout state." | Explains which user is blocked, the tradeoff, the risk control, and whether the change should proceed. |
| Acceptance | "Tests pass." | Explains the visible product result, how a designer can verify it, what remains unverified, and the next recommended action. |
| Scope | "Also clean up adjacent code." | Keeps the requested change isolated and labels related work as out-of-scope advice. |

## Install in Codex

Clone this repository directly into Codex's user Skill directory:

```bash
git clone https://github.com/Roqi-zhang/product-perspective-skill.git \
  ~/.codex/skills/product-perspective
```

Restart or reload Codex if its Skill catalog is already open, then invoke it explicitly:

```text
$product-perspective Create an implementation plan for this workflow change.
```

Update with `git -C ~/.codex/skills/product-perspective pull --ff-only`. To remove it, delete only `~/.codex/skills/product-perspective`.

## Use in another Agent

Agents that can load a Markdown Skill can use the root [`SKILL.md`](SKILL.md) directly. Agents without native Skill discovery can copy [`adapters/generic-prompt.md`](adapters/generic-prompt.md) into their custom instructions, system prompt, or project rules.

| Support level | Meaning |
| --- | --- |
| Fully verified | Codex, using `agents/openai.yaml` and explicit `$product-perspective` invocation. |
| Rule-compatible | Any Agent that can load Markdown instructions and inspect/write local project files. |
| Read-only fallback | The Agent explains the proposed project-progress entry but does not write files. |

## Project progress behavior

For a writable local project, first use locates the project root, creates `PROGRESS.md` only when absent, and adds one idempotent recording rule to root `AGENTS.md`. Later progress entries are always shown first and are written only after explicit user approval. Secrets, private data, and disposable logs are never recorded.

## Quality and releases

Run `python3 scripts/validate.py` before contributing. The repository validates metadata, explicit Codex invocation, adapter parity, required publication files, and obvious sensitive-value patterns on every pull request.

Use semantic version tags. Treat changes to `SKILL.md` behavior, output structure, or progress-recording rules as release-note-worthy changes.

See [`examples/`](examples/) for expected behavior and [`tests/cases.md`](tests/cases.md) for the behavioral regression suite.
