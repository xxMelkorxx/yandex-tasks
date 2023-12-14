"""
Задача 2. Хорошая последовательность:
    Последовательность точек на плоскости называется тривиальной, если она является строго 
    упорядоченной по возрастанию или по убыванию расстояния до одной из точек этой последовательности.
    Последовательность точек в трёхмерном пространстве называется хорошей, если ни одна из последовательностей, 
    полученных взятием проекции исходной на одну из базовых плоскостей (Oxy, Oyz и Oxz), не является тривиальной.
    Дана последовательность из n точек с целочисленными координатами в трёхмерном пространстве. Необходимо найти 
    такую чётную перестановку её индексов, что после её применения последовательность становится хорошей.
    Гарантируется, что решение существует.

Формат ввода:
    В первой строке входных данных записано целое число n (3 ≤ n ≤ 1000), в следующих n
    строчках через пробел записаны по три целочисленных координаты xi, yi, zi (-1e4 ≤ xi, yi, zi ≤ 1e4) каждой из точек.
    Гарантируется, что проекции всех точек на любую из базовых плоскостей различны.

Формат вывода:
    Выведите n чисел: искомая перестановка индексов от 1 до n. 
    Если существует несколько решений, выведите любое из них. Числа в строке следует разделять пробелами.

Примечания:
Инверсией в перестановке p порядка n называется всякая пара индексов (i, j) такая, что 1 ≤ i < j ≤ n и 
pi > pj. Чётность числа инверсий в перестановке определяет чётность перестановки.
"""

from enum import Enum

class Plane(Enum):
    Oxy = 'Oxy'
    Oyz = 'Oyz'
    Oxz = 'Ozx'

class Points:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x} {self.y} {self.z}"

# Рассчёт дистанции между точками на одно из плоскостей.
def distance(p1: Points, p2: Points, plane: Plane) -> float:
    if plane == Plane.Oxy:
        return ((p2.y - p1.y) ** 2 + (p2.x - p1.x) ** 2) ** 0.5
    if plane == Plane.Oyz:
        return ((p2.y - p1.y) ** 2 + (p2.z - p1.z) ** 2) ** 0.5
    if plane == Plane.Oxz:
        return ((p2.x - p1.x) ** 2 + (p2.z - p1.z) ** 2) ** 0.5

# Проверка, является ли последовательность точек на плоскости тривиальной.
def is_trivial(points: list, plane: Plane) -> bool:
    curr_d, istriv = 0, True
    for i in range(1, len(points)):
        d = distance(points[0], points[i], plane)
        # print(f"p0: {points[0]}, p{i}: {points[i]}, d = {d}, plane - {plane.value}")
        if d > curr_d:
            curr_d = d
        else:
            istriv = False
    return istriv

# Проверка, является ли последовательность точек хорошей.
def is_good(points: list) -> bool:
    is_triv_xy = is_trivial(points, Plane.Oxy)
    # print(f"Последовательность тривиальная? - {is_triv_xy}")
    is_triv_yz = is_trivial(points, Plane.Oyz)
    # print(f"Последовательность тривиальная? - {is_triv_yz}")
    is_triv_xz = is_trivial(points, Plane.Oxz)
    # print(f"Последовательность тривиальная? - {is_triv_xz}")
    return not (is_triv_xy and is_triv_yz and is_triv_xz)

def permute(nums):
    result = []
    generate_permutations(nums, 0, result)
    return result

def generate_permutations(nums, index, result):
    if index == len(nums):
        result += [nums[:]]
        return

    for i in range(index, len(nums)):
        nums[index], nums[i] = nums[i], nums[index]
        generate_permutations(nums, index + 1, result)
        nums[index], nums[i] = nums[i], nums[index]

if __name__ == '__main__':
    n, list_p = int(input()), []
    # Получение точек.
    for _ in range(n):
        p = input().split()
        list_p += [Points(int(p[0]), int(p[1]), int(p[2]))]
    # print(f"Является ли последовательность хорошей? - {is_good(list_p)}")

    # Получение всех возможных перестановок индексов.
    permutations = []
    generate_permutations(list(range(n)), 0, permutations)
    for p in permutations:
        for j in p:
            print(j, end=' ')
        print(f"- {is_good([list_p[i - 1] for i in p])}")

    print()
    for i, perm in enumerate(permutations):
        if i % 2 == 0 and is_good([list_p[i] for i in perm]):
            for j in perm:
                print(j + 1, end=' ')
            print()
            # break
