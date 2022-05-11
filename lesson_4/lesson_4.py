# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего задания первых трех уроков.

# Создание матрицы

import random
import timeit
import cProfile
import sys


# --------------------------------------------------------------------------------------
# №1 создание матрицы двумя циклами
def m_create_2_for(range_raw, range_coll):
    matrix = [[random.randint(1, 100) for _ in range(1, range_coll)] for _ in range(1, range_raw)]


# timeit m_create_2_for(10, 10):
# 100 loops, best of 3: 157 usec per loop

# timeit m_create_2_for(100, 100):
# 100 loops, best of 3: 18.5 msec per loop

# timeit m_create_2_for(150, 150):
# 100 loops, best of 3: 41.2 msec per loop

# cProfile.run('m_create_2_for(10, 10)')
# 1 0.000 0.000 0.000 0.000 task_01.py: 8(speed_test)

# cProfile.run('m_create_2_for(100, 100)')
# 1    0.000    0.000    0.025    0.025 task_01.py:8(speed_test)

# cProfile.run('m_create_2_for(1000, 1000)')
#  1    0.000    0.000    2.634    2.634 task_01.py:8(speed_test)

# Итог: сложность данного алгоритма = О(N**2)

# --------------------------------------------------------------------------------------
# №2 Создание матрицы 1 циклом
def m_create_1_for(size_matrix):
    matrix = []
    temp_array = []

    for i in range(1, (size_matrix ** 2) + 1):
        val = random.randint(1, 100)

        if i % size_matrix == 0:
            temp_array.append(val)
            matrix.append(temp_array)
            temp_array = []
        else:
            temp_array.append(val)
    print(matrix)


# timeit m_create_1_for(10):
# 100 loops, best of 3: 438 usec per loop

# timeit m_create_1_for(100):
# 100 loops, best of 3: 25.9 msec per loop

# timeit m_create_1_for(150):
# 100 loops, best of 3: 55.6 msec per loop

# cProfile.run("m_create_1_for(10)")
# 1 0.000 0.000 0.000 0.000 task_01.py: 33(m_create_1_for)

# cProfile.run("m_create_1_for(100)")
# 1    0.006    0.006    0.039    0.039 task_01.py:33(m_create_1_for)

# cProfile.run("m_create_1_for(1000)")
# 1    0.663    0.663    3.401    3.401 task_01.py:33(m_create_1_for)

# Итог: сложность данного алгоритма = О(N**2), при этом данный алгоритм медленнее чем алгоритм №1

# ---------------------------------------------------------------------------------------------
# №3 Создание матрицы рекурсией
sys.setrecursionlimit(2000)

def m_create_recursion(range_raw, range_coll, coll_count=0, f_matrix = []):
    matrix = []
    if coll_count + 1 == range_coll:
        for _ in range(range_raw):
            matrix.append(random.randint(1, 100))
        f_matrix.append(matrix)
        return f_matrix
    else:
        for _ in range(range_raw):
            matrix.append(random.randint(1, 100))
        coll_count += 1
        f_matrix = m_create_recursion(range_raw, range_coll, coll_count)
        f_matrix.append(matrix)
        return f_matrix

# timeit m_create_recursion(10, 10):
# 100 loops, best of 3: 198 usec per loop

# timeit m_create_recursion(100, 100):
# 100 loops, best of 3: 20 msec per loop

# timeit m_create_recursion(150, 150):
#100 loops, best of 3: 45.4 msec per loop

# cProfile.run('m_create_recursion(10, 10)')
# 10/1    0.000    0.000    0.001    0.001 task_01.py:77(m_create_recursion)

# cProfile.run('m_create_recursion(100, 100)')
# 100/1    0.006    0.000    0.031    0.031 task_01.py:77(m_create_recursion)

# cProfile.run('m_create_recursion(1000, 1000)')
# 1000/1    0.583    0.001    3.165    3.165 task_01.py:79(m_create_recursion)

# Итог: сложность данного алгоритма так же О(N**2), при этом на небольшом размере матрицы (10, 10) он медленнее
# алгоритмов №1 и №2, но на размере 100 и >, он выигрывает по времени у алгоритма №2, но для таких значений требуется
# увеличения стека для рекурсии, так как при стандартном размере стек переполняется, не давая алгоритму
# завершить действие.

# По итогу проведения оценки скорости работы алгоритмов, с уверенностью можно сказать, что наиболее выгодным алгоритмом
# для создания матриц является алгоритм №1