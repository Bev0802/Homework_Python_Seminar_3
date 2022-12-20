''''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

import random

n=int(input('Введите размер списка: '))

print(list_rd:= list(random.sample(range(1,50), n)))
list_odd=[]
list_dis={}
sum=0
for x in range(0, len(list_rd)):
    if x%2!= 0:
        list_dis[x] = list_rd[x]
        sum = sum + list_rd[x]
print(f"На нечётных позициях элементы: {list_dis} -> сумма: {sum}")


