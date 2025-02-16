# 1. Вывести числа, для которых ai ≥ i
def print_valid_numbers(arr):
    result = [arr[i] for i in range(len(arr)) if arr[i] >= (i + 1)]
    print("Числа, для которых ai ≥ i:", result)

# Ввод последовательности
arr = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
print_valid_numbers(arr)

# 2. Разворот массива без использования другого массива
def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

# Ввод массива
arr = list(map(int, input("Введите массив X[N] через пробел: ").split()))
reverse_array(arr)
print("Массив в обратном порядке:", arr)

# 3. Подсчет количества различных чисел
def count_unique_numbers(arr):
    unique_numbers = set(arr)
    return len(unique_numbers)

# Ввод последовательности
arr = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
print("Количество различных чисел:", count_unique_numbers(arr))