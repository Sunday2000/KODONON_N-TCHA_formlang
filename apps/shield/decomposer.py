"""AttackDecomposer (instancie formlang.tree). À COMPLÉTER : règles Delta.
-> Jour 3 (E3.3). 100% structurel. Constructeurs FOURNIS."""
from formlang.tree import Term, TreeAutomaton

SAFE, OVR, ROLE, DANGER = "safe", "ovr", "role", "danger"
_SEV = {SAFE: 0, OVR: 1, ROLE: 2}
_BY_SEV = {0: SAFE, 1: OVR, 2: ROLE}
_ALL = (SAFE, OVR, ROLE, DANGER)


def _seq(x, y):
    # TODO (E3.3) : règle de fusion pour seq.
    raise NotImplementedError("_seq — à compléter (E3.3)")


def shield_automaton() -> TreeAutomaton:
    A = TreeAutomaton(final_states={DANGER})
    # TODO (E3.3) : ajouter les règles avec A.add_rule(...).
    raise NotImplementedError("shield_automaton — à compléter (E3.3)")


# ----- constructeurs FOURNIS ------------------------------------------------
def txt():  return Term("txt")
def enc():  return Term("enc")
def ovr():  return Term("ovr")
def role(): return Term("role")
def seq(a, b): return Term("seq", (a, b))
def frame(a):  return Term("frame", (a,))
def sys(a):    return Term("sys", (a,))


def is_blocked(A: TreeAutomaton, t: Term) -> bool:
    return A.accepts(t)

# ----- P4.5 : « dangereux ET doublement encodé » (produit A x A_enc) ---------
def enc_automaton() -> TreeAutomaton:
    # TODO (E3.6) : automate qui COMPTE les feuilles `enc` (plafonné à 2),
    #   final = {2}. Même signature que shield_automaton :
    #     feuilles txt/ovr/role -> 0, enc -> 1
    #     seq(x,y) -> min(2, x+y) ; frame(x)->x ; sys(x)->x  (pour x in 0,1,2)
    raise NotImplementedError("enc_automaton — à compléter (E3.6)")


def dangerous_and_double_encoded() -> TreeAutomaton:
    # TODO (E3.6) : intersection via formlang.tree.product :
    #   return product(shield_automaton(), enc_automaton())
    raise NotImplementedError("dangerous_and_double_encoded — à compléter (E3.6)")
