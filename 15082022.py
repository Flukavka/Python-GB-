from ast import match_case
import math
from unicodedata import digit
# 1 По двум заданным числам проверить является ли одно квадратом второго
""" num1 = 16
num2 = 4

if (math.sqrt(num1) == num2):
    print(str(num2) + ' является квадратом ' + str(num1)) """

# 2 Найти максимальное из пяти чисел
'''a = [1, 2, 3, 4, 5]
max_number = max(a)
print("Наибольшее число:", max_number)'''

# 3 Вывести на экран числа от -N до N


# 4	Показать первую цифру дробной части числа
"""user_input = input("Введите дробное число: ")
parts = user_input.split('.')
if (len(parts) > 0):
    print(parts[1][0])"""

# 5 Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
'''n = int(input("Введите число n:"))
def check(n: int):
    return ((n % 5 == 0) and (n % 10 == 0)) or (n % 15 == 0 and n % 30 != 0)
print(check(n))'''

# 6 Дано число обозначающее день недели. Вывести его название и указать является
# ли он выходным.
""" day = int(input('Введите число обозначающее день недели: '))
match day:
    case 1:
        print('Понедельник')
    case 2:
        print('Вторник')
    case 3:
        print('Среда')
    case 4:
        print('Четверг')
    case 5:
        print('Пятница')
    case 6:
        print('Суббота, выходной')
    case 7:
        print('Воскресенье, выходной') """


# 7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех
# значений предикат


# 8 Сообщить в какой четверти координатной плоскости или на какой оси
# находится точка с координатами Х и У
"""x = int(input("x="))
y = int(input("y="))

if x > 0 and y > 0:
    print("I")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
elif x > 0 and y < 0:
    print("IV")"""


# 9	Указав номер четверти прямоугольной системы координат, показать
# допустимые значения координат для точек этой четверти

"""
number_quarter = int(
    input("Введите номер четверти прямоугольной системы координат:"))
if number_quarter == 1:
    print("OX(0; +Infinity) OY(0; +Infinity)")
elif number_quarter == 2:
    print("OX(0; -Infinity) OY(0; +Infinity)")
elif number_quarter == 3:
    print("OX(0; -Infinity) OY(0; -Infinity)")
elif number_quarter == 4:
    print("OX(0; +Infinity) OY(0; -Infinity)")"""


# 10 Найти расстояние между двумя точками пространства
"""
a_x = int(input("Введите значение по оси ОX для точки А:"))
a_y = int(input("Введите значение по оси ОY для точки А:"))
a_z = int(input("Введите значение по оси ОZ для точки А:"))
b_x = int(input("Введите значение по оси ОХ для точки B:"))
b_y = int(input("Введите значение по оси ОY для точки B:"))
b_z = int(input("Введите значение по оси ОZ для точки B:"))

a_b = round(math.sqrt(((b_x - a_x) ** 2) +
            ((b_y - b_x) ** 2) + ((b_z - a_z) ** 2)), 1)
print(a_b)"""

""" x1, y1, z1 = list(map(int, input('Enter the coordinates of the first point separated by a space: ')))
x2, y2, z2 = list(map(int, input('Enter the coordinates of the first point separated by a space: ')))

distance = round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2)), 1)
print(distance) """

