# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
#
# def cred_output(name, age, city):
#     agm = 'год'
#     if 20 >= int(age) > 4:
#         agm = 'лет'
#     elif int(age[-1]) == 0 or int(age[-1]) > 4:
#         agm = 'лет'
#     elif int(age[-1]) > 1:
#         agm = 'года'
#
#     print(f'{name}, {age} {agm}, проживает в городе {city}.')
#
# name = input('Введите имя ',)
# age = input('Введите возраст ',)
# city = input('Введите город проживания ',)
#
# cred_output(name, age, city)

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

# def mymax(numbers):
#     numbersint = list(map(int, numbers.split(",")))
#     mmax = 0
#     for i in numbersint:
#         if i > mmax:
#             mmax = i
#     return mmax
#
#
# numb = input('Введите 3 числа через запятую: ')
# print(f'Наибольшим числом из {numb} является {mymax(numb)}')


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов
#
def longest_str(*args):
    ret = ''
    for i in args:
        if len(i) > len(ret):
            ret = i
    return ret

print(longest_str('True', 'FX', 'Entertainment', 'OneLongWordForTest'))
