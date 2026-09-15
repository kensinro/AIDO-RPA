# AIDO-RPA — Minimal Public Reference Layer

This repository provides a **minimal public reference layer for Reasoning Path Audit (RPA)** as described in the manuscript:

> *Auditing reasoning structure beyond claim-level scientific entitlement: structural localization, consequence containment, and boundary-preserving adjudication*

RPA treats represented reasoning structure as an auditable information object. Its purpose is not to replace domain science, prove truth, or automate publication decisions. The public layer demonstrates the manuscript-level governance mechanics needed to inspect how structural findings are localized, how consequences are bounded by material dependency, how admissible non-singleton outcomes are preserved, and how reporting language is constrained by the surviving evidence boundary.

## Public scope

The repository contains only the minimum material needed to support inspection and methodological reconstruction of the submitted manuscript:

- the five reasoning-object classes used in the paper: `NODE`, `EDGE`, `HYPEREDGE`, `PATH`, `GRAPH`;
- the four canonical reasoning states: `SUPPORTED`, `UNSUPPORTED`, `UNDERDETERMINED`, `NOT_AUDITABLE`;
- an explicit separation between state, failure existence, localization, failure type, dependency, and consequence;
- the public decision rules corresponding to manuscript Box 1;
- a worked C05-style branch-convergence example;
- a public evidence index for the **38-case analysed set (Zones A–E)**;
- a small reference workflow and regression tests.

## What this repository does *not* contain

This is **not** the complete internal AIDO development codebase and is not a production reasoning engine. It does not include private development ledgers, unreleased rule libraries, internal orchestration, unpublished branches, proprietary materials, or later AIDO modules.

The reference code does **not** infer scientific materiality autonomously. Materiality remains a scientific/adjudicative input: the public workflow shows how a material-dependency decision is represented and propagated once that decision has been justified from the evidence.

## Repository structure

- `reference_mvp/rpa.py` — minimal governance/reference workflow
- `examples/C05_WORKED_EXAMPLE.json` — public-safe worked example
- `manuscript_support/EVIDENCE_INDEX.md` — analysed-set and evidence-availability map
- `METHOD_SPEC.md` — manuscript-aligned operational specification
- `PUBLIC_DISCLOSURE_BOUNDARY.md` — disclosure and authority boundary
- `supplementary/` — archival mirror area for manuscript supplementary material
- `tests/test_reference_mvp.py` — regression tests for the public reference layer

## Supplementary material

The repository includes a dedicated archival area for the manuscript's supplementary resource:

**Online Resource 1 — Archival Evidence Inventory and Claim–Evidence Crosswalk**

The frozen submission PDF is designated `supplementary/ESM_1.pdf`. Its SHA256 is recorded in `supplementary/README.md` so that the public copy can be checked against the submission-stage file. The journal-submitted Online Resource remains the authoritative submission record; the GitHub copy is a public archival mirror rather than a replacement for the publisher record.

## Minimal reproduction

The reference layer uses only the Python standard library.

```bash
python -m unittest discover -s tests -v
```

The tests check governance invariants such as selective consequence propagation, preservation of unaffected branches, retention of non-singleton outcomes, and refusal to convert `NOT_AUDITABLE` into a failure by default.

## Evidence boundary

The manuscript's analysed evidence set is **38 documented prospective cases across Zones A–E**. A later historical extension is excluded from the analysed denominator because its case-level records are not available in the retained submission archive. This repository does not back-fill or reconstruct unavailable case rows.

## Authority boundary

RPA provides an auditable structural assessment and a bounded reporting-entitlement output. Human scientific responsibility remains outside the code. The public reference layer does not authorize publication, establish scientific truth, or replace Human Gate adjudication.

## Citation

Please cite the associated manuscript when using or discussing this repository. Citation metadata will be updated after a stable bibliographic record is available.

## Rights

Copyright © 2026 Sin Guan Kong. All rights reserved. No open-source license is granted at the current submission stage beyond rights necessarily provided by GitHub's Terms of Service and applicable law.
