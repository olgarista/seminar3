# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
my_lst = []

for i in range(randint(4, 10)):
    my_lst.append(randint(1, 10))
print(my_lst)

sum = 0
for i in range(len(my_lst)):
    if i % 2 == 1:
        sum += my_lst[i]
print(f'Сумма элементов на нечётных позициях = {sum}')

# 2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# *Пример:*
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
my_list = []
for i in range(randint(4, 10)):
    my_list.append(randint(1, 10))
print(my_list)

list_mult = []
ln = len(my_list)
for i in range(ln):
    if i >= ln/2:
        break
    print(my_list[i] * my_list[-1-i], end=' ')
print()

# 3 Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# *Пример:*
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

n = int(input('Введите размер списка '))
list1 = []
for i in range(n):
    f = uniform(0, 9)
    list1.append(round(f, 2))

min = list1[0]
max = 0
for i in range(len(list1)):
    if max < list1[i]:
        max = list1[i]
    if min > list1[i]:
        min = list1[i]
dif = (max - int(max)) - (min - int(min))

print(list1)
print(max, min)
print(round(dif, 2))

# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))
print(f'Число {n} в двоичной системе: ' '{0:b}'.format(n))

# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))
def fibo(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n + 1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums
print(fibo(n))






