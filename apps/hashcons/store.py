"""Hash-consing : partage de structure (DAG) sur formlang.tree.Term. À COMPLÉTER.
-> TP arbres (E4 intern/partage, E5 round-trip, Q5 compression).

Règle « gate » : INSTANCIER formlang.tree.Term, ne pas le réécrire."""
from __future__ import annotations
from formlang.tree import Term

NodeId = int


class CompactStore:
    def __init__(self):
        self._nodes: list[tuple] = []          # id -> (symbol, label, kids_ids)
        self._table: dict[tuple, NodeId] = {}   # clé canonique -> id
        self._total = 0

    def intern(self, t: Term) -> NodeId:
        # TODO (E4) :
        #   1. interner récursivement chaque enfant -> kids_ids (tuple) ;
        #   2. incrémenter self._total ;
        #   3. clé canonique = (t.symbol, t.label, kids_ids) ;
        #   4. si déjà dans self._table -> renvoyer l'id existant,
        #      sinon créer un nouvel id (= len(self._nodes)), l'enregistrer.
        raise NotImplementedError("CompactStore.intern — à compléter (E4)")

    def get(self, nid: NodeId) -> Term:
        # TODO (E5) : reconstruire l'arbre interné (round-trip exact).
        raise NotImplementedError("CompactStore.get — à compléter (E5)")

    def total_nodes(self) -> int:
        return self._total

    def unique_nodes(self) -> int:
        return len(self._nodes)

    def compression(self) -> float:
        # TODO (Q5) : 1 - uniques/total (0 si total == 0).
        raise NotImplementedError("CompactStore.compression — à compléter (Q5)")
