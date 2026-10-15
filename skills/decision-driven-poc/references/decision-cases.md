# Decision-Driven PoC — contrasting cases

Synthetic, non-proprietary examples, not results of real trials.

## A. Technology enthusiasm expands the experiment

**Opportunity:** A new model might classify manufacturing anomalies from video.

**Proposal:** Build a complete annotation platform, streaming inference service, and interactive product demo before examining the available footage and operational use case.

**Expected judgment:** Identify the adoption decision and key unknowns first. Test a bounded representative sample against a useful baseline, with clear data and error limits. Decide what evidence would justify a larger investment or stopping.

## B. A demo cannot answer the actual question

**Decision:** Can a proposed method remain reliable when camera conditions vary significantly?

**Proposal:** Demo five hand-picked daytime videos with a polished interface and stop on visible success.

**Expected judgment:** The proposed evidence is insufficient. A bounded but varied set of conditions with a credible failure oracle matters more than interface polish.

**Countercase:** A production feature already has approved requirements and operational acceptance gates. Do not recast its delivery as an exploratory PoC.

**Try it:** Ask: "Use $decision-driven-poc to compare these proposals and give explicit proceed/pivot/stop criteria, without inventing product-demand evidence."
