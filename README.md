```
<button type="submit">Confirm</button>
<button type="button">Cancel</button>
<button type="reset">Cancel</button>
```
- Primary button (type="submit") confirms the action.
- Secondary button (type="button") performs a cancel or close operation, but the functionality can be defined via JavaScript or another mechanism.
- or Secondary buttons (like type="reset") can suggest a secondary or alternative action that doesn’t finalize anything, such as "Cancel", "Back", or "Reset".

only having two options:

```
<button>Click</button> (<button type="button">Click</button>)
<button type="reset">Cancel</button>
```


- Using type="button" for primary actions communicates that the button is meant to trigger an important or final action.
- Using type="reset" for secondary actions (like canceling or reverting) semantically aligns the button's purpose with its function, which is often to undo changes or clear input fields.
