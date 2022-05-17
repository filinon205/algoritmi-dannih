'''1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python и разрядность
вашей ОС.'''

#  Current Version of Python interpreter we are using- 3.9.7
# OC 64bit

from count_size import count_size

x1 = float(input('Введите координату X первой точки '))
y1 = float(input('Введите координату Y первой точки '))
x2 = float(input('Введите координату X второй точки '))
y2 = float(input('Введите координату Y второй точки '))
if x2 == x1:
    print('Error')
    exit()
k = (y2 - y1) / (x2 - x1)
b = (y1 - k * x1)
if b == 0:
    print(f'Уравнение прямой y = {k:.2f}x')
elif b > 0:
    print(f'Уравнение прямой y = {k:.2f}x + {b:.2f}')
else:
    print(f'Уравнение прямой y = {k:.2f}x - {abs(b):.2f}')

sum_ = 0
var_lst = (x1, y1, x2, y2, k, b)
for i in var_lst:
    sum_ += count_size(i)
print(f'Под переменные задействованно {sum_} байт памяти')
# Под переменные задействованно 144 байт памяти
# 6 * 24 =144 все верно

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во
# второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 – если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

# Python 3.6.6
# OS - 64bit

import random
from count_size import count_size


LST_LEN = 10
num_lst = [random.randint(0, 11) for _ in range(LST_LEN)]
even_num = []
for i in range(LST_LEN):
    if num_lst[i] % 2 == 0:
        even_num.append(i + 1)
print(f'Базовый массив\n{num_lst}')
print(f'Массив идексов четных чисел\n{even_num}')

sum_ = 0
var_lst = (LST_LEN, num_lst, even_num, i)
for i in var_lst:
    sum_ += count_size(i)
print(f'Под переменные задействованно {sum_} байт памяти')

# Под переменные задействованно 792 байт памяти
# Два списка, две переменные типа инт

# 3 варианта одной задачи

from count_size import count_size


n = int(input('Введите n: '))


def var_sum(var_lst):
    summa = 0
    for i in var_lst:
        summa += count_size(i)
    print(f'Под переменные задействованно {summa} байт памяти')


sum_ = 0
for i in range(n):
    sum_ += (-1) ** i / 2 ** i

var_sum([sum_, i])
# Под переменные задействованно 52 байт памяти
# 24 + 28(?) = 52 все верно
# Итерируемая переменная в цикле занимает больше памяти (может больше ссылок?)


item = 1
summ = 0
for _ in range(n):
    summ += item
    item /= -2

var_sum([item, summ, _])

# Под переменные задействованно 76 байт памяти
# 24 + 24 + 28 = 76 все верно

summa_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))

var_sum([summa_2])
# Под переменные задействованно 24 байт памяти
# Очевидно, что по памяти эффективнее программа с одной переменной