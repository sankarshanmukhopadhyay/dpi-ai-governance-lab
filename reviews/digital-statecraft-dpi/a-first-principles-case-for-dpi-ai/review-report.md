# TRACE review — A First Principles Case for DPI + AI

## Evaluation stance

This review does not assess whether the essay's policy thesis is correct. It asks what an implementer would still need to specify before turning the propositions into an operational DPI + AI system.

## Strong implementation signals

The essay is unusually clear that DPI is shared trust infrastructure rather than digitized forms. It identifies identity, authoritative registries, directories, verifiable credentials, consented data exchange and interoperable payments, and it explicitly warns about surveillance, exclusion, data breach and platform concentration. It also preserves courts, due process and irreducible human judgment rather than treating AI as a replacement for governance.

## Material implementation-distance findings

### 1. Authority must become runtime-bounded

The essay says directories should make authorized actors navigable, but an operator still needs machine-verifiable delegation scope, validity, revocation and runtime authorization evidence before an automated service can exercise consequential authority.

Required capability: `CAP-AUTHORITY-BOUNDED-DELEGATION`.

### 2. Cross-institutional reliance needs admissibility semantics

The essay expects departments and other actors to rely on reusable trusted data and portable credentials. Authenticity and issuer authority alone do not determine whether a receiving institution may rely on a particular upstream output for a particular downstream decision, purpose, jurisdiction or liability regime.

Required capability: `CAP-INTERINSTITUTIONAL-ADMISSIBILITY`.

### 3. Grievance redress must be executable

Strong grievance redressal and independent oversight are explicit design principles, but deployment requires a concrete authority, intake/review/disposition/remedy lifecycle, measurable timing and evidence of exercised appeals.

Required capability: `CAP-REDRESS-APPEAL`.

## Overall assessment

The essay supplies a strong constitutional and architectural direction for DPI + AI. The remaining distance is primarily in executable authority, reliance and redress contracts rather than in the high-level identification of risks.
