# MASTER_ROADMAP.md

# ATLAS Master Roadmap (Living Document)

**Status:** ACTIVE\
**Current Phase:** Phase 1 -- Infrastructure

------------------------------------------------------------------------

# Rules

-   Research before Core.
-   Core before Studio.
-   Never build from assumptions.
-   Every major decision must be backed by evidence.
-   Every phase must have a Definition of Done (DoD).

------------------------------------------------------------------------

# Phase 0 -- Foundation ✅

## Goal

Freeze philosophy and project direction.

### Deliverables

-   DNA of ATLAS Vol. I--XXIII
-   Founder Handbook
-   Folder structure

**DoD:** No more philosophy documents.

------------------------------------------------------------------------

# Phase 1 -- Infrastructure 🚧 (CURRENT)

## Goal

Acquire reliable market data.

### Tasks

-   [ ] Angel One account approved
-   [ ] SmartAPI setup
-   [ ] Python environment
-   [ ] Git repository
-   [ ] SQLite database
-   [ ] WebSocket connection
-   [ ] Save live ticks
-   [ ] Automatic reconnect
-   [ ] Logging

### DoD

ATLAS records live market ticks without manual intervention.

------------------------------------------------------------------------

# Phase 2 -- Historical Data

## Goal

Own the dataset.

### Tasks

-   Download NIFTY historical candles
-   Download BANKNIFTY
-   Validate completeness
-   Store locally

### DoD

Historical database is complete and reproducible.

------------------------------------------------------------------------

# Phase 3 -- Data Validation

## Tasks

-   Tick validation
-   Candle validation
-   Missing-data detection
-   Timestamp verification

### DoD

Research trusts the dataset.

------------------------------------------------------------------------

# Phase 4 -- Feature Engine V0

## Initial Features

-   Returns
-   ATR
-   VWAP
-   Volume
-   Rolling Volatility

### DoD

Feature table generated automatically.

------------------------------------------------------------------------

# Phase 5 -- Market Autopsy

## Questions

Why do option trades fail?

### Categories

-   Wrong Direction
-   IV Crush
-   Theta
-   Late Entry
-   Spread
-   Sideways Market

### DoD

Failure distribution is quantified.

------------------------------------------------------------------------

# Phase 6 -- Baselines

Build simple deterministic systems.

Compare against: - Random - EMA - RSI

### DoD

Baseline performance established.

------------------------------------------------------------------------

# Phase 7 -- Research

Every hypothesis enters the Research Ledger.

Rejected ideas stay archived.

### DoD

Evidence exists before ML.

------------------------------------------------------------------------

# Phase 8 -- Machine Learning

Candidates: - LightGBM - XGBoost

Only trained on validated research labels.

### DoD

Model beats baselines.

------------------------------------------------------------------------

# Phase 9 -- Shadow Mode

No real money.

Log predictions only.

### DoD

Weeks of stable forward performance.

------------------------------------------------------------------------

# Phase 10 -- Decision Engine

Generate: - Direction - Probability - Risk - Explanation

Human executes.

### DoD

Decision support operational.

------------------------------------------------------------------------

# Phase 11 -- ATLAS Studio

Only after Core proves edge.

UI Visualization Dashboards

### DoD

Production-ready workstation.

------------------------------------------------------------------------

# Living Documents

-   RESEARCH_LEDGER.md
-   FEATURE_REGISTRY.md
-   MODEL_REGISTRY.md
-   ADR/
-   INCIDENTS/
-   TRADE_CASE_STUDIES/

------------------------------------------------------------------------

Last Updated: (To be maintained continuously.)
