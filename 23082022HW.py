#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
#элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

""" list = [2, 3, 5, 9, 3]
l = len(list)

nechet = []
for i in range(l):
    if i % 2 != 0:
        nechet.append(list[i])

print(sum(nechet)) """


#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

""" НЕ ПОЛУЧИЛОСЬ ВЫПОЛНИТЬ ЗАДАНИЕ """


#Задайте список из вещественных чисел. Напишите программу, которая найдёт
#разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

""" from math import *
list_num = [1.1, 1.2, 3.1, 5, 10.01]
num_variable = []

for num in list_num:
    x = num
    y = x - floor(x)
    num_variable.append(y)

num_variable.sort()
difference = num_variable[-1] - num_variable[0]
print(int(difference *100) / 100) """


#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

""" n = int(input('Введите число: '))

b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2

print(b) """


#Задайте число. Составьте список чисел Фибоначчи, в том числе для
#отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так:
#[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


""" k = int(input('Введите число: '))

j = -k
nega = [1, -1]
f1 = 1
f2 = -1
while j < -2:
    f1, f2 = f2, f1 - f2
    j += 1
    nega.append(f2)
nega_reverse = nega[::-1]
str_nega_reverse = ' '.join(map(str, nega_reverse))
print(str_nega_reverse, end=' ')

f0 = 0
f1 = 1
f2 = 1
print(f0, f1, f2, end=' ')

while k > 2:
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
    k -= 1 """