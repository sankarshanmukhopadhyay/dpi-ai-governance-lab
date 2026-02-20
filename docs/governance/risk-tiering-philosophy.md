# Risk-tiering philosophy

Not all AI use-cases deserve the same governance burden.

This repo uses a **tiered** model:

- Tier 0: Informational
- Tier 1: Operational support
- Tier 2: Rights-affecting decision support
- Tier 3: Automated rights-affecting action

The goal is to:
- Make Tier 0–1 safe and scalable
- Make Tier 2 defensible and auditable
- Make Tier 3 rare, heavily conditioned, and rollback-ready
