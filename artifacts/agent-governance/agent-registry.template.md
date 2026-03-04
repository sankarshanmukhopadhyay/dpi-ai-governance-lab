# Agent registry (template)

Maintain a registry of every operational agent/workflow.

Minimum fields:
- agent_id
- agent_type
- operator (accountable role + contact)
- mandate_ref
- risk_class
- status (active/suspended/revoked/retired)
- created_at / expiry_at
- revocation (if applicable)
- capability_manifest_ref
- policy_constraints_ref

Notes:
- For agents with tool write-access, mandate expiry SHOULD be short and renewable.
- Registry entries SHOULD be signed and versioned.
