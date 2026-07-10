"""Calculatrice unaire. À COMPLÉTER.  -> Jour 4 (E4.3)."""
from .machines import ADD, SUB


def _ones(s: str) -> int:
    return s.count("1")


class Calculatrice:
    def addition(self, n: int, m: int) -> int:
        return _ones(ADD.run("1" * n + "+" + "1" * m).tape)

    def soustraction(self, n: int, m: int) -> int:   # tronquée à 0
        if m > n:
            return 0
        return _ones(SUB.run("1" * n + "-" + "1" * m).tape)

    def multiplication(self, n: int, m: int) -> int:
        total = 0
        for _ in range(m):
            total = self.addition(total, n)
        return total

    def division(self, n: int, m: int):              # -> (quotient, reste)
        if m == 0:
            raise ZeroDivisionError("division par zéro")
        q, r = 0, n
        while r >= m:
            r = self.soustraction(r, m)
            q += 1
        return (q, r)

    def chainer(self, v0: int, ops: list) -> int:
        v = v0
        for op, x in ops:
            if op == "+":
                v = self.addition(v, x)
            elif op == "-":
                v = self.soustraction(v, x)
            elif op == "*":
                v = self.multiplication(v, x)
            elif op == "/":
                v, _ = self.division(v, x)
        return v
