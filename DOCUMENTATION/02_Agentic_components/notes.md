# Agent Components

AI Agents are built using multiple components that work together to understand a user's request, plan the execution, perform actions, observe the results, and return the final response.

---

# 1. Planner

## What is a Planner?

The Planner is responsible for deciding **how** a task should be completed.

Instead of immediately generating a response, it breaks a complex problem into smaller executable steps.

### Responsibilities

- Understand the user's goal.
- Create an execution plan.
- Decide whether tools are required.
- Determine the order of execution.

### Example

User:

> Summarize this PDF and email me the summary.

Planner:

1. Read the PDF.
2. Generate the summary.
3. Send the email.

---

# 2. Executor

## What is an Executor?

The Executor performs the actions decided by the Planner.

It executes tool calls, API requests, database queries, or LLM responses.

### Responsibilities

- Execute planned tasks.
- Call external tools.
- Return outputs to the agent.

### Example

Planner decides:

Use Calculator Tool

Executor:

Runs the calculator and returns the answer.

---

# 3. Observer

## What is an Observer?

The Observer evaluates the output produced by the Executor.

If the result is incomplete or incorrect, it informs the Planner so that another action can be taken.

### Responsibilities

- Validate outputs.
- Detect failures.
- Trigger re-planning when required.

### Example

Search API returned no results.

Observer:

Requests another search using different keywords.

---

# 4. Router

## What is a Router?

The Router decides where a request should be sent.

It selects the appropriate workflow, tool, or specialized agent based on the user's input.

### Responsibilities

- Route requests.
- Select workflows.
- Enable conditional execution.
- Support multi-agent systems.

### Example

User asks:

> Translate this document.

Router selects:

Translation Agent

instead of

Math Agent.

---

# Component Workflow

```

User Request

↓

Planner

↓

Executor

↓

Observer

↓

Goal Achieved?

↓

Router (if another workflow is needed)

↓

Final Response

```

---

# Key Takeaways

- Planner decides what to do.
- Executor performs the task.
- Observer checks the result.
- Router decides where the request should go.
- Together, these components make AI Agents capable of solving complex tasks.
