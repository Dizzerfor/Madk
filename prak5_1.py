def count_divisors(num):
    if num < 1:
        return 0
    count = 0
    sqrt_num = int(num ** 0.5)
    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            j = num // i
            if i == j:
                count += 1
            else:
                count += 2
    return count

def find_max_divisors(n, m):
    if n > m:
        return None  # Некорректный интервал
    max_count = -1
    result = n
    for num in range(n, m + 1):
        cnt = count_divisors(num)
        if cnt > max_count:
            max_count = cnt
            result = num
    return result

# Ввод данных и вывод результата
n = int(input("Введите начало интервала (n): "))
m = int(input("Введите конец интервала (m): "))
result = find_max_divisors(n, m)
if result is not None:
    print(f"Число с наибольшим количеством делителей в интервале [{n}, {m}]: {result}")
else:
    print("Заданный интервал некорректен (n > m)")