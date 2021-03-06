# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list1 = [1, 2, 4, 0]
list2 = [x ** 2 for x in list1]
print(list2)



# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fr1 = ['Apple', 'Lime', 'Mango', 'Pineapple', 'Fig', 'Strawberry']
fr2 = ['Jostaberry', 'Jujube', 'Mangosteen', 'Mango', 'Strawberry']
fr3 = [y for y in fr1 if y in fr2]
print(fr3)



# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
list3 = [random.randint(-100, 100) for x in range(40)]
print(list3)
list2 = [z for z in list3 if (z % 3 == 0) and z > 0 and (z % 4 !=0)]
print(list2)