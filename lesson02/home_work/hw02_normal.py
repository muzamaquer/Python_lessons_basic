from datetime import datetime
import random
import math

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

list1 = []
for x in range(15):
    list1.append(random.randint(-100, 100))
print(list1)
list2 = []
for y in list1:
    if y >= 0 and math.sqrt(y).is_integer():
        list2.append(y ** 0.5)
print(list2)


# list1 = [random.randint(-100, 100) for x in range(15)]
#
# print(list1)
#
# list2 = [int(y ** 0.5) for y in list1 if y >= 0 and math.sqrt(y).is_integer()]
#
# print(list2)

print('-'*25)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

curr_date = datetime.now()

mlist = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

mnth_idx = curr_date.month - 1

day = curr_date.day

month = mlist[mnth_idx]

year = curr_date.year

result = f"{day} {month} {year} года."

print(result)

print('-'*25)

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


qty = int(input('Введите количество элементов в списке = ',))

print([random.randint(-100, 100) for x in range(qty)])

print('-'*25)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


rptdlst = [1, 2, 4, 5, 6, 2, 5, 2]

nrptdlst = list(set(rptdlst))

print(nrptdlst)

rptdlst1 = [1, 2, 4, 5, 6, 2, 5, 2]

nrptdlst1 = [x for x in rptdlst1 if rptdlst1.count(x) == 1]

print(nrptdlst1)




