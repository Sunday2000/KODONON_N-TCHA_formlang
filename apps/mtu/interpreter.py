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
        return self._U.run(encode(machine), word, **kw)


def addition_via_utm(n: int, m: int) -> int:
    interp = UniversalInterpreter()
    res = interp.run(ADD, "1" * n + "+" + "1" * m)
    return res.tape.count("1")


def soustraction_via_utm(n: int, m: int) -> int:
    if m > n:
        return 0
    interp = UniversalInterpreter()
    res = interp.run(SUB, "1" * n + "-" + "1" * m)
    return res.tape.count("1")
