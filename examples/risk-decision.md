# Risk decision example — remove a confirmation dialog

## Input

> Remove the confirmation dialog before deleting a workflow to make the operation faster.

## Expected response characteristics

The response should not assume the change is good. It should compare the speed benefit with accidental deletion, lost work, and recovery cost. It should suggest a safer alternative such as undo, soft delete, or a confirmation only for published workflows.

The risk card should make clear that the risk is only partly avoidable when deletion is irreversible. It should recommend proceeding only when recovery exists and the destructive action is visually unambiguous; otherwise it should recommend against removing confirmation.
