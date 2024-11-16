import time

# 1 - Ler o arquivo de listagem
with open('listagem_completa.txt', 'r') as file:
    files = [line.strip() for line in file.readlines()]

# 2 - Algoritmos de ordenação
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 3 - Testar cada algoritmo e medir o tempo
for sort_func in [bubble_sort, selection_sort, insertion_sort]:
    arr_copy = files[:]
    start_time = time.time()
    sort_func(arr_copy)
    end_time = time.time()
    print(f"{sort_func.__name__} executed in: {end_time - start_time:.5f} seconds")
