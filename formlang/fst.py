"""Transducteur fini séquentiel. À COMPLÉTER : transduce.  -> Jour 1 (E1.4)."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class SequentialFST:
    transitions: dict            # (state, in_sym) -> (next_state, out_sym)
    start: str
    finals: set
    identity_on_missing: bool = False

    def transduce(self, w: str) -> str:
        # TODO (E1.4) : lettre par lettre, à partir de self.start.
        raise NotImplementedError("SequentialFST.transduce — à compléter (E1.4)")


def compose(t1: "SequentialFST", t2: "SequentialFST") -> "SequentialFST":
    # FOURNI : t(w) = t2(t1(w)). États = paires.
    trans = {}
    for (s1, a), (s1n, b) in t1.transitions.items():
        for (s2, x), (s2n, c) in t2.transitions.items():
            if x == b:
                trans[((s1, s2), a)] = ((s1n, s2n), c)
    finals = {(f1, f2) for f1 in t1.finals for f2 in t2.finals}
    return SequentialFST(trans, (t1.start, t2.start), finals)


def leet_fst() -> "SequentialFST":
    # TODO (E1.4) : un seul état 'q0' (final) ; 4/a 3/e 0/o 1/i 5/s ;
    # identité sinon (utiliser identity_on_missing=True).
    raise NotImplementedError("leet_fst — à compléter (E1.4)")


def reverse_twoway(w: str) -> str:
    # FOURNI : renversement (modélise une transduction bidirectionnelle).
    return w[::-1]
