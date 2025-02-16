import math

# Функция безопасного ввода
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

# 1. Вычисление значений по формулам
def calculate_formulas(x, y):
    if x == 0:
        f1 = "Ошибка: x не должен быть 0 (деление на ноль)"
    else:
        f1 = x - (x**3 / 3) + (x**5 / 5)

    denominator = 1 + x**2 * abs(y - math.tan(x))
    if denominator == 0:
        f2 = "Ошибка: знаменатель не должен быть 0"
    else:
        f2 = (3 + math.exp(x) - 1) / denominator

    return f1, f2

x = safe_input("Введите x: ", float)
y = safe_input("Введите y: ", float)

f1, f2 = calculate_formulas(x, y)
print(f"Результаты: F1 = {f1}, F2 = {f2}")

# 2. Расчёт сопротивления
def parallel_resistance(r1, r2, r3=None, r_total=None):
    if r3 is None:  # Найти полное сопротивление
        return 1 / (1 / r1 + 1 / r2 + 1 / r_total)
    elif r_total is None:  # Найти один из резисторов
        return 1 / (1 / r1 + 1 / r2)
    else:
        return "Ошибка"

choice = safe_input("Выберите задачу (1 - найти Rобщ, 2 - найти R3): ", int, lambda x: x in [1, 2])

if choice == 1:
    r1 = safe_input("Введите R1: ", float, lambda x: x > 0)
    r2 = safe_input("Введите R2: ", float, lambda x: x > 0)
    r3 = safe_input("Введите R3: ", float, lambda x: x > 0)
    print(f"Общее сопротивление: {parallel_resistance(r1, r2, r3)} Ом")
elif choice == 2:
    r1 = safe_input("Введите R1: ", float, lambda x: x > 0)
    r2 = safe_input("Введите R2: ", float, lambda x: x > 0)
    r_total = safe_input("Введите Rобщ: ", float, lambda x: x > 0)
    print(f"R3 = {parallel_resistance(r1, r2, r_total=r_total)} Ом")

# 3. Проверка на истину (один из символов не цифра)
def check_truth(val1, val2):
    return (val1.isdigit() and not val2.isdigit()) or (val2.isdigit() and not val1.isdigit())

val1 = input("Введите первый символ: ")
val2 = input("Введите второй символ: ")

print("Результат:", check_truth(val1, val2))

# 4. Проверка попадания точки в заштрихованную область
def is_inside_shaded_area(x, y):
    return (x**2 + y**2 <= 9 and y >= 0) or (-3 <= x <= 3 and -3 <= y <= 0)

x = safe_input("Введите x: ", float)
y = safe_input("Введите y: ", float)

print("Точка принадлежит заштрихованной области:", is_inside_shaded_area(x, y))