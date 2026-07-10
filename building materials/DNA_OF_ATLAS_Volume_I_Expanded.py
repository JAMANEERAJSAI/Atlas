"""
===============================================================================
DNA OF ATLAS
Volume I — The Birth of an Idea
Founder Transfer Handbook
Version 1.1 (Expanded Draft)
===============================================================================

READ THIS FIRST
---------------

This file is NOT source code.

It is the institutional memory of Project ATLAS.

If you are a future engineer or AI:
    Don't start by changing the architecture.
    Start by understanding why it exists.

===============================================================================
CHAPTER 1 — THE FIRST PROJECT (THE FAILURE)
===============================================================================

ATLAS was not the first attempt.

Before ATLAS there was another stock-market project.

That project was indicator-centric.

The thinking was simple:

    More indicators
    + Better ML
    + Better UI
    = Better trading.

It slowly became an enormous collection of features.

There were indicators everywhere.

The bot almost never committed to a trade.
Most outputs were simply:

    HOLD
    HOLD
    HOLD

Looking back, that failure taught more than any success could.

The project failed because we optimized architecture before understanding
the market.

This lesson became the seed that eventually grew into ATLAS.

===============================================================================
CHAPTER 2 — THE QUESTION THAT CHANGED EVERYTHING
===============================================================================

The project asked:

    "Which model should we use?"

Wrong question.

The better question was:

    "What is the exact problem we are trying to solve?"

That single change completely redirected development.

From then on every discussion had to begin with a measurable problem.

Not with technology.

===============================================================================
CHAPTER 3 — OPTIONS ARE DIFFERENT
===============================================================================

One of the biggest discoveries was that predicting the underlying index
does not automatically create profitable option trades.

Examples:

Case A:
NIFTY rises exactly as expected.
Call option barely makes money because IV collapsed.

Case B:
NIFTY reaches the target.
Premium loses value because too much time passed.

Case C:
Direction correct.
Execution late.
Risk-reward destroyed.

Conclusion:

The prediction target cannot simply be:

    "Will NIFTY go up?"

ATLAS must evaluate:

• Direction
• Timing
• Volatility
• Liquidity
• Premium behaviour
• Confidence

===============================================================================
CHAPTER 4 — WHY MANUAL EXECUTION STAYED
===============================================================================

Multiple times we discussed automatic execution.

We deliberately rejected it.

Reasons:

1. Trust.
2. Psychological ownership.
3. Simplicity.
4. Lower legal and engineering complexity.
5. The founder wanted ATLAS beside him—not replacing him.

Therefore this decision is LOCKED.

ATLAS recommends.

Human executes.

===============================================================================
CHAPTER 5 — THE API DEBATE
===============================================================================

Several possibilities were investigated.

- Broker APIs
- Screen OCR
- Computer Vision
- Reading charts visually
- Browser automation

The attractive idea was avoiding APIs completely.

After researching the trade-offs we concluded:

Computer vision is interesting but maintenance-heavy.

Official APIs are boring—but reliable.

Architecture decision:

Use official market data whenever possible.

Keep the provider abstract so Angel One can later be replaced without
rewriting Core.

===============================================================================
CHAPTER 6 — WHAT WE NOW BELIEVE
===============================================================================

These beliefs have relatively high confidence.

1. Good data beats fancy models.

2. Explainability beats mystery.

3. Opportunity filtering may matter more than price prediction.

4. Most ideas should die inside Research.

5. A small working system is worth more than a perfect architecture.

===============================================================================
CHAPTER 7 — WHAT WE DO NOT KNOW
===============================================================================

Unknowns remain.

Examples:

• Which features actually contain predictive power?

• Does regime detection improve results?

• How useful is IV Rank?

• Are probability cones genuinely actionable?

None of these are accepted truths.

Research must answer them.

===============================================================================
CHAPTER 8 — FOUNDER WARNINGS
===============================================================================

If future development starts sounding like:

    "Let's add another engine."

Stop.

Ask:

"What experiment proved we need it?"

If the answer is:

"We think..."

The work belongs in Research.

Not Core.

===============================================================================
END OF CURRENT EXPANSION

Future additions should continue growing this document rather than replacing
older reasoning. Preserve mistakes. Preserve debates. Preserve uncertainty.

The objective is to remember HOW we learned—not just WHAT we concluded.
"""