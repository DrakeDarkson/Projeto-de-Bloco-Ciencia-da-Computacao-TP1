import time
import tracemalloc
from collections import deque

# 1 - Ler o arquivo de listagem
with open('listagem_completa.txt', 'r') as file:
    files = [line.strip() for line in file.readlines()]

# 2 - Hashtable (dicionário)
hashtable = {i: files[i] for i in range(len(files))}
# 2 - Pilha (usando lista)
stack = files[:]
# 2 - Fila (usando deque)
queue = deque(files)

# 3 - Função para recuperar arquivos em posições específicas
def get_files_at_positions(structure):
    positions = [1, 100, 1000, 5000, len(structure) - 1]
    return [structure[i] for i in positions if i < len(structure)]

# Testar operações em cada estrutura
structures = {"Hashtable": hashtable, "Stack": stack, "Queue": queue}

for name, structure in structures.items():
    # 4 - Iniciar monitoramento de memória
    tracemalloc.start()

    # 4 - Medir tempo de execução das operações
    start_time = time.time()

    # 5 - Adicionar e remover itens
    if name == "Hashtable":
        structure[len(structure)] = "new_file"
        structure.pop(len(structure) - 1)
    elif name == "Stack":
        structure.append("new_file")
        structure.pop()
    elif name == "Queue":
        structure.append("new_file")
        structure.popleft()
    end_time = time.time()

    # Recuperar arquivos nas posições específicas
    if name == "Hashtable":
        retrieved_files = get_files_at_positions(list(structure.values()))
    else:
        retrieved_files = get_files_at_positions(structure)

    # 6 - Capturar uso de memória
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # 6 - Exibir resultados
    print(f"{name} operations executed in: {end_time - start_time:.5f} seconds")
    print(f"Memory usage: Current = {current / 1024:.2f} KB, Peak = {peak / 1024:.2f} KB")
    print(f"Files at specific positions: {retrieved_files}")
