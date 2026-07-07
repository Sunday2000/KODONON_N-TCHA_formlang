"""SingularityDetector. À COMPLÉTER : table de l'AFD 'or'.  -> Jour 1 (E1.1)."""
from formlang.dfa import DFA

_DFA_OR = DFA(
    transitions={
        # TODO (E1.1)
    },
    start="A", accept={"C"}, alphabet={"a", "o", "r"},
)


def contains_or(w: str) -> bool:
    return _DFA_OR.accepts(w)


def detector_dfa() -> DFA:
    return _DFA_OR
