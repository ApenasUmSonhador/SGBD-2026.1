class IndexNode:
    def __init__(self, keys, children=[], level=0,label=None):
        self.label = label          # Identificador (ex: "Nó A")
        self.keys = keys          # Lista de chaves separadoras (ex: [20, 33])
        self.level = level          # Ni
        self.capacity = len(keys) + 1
        self.children = children  # Lista de referências (outros IndexNodes ou LeafPages)

    def find_child(self, key):
        """
        Lógica clássica de árvore de busca:
        Se temos chaves [20, 33], os intervalos são:
        key < 20          -> filho[0]
        20 <= key < 33    -> filho[1]
        key >= 33         -> filho[2]
        """
        for i, k in enumerate(self.keys):
            if key < k:
                return self.children[i]
        # Se for maior ou igual à última chave, retorna o último filho
        return self.children[-1]
