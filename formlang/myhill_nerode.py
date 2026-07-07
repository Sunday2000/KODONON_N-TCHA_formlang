"""Classes de Myhill-Nerode (approx. sur suffixes témoins). À COMPLÉTER.
-> Jour 5 (E5.3)."""
from __future__ import annotations


def nerode_classes(accepts, words, suffixes):
    # TODO (E5.3) : regrouper words par signature
    #   sig(w) = tuple(accepts(w + s) for s in suffixes)
    raise NotImplementedError("nerode_classes — à compléter (E5.3)")


def equivalent(u, v, accepts, suffixes) -> bool:
    # FOURNI
    return all(accepts(u + s) == accepts(v + s) for s in suffixes)
