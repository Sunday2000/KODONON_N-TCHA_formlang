"""Automate morphologique (instancie formlang.tree). À COMPLÉTER : règles Delta.
-> Jour 3 (E3.2). Constructeurs et classify FOURNIS."""
from formlang.tree import Term, TreeAutomaton


# ----- constructeurs FOURNIS ------------------------------------------------
def prefix(s): return Term("prefix", label=s)
def root(s):   return Term("root",   label=s)
def suffix(s): return Term("suffix", label=s)
def nil():     return Term("nil")
def prefixes(h, t): return Term("prefixes", (h, t))
def suffixes(h, t): return Term("suffixes", (h, t))
def rest(r, s):     return Term("rest", (r, s))
def word(p, r):     return Term("word", (p, r))


def build_word(pres, root_str, sufs) -> Term:
    pc = nil()
    for p in reversed(pres):
        pc = prefixes(prefix(p), pc)
    sc = nil()
    for s in reversed(sufs):
        sc = suffixes(suffix(s), sc)
    return word(pc, rest(root(root_str), sc))


# ----- à compléter ----------------------------------------------------------
def morpho_automaton() -> TreeAutomaton:
    A = TreeAutomaton(final_states={"WORD"})
    # TODO (E3.2) : ajouter les règles avec A.add_rule(symbole, (états...), résultat).
    raise NotImplementedError("morpho_automaton — à compléter (E3.2)")


# ----- FOURNI ---------------------------------------------------------------
def _contains(t: Term, sym: str) -> bool:
    if t.symbol == sym:
        return True
    return any(_contains(c, sym) for c in t.children)


def classify(A: TreeAutomaton, t: Term) -> str:
    if not A.accepts(t):
        return "INVALID"
    p, s = _contains(t, "prefix"), _contains(t, "suffix")
    if p and s:
        return "CIRCUMFIXED"
    if s:
        return "SUFFIXED"
    if p:
        return "PREFIXED"
    return "BARE"
