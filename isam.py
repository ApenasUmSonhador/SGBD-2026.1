from leaf import LeafPage


class ISAM:
    def __init__(self):
        # Raiz adotada pelo documento
        self.root = 40
        # Estrutura fixa com 6 folhas pré-definidas pelo documento
        self.leaves = {
            "A": LeafPage([10, 15]),
            "B": LeafPage([20, 27]),
            "C": LeafPage([33, 37]),
            "D": LeafPage([40, 46]),
            "E": LeafPage([51, 55]),
            "F": LeafPage([63, 97]),
        }

    def _find_leaf(self, key):
        # Folhas esquerdas
        if key < self.root:
            if key < 20:
                return self.leaves["A"]
            elif key < 33:
                return self.leaves["B"]
            else:
                return self.leaves["C"]
            
        # Folhas direitas
        else:
            if key < 51:
                return self.leaves["D"]
            elif key < 63:
                return self.leaves["E"]
            else:
                return self.leaves["F"]

    # Operações básicas
    def insert(self, key):
        leaf = self._find_leaf(key)
        leaf.insert(key)

    def search(self, key):
        leaf = self._find_leaf(key)
        return leaf.search(key)

    def remove(self, key):
        leaf = self._find_leaf(key)
        return leaf.remove(key)

    # Busca por intervalo
    def range_search(self, start, end):
        result = []

        ordered_leaves = ["A", "B", "C", "D", "E", "F"]

        # Encontra folha inicial
        start_leaf = self._find_leaf(start)

        start_index = list(self.leaves.values()).index(start_leaf)

        for i in range(start_index, len(ordered_leaves)):
            leaf = self.leaves[ordered_leaves[i]]

            for k in leaf.get_all():
                if start <= k <= end:
                    result.append(k)

            # para quando passar do intervalo
            if leaf.get_all() and min(leaf.get_all()) > end:
                break

        return sorted(result)

    # Bônus: função para mostrar a estrutura atual (para debug)
    def print_structure(self):
        print(r"""    ╔════════════════════════════════════════╗
    ║          Estrutura ISAM atual          ║
    ╚════════════════════════════════════════╝
    ╔════════════════════════════════════════╗""")
        
        for name, leaf in self.leaves.items():
            content = f"{name}: {leaf.keys}"
            
            if leaf.overflow:
                current = leaf.overflow
                while current:
                    content += f" → {current.keys}"
                    current = current.next
            
            print(content.center(50))
        
        print(r"""
    ╚════════════════════════════════════════╝""")