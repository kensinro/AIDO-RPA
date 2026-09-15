# Public Disclosure and Authority Boundary

This repository is a bounded public reference layer for the manuscript-described Reasoning Path Audit (RPA).

## Included

- manuscript-aligned object and state definitions;
- public decision rules for material dependency, non-singleton retention, consequence containment, and wording ceilings;
- a public-safe C05 worked example;
- a minimal reference workflow showing selective consequence propagation once materiality has been adjudicated;
- public regression tests for governance invariants;
- a public-safe index of the 38-case analysed evidence set.

## Not included

- complete internal AIDO source code;
- unpublished development branches;
- private case ledgers or proprietary/copyrighted source materials;
- unreleased rule libraries;
- internal orchestration and agent logic;
- later AIDO-AIT / AIT-II development branches;
- private research-development or experience ledgers;
- autonomous scientific-materiality inference;
- autonomous manuscript or publication authority.

## Scientific boundary

The public reference code does not infer truth and does not infer material scientific dependency from raw evidence. It receives evidence-constrained adjudicative inputs and demonstrates the downstream governance rules described in the manuscript.

The following distinctions remain mandatory:

`STATE != FAILURE TYPE != LOCALIZATION != CONSEQUENCE`

and

`FAILURE EXISTENCE != FAILURE LOCATION != FAILURE TYPE != FAILURE CONSEQUENCE`.

`UNDERDETERMINED` and `NOT_AUDITABLE` are valid boundary outcomes and are not automatically failures.

## Historical evidence boundary

The analysed manuscript set is limited to 38 documented cases across Zones A–E. A later historical extension is excluded from the analysed denominator because its case-level records are not available in the retained submission archive. This repository does not reconstruct unavailable case rows.

## Human authority

All scientific interpretations and publication decisions remain human-governed. This repository is designed for inspection, reproducibility of the public workflow, and methodological evaluation only.
