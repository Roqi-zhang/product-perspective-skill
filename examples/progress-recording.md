# Project-progress example — approval required

## Situation

The agent has completed a durable decision: generation requests will use server-side idempotency keys to prevent duplicate tasks.

## Expected interaction

Before writing, the agent should show:

> Proposed `PROGRESS.md` entry: "Generation creation uses server-side idempotency keys. This prevents repeated clicks or network retries from creating duplicate tasks and consuming extra quota."
>
> Reason: this is a lasting reliability and product-cost decision that future work on generation retries must preserve.

The agent must wait for an explicit approval. A response such as "looks good" or silence is not approval unless the user unambiguously authorizes the write. It must never include request tokens, IDs that identify private users, or environment values.
