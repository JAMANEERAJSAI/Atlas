"""
===============================================================================
DNA OF ATLAS
VOLUME VII — THE DATA BIBLE
Founder Transfer Handbook
Version 1.0
===============================================================================

PURPOSE
-------

This volume defines how ATLAS treats data.

The quality of ATLAS will never exceed the quality of its data.

Garbage in.

Garbage out.

No exception.

===============================================================================
CHAPTER 1 — DATA IS THE MOAT
===============================================================================

Models come and go.

Libraries change.

Algorithms improve.

The one asset that compounds is clean, well-labelled market data.

Protect it.

Back it up.

Never casually delete it.

===============================================================================
CHAPTER 2 — DATA SOURCES
===============================================================================

Preferred order:

1. Official broker WebSocket
2. Official historical APIs
3. Official exchange archives
4. Other legitimate public datasets

Avoid scraping if an official source exists.

===============================================================================
CHAPTER 3 — DATA TIERS
===============================================================================

Tier 1
Raw market ticks.

Tier 2
Candles.

Tier 3
Derived features.

Tier 4
Predictions.

Tier 5
Trade outcomes.

Never mix these together.

===============================================================================
CHAPTER 4 — RAW DATA
===============================================================================

Raw data is sacred.

Never overwrite it.

If a bug exists in feature generation,
raw data allows regeneration.

Without raw data,
mistakes become permanent.

===============================================================================
CHAPTER 5 — DATA VALIDATION
===============================================================================

Every incoming record should be checked.

Missing timestamp?

Duplicate packet?

Impossible price?

Negative volume?

Future timestamp?

Flag it.

Do not silently continue.

===============================================================================
CHAPTER 6 — LABELLING
===============================================================================

Labels are part of the dataset.

Changing a label definition changes every experiment built upon it.

Version labels.

Document labels.

Never modify them casually.

===============================================================================
CHAPTER 7 — FEATURE STORE
===============================================================================

Features should be reproducible.

Every feature records:

Name.

Formula.

Parameters.

Version.

Origin.

A feature nobody understands should not exist.

===============================================================================
CHAPTER 8 — DATA DRIFT
===============================================================================

Markets evolve.

Data distributions evolve.

Monitor drift continuously.

If today's data no longer resembles training data,
confidence should decrease automatically.

===============================================================================
CHAPTER 9 — BACKUPS
===============================================================================

Primary storage:
Local.

Secondary:
Cloud backup.

Backups are insurance,
not primary infrastructure.

===============================================================================
CHAPTER 10 — FINAL PRINCIPLE
===============================================================================

The first responsibility of ATLAS is not prediction.

It is preserving truthful observations.

Everything else is built upon that foundation.

END OF VOLUME VII
"""
