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

# 1. Обработка чисел a, b, c
def process_numbers(a, b, c):
    if a > b > c:
        return 2 * a, 2 * b, 2 * c
    else:
        return abs(a), abs(b), abs(c)

a = safe_input("Введите a: ", float)
b = safe_input("Введите b: ", float)
c = safe_input("Введите c: ", float)

a, b, c = process_numbers(a, b, c)
print(f"Обработанные числа: a = {a}, b = {b}, c = {c}")

# 2. Проверка, лежат ли точки на одной прямой
def are_collinear(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)

def angle_between_vectors(x1, y1, x2, y2, x3, y3):
    # Векторы AB и BC
    ab_x, ab_y = x2 - x1, y2 - y1
    bc_x, bc_y = x3 - x2, y3 - y2

    # Длина векторов
    len_ab = math.sqrt(ab_x**2 + ab_y**2)
    len_bc = math.sqrt(bc_x**2 + bc_y**2)

    # Скалярное произведение
    dot_product = ab_x * bc_x + ab_y * bc_y

    # Косинус угла
    cos_theta = dot_product / (len_ab * len_bc)

    # Угол в градусах
    theta = math.acos(cos_theta) * (180 / math.pi)
    return theta

x1 = safe_input("Введите x1: ", float)
y1 = safe_input("Введите y1: ", float)
x2 = safe_input("Введите x2: ", float)
y2 = safe_input("Введите y2: ", float)
x3 = safe_input("Введите x3: ", float)
y3 = safe_input("Введите y3: ", float)

if are_collinear(x1, y1, x2, y2, x3, y3):
    print("Точки лежат на одной прямой.")
else:
    angle = angle_between_vectors(x1, y1, x2, y2, x3, y3)
    print(f"Точки не лежат на одной прямой. Угол ABC = {round(angle, 2)}°")

# 3. Вычисление функции F(x)
def compute_function(x):
    if x <= 3:
        return -x**2 + 3*x + 9
    else:
        return x / (x**2 + 1)

x = safe_input("Введите x: ", float)
print(f"F({x}) = {round(compute_function(x), 5)}")