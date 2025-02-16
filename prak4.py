import math

# Функция для проверки корректности числового ввода
def safe_input(prompt, type_func, condition=lambda x: True):
    while True:
        try:
            value = type_func(input(prompt).strip())
            if condition(value):
                return value
            else:
                print("Ошибка: значение не соответствует требованиям.")
        except ValueError:
            print("Ошибка: введите корректное число.")

# 1. Найти сумму всех n-значных чисел (1 <= n <= 4)
def sum_n_digit_numbers(n):
    if 1 <= n <= 4:
        min_num = 10**(n-1)
        max_num = 10**n - 1
        return sum(range(min_num, max_num + 1))
    else:
        return "Ошибка: n должно быть в диапазоне 1 <= n <= 4."

n = safe_input("Введите n (1 <= n <= 4): ", int, lambda x: 1 <= x <= 4)
print("Сумма всех", n, "-значных чисел:", sum_n_digit_numbers(n))

# 2. Вычислить сумму ряда
def series_sum(a, n):
    return sum(1 / (a ** (2 * i - 2)) for i in range(1, n + 1))

a = safe_input("Введите действительное число a: ", float, lambda x: x != 0)
n = safe_input("Введите натуральное число n: ", int, lambda x: x > 0)
print("Сумма ряда:", series_sum(a, n))

# 3. Вычислить значения функции F(x) = (1/2) * sin(x/4) + 1 на отрезке [a, b] с шагом h
def function_values(a, b, h):
    x = a
    results = []
    while x <= b:
        f_x = (1/2) * math.sin(x/4) + 1
        results.append((round(x, 5), round(f_x, 5)))
        x += h
    return results

a = safe_input("Введите a: ", float)
b = safe_input("Введите b (b > a): ", float, lambda x: x > a)
h = safe_input("Введите шаг h (h > 0): ", float, lambda x: x > 0)

values = function_values(a, b, h)
print("Значения функции:")
for x, fx in values:
    print(f"F({x}) = {fx}")

# 4. Найти наименьший номер последовательности, где M выполняется
def find_sequence(m, k, eps):
    a = [m]
    i = 1
    while True:
        next_a = 0.5 * (a[-1] + 2 / a[-1])
        a.append(next_a)
        if abs(a[-1] - k) < eps:
            return i, a
        i += 1

m = safe_input("Введите M: ", float)
k = safe_input("Введите k: ", float)
eps = safe_input("Введите eps (eps > 0): ", float, lambda x: x > 0)

index, sequence = find_sequence(m, k, eps)
print("Минимальный номер:", index)
print("Последовательность:", [round(ai, 5) for ai in sequence])