# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде
# функции. По возможности доработайте алгоритм (сделайте его умнее).
import random

lst = [random.randint(-100, 100) for i in range(10)]
print(f'Исходный целочисленный список :\n{lst}')


def bubble_sort(lst):
    n = 1

    while n < len(lst):
        sorted = True  # Для оптимизации алгоритма.(Цикл завершается, если замен больше не происходит)

        for i in range(len(lst) - n):

            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorted = False

        if sorted == True:
            break

        n += 1

    print(f'"Отпузыренный" список по убыванию:\n {lst}')


bubble_sort(lst)

print('===================================================')


# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
# [0; 50). Выведите на экран исходный и отсортированный массивы.


def merge_sort(array):
    if len(array) <= 1:
        return array

    # необязательное дополненение
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    i, j = 0, 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        array[i + j] = left[i]
        i += 1
    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


data = [round(random.uniform(1, 50, ), 2) for i in range(8)]
print(data)
merge_sort(data)
print(data)

print('===================================================')
# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

# Алгоритм нахождения медианы в неотсортированном списке

m = 4
size = 2 * m + 1
lst3 = [random.randint(1, 50) for i in range(size)]

print(f'Исходный НЕотсортированный список:\n {lst3}\n')


def median(lst):
    # нахождение медианы для четного кол-ва элементов
    if len(lst) % 2 == 0:
        center = []

        for i in lst:
            b = 0

            for j in lst:

                if i < j:
                    b += 1

            if len(lst) == b * 2 + 2 or len(lst) == b * 2:
                center.append(i)
        return sum(center) / 2

    # нахождение медианы для НЕ четного кол-ва элементов
    else:
        for i in lst:
            num = i
            b = 0

            for j in lst:

                if i < j:
                    b += 1

            if len(lst) == 2 * b + 1:
                return num


print(f'Медиана НЕотсортированного списка: {median(lst3)}\n')

print(f'Отсортированный список: \n{sorted(lst3)}')