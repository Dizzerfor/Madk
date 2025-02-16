def arabic_to_roman(n):
    # Проверка корректности ввода
    if not isinstance(n, int) or n < 1 or n >= 4000:
        raise ValueError("Число должно быть целым в диапазоне 1-3999")
    
    # Список соответствий арабских и римских чисел
    val = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
        (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
        (1, 'I')
    ]
    
    roman_num = ''
    for (num, symbol) in val:
        # Пока число больше текущего значения, добавляем символ
        while n >= num:
            roman_num += symbol
            n -= num
    return roman_num

# Ввод данных и вывод результата
try:
    n = int(input("Введите арабское число (1-3999): "))
    print(f"Римское представление: {arabic_to_roman(n)}")
except ValueError as e:
    print(f"Ошибка: {e}")