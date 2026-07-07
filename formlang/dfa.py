"""AFD. À COMPLÉTER : run, accepts, minimize (Moore).  -> Jour 1 (E1.1, E1.2)."""
from __future__ import annotations
from dataclasses import dataclass, field
from collections import deque


@dataclass
class DFA:
    transitions: dict            # (state, sym) -> state
    start: str
    accept: set
    alphabet: set = field(default_factory=set)

    def __post_init__(self):
        if not self.alphabet:
            self.alphabet = {a for (_, a) in self.transitions}

    def run(self, w: str):
        state = self.start
        for l in w:
            state = self.transitions[(state, l)]
        return state in self.accept

    def accepts(self, w: str) -> bool:
        return self.run(w)

    # ----- fourni : utilitaires pour la minimisation --------------------------
    def _reachable(self) -> set:
        seen, todo = {self.start}, deque([self.start])
        while todo:
            s = todo.popleft()
            for a in self.alphabet:
                t = self.transitions.get((s, a))
                if t is not None and t not in seen:
                    seen.add(t)
                    todo.append(t)
        return seen

    def _completed(self):
        SINK = "__sink__"
        trans = dict(self.transitions)
        states = self._reachable()
        need = False
        for s in states:
            for a in self.alphabet:
                if (s, a) not in trans:
                    trans[(s, a)] = SINK
                    need = True
        if need:
            states = states | {SINK}
            for a in self.alphabet:
                trans[(SINK, a)] = SINK
        return states, trans
    
    def moore(self, *packets):
        _, trans = self._completed()
        alphabet = sorted(self.alphabet)

        def block_of(state):
            for i, p in enumerate(packets):
                if state in p:
                    return i
            return None

        new_packets = []
        for block in packets:
            groups = {}
            for state in block:
                signature = tuple(block_of(trans[(state, a)]) for a in alphabet)
                groups.setdefault(signature, set()).add(state)
            new_packets.extend(groups.values())

        if len(new_packets) == len(packets):
            return tuple(packets)
        return self.moore(*new_packets)

    def minimize(self) -> "DFA":
        states, trans = self._completed()
        packet_1 = states - self.accept
        packet_2 = states & self.accept
        packets = tuple(p for p in (packet_1, packet_2) if p)

        blocks = self.moore(*packets)

        block_of_state = {}
        for block in blocks:
            fblock = frozenset(block)
            for s in block:
                block_of_state[s] = fblock

        new_transitions = {}
        for block in blocks:
            rep = next(iter(block))
            fblock = frozenset(block)
            for a in self.alphabet:
                new_transitions[(fblock, a)] = block_of_state[trans[(rep, a)]]

        new_start = block_of_state[self.start]
        new_accept = {frozenset(block) for block in blocks if block & self.accept}

        return DFA(transitions=new_transitions, start=new_start,
                   accept=new_accept, alphabet=self.alphabet)

    def num_states(self) -> int:
        st = {self.start}
        for (s, _), t in self.transitions.items():
            st.add(s)
            st.add(t)
        return len(st)
