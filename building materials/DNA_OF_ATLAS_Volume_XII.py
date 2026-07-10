"""
===============================================================================
DNA OF ATLAS
VOLUME XII — THE EXPERIMENT BIBLE
Founder Transfer Handbook
Version 1.0
===============================================================================

PURPOSE
-------

Research without discipline becomes opinion.

This volume defines how every experiment inside ATLAS should be designed,
executed, reviewed and archived.

===============================================================================
CHAPTER 1 — EVERY EXPERIMENT BEGINS WITH A QUESTION
===============================================================================

Bad:

"Let's try XGBoost."

Good:

"Can XGBoost reduce false breakout entries compared with LightGBM?"

Technology never starts an experiment.

Questions do.

===============================================================================
CHAPTER 2 — HYPOTHESIS FORMAT
===============================================================================

Every hypothesis must contain:

Question

Reason

Expected outcome

Success metric

Failure metric

Dataset

Confidence before experiment

===============================================================================
CHAPTER 3 — BASELINES
===============================================================================

Every experiment competes against:

Random

Current production logic

Simplest possible rule

If the new approach loses,

it is rejected.

===============================================================================
CHAPTER 4 — REPRODUCIBILITY
===============================================================================

Every experiment records:

Dataset version

Feature version

Model version

Parameters

Random seed

Timestamp

A result that cannot be reproduced is not evidence.

===============================================================================
CHAPTER 5 — STATISTICAL DISCIPLINE
===============================================================================

Do not celebrate tiny improvements.

Ask:

Is it statistically meaningful?

Is it consistent?

Does it survive forward testing?

===============================================================================
CHAPTER 6 — PROMOTION RULE
===============================================================================

Research
      ↓
Independent validation
      ↓
Forward test
      ↓
Production trial
      ↓
Core

Ideas skip no stages.

===============================================================================
CHAPTER 7 — REJECTION
===============================================================================

Rejected ideas remain archived.

Future knowledge may explain why they failed.

Never erase history.

===============================================================================
CHAPTER 8 — EXPERIMENT REPORT
===============================================================================

Every completed experiment ends with:

What was learned?

What changed?

What remains unknown?

Should this continue?

===============================================================================
CHAPTER 9 — SUCCESS METRIC
===============================================================================

The objective is not to maximize accuracy.

The objective is to improve trading decisions after costs,
risk and execution realities.

===============================================================================
CHAPTER 10 — FINAL PRINCIPLE
===============================================================================

Research is not complete when an experiment succeeds.

Research is complete when the result can be trusted.

END OF VOLUME XII
"""
