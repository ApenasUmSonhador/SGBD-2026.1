# Implementação de ISAM em Python

```txt
  ____              Trabalho Prático
 /\' .\    _____     ISAM em Python
/: \___\  / .  /\    - SGBD 2026.1 -
\' / . / /____/..\    Arthur Nunes
 \/___/  \'  '\  /    Samyra Vitoria 
          \'__'\/     Maria Vitoria
```

## Descrição

Este projeto consiste na implementação de uma simulação da estrutura de dados ISAM (Indexed Sequential Access Method) em Python, conforme proposto na disciplina de Sistema de Gerenciamento de Banco de Dados 2026.1

**O ISAM é uma estrutura de indexação estática, na qual:**

- Os índices permanecem fixos após a criação
- As inserções e remoções ocorrem apenas nas páginas folha
- O excesso de dados é tratado por meio de páginas de overflow encadeadas

## Objetivo

Simular o funcionamento de um índice ISAM, permitindo observar:

- Inserções de registros
- Remoções de registros
- Buscas por igualdade
- Buscas por intervalo
- Crescimento e impacto das páginas de overflow

## Estrutura do Projeto

``` bash
isam/
│── overflow.py   # Implementação das páginas de overflow encadeadas
│── leaf.py       # Implementação das páginas folha
│── isam.py       # Estrutura principal do índice ISAM
│── main.py       # Interface interativa (menu)
```

## Estrutura Inicial do Índice

A simulação inicia com uma estrutura fixa de índice conforme especificado no enunciado:

- Raiz com separador: 40
- Nós intermediários: 20, 33, 51, 63
- Páginas folha contendo 2 registros cada:

```txt
A: [10, 15]
B: [20, 27]
C: [33, 37]
D: [40, 46]
E: [51, 55]
F: [63, 97]
```

Essa estrutura não se altera durante a execução, respeitando a característica estática do ISAM.

Funcionalidades Implementadas

### Inserção

- O registro é direcionado à folha correta via índice
- Caso a folha esteja cheia:
  - Uma página de overflow é criada
  - Se necessário, novas páginas são encadeadas

### Remoção

- Remove da folha ou da cadeia de overflow
- Páginas de overflow vazias são automaticamente liberadas

### Busca por Igualdade

- Navega pelo índice até a folha
- Verifica a folha e suas páginas de overflow

### Busca por Intervalo

- Percorre sequencialmente as folhas
- Considera também os registros em overflow
- Retorna todos os valores dentro do intervalo

## Páginas de Overflow

As páginas de overflow:

- Possuem capacidade limitada (2 registros)
- São organizadas como uma lista encadeada
- São utilizadas apenas quando a folha está cheia

### Exemplo

D: [40, 46] -> [41, 42] -> [43, 44]

## Como Executar

- Execute o programa:

```bash
python main.py
```

- Para executar os testes:

```bash
python -m pytest
```

## Interface do Sistema

```txt
1 - Inserir
2 - Remover
3 - Buscar (igualdade)
4 - Buscar (intervalo)
5 - Mostrar estrutura
0 - Sair
```

## Exemplo de Execução

Ao iniciar, o sistema:

1. Exibe a estrutura inicial
2. Insere automaticamente os valores:
23, 48, 41, 42

3. Demonstra o uso de overflow:

```txt
B: [20, 27] -> [23]
D: [40, 46] -> [41, 42] -> [48]
```

## Análise

A implementação permite observar que:

- O ISAM mantém alta eficiência para buscas iniciais
- O desempenho degrada com o crescimento do overflow
- Não há reorganização automática da estrutura

## Limitações

- Não há persistência em disco (simulação em memória)
- Não há rebalanceamento do índice
- Estrutura fixa (não dinâmica como B+ Tree)

## Possíveis Melhorias

- Contagem de acessos (simulação de custo)
- Visualização gráfica da estrutura
- Ponteiros entre folhas
- Persistência em arquivos

## Autores

- [Arthur Vinicius Carneiro Nunes](https://github.com/ApenasUmSonhador)
- [Samyra Vitoria Lima de Almeida](https://github.com/samyraalmeida)
- [Maria Vitoria Alves da Silva](https://github.com/torishua)
