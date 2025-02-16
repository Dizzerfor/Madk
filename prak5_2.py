def is_sum_of_k_powers(n, k):
    if n <= 0 or k <= 0:
        return False
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** k
        n = n // 10
    return total == original

# Ввод данных и вывод результата
n = int(input("Введите натуральное число n: "))
k = int(input("Введите степень k: "))
if is_sum_of_k_powers(n, k):
    print(f"{n} равно сумме {k}-х степеней своих цифр")
else:
    print(f"{n} НЕ равно сумме {k}-х степеней своих цифр")