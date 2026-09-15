from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, FrozenSet


class ReasoningState(str, Enum):
    SUPPORTED = "SUPPORTED"
    UNSUPPORTED = "UNSUPPORTED"
    UNDERDETERMINED = "UNDERDETERMINED"
    NOT_AUDITABLE = "NOT_AUDITABLE"


class ObjectClass(str, Enum):
    NODE = "NODE"
    EDGE = "EDGE"
    HYPEREDGE = "HYPEREDGE"
    PATH = "PATH"
    GRAPH = "GRAPH"


@dataclass(frozen=True)
class AuditObject:
    object_id: str
    object_class: ObjectClass
    state: ReasoningState


@dataclass(frozen=True)
class DependencyDecision:
    upstream_id: str
    downstream_id: str
    graph_reachable: bool
    material_dependency: bool


@dataclass(frozen=True)
class ConsequenceResult:
    affected: FrozenSet[str]
    preserved: FrozenSet[str]


def contain_consequence(
    localized_defect_id: str,
    decisions: Iterable[DependencyDecision],
    candidate_downstream_ids: Iterable[str],
) -> ConsequenceResult:
    """Reference implementation of selective consequence propagation.

    This function does not infer scientific materiality. Each
    `material_dependency` value is an evidence-constrained adjudicative input.
    The function demonstrates the manuscript rule that graph reachability alone
    is insufficient for downstream invalidation.
    """
    candidates = set(candidate_downstream_ids)
    affected = {
        d.downstream_id
        for d in decisions
        if d.upstream_id == localized_defect_id
        and d.downstream_id in candidates
        and d.graph_reachable
        and d.material_dependency
    }
    preserved = candidates - affected
    return ConsequenceResult(frozenset(affected), frozenset(preserved))


def retain_admissible_states(states: Iterable[ReasoningState]) -> FrozenSet[ReasoningState]:
    """Preserve all explicitly retained materially defensible states.

    This function does not decide which states are scientifically defensible;
    that determination belongs to the evidence-constrained audit.
    """
    retained = frozenset(states)
    if not retained:
        raise ValueError("At least one admissible state must be retained")
    return retained


def requires_human_gate(states: Iterable[ReasoningState]) -> bool:
    """Decision-bearing non-singleton state sets require human adjudication."""
    return len(retain_admissible_states(states)) > 1


def is_failure_state(state: ReasoningState) -> bool:
    """Only UNSUPPORTED is intrinsically a failure state in this minimal layer.

    UNDERDETERMINED and NOT_AUDITABLE are boundary states, not automatic
    scientific failures.
    """
    return state is ReasoningState.UNSUPPORTED
