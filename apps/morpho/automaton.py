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

    A.add_rule("nil", (), "NIL")

    A.add_rule("prefix", (), "PREFIX")
    A.add_rule("prefixes", ("PREFIX", "NIL"), "PREFIXES")
    A.add_rule("prefixes", ("PREFIX", "PREFIXES"), "PREFIXES")

    A.add_rule("suffix", (), "SUFFIX")
    A.add_rule("suffixes", ("SUFFIX", "NIL"), "SUFFIXES")
    A.add_rule("suffixes", ("SUFFIX", "SUFFIXES"), "SUFFIXES")

    A.add_rule("root", (), "ROOT")
    A.add_rule("rest", ("ROOT", "NIL"), "REST")
    A.add_rule("rest", ("ROOT", "SUFFIXES"), "REST")

    A.add_rule("word", ("NIL", "REST"), "WORD")
    A.add_rule("word", ("PREFIXES", "REST"), "WORD")

    return A


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
