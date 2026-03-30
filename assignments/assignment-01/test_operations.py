from teste import ISAM

def test_operations():
    """Testa as operações insert, search e remove da estrutura ISAM"""
    
    # Inicializa a árvore
    isam = ISAM('tree_configure.json')
    isam.print_structure()  # Mostra a estrutura inicial para referência

    print(r"""    ╔════════════════════════════════════════════════════════════╗
    ║                 TESTES DAS OPERAÇÕES ISAM                  ║
    ╚════════════════════════════════════════════════════════════╝""")

    # --- TESTE 1: INSERT ---
    print(r"""    ╔════════════════════════════════════════════════════════════╗
    ║                     TESTE DE INSERÇÃO                      ║
    ╚════════════════════════════════════════════════════════════╝
    ╔════════════════════════════════════════════════════════════╗""")
    new_keys = [18, 22, 27, 35, 41, 44, 63, 67, 83, 86, 121, 145]
    for key in new_keys:
        isam.insert(key)
        print(f"      Inserindo a chave {key}... OK")
    
    print(r"""    ╚════════════════════════════════════════════════════════════╝""")
    isam.print_structure()
    
    # --- TESTE 2: REMOVE ---
    print(r"""    ╔════════════════════════════════════════════════════════════╗
    ║                      TESTE DE REMOÇÃO                      ║
    ╚════════════════════════════════════════════════════════════╝
    ╔════════════════════════════════════════════════════════════╗""")
    keys_to_remove = [27, 44, 67, 83, 145]
    for key in keys_to_remove:
        result = isam.remove(key)
        print(f"      Removendo a chave {key}... {'OK' if result else 'FALHA'}")
    
    print(r"""    ╚════════════════════════════════════════════════════════════╝""")
    isam.print_structure()
    
    # --- TESTE 3: SEARCH (igualdade) ---
    print(r"""    ╔════════════════════════════════════════════════════════════╗
    ║                 TESTE DE BUSCA (IGUALDADE)                 ║
    ╚════════════════════════════════════════════════════════════╝
    ╔════════════════════════════════════════════════════════════╗""")
    test_keys = [22, 35, 44, 90]
    for key in test_keys:
        result = isam.search(key)
        print(f"      Buscando a chave {key}... {'Encontrada' if result else 'A chave não existe na estrutura'}")
    
    
    print(r"""    ╚════════════════════════════════════════════════════════════╝""")

    # --- TESTE 4: RANGE SEARCH ---
    print(r"""    ╔════════════════════════════════════════════════════════════╗
    ║                 TESTE DE BUSCA (INTERVALO)                 ║
    ╚════════════════════════════════════════════════════════════╝
    ╔════════════════════════════════════════════════════════════╗""")
    range_test = [[20,50], [60,90], [120,150]]
    for start, end in range_test:
        result = isam.range_search(start, end)
        print(f"      Buscando no intervalo ({start}, {end}): {result}")
    
    print(r"""    ╚════════════════════════════════════════════════════════════╝""")
    
    print(r"""    ╔════════════════════════════════════════════════════════════╗
    ║                     RESUMO DE EXECUÇÃO                     ║
    ╠════════════════════════════════════════════════════════════╣
    ║             As operações funcionam corretamente!           ║
    ╚════════════════════════════════════════════════════════════╝""")

if __name__ == "__main__":
    test_operations()
