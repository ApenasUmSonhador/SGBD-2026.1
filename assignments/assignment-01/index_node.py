class IndexNode:
    def __init__(self, keys:list=None, children:list=None, label:str=None, 
                 capacity:int=None, is_root:bool=False):
        self.keys = keys if keys is not None else []
        self.children = children if children is not None else []
        self.label = label
        self.capacity = capacity if capacity is not None else len(self.keys) + 1
        self.is_root = is_root or (label is not None and label.upper() == "ROOT")
        self.overflow = None  # Para compatibilidade com LeafPage
    
    def find_child(self, key):
        # Se não tem filhos, retorna None
        if not self.children:
            return None
        
        # Se há apenas um filho, sempre o retorna
        if len(self.children) == 1:
            return self.children[0]
        
        # Estratégia 1: Se há N chaves e N+1 filhos (B-tree padrão)
        if len(self.keys) + 1 == len(self.children):
            for i, k in enumerate(self.keys):
                if key < k:
                    return self.children[i]
            
            # A chave buscada é maior que a ultima key, retorna o ultimo filho
            return self.children[-1]

        # Estratégia desnecessária pois a configuração dada tem exatamente N chaves e N+1 filhos,
        #  mas deixo aqui para mostrar como estávamos abordando o problema.
        # # Estratégia 2: Outro cenário - verifica ranges dos filhos, para compatibilidade com a configuração dada
        # for child in self.children:
        #     if child.keys:
        #         min_key = min(child.keys)
        #         max_key = max(child.keys)
                
        #         if min_key <= key <= max_key:
        #             return child
        
        # Fallback: retorna o último filho
        return self.children[-1]
    
    def print_structure(self, level=0, tab="  "):
        # Imprime a estrutura da árvore para debug.

        indent = tab * (level+3)
        node_type = "ROOT" if self.is_root else f"›▸ INDEX {self.label}" if self.label else "INDEX"
        
        print(f"{indent} {node_type}: {self.keys}")
        
        for i, child in enumerate(self.children):
            if isinstance(child, IndexNode):
                child.print_structure(level + 1)
            else:
                # É uma folha
                leaf_info = f"{indent}   ›▸ LEAF "
                leaf_info += f"{child.label}: {child.keys}" if child.label else f": {child.keys}"
                
                # Mostra páginas de overflow se existirem
                if child.overflow:
                    current = child.overflow
                    while current:
                        leaf_info += f" → {current.keys}"
                        current = current.next
                
                print(leaf_info)
        
        