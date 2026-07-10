"""Machine universelle. À COMPLÉTER : encode/decode et run.  -> Jour 4 (E4.2)."""
from __future__ import annotations
import json
from .turing import TuringMachine, TMResult


def encode(machine: "TuringMachine") -> str:
    data = {
        "transitions": [[[q, a], [q2, b, d]] for (q, a), (q2, b, d) in machine.transitions.items()],
        "start": machine.start,
        "accept": sorted(machine.accept),
        "reject": sorted(machine.reject),
        "blank": machine.blank,
    }
    return json.dumps(data, sort_keys=True)


def decode(desc: str) -> "TuringMachine":
    data = json.loads(desc)
    transitions = {(q, a): (q2, b, d) for (q, a), (q2, b, d) in data["transitions"]}
    return TuringMachine(
        transitions=transitions,
        start=data["start"],
        accept=set(data["accept"]),
        blank=data["blank"],
        reject=set(data["reject"]),
    )


class UniversalTM:
    def run(self, encoded_machine: str, word: str, **kw) -> "TMResult":
        return decode(encoded_machine).run(word, **kw)
