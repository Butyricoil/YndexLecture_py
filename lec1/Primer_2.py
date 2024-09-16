# А задача: Тоннель 3 целых числа. A B C
# Найди все корни уравнения. ax^2 + bx + c = 0
# И выведи их в порядке возрастания.
import math
a = input()
b = input()
c = input()
d =  b ** 2 - 4 * a * c
x1 = (-b - math.sqrt(d)) / (2 * a)
x2 = (-b + math.sqrt(d)) / (2 * a)

print (x1, x2)