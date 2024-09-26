first = int(input('Введите целое число: '))
second = int(input('Введите целое число: '))
third = int(input('Введите целое число: '))
if first == second == third:
    print('Одинаковых чисел: ', 3)
elif first == second or first == third or second == third:
    print('Одинаковых чисел: ', 2)
else:
    print('Одинаковых чисел: ', 0)