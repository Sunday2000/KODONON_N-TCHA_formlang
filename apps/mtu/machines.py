"""Opérations comme VRAIES machines de Turing. À COMPLÉTER : tables ADD, SUB.
-> Jour 4 (E4.3)."""
from formlang.turing import TuringMachine

ADD = TuringMachine(
    transitions={
        # 1^n + 1^m : le '+' devient un '1' puis on efface le dernier '1'.
        ("q0", "1"): ("q0", "1", "R"),
        ("q0", "+"): ("q1", "1", "R"),
        ("q1", "1"): ("q1", "1", "R"),
        ("q1", "_"): ("q2", "_", "L"),
        ("q2", "1"): ("qf", "_", "S"),
    },
    start="q0", accept={"qf"},
)

SUB = TuringMachine(
    transitions={
        # 1^n - 1^m (tronquée à 0) : on apparie un '1' de gauche avec un '1'
        # de droite à chaque tour (marqueur 'y'), en gardant '-' comme pivot fixe.
        ("q0", "1"): ("q0", "1", "R"),
        ("q0", "-"): ("qFindL", "-", "L"),

        ("qFindL", "y"): ("qFindL", "y", "L"),
        ("qFindL", "1"): ("qBackL", "y", "R"),
        ("qFindL", "_"): ("qZero", "_", "R"),

        ("qBackL", "y"): ("qBackL", "y", "R"),
        ("qBackL", "-"): ("qFindR", "-", "R"),

        ("qFindR", "y"): ("qFindR", "y", "R"),
        ("qFindR", "1"): ("qBackR", "y", "L"),
        ("qFindR", "_"): ("qKeep", "_", "L"),

        ("qBackR", "y"): ("qBackR", "y", "L"),
        ("qBackR", "-"): ("qFindL", "-", "L"),

        # droite épuisée avant la gauche -> résultat = n - m (restaure 1 unité)
        ("qKeep", "y"): ("qKeep", "_", "L"),
        ("qKeep", "-"): ("qKeepRestore", "_", "L"),
        ("qKeepRestore", "y"): ("qKeepAfter", "1", "L"),
        ("qKeepAfter", "y"): ("qKeepAfter", "_", "L"),
        ("qKeepAfter", "1"): ("qf", "1", "S"),
        ("qKeepAfter", "_"): ("qf", "_", "S"),

        # gauche épuisée avant (ou en même temps que) la droite -> résultat = 0
        ("qZero", "y"): ("qZero", "_", "R"),
        ("qZero", "-"): ("qZero", "_", "R"),
        ("qZero", "1"): ("qZero", "_", "R"),
        ("qZero", "_"): ("qf", "_", "S"),
    },
    start="q0", accept={"qf"},
)
