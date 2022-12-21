'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

import random
import math

#Функция создает список случаныйх не целых числе с точностью до сотых. Размер и диапазн задет пользователь.
def CreatListRandomNumbersFloat(size, min, max, accuracy):
    i=0
    list_rd=[]
    while i<size:
        list_rd.append(round(random.uniform(min, max), accuracy))
        i=i+1
    return list_rd

#Функция из списка с целой и доробной частью создает список без целой части, только дробное.
def CreatesListOnlyFractional(list,accuracy):
    list_mod=[]
    for i in list:
        x = math.modf(i)
        list_mod.append(round((x[0]), accuracy))
    return list_mod


listRandomNumbersFloat = CreatListRandomNumbersFloat(5, 1.01, 15.99,2)
#print(listRandomNumbersFloat)

ListOnlyFractional = CreatesListOnlyFractional(listRandomNumbersFloat,2)
#print(ListOnlyFractional)

rezalt = (max:=max((ListOnlyFractional))-(min:=min(ListOnlyFractional)))

print(f'{listRandomNumbersFloat} => {rezalt}')