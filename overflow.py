class OverflowPage:
    # Cada página de overflow pode armazenar até 2 chaves
    # Isso está implícito no documento
    CAPACITY = 2

    def __init__(self):
        self.keys = []
        self.next = None


    def insert(self, key):
        current = self

        # Percorre até achar uma página com espaço
        while True:
            if len(current.keys) < self.CAPACITY:
                current.keys.append(key)
                current.keys.sort()
                return
            if current.next is None:
                current.next = OverflowPage()
            # Move para próxima página de overflow
            current = current.next

    # Busca simples na cadeia de overflow
    def search(self, key):
        current = self
        while current:
            if key in current.keys:
                return True
            current = current.next
        return False

    # Remove chave da cadeia de overflow e limpa páginas vazias
    def remove(self, key):
        current = self
        prev = None

        while current:
            if key in current.keys:
                current.keys.remove(key)

                # Remove página vazia da cadeia
                if len(current.keys) == 0:
                    if prev:
                        prev.next = current.next
                    else:
                        # Caso seja a primeira overflow
                        if current.next:
                            self.keys = current.next.keys
                            self.next = current.next.next
                        else:
                            self.keys = []
                            self.next = None
                return True

            prev = current
            current = current.next

        return False

    # Verifica se a página de overflow está vazia (sem chaves e sem próxima)
    # Utilizado em LeafPage para limpar referências a páginas de overflow vazias
    def is_empty(self):
        return len(self.keys) == 0 and self.next is None

    # Retorna todas as chaves da cadeia de overflow
    def get_all(self):
        result = []
        current = self
        while current:
            result.extend(current.keys)
            current = current.next
        return result
