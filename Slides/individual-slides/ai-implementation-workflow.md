---
marp: true
theme: default
paginate: true
ai_generated: true
model: "openai/gpt-5.4@2026-03-22"
operator: "johnmillerATcodemag-com"
chat_id: "ai-implementation-workflow-20260322"
prompt: |
  create a marp deck explaining the following content:

  ## Section 8: AI Implementation Workflow (Duration: ~00:10:00)

  **Time Range**: 01:11:51 - 01:21:50

  ### Key Topics

  - Getting AI implementation proposals
  - Verifying AI understanding of issues
  - Starting implementation execution
  - Implementation monitoring

  ### Subsection 8.1: Implementation Request Process

  #### Best Practice Workflow

  1. **Request Proposal First**: Don't execute immediately
     - "Propose implementation to address issue"
     - Review what AI thinks it will do
     - Verify understanding before execution

  2. **Review Proposed Fix**
     - AI reads issue description
     - AI proposes specific fix
     - Human reviews for completeness

  3. **Identify Gaps**
     - Check for missing steps
     - Example: JWT issue didn't include GitHub removal steps
     - Add requirements before proceeding

  4. **Proceed with Implementation**
     - "Go ahead with the implementation"
     - Can reference conversation on different machine later
     - Save implementation plan as reference

  ### Subsection 8.2: Multi-Tasking with AI

  **Concurrent Work**:

  - Can start implementation in one session
  - Continue with other tasks
  - Monitor progress via notifications
  - AI works autonomously once started

  ### Preview of Next Topic

  **Instructor Note**: Will demonstrate multi-implementation comparison

  - Technique for evaluating pros and cons
  - Compare different solutions to problems
  - Find and evaluate alternatives
started: "2026-03-22T02:42:27Z"
ended: "2026-03-22T02:47:10Z"
task_durations:
  - task: "slide authoring"
    duration: "00:04:43"
total_duration: "00:04:43"
ai_log: "ai-logs/2026/03/22/ai-implementation-workflow-20260322/conversation.md"
source: "johnmillerATcodemag-com"
---

## AI Implementation Workflow

- Getting AI implementation proposals
- Verifying AI understanding of issues
- Starting implementation execution
- Implementation monitoring

::: notes
Use this slide to orient the audience to the flow of the segment. Explain that the process starts before any code is written, because the first step is to see what the AI thinks the problem is and how it plans to solve it. Emphasize that the four topics form a natural sequence and that skipping the early review steps usually creates rework later. Spend about one minute here, then transition into the detailed implementation request process.
:::

---

## Best Practice: Request a Proposal First

1. **Request Proposal First**
   - "Propose implementation to address issue"
   - Review what AI thinks it will do
   - Verify understanding before execution

2. **Review Proposed Fix**
   - AI reads issue description
   - AI proposes specific fix
   - Human reviews for completeness

::: notes
Explain that the best first prompt is not "implement this now" but "propose implementation to address the issue." That gives you a chance to inspect the AI's understanding before it starts changing files, which is especially useful on brownfield systems. Point out that the human role here is not passive approval; it is active review for scope, assumptions, and missing details. Spend about two minutes here and tell the audience this is often the difference between one clean run and several correction cycles.
:::

---

## Identify Gaps Before Execution

3. **Identify Gaps**
   - Check for missing steps
   - Example: JWT issue did not include GitHub removal steps
   - Add requirements before proceeding

4. **Proceed with Implementation**
   - "Go ahead with the implementation"
   - Can reference conversation on different machine later
   - Save implementation plan as reference

::: notes
Walk through the idea that a proposal can be directionally right and still incomplete. Use the JWT example to show how an AI may understand the main bug but miss adjacent work, such as removing a related GitHub integration or updating dependent configuration. Once the proposal is complete, you can explicitly authorize execution with something like "go ahead with the implementation" and preserve that plan for later reference, even from another machine. Spend about two minutes here and reinforce that requirement clarification before coding is cheaper than cleanup after coding.
:::

---

## Multi-Tasking with AI

### Concurrent Work

- Start implementation in one session
- Continue with other tasks
- Monitor progress via notifications
- AI works autonomously once started

::: notes
Describe this as one of the most practical productivity benefits of modern AI tooling. Once the implementation task is well-scoped and approved, you can let the AI work while you continue with documentation, reviews, or another investigation. Emphasize that autonomy is not the same as abandonment; the human still monitors progress, watches notifications, and steps in if the task drifts or new information appears. Spend about ninety seconds here and connect it to how engineers naturally juggle multiple parallel activities during a workday.
:::

---

## Next: Compare Multiple Implementations

**Preview of Next Topic**

- Evaluate pros and cons of different approaches
- Compare different solutions to the same problem
- Find and assess alternatives before choosing

::: notes
Close by previewing the next teaching move: comparing multiple implementations instead of accepting the first reasonable answer. Explain that once students know how to get and approve one implementation, the next maturity step is evaluating alternatives for trade-offs like simplicity, safety, and maintainability. This sets up a useful bridge to the next topic while reinforcing that AI can generate options, but humans still choose among them. Spend about one minute here and then hand off to the demo or next section.
:::
