from overflow import OverflowPage


class LeafPage:
    # Cada folha pode armazenar até 2 chaves (sem contar overflow)
    CAPACITY = 2

    def __init__(self, keys, label=None):
        self.keys = keys
        self.label = label
        self.overflow = None

    # Insere chave na folha ou na cadeia de overflow
    def insert(self, key):
        if len(self.keys) < self.CAPACITY:
            self.keys.append(key)
            self.keys.sort()
        else:
            if self.overflow is None:
                self.overflow = OverflowPage()
            self.overflow.insert(key)

    # Busca chave na folha ou na cadeia de overflow
    def search(self, key):
        if key in self.keys:
            return True
        return self.overflow.search(key) if self.overflow else False

    # Remove chave da folha ou da cadeia de overflow
    def remove(self, key):
        if key in self.keys:
            self.keys.remove(key)
            return True

        if self.overflow:
            removed = self.overflow.remove(key)
            if self.overflow.is_empty():
                self.overflow = None
            return removed

        return False

    # Retorna todas as chaves da folha e da cadeia de overflow
    def get_all(self):
        result = self.keys[:]
        if self.overflow:
            result.extend(self.overflow.get_all())
        return sorted(result)