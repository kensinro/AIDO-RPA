# RPA Minimal Public Method Specification

## 1. Purpose

Reasoning Path Audit (RPA) audits represented reasoning structure rather than only terminal claims. It separates:

- reasoning state;
- failure existence;
- failure localization;
- failure type;
- dependency;
- downstream consequence.

These dimensions must not be collapsed into one another.

## 2. Auditable object classes

RPA uses five public reasoning-object classes:

1. `NODE` — an evidential or claim object;
2. `EDGE` — a directed inferential relation between two objects;
3. `HYPEREDGE` — a joint inferential relation whose material semantics cannot be decomposed into independent pairwise edges without loss;
4. `PATH` — an ordered composition of inferential relations;
5. `GRAPH` — the represented reasoning structure containing multiple interacting paths or branches.

### Lowest-sufficient-scope rule

Localize at the smallest object scope that preserves the material scientific semantics of the defect. Do not localize to an edge when the failure arises only from joint premises, path composition, convergence, aggregation, or graph-level structure.

## 3. Canonical reasoning states

- `SUPPORTED` — the represented inferential function is sufficiently supported for the audited purpose.
- `UNSUPPORTED` — the represented inferential function exceeds what the evidence supports.
- `UNDERDETERMINED` — available evidence does not justify a unique supported assignment among materially defensible alternatives.
- `NOT_AUDITABLE` — the available representation/evidence is insufficient for a valid structural adjudication at the audited scope.

`UNDERDETERMINED` and `NOT_AUDITABLE` are not automatically failures.

## 4. Material dependency

A downstream object is materially dependent on an upstream object when bounding, removing, or changing the upstream support can change the downstream object's entitled state or reporting ceiling under the represented reasoning contract.

Graph reachability alone is insufficient. Reachability identifies candidate descendants; materiality determines whether consequence is scientifically entitled to propagate.

## 5. Materially defensible alternatives

An alternative remains materially defensible when it is compatible with the retained evidence and unresolved constraints such that removing it would require an unsupported evidential or inferential commitment.

An over-wide admissible set is itself an audit error when the retained evidence uniquely supports a narrower set.

## 6. Admissible state sets and wording ceiling

When more than one canonical state or interpretation remains materially defensible, preserve the admissible set rather than forcing a singleton.

The robust wording ceiling is the strongest reporting formulation supported across all retained admissible interpretations. This is analogous in spirit to skeptical acceptance across surviving admissible interpretations, but the public specification does not claim formal equivalence to any particular abstract-argumentation extension semantics.

## 7. Consequence containment

After localizing a defect:

1. identify graph-reachable downstream candidates;
2. evaluate material dependency for each candidate;
3. propagate consequence only where material dependency is present;
4. preserve independently supported reasoning outside that boundary;
5. derive the reporting ceiling from the surviving admissible structure.

A local defect does not imply global graph invalidation.

## 8. Public decision rules

| Question | Public rule | Audit error when |
|---|---|---|
| Is the dependency material? | Changing/bounding the implicated support can change entitled state or wording ceiling | consequence is propagated from mere graph reachability |
| Collapse to singleton? | Only when retained evidence excludes materially defensible alternatives | singleton is forced despite unresolved alternatives |
| Preserve non-singleton? | When two or more materially defensible alternatives survive | admissible alternatives are removed without evidential warrant |
| Assign UNDERDETERMINED? | The audit is valid but evidence does not support unique adjudication | used as an escape when evidence actually requires localization |
| Assign NOT_AUDITABLE? | Required representation/evidence for valid adjudication is unavailable | treated as a scientific failure by default, or used despite sufficient audit evidence |
| Propagate consequence? | Only through materially dependent downstream objects | independent valid branches are invalidated |
| Preserve branch? | The branch remains independently supported after the localized defect is bounded | surviving support is discarded merely because another branch failed |

## 9. Reachable failure conditions

A case may fail the public audit contract if, for example, the audit:

- misses a designated structural defect;
- invents a defect in a hard-negative case;
- falsely localizes a defect;
- forces a singleton under unresolved material ambiguity;
- preserves an over-wide admissible set when evidence uniquely resolves it;
- propagates consequence beyond material dependency;
- fails to propagate a consequence that is materially required;
- invalidates an independently supported branch;
- assigns `NOT_AUDITABLE` despite sufficient audit evidence;
- cannot represent the prespecified structural challenge using the public object/state kernel.

## 10. Human authority

The public reference layer represents governance logic. It does not autonomously determine scientific truth, materiality, or publication entitlement. Material scientific judgments remain evidence-constrained and human-governed.
