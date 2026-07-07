"""Automate à pile (acceptation pile vide). À COMPLÉTER.  -> Jour 2 (E2.1)."""
from __future__ import annotations


class DelimiterPDA:
    def __init__(self, pairs=(("[", "]"), ("(", ")")), ignore=("a", "o", "r", "e")):
        self.open = {o for o, _ in pairs}
        self.match = {c: o for o, c in pairs}     # fermant -> ouvrant attendu
        self.ignore = set(ignore)

    def accepts(self, w: str) -> bool:
        # TODO (E2.1) : avec une pile (list).
        raise NotImplementedError("DelimiterPDA.accepts — à compléter (E2.1)")
