"""
===============================================================================
DNA OF ATLAS
VOLUME XIV — ARCHITECTURE DECISION RECORDS (ADR)
Founder Transfer Handbook
Version 1.0
===============================================================================

PURPOSE
-------

Every important architectural decision must be recorded.

Future engineers should understand not only WHAT was chosen,
but WHY it was chosen and WHAT alternatives were rejected.

===============================================================================
CHAPTER 1 — ADR FORMAT
===============================================================================

Every ADR contains:

Decision ID

Date

Problem

Options Considered

Chosen Option

Rejected Options

Reasoning

Consequences

Future Reconsideration Trigger

===============================================================================
CHAPTER 2 — ADR 001
===============================================================================

Decision:

ATLAS will remain a decision-support system.

Rejected:

Fully automated execution.

Reason:

Human control, trust, simplicity and reduced operational risk.

===============================================================================
CHAPTER 3 — ADR 002
===============================================================================

Decision:

Research precedes Core.

Rejected:

Architecture-first development.

Reason:

Prevent over-engineering.

===============================================================================
CHAPTER 4 — ADR 003
===============================================================================

Decision:

Official market data providers are preferred.

Rejected:

OCR-first and computer-vision-first architectures.

Reason:

Reliability, lower maintenance and clearer legality.

===============================================================================
CHAPTER 5 — ADR 004
===============================================================================

Decision:

Indicators become features.

Rejected:

Indicator-driven BUY/SELL systems.

Reason:

Measurements are more valuable than isolated signals.

===============================================================================
CHAPTER 6 — CHANGE CONTROL
===============================================================================

Every architectural change must answer:

What problem exists?

What evidence supports the change?

What new risks appear?

How will success be measured?

===============================================================================
CHAPTER 7 — REVERSIBILITY
===============================================================================

Prefer decisions that can be reversed cheaply.

Avoid locking the project into one broker,
one model or one technology.

===============================================================================
CHAPTER 8 — DOCUMENTATION
===============================================================================

If an engineer cannot explain why a subsystem exists,

it probably should not exist.

===============================================================================
CHAPTER 9 — EVOLUTION
===============================================================================

Architecture is expected to evolve.

Principles evolve slowly.

Implementation evolves frequently.

Never confuse the two.

===============================================================================
CHAPTER 10 — FINAL PRINCIPLE
===============================================================================

Every important decision should leave a trail.

Future engineers should inherit reasoning,
not mysteries.

END OF VOLUME XIV
"""
