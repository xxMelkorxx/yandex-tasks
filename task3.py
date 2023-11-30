"""
Задача 3. Игра с числами:
    Дана последовательность n положительных чисел a1, a2, ..., an. 
    Пока среди них есть различные, выполняется следующая операция: выбирается некоторое максимальное число 
    и из него вычитается минимальное число.
    Через сколько операций числа станут одинаковыми?

Формат ввода:
    В первой строке входных данных задано число n (1 ≤ n ≤ 1000). В следующей строке
    заданы n чисел ai (1 ≤ ai ≤ 1e9).

Формат вывода:
    Количество операций, после которых все числа станут одинаковыми.
"""

# Вычитание числа a из всех чисел массива до тех пор, пока числа массива не станут <= 2*a
def calc(a):
    count = 0
    for i in range(len(nums)):
        if nums[i] >= 2 * a:
            k = nums[i] // a - 1
            count += k
            nums[i] = int(nums[i] - a * k)
    return count


n, nums = int(input()), [int(i) for i in input().split()]
counter, curr_min = 0, min(nums)

while True:
    counter += calc(curr_min)  # вычитаем min число из всех чисел, которые >= 2*min 
    curr_max = max(nums)  # получение максимума 
    if curr_max != curr_min:  # находим число, которое < 2*min
        nums[nums.index(curr_max)] -= curr_min  # вычитаем из него текущий минимум
        counter += 1  # увеличиваем счётчик
        curr_min = curr_max - curr_min  # обновляем минимум
    else:
        break

print(int(counter))
