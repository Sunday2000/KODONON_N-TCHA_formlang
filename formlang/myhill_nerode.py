"""Classes de Myhill-Nerode (approx. sur suffixes témoins). À COMPLÉTER.
-> Jour 5 (E5.3)."""
from __future__ import annotations


def nerode_classes(accepts, words, suffixes):
    groups: dict[tuple, set] = {}
    for w in words:
        sig = tuple(accepts(w + s) for s in suffixes)
        groups.setdefault(sig, set()).add(w)
    return list(groups.values())


def equivalent(u, v, accepts, suffixes) -> bool:
    # FOURNI
    return all(accepts(u + s) == accepts(v + s) for s in suffixes)
