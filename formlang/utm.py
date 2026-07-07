"""Machine universelle. À COMPLÉTER : encode/decode et run.  -> Jour 4 (E4.2)."""
from __future__ import annotations
import json
from .turing import TuringMachine, TMResult


def encode(machine: "TuringMachine") -> str:
    # TODO (E4.2) : linéarisation INJECTIVE de M en JSON (chaîne <M>).
    raise NotImplementedError("encode — à compléter (E4.2)")


def decode(desc: str) -> "TuringMachine":
    # TODO (E4.2) : reconstruire M depuis <M> (réciproque exacte de encode).
    raise NotImplementedError("decode — à compléter (E4.2)")


class UniversalTM:
    def run(self, encoded_machine: str, word: str, **kw) -> "TMResult":
        # TODO (E4.2) : U décode <M> puis simule sur w.
        raise NotImplementedError("UniversalTM.run — à compléter (E4.2)")
