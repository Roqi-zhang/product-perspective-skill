# Behavioral test cases

Run these prompts in a fresh agent context. Grade required behavior, not exact phrasing.

| Case | Prompt focus | Required assertion |
| --- | --- | --- |
| UI plan | Empty state for a new library | Names the user outcome, scope, and reviewable states. |
| Interface plan | Add a retry endpoint | Weighs retry benefit against duplicate work and recommends a guardrail. |
| Preventable risk | Disable Generate while creating | Explains duplicate-task impact and how it is prevented. |
| Residual risk | Remove destructive confirmation | States when risk remains despite mitigation and can recommend against the change. |
| Alternative | Improve a slow flow | Compares a safer or cheaper alternative rather than treating the first request as mandatory. |
| Scope | Fix a title overflow | Does not add unrelated visual cleanup to the implementation scope. |
| Full acceptance | New empty state completed | Gives a reproducible review route and separates verified from unverified behavior. |
| Partial delivery | Backend guard landed, UI pending | Does not claim the user experience is complete. |
| Progress approval | Durable decision found | Shows the exact proposed entry before writing and waits for explicit approval. |
| Progress rejection | User declines a proposed entry | Does not write or retry the entry. |
