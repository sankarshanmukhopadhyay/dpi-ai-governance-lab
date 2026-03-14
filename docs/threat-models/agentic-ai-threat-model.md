# Agentic AI Governance Threat Model

Agentic systems introduce a new category of mischief: they can chain actions, consume authority, and produce outcomes whose accountability dissolves across tools, prompts, and delegations.

## Threat classes

### 1. Mandate overreach
The system acts outside its authorized scope because goals are underspecified or policy constraints are weak.

### 2. Tool-mediated harm
A seemingly safe model causes damage through connectors, APIs, registries, or operational tools.

### 3. Delegation opacity
Humans cannot reconstruct which actor or subsystem held decision authority at each stage.

### 4. Policy evasion through decomposition
Prohibited actions are achieved indirectly by splitting intent across many individually benign steps.

### 5. Continuous adaptation without governance refresh
The system evolves faster than the institution's control, testing, or approval loop.

## Governance implications

- Mandates must be explicit, revocable, and testable.
- Tool access should be tiered and logged.
- Human override must be operational, not ceremonial.
- Incident analysis should reconstruct the authority chain, not just the model output.

## Minimum evidence expectations

- Agent mandate definition
- Tool inventory and scope constraints
- Logged intervention and stop-right events
- Change history for prompts, policies, and delegated permissions
