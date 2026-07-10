"""
===============================================================================
DNA OF ATLAS
VOLUME VIII — THE MACHINE LEARNING BIBLE
Founder Transfer Handbook
Version 1.0
===============================================================================

PURPOSE
-------

This volume records how ATLAS should approach Machine Learning.

Machine Learning is a tool.

It is not the product.

Research determines what should be learned.

===============================================================================
CHAPTER 1 — ML EXISTS TO ASSIST
===============================================================================

ATLAS does not attempt to predict every candle.

Its objective is to improve decision quality.

Every model must answer:

"Does this improve trading decisions?"

Not:

"Does this improve benchmark accuracy?"

===============================================================================
CHAPTER 2 — LABELS FIRST
===============================================================================

Never choose a model before defining labels.

Bad labels produce useless models.

Good labels create useful research.

Label design is part of science.

===============================================================================
CHAPTER 3 — FEATURES
===============================================================================

Models learn from features.

Features originate from:

Price.

Volume.

Volatility.

Liquidity.

Option chain.

Market internals.

Derived features should always be reproducible.

===============================================================================
CHAPTER 4 — TRAIN / VALIDATE / TEST
===============================================================================

Never evaluate on training data.

Always separate:

Training.

Validation.

Forward testing.

The market rewards generalization.

===============================================================================
CHAPTER 5 — CALIBRATION
===============================================================================

Confidence must be calibrated.

70% confidence should historically behave like 70%.

Overconfident models lose trust.

===============================================================================
CHAPTER 6 — MODEL REGISTRY
===============================================================================

Every model stores:

Version.

Training data window.

Features used.

Label version.

Metrics.

Creation date.

Nothing is anonymous.

===============================================================================
CHAPTER 7 — DRIFT
===============================================================================

Monitor:

Feature drift.

Prediction drift.

Performance drift.

Retraining should be triggered by evidence,
not by a fixed calendar alone.

===============================================================================
CHAPTER 8 — ENSEMBLES
===============================================================================

Multiple simple models often outperform
one complicated model.

Complexity must justify itself.

===============================================================================
CHAPTER 9 — EXPLAINABILITY
===============================================================================

Every prediction should explain:

Top contributing factors.

Major risks.

Confidence.

Invalidation conditions.

No black boxes.

===============================================================================
CHAPTER 10 — FINAL PRINCIPLE
===============================================================================

Data creates knowledge.

Research creates understanding.

Machine Learning converts both into probabilities.

Humans make the final decision.

END OF VOLUME VIII
"""
