# Análise de Algoritmos no Projeto ConfereAí

Este documento detalha a implementação em Python de estruturas de dados e algoritmos clássicos aplicados ao sistema de gestão de almoxarifado "ConfereAí". O script simula o registro de consumo de insumos hospitalares, a busca por itens e a ordenação de dados para exibição em um painel de controle.

## Como Executar o Código

1.  Salve o código em um arquivo com a extensão `.py` (por exemplo, `simulador_confereai.py`).
2.  Abra um terminal ou prompt de comando.
3.  Navegue até o diretório onde salvou o arquivo.
4.  Execute o comando: `python simulador_confereai.py`

O terminal exibirá o passo a passo da simulação, demonstrando o funcionamento de cada estrutura de dados e algoritmo.

## Estrutura do Código

O script é dividido em cinco partes principais:

1.  [cite_start]**Configuração Inicial**: Inicializa uma lista de dicionários chamada `inventario`, que simula o banco de dados de insumos do almoxarifado, com base nos dados do protótipo do projeto[cite: 98, 103].
2.  **Fila e Pilha**: Implementa as estruturas para gerenciar o registro de consumo. A **Fila** (`deque`) garante a ordem cronológica (FIFO), essencial para relatórios históricos precisos. A **Pilha** (`list`) é usada para consultas de operações recentes (LIFO).
3.  [cite_start]**Estruturas de Busca**: Contém as funções `busca_sequencial` e `busca_binaria` para localizar itens específicos, correspondendo ao caso de uso "Consultar Item"[cite: 61].
4.  **Ordenação (Quick Sort)**: Apresenta o algoritmo Quick Sort para organizar o inventário com base em diferentes critérios (como a quantidade em estoque).
5.  **Simulação da Operação**: O bloco principal que executa as funções em uma sequência lógica para demonstrar todas as funcionalidades, desde o registro de consumo até a exibição de dados ordenados no dashboard.

---

## Análise Detalhada: Pilha e Quick Sort

Conforme solicitado, esta seção aprofunda o uso da **Pilha** e do **Quick Sort** no código.

### Uso da Pilha (Stack): Consultas em Ordem Inversa

A pilha é uma estrutura de dados que segue o princípio **LIFO (Last-In, First-Out)**, ou "o último a entrar é o primeiro a sair". No projeto, ela é ideal para simular a necessidade de um operador consultar ou verificar rapidamente as últimas operações realizadas.

#### Por que usar uma Pilha aqui?

[cite_start]Imagine que o almoxarife, Rogério, acabou de passar vários itens na esteira e quer verificar se o último item foi registrado corretamente[cite: 32, 82]. Em vez de procurar em um longo relatório cronológico, um sistema com uma pilha permite que ele acesse imediatamente a transação mais recente. É análogo a usar "Ctrl + Z" (Desfazer), que sempre desfaz a última ação.

#### Aplicação no Código

1.  **Inicialização:**
    ```python
    # Pilha para simular consultas em ordem inversa (Último que Entra, Primeiro que Sai - LIFO)
    pilha_ultimos_consumos = []
    ```
    Uma lista vazia em Python (`[]`) funciona perfeitamente como uma pilha.

2.  **Adicionando Itens (Push):**
    Dentro da função `registrar_consumo`, toda vez que um novo consumo é validado, ele é adicionado ao topo da pilha usando o método `.append()`.
    ```python
    # Adiciona ao topo da pilha
    pilha_ultimos_consumos.append(registro)
    ```

3.  **Removendo Itens (Pop):**
    A função `consultar_ultimo_consumo` foi criada especificamente para essa finalidade. Ela utiliza o método `.pop()`, que remove e retorna o último elemento da lista (o topo da pilha).
    ```python
    def consultar_ultimo_consumo():
        # ...
        ultimo = pilha_ultimos_consumos.pop()
        print(f"↩️ Consulta Inversa: Último consumo foi de {ultimo['item']} às {ultimo['timestamp']}.")
        return ultimo
    ```
    Na simulação, chamar esta função duas vezes seguidas mostra primeiro o último consumo registrado, e depois o penúltimo, demonstrando perfeitamente o comportamento LIFO.

### Uso do Quick Sort: Ordenação do Inventário

O Quick Sort é um algoritmo de ordenação eficiente que utiliza uma estratégia de "dividir para conquistar". [cite_start]Sua principal aplicação no projeto "ConfereAí" é organizar os dados do inventário para exibição no painel de controle do administrador, permitindo uma análise visual rápida e eficiente[cite: 25, 90].

#### Por que usar Quick Sort aqui?

[cite_start]O dashboard do administrador precisa apresentar informações claras[cite: 67]. [cite_start]Um gestor pode querer ver os itens ordenados por quantidade para identificar rapidamente quais estão com estoque baixo e precisam de reposição[cite: 28, 96]. Uma lista de itens desordenada não oferece essa inteligência de forma ágil. [cite_start]O Quick Sort organiza essa lista de forma muito rápida, mesmo com um grande volume de itens, o que é esperado em hospitais de médio e grande porte[cite: 14].

#### Aplicação no Código

1.  **Função Genérica:**
    A função foi projetada para ser reutilizável. Ela aceita não apenas a lista a ser ordenada, mas também uma `chave`, que define o critério de ordenação.
    ```python
    def quick_sort(lista, chave):
        """Ordena uma lista de dicionários com base em uma chave (ex: 'estoque_atual')."""
    ```

2.  **Lógica do Algoritmo:**
    A implementação segue os passos clássicos do Quick Sort:
    * **Caso Base:** Se a lista tem um ou nenhum elemento, ela já está ordenada.
    * **Pivô:** O primeiro elemento da lista é escolhido como pivô.
    * **Partição:** A lista é dividida em duas sub-listas: `menores` (elementos menores ou iguais ao pivô) e `maiores` (elementos maiores que o pivô). A comparação é feita usando o valor da `chave` especificada (ex: `i[chave] <= pivo[chave]`).
    * **Recursão:** A função `quick_sort` é chamada recursivamente para as duas sub-listas, e os resultados são concatenados: `menores_ordenados + [pivo] + maiores_ordenados`.

3.  **Chamada na Simulação:**
    No final do script, o Quick Sort é usado para simular a visualização do dashboard, ordenando os itens pela chave `'estoque_atual'`.
    ```python
    print("\n[Dashboard: Itens ordenados por quantidade em estoque (do menor para o maior)]")
    inventario_ordenado_por_estoque = quick_sort(inventario, 'estoque_atual')
    for item in inventario_ordenado_por_estoque:
        print(f" -> Item: {item['item']:<30} | Estoque Atual: {item['estoque_atual']}")
    ```
    [cite_start]O resultado é uma lista de insumos exibida do mais crítico (menor estoque) ao mais abundante, atacando diretamente a dor do gestor de precisar de um controle ágil e preciso do inventário[cite: 30].
