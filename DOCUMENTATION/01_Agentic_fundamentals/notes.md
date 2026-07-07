# Agent Fundamentals

## 1. What is an AI Agent?

An AI Agent is an autonomous software system that uses a Large Language Model (LLM), memory, planning, and tools to accomplish a user's goal.

In simple terms:

> **Agent = Model + Harness**

- **Model:**  Performs reasoning and generates responses.
- **Harness:** Provides the model with the right context, tools, and execution flow.

Unlike an LLM, an AI Agent can plan tasks, use tools, maintain memory, and perform multi-step execution.

---

## 2. Agent Lifecycle

```
User Request
      │
      ▼
Perceive Input
      │
      ▼
Understand Context
      │
      ▼
Reason & Plan
      │
      ▼
Select Required Tools
      │
      ▼
Execute Action
      │
      ▼
Observe Result
      │
      ▼
Goal Achieved?
      │
 ┌────┴────┐
 │         │
No        Yes
 │         │
 ▼         ▼
Re-plan  Final Response
```

### Explanation

- **Perceive** – Receive the user's request.
- **Understand Context** – Analyze the request.
- **Reason & Plan** – Decide how to solve it.
- **Select Tools** – Choose the required tool.
- **Execute** – Perform the action.
- **Observe** – Check the output.
- **Re-plan** – Repeat if needed.
- **Final Response** – Return the result.

---

## 3. LLM vs AI Agent

| LLM | AI Agent |
|------|----------|
| Stateless | Stateful |
| Generates text | Performs actions |
| No planning | Has planning |
| No tools | Uses tools |
| No memory | Can maintain memory |
| One-shot response | Multi-step execution |

---

## 4. Agent Architecture

```
User
 │
 ▼
Prompt
 │
 ▼
LLM
 │
 ▼
Planner
 │
 ▼
Tools
 │
 ▼
Executor
 │
 ▼
Observation
 │
 ▼
Memory
 │
 ▼
Final Response
```

