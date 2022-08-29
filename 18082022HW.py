import math
import random
# 1 Подсчитать сумму цифр в вещественном числе.
""" n = (str(float(input('Введите вещественное число: ')))).replace('.','')
a = int(n)
summa = 0

while a > 0:
    digit_a = a % 10
    summa = summa + digit_a
    a = a // 10
print(summa) """

# 2 Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N. [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

""" n = int(input('Введите число: '))
a = []
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    a.append(factorial)

print(a) """

# 3 Реализуйте алгоритм перемешивания списка.
""" list = ['Проснуться', 'Принять душ', 'Почистить зубы', 'Позавтракать']
random.shuffle(list)

print(list) """