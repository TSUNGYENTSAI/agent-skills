# Semantic Boundary Review — contrasting cases

Synthetic examples only. They contain no confidential system details.

## A. An assumption becomes a fact

**Input:** A source supplies device identifiers and positions but no permissible travel directions.

**Proposal:** Infer directions from proximity and store them as confirmed domain topology.

**Expected judgment:** Reject the promotion of inference to fact. Keep the proposed directions explicitly provisional, identify the authority that can confirm them, and fail or defer decisions that require confirmed topology.

## B. Representation fidelity has a price

**Input:** A prototype collision planner needs conservative obstacle occupancy; a detailed source mesh remains available.

**Proposal:** Every solver state must retain the complete high-resolution mesh.

**Expected judgment:** Challenge the added cost. A conservative lower-fidelity representation can be suitable if error bounds, downstream invariants, and reconstruction needs are made explicit. In a precision-critical acceptance path, the higher fidelity may be required.

**Try it:** Ask: "Use $semantic-boundary-review to identify the consequential semantic and fidelity boundaries. Avoid prescribing a full domain framework."
