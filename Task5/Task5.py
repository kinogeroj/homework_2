# Реализуйте алгоритм перемешивания списка.

import os
import random

os.system('cls')

print('Перемешаем список случайным образом.')

a = map(float, input('Введите список вещественных чисел через пробел: ').split())

a = list(a)

def mix_list(list_orig):
    
    list = list_orig[:]
    length = len(list)
    
    for i in range(length):
        index_new = random.randint(0, length - 1)
        temp = list[i]
        list[i] = list[index_new]
        list[index_new] = temp

    return list

b = mix_list(a)

print(f'Получившийся изначальный список: {a}.')

print(f'Перемешанный список будет такой: {b}.')