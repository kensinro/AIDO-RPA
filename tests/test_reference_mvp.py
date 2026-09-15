import unittest

from reference_mvp.rpa import (
    DependencyDecision,
    ReasoningState,
    contain_consequence,
    is_failure_state,
    requires_human_gate,
    retain_admissible_states,
)


class TestRPAReferenceMVP(unittest.TestCase):
    def test_selective_consequence_propagation(self):
        decisions = [
            DependencyDecision("DEFECT", "GLOBAL", True, True),
            DependencyDecision("DEFECT", "P1", True, False),
            DependencyDecision("DEFECT", "P2", True, False),
        ]
        result = contain_consequence("DEFECT", decisions, ["GLOBAL", "P1", "P2"])
        self.assertEqual(result.affected, frozenset({"GLOBAL"}))
        self.assertEqual(result.preserved, frozenset({"P1", "P2"}))

    def test_reachability_alone_does_not_propagate(self):
        decisions = [DependencyDecision("DEFECT", "P1", True, False)]
        result = contain_consequence("DEFECT", decisions, ["P1"])
        self.assertEqual(result.affected, frozenset())
        self.assertEqual(result.preserved, frozenset({"P1"}))

    def test_non_singleton_is_preserved(self):
        states = retain_admissible_states(
            [ReasoningState.SUPPORTED, ReasoningState.UNDERDETERMINED]
        )
        self.assertEqual(len(states), 2)
        self.assertTrue(requires_human_gate(states))

    def test_not_auditable_is_not_automatic_failure(self):
        self.assertFalse(is_failure_state(ReasoningState.NOT_AUDITABLE))

    def test_underdetermined_is_not_automatic_failure(self):
        self.assertFalse(is_failure_state(ReasoningState.UNDERDETERMINED))

    def test_unsupported_is_failure_state(self):
        self.assertTrue(is_failure_state(ReasoningState.UNSUPPORTED))

    def test_empty_admissible_set_rejected(self):
        with self.assertRaises(ValueError):
            retain_admissible_states([])


if __name__ == "__main__":
    unittest.main()
