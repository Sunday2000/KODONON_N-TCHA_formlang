"""Grammaire hors-contexte : génération bornée. À COMPLÉTER.  -> Jour 2 (E2.2)."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class CFG:
    rules: dict
    start: str
    nonterminals: set

    def generate(self, max_len: int) -> set:
        lang = {nt: set() for nt in self.nonterminals}
        changed = True
        while changed:
            changed = False
            for nt in self.nonterminals:
                produced = set(lang[nt])
                for production in self.rules.get(nt, []):
                    candidates = {""}
                    for sym in production:
                        options = lang[sym] if sym in self.nonterminals else {sym}
                        candidates = {c + o for c in candidates for o in options
                                      if len(c) + len(o) <= max_len}
                        if not candidates:
                            break
                    produced |= candidates
                if produced != lang[nt]:
                    lang[nt] = produced
                    changed = True
        return lang[self.start]


def balanced_cfg() -> "CFG":
    # FOURNI : S -> S S | [ S ] | ( S ) | a | o | r | eps
    return CFG(
        rules={"S": [("S", "S"), ("[", "S", "]"), ("(", "S", ")"),
                     ("a",), ("o",), ("r",), ()]},
        start="S", nonterminals={"S"},
    )
