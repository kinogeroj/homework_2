# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
#  -2 -1 0 1 2 Позиции: 0,1 -> 2

import os

os.system('cls')

print('Найдем произведение чисел ряда по заранее заданным позициям. Позиции заданы в файле positions.txt.')

n = int(input('Введите число N (определяет промежуток [-N, N]): '))

elements = []
result = 1

for i in range(-n, n + 1):
    elements.append(i)
i = 0

print(f'Получился такой ряд чисел: {elements}.')
print()

InputPositions = input('Введите позиции чисел ряда, которые хотите перемножить (они будут внесены в файл positions.txt): ').split()

with open('positions.txt', 'w') as file:
    file.write('\n'.join(InputPositions))

with open('positions.txt', 'r') as file:
    ReadPositions = list(map(int, file.read().splitlines()))

while i < len(ReadPositions):
    index = ReadPositions[i]
    result = result * elements[index]
    i += 1

print()
print(f'Произведение элементов ряда {elements} на позициях {ReadPositions} равно: {result}.')