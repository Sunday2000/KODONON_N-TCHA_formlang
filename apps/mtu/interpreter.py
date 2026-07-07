"""La machine de Turing UNIVERSELLE comme application (TP MTU). À COMPLÉTER.

L'interpréteur ne doit PAS réécrire de boucle d'exécution : il encode M puis
DÉLÈGUE à formlang.utm.UniversalTM.  -> Jour 4 (E4.2 / E4.4)."""
from __future__ import annotations
from formlang.utm import UniversalTM, encode
from .machines import ADD, SUB


class UniversalInterpreter:
    def __init__(self):
        self._U = UniversalTM()

    def run(self, machine, word, **kw):
        # TODO : encoder `machine` puis déléguer à self._U.run(<M>, word, **kw).
        raise NotImplementedError("UniversalInterpreter.run — à compléter")


def addition_via_utm(n: int, m: int) -> int:
    # TODO : lancer ADD via la machine universelle ; compter les '1' du ruban.
    raise NotImplementedError("addition_via_utm — à compléter")


def soustraction_via_utm(n: int, m: int) -> int:
    # TODO : si m > n -> 0 ; sinon lancer SUB via U.
    raise NotImplementedError("soustraction_via_utm — à compléter")
