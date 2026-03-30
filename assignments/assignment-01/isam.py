from index_node import IndexNode
from leaf import LeafPage

import json

class ISAM:
    def __init__(self, filename='tree_configure.json'):
        self.config = self._read_index_config(filename=filename)
        self.root: IndexNode = self._build_tree()

    def _read_index_config(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    def _build_tree(self):
        leaves = []
        for i in self.config["leaves"]:
            keys, label = i.values()
            leaves.append(LeafPage(keys, label))

        # construindo os índices
        last_level = leaves
        for index, level in enumerate(reversed(self.config["static"])):
            # print(index, level)
            nodes = level["nodes"]
            current_level = []
            for node in nodes:
                keys = node.get("keys", None)
                label = node.get("label", None)
                capacity = node.get("capacity", None)
                new_node = IndexNode(keys=keys, label=label, capacity=capacity)
                
                for _ in range(new_node.capacity):
                    new_node.children.append(last_level.pop(0))  # Adiciona um filho da última camada (inicialmente as folhas)
                
                current_level.append(new_node)
            last_level = current_level

        root = last_level[0]  # O último nível processado será a raiz
        
        return root
    
    def _find_leaf(self, key):
        # Começa pela raiz
        current_node = self.root
        
        # Navega pela árvore até encontrar uma folha
        while True:
            if isinstance(current_node, LeafPage):
                return current_node
            # Usa o método find_child do IndexNode para encontrar o filho apropriado
            current_node = current_node.find_child(key)

        return current_node
    
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
    
    def _collect_all_leaves(self, node=None):
        """
        Coleta todas as folhas da árvore em ordem (left to right).
        
        Args:
            node: Nó a partir do qual coletar (se None, usa a raiz)
            
        Returns:
            list: Lista de todas as LeafPages em ordem
        """
        if node is None:
            node = self.root
        
        # Se é uma folha, retorna ela em uma lista
        if isinstance(node, LeafPage):
            return [node]
        
        # Se é um nó de índice, coleta folhas de todos os filhos
        all_leaves = []
        for child in node.children:
            all_leaves.extend(self._collect_all_leaves(child))
        
        return all_leaves
    
    def range_search(self, start, end):
        """
        Busca todas as chaves no intervalo [start, end].
        Percorre as folhas em ordem e coleta as chaves que estão no intervalo.
        
        Args:
            start: Chave inicial do intervalo (inclusive)
            end: Chave final do intervalo (inclusive)
            
        Returns:
            list: Lista de chaves encontradas no intervalo, em ordem
        """
        result = []
        
        # Coleta todas as folhas em ordem
        all_leaves = self._collect_all_leaves()
        
        # Percorre cada folha
        for leaf in all_leaves:
            # Pega todas as chaves da folha (incluindo overflow)
            leaf_keys = leaf.get_all()
            
            # Filtra as chaves que estão no intervalo
            for key in leaf_keys:
                if start <= key <= end:
                    result.append(key)
            
            # Otimização: para quando as chaves passam do intervalo
            if leaf_keys and min(leaf_keys) > end:
                break
        
        return sorted(result)
    
    def print_structure(self):
        print(r"""    ╔════════════════════════════════════════════════════════════╗
    ║                    ESTRUTURA ISAM ATUAL                    ║
    ╚════════════════════════════════════════════════════════════╝
    ╔════════════════════════════════════════════════════════════╗""")
        self.root.print_structure()
        print(r"""
    ╚════════════════════════════════════════════════════════════╝""")

        return None