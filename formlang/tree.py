"""Automate d'arbres ascendant (BUTA) générique. À COMPLÉTER : run, accepts,
product.  -> Jour 3 (E3.1, E3.4)."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Hashable


@dataclass(frozen=True)
class Term:
    symbol: str
    children: tuple["Term", ...] = ()
    label: Optional[str] = None


class _Reject:
    __slots__ = ()
    def __repr__(self):
        return "REJECT"


REJECT = _Reject()


class TreeAutomaton:
    def __init__(self, final_states):
        self.delta: dict[tuple[str, tuple], Hashable] = {}
        self.final: set = set(final_states)

    def add_rule(self, symbol: str, child_states, result) -> None:
        # FOURNI
        self.delta[(symbol, tuple(child_states))] = result

    def run(self, t: "Term"):
        child_states = tuple(self.run(c) for c in t.children)
        if REJECT in child_states:
            return REJECT
        return self.delta.get((t.symbol, child_states), REJECT)

    def accepts(self, t: "Term") -> bool:
        return self.run(t) in self.final


def product(a1: "TreeAutomaton", a2: "TreeAutomaton") -> "TreeAutomaton":
    P = TreeAutomaton(final_states={(f1, f2) for f1 in a1.final for f2 in a2.final})
    for (sym1, children1), r1 in a1.delta.items():
        for (sym2, children2), r2 in a2.delta.items():
            if sym1 == sym2 and len(children1) == len(children2):
                P.add_rule(sym1, tuple(zip(children1, children2)), (r1, r2))
    return P
