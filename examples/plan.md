# Plan example — avoid duplicate generation requests

## Input

> Add a disabled state to the Generate button while a generation request is being created.

## Expected response characteristics

The response should say that users cannot accidentally create multiple generation tasks while a slow network makes the first click appear unresponsive. It should keep the scope to the button and request flow, rather than redesigning the generation page.

It should weigh a client-only disabled state against server-side idempotency, recommend both when duplicate task creation has a material cost, and state that a client-only state reduces but cannot fully prevent duplicate requests.

Its risk card should connect retrying or double-clicking to duplicate tasks, extra quota consumption, and confusing duplicate results. It should include the condition to proceed: the request has an in-flight state and the service can reject duplicate request identifiers.
