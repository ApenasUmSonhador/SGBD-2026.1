from teste import ISAM
from os import system, name

# Função para limpar a tela (compatível com Windows e Unix)
def clear_screen():
    system('cls' if name == 'nt' else 'clear')

# Função para exibir arte ASCII (apenas para diversão)
def ascii_art():
    # Creditos para: https://www.asciiart.eu/art/147e286317b77955
    print(r"""Por Arthur Nunes, Samyra Vitoria e Maria Vitoria
                 ____
                /\' .\    _____
               /: \___\  / .  /\
               \' / . / /____/..\
                \/___/  \'  '\  /
                         \'__'\/
    """)

# Função para exibir o menu de opções
def menu():
    print(r"""    ╔════════════════════════════════════════════════════════════╗
    ║                       Simulador ISAM                       ║
    ╠════════════════════════════════════════════════════════════╣
    ║  [1] Inserir                                               ║
    ║  [2] Remover                                               ║
    ║  [3] Buscar (igualdade)                                    ║
    ║  [4] Buscar (intervalo)                                    ║
    ║  [5] Mostrar estrutura                                     ║
    ║  [0] Sair                                                  ║
    ╚════════════════════════════════════════════════════════════╝""")


# Função principal que controla o fluxo do programa
def main():
    # Inicializa a instância do ISAM
    isam = ISAM()
    clear_screen()
    ascii_art()
    # Loop infinito para manter o menu ativo
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        clear_screen()
        ascii_art()

        # Opção 1: Inserir uma chave
        if opcao == "1":
            key = int(input("Digite a chave para inserir: "))
            isam.insert(key)
            print("Inserido com sucesso.")

        # Opção 2: Remover uma chave
        elif opcao == "2":
            key = int(input("Digite a chave para remover: "))
            if isam.remove(key):
                print("Removido com sucesso.")
            else:
                print("Chave não encontrada.")

        # Opção 3: Buscar uma chave específica
        elif opcao == "3":
            key = int(input("Digite a chave para buscar: "))
            if isam.search(key):
                print("Chave encontrada.")
            else:
                print("Chave não encontrada.")

        # Opção 4: Buscar chaves em um intervalo
        elif opcao == "4":
            start = int(input("Início do intervalo: "))
            end = int(input("Fim do intervalo: "))
            result = isam.range_search(start, end)
            print("Resultado:", result)

        # Opção 5: Exibir a estrutura do ISAM
        elif opcao == "5":
            isam.print_structure()

        # Opção 0: Sair do programa
        elif opcao == "0":
            print("Encerrando...")
            break

        # Mensagem de erro para opção inválida
        else:
            print("Opção inválida.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()