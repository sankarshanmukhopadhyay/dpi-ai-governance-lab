# Risk tier decision tree (v0.1)

1. Does the system **trigger or execute** an action affecting rights/entitlements/enforcement?
   - Yes → Tier 3
   - No → go to 2
2. Does the system **influence** a consequential decision (eligibility, risk score, prioritization, enforcement)?
   - Yes → Tier 2
   - No → go to 3
3. Does the system **shape** operational workflows (triage, recommendations, alerts) with a human decision-maker?
   - Yes → Tier 1
   - No → Tier 0
