"""Calculatrice unaire. À COMPLÉTER.  -> Jour 4 (E4.3)."""
from .machines import ADD, SUB


def _ones(s: str) -> int:
    return s.count("1")


class Calculatrice:
    def addition(self, n: int, m: int) -> int:
        # TODO (E4.3)
        raise NotImplementedError("addition — à compléter (E4.3)")

    def soustraction(self, n: int, m: int) -> int:   # tronquée à 0
        # TODO (E4.3)
        raise NotImplementedError("soustraction — à compléter (E4.3)")

    def multiplication(self, n: int, m: int) -> int:
        # TODO (E4.3)
        raise NotImplementedError("multiplication — à compléter (E4.3)")

    def division(self, n: int, m: int):              # -> (quotient, reste)
        # TODO (E4.3)
        raise NotImplementedError("division — à compléter (E4.3)")

    def chainer(self, v0: int, ops: list) -> int:
        # TODO (E4.3)
        raise NotImplementedError("chainer — à compléter (E4.3)")
