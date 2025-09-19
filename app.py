import datetime
from collections import deque

# --- 1. CONFIGURAÇÃO INICIAL E DADOS DO INVENTÁRIO ---
# Baseado na imagem do protótipo do projeto "ConfereAí" 
inventario = [
    {'codigo': 'SER-10ML', 'item': 'Seringa Descartável 10ml', 'categoria': 'Insumos', 'estoque_atual': 850},
    {'codigo': 'LUV-CIR-M', 'item': 'Luva Cirúrgica (Par)', 'categoria': 'EPI', 'estoque_atual': 150},
    {'codigo': 'GAZ-EST-100', 'item': 'Gaze Estéril (Pacote c/ 100)', 'categoria': 'Curativos', 'estoque_atual': 75},
    {'codigo': 'ALC-70-1L', 'item': 'Álcool Etílico 70% (1L)', 'categoria': 'Antissépticos', 'estoque_atual': 48},
    {'codigo': 'SUT-NY-30', 'item': 'Fio de Sutura Nylon 3-0', 'categoria': 'Cirúrgico', 'estoque_atual': 35},
    {'codigo': 'MAS-N95', 'item': 'Máscara N95', 'categoria': 'EPI', 'estoque_atual': 1200},
    {'codigo': 'ATA-CRP-10', 'item': 'Atadura de Crepe 10cm', 'categoria': 'Curativos', 'estoque_atual': 210}
]

# --- 2. FILA E PILHA PARA CONTROLE DE CONSUMO ---

# Fila para registrar o consumo em ordem cronológica (Primeiro que Entra, Primeiro que Sai - FIFO)
fila_consumo_diario = deque()

# Pilha para simular consultas em ordem inversa (Último que Entra, Primeiro que Sai - LIFO)
pilha_ultimos_consumos = []

def registrar_consumo(codigo_produto, quantidade):
    """
    Simula a passagem de um item pela esteira RFID no modo "Saída".
    Registra a movimentação na fila e na pilha.
    """
    # Encontra o item no inventário para registrar o nome
    item_encontrado = None
    for item in inventario:
        if item['codigo'] == codigo_produto:
            item_encontrado = item
            # Atualiza o estoque (simulação)
            item['estoque_atual'] -= quantidade
            break
    
    if item_encontrado:
        registro = {
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'codigo': codigo_produto,
            'item': item_encontrado['item'],
            'quantidade': quantidade
        }
        
        # Adiciona ao final da fila
        fila_consumo_diario.append(registro)
        # Adiciona ao topo da pilha
        pilha_ultimos_consumos.append(registro)
        print(f"✅ Consumo registrado: {quantidade} unidade(s) de {item_encontrado['item']}.")
    else:
        print(f"❌ Erro: Produto com código '{codigo_produto}' não encontrado.")

def consultar_ultimo_consumo():
    """Remove e retorna o último consumo registrado na pilha."""
    if not pilha_ultimos_consumos:
        print("ℹ️ Nenhuma consulta recente para exibir.")
        return None
    
    ultimo = pilha_ultimos_consumos.pop()
    print(f"↩️ Consulta Inversa: Último consumo foi de {ultimo['item']} às {ultimo['timestamp']}.")
    return ultimo

# --- 3. ESTRUTURAS DE BUSCA ---

def busca_sequencial(lista, codigo):
    """Busca um item pelo código em uma lista não ordenada."""
    for item in lista:
        if item['codigo'] == codigo:
            return item
    return None

def busca_binaria(lista_ordenada, codigo):
    """Busca um item pelo código em uma lista JÁ ORDENADA."""
    inicio, fim = 0, len(lista_ordenada) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista_ordenada[meio]['codigo'] == codigo:
            return lista_ordenada[meio]
        elif lista_ordenada[meio]['codigo'] < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return None

# --- 4. ORDENAÇÃO (QUICK SORT) ---

def quick_sort(lista, chave):
    """Ordena uma lista de dicionários com base em uma chave (ex: 'estoque_atual')."""
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i[chave] <= pivo[chave]]
        maiores = [i for i in lista[1:] if i[chave] > pivo[chave]]
        return quick_sort(menores, chave) + [pivo] + quick_sort(maiores, chave)

# --- SIMULAÇÃO DA OPERAÇÃO ---

print("--- INÍCIO DA SIMULAÇÃO: ConfereAí ---")

# a) Registrando o consumo diário (populando a Fila e a Pilha)
print("\n[Simulando Consumo Diário com RFID...]")
registrar_consumo('GAZ-EST-100', 10)
registrar_consumo('SER-10ML', 50)
registrar_consumo('ALC-70-1L', 2)

# b) Visualizando os registros
print("\n--- Fila e Pilha ---")
print("\n[Fila de Consumo (Ordem Cronológica - FIFO)]")
for registro in fila_consumo_diario:
    print(f" -> {registro['timestamp']}: Saída de {registro['quantidade']} de {registro['item']}")

print("\n[Consulta de Últimos Consumos (Ordem Inversa - LIFO)]")
consultar_ultimo_consumo()
consultar_ultimo_consumo()

# c) Buscando itens no inventário
print("\n--- Estruturas de Busca ---")
print("\n[Busca Sequencial por 'SUT-NY-30']")
resultado_seq = busca_sequencial(inventario, 'SUT-NY-30')
print(f"Resultado: {resultado_seq}")

print("\n[Busca Binária por 'LUV-CIR-M']")
# Para a busca binária, o inventário precisa estar ordenado pelo campo de busca (código)
inventario_ordenado_por_codigo = sorted(inventario, key=lambda x: x['codigo'])
resultado_bin = busca_binaria(inventario_ordenado_por_codigo, 'LUV-CIR-M')
print(f"Resultado: {resultado_bin}")

# d) Ordenando o inventário para visualização no Dashboard
print("\n--- Ordenação (Quick Sort) ---")
print("\n[Dashboard: Itens ordenados por quantidade em estoque (do menor para o maior)]")
inventario_ordenado_por_estoque = quick_sort(inventario, 'estoque_atual')
for item in inventario_ordenado_por_estoque:
    print(f" -> Item: {item['item']:<30} | Estoque Atual: {item['estoque_atual']}")
    
print("\n--- FIM DA SIMULAÇÃO ---")