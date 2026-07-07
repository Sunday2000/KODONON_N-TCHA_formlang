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
        # TODO (E3.1) : étiquetage POST-ORDRE (feuilles -> racine).
        raise NotImplementedError("TreeAutomaton.run — à compléter (E3.1)")

    def accepts(self, t: "Term") -> bool:
        # TODO (E3.1) : True ssi run(t) in self.final.
        raise NotImplementedError("TreeAutomaton.accepts — à compléter (E3.1)")


def product(a1: "TreeAutomaton", a2: "TreeAutomaton") -> "TreeAutomaton":
    # TODO (E3.4) : automate produit, L = L(a1) inter L(a2).
    raise NotImplementedError("product — à compléter (E3.4)")
