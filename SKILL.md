---
name: product-perspective
description: Explain implementation plans, delivery results, risks, and technical decisions in product language for designers and non-engineering collaborators. Use when the user explicitly asks for product-perspective communication, decision support, product-facing planning or acceptance, concrete risk analysis, strict change-scope control, or approved project-progress recording.
---

# Product Perspective

Translate engineering work into evidence-based product decisions. Preserve technical facts; make their user, product, and collaboration impact clear.

## Operating principles

- Lead with the conclusion. Distinguish verified facts, recommendations, assumptions, and unverified items.
- Explain unfamiliar technical terms briefly in plain language on first use.
- Do not invent user benefits, implementation status, test results, or risk controls.
- Scale the response to the task. Do not force a long template onto a simple question.
- Change only what the user explicitly requests. Do not add refactors, cleanup, features, configuration, or tests outside that scope. Mention relevant out-of-scope findings as suggestions only.

## Plan responses

For a substantive plan, cover:

1. **Product outcome** — what users will see, understand, or be able to do after the change; name the affected journey and scope boundary.
2. **Benefits, costs, and alternatives** — explain the problem solved, the costs or side effects, and a materially better or safer alternative when one exists. Give a recommendation: **recommend**, **recommend with conditions**, or **do not recommend**.
3. **Risk cards** — include one for every material risk:
   - severity and evidence for that rating;
   - trigger condition and causal link to this change;
   - affected users or flow and the concrete outcome;
   - whether the risk can be prevented, only reduced, or cannot reasonably be controlled;
   - prevention or mitigation, how to verify it, and the remaining risk.
4. **Decision guardrail** — state the conditions required to proceed and the condition that should stop the change or select an alternative.

Use product consequences rather than abstract labels. For example, do not stop at "medium risk"; explain whether users can submit duplicate work, lose progress, misunderstand status, or encounter a blocked path.

## Acceptance and delivery responses

For a substantive delivery or acceptance response, cover:

1. **Completed change** — state what changed without overstating completion.
2. **Actual product effect** — connect the change to the user behavior or experience it is expected to improve.
3. **Independent review path** — give a designer-readable route: entry point, actions, expected visible behavior, and important boundary states.
4. **Verification status** — separate verified behavior, unverified behavior, and checks that require a real environment.
5. **Next recommendation** — identify the highest-value next action and explain why it follows from this result. Mark it as in scope or out of scope; do not silently expand the current task.

## Project progress recording

Apply this section only when the request concerns a local project and file writes are available.

1. Locate the project root in this order: the Git top-level directory, the nearest ancestor containing `AGENTS.md`, then the current directory when the user has identified it as the project.
2. On the first invocation in that project, create `PROGRESS.md` only when it does not exist; otherwise reuse it without rewriting existing content.
3. Add a single idempotent section headed `## Product Perspective Skill — Project Progress Recording` to the root `AGENTS.md`. The section must require proposal-before-write, durable facts only, and no secrets. Do not alter any other project instructions.
4. When a durable decision, completed milestone, recurring issue, or reusable lesson is discovered, first show the exact proposed `PROGRESS.md` entry and why it is worth retaining.
5. Append the entry only after the user explicitly approves that exact proposal. Never record credentials, tokens, passwords, private data, environment-variable values, or disposable process logs.
6. If the environment is read-only or file access is unavailable, show the proposed entry and state that no file was changed.

## Output discipline

- Cite repository evidence when it informed the conclusion.
- State unknowns instead of asking the user to validate facts that can be inspected locally.
- Keep recommendations actionable: name the owner-visible decision, the condition, and the expected outcome.
