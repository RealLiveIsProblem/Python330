from random import randint
import math
import time
import locale
import builtins


# locale.setlocale(locale.LC_ALL, 'ru')


# a = 7
# b = 9
# print('a =', a, ' b =', b)
#
# a = a + b
# b = a - b
# a = a - b
# print('a =', a, ' b =', b)
#
# a = a * b
# b = a / b
# a = a / b
# print('a =', a, ' b =', b)
#
# a, b = b, a
# print('a =', a, ' b =', b)
# psw = 'admin'
# match psw:
#     case 'admin':
#         print(psw)
#     case 'user':
#         print(psw)
#     case _:
#         print('default')
#
# for i in range(5):
#     print(i)

# i = 1
# while i <= 10:
#     b = i*2
#     print(b)
#     i += 1

# print('*' * int(input("введите число: ")))
# res = 1
# while True:
#     numb = int(input('Введите число: '))
#     if numb == 0:
#         print("Результат:", res)
#         break
#     res *= numb

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# a = 23
# print(a % 10)
# print(int(a / 10))

# a = int(input('Ширина'))
# b = int(input('Высота'))
# for i in range(b):
#     if i == 0 or i == b - 1:
#         print('*' * a)
#     else:
#         print('*' + (' ' * (a - 2))+'*')

# a = [1,2,3]
# for i in a:
#     print(i)

# res = 0
# a = [int(input('-->')) for i in range(int(input('Количество чисел ')))]
# for i in a:
#     if i < 0:
#         res += i
# print(res)

# res = 0
# summ = 0
# a = list(range(21, 41))
# for i in a:
#     if i % 2 == 0:
#         summ += 1
#     else:
#         res += i
# print('Количество четных элементов списка: ', summ, '\n сумма нечетных элементов списка: ', res)

# `s = [1, 2, 3, 4, 5, 6]
# # list[start:stop:step]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::-1])
# print(s[::2])
# print(s[5:1:-1])

# m = []
# for i in range(int(input('n= '))):
#     n = int(input('-->'))
#     if n == 0:
#         continue
#     m.append(n)
# print(sum(m) / len(m))

# numbers = []
# for i in range(int(input('Количество элементов: '))):
#     numb = int(input('Введите число кратное 3: '))
#     if numb % 3 != 0:
#         print(numb, 'не делится на 3 без остатка')
#         continue
#     numbers.append(numb)
# print(numbers)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# a, b = b, a
# print(a)
# print(b)
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# a = [int(input('->')) for i in range(int(input('n = ')))]
# a.pop(int(input('Введите индекс для удаления:')))
# print(a)

# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]
# for i in m:
#     for j in i:
#         print(j*j, end='\t')
#     print()

# w, h = 5, 3
# m = [[0 for i in range(w)] for y in range(h)]
# for i in m:
#     print(i)

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, '=', x + y)

# w, h = 3, 4
# m = [[randint(-20, 10) for i in range(w)] for y in range(h)]
# res = 0
# for i in m:
#     for j in i:
#         if j < 0:
#             res += 1
#         print(j, end='\t')
#     print()
# print(res)

# num1 = math.sqrt(4)
# num2 = round(4.6345,2)
# num3 = math.ceil(4.6345)
# num4 = math.floor(4.6345)
# print(num1)
# print(num2)
# print(num3)
# print(num4)
# sec = time.time()
# print(sec)
#
# local = time.ctime()
# print(local)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# print(time.strftime('Сегодня %B %d, %Y'))
# print(time.strftime('%m/%d/%Y, %H:%M:%S'))

# text = input('Название напоминания: ')
# local_time = float(input('Через сколько минут: '))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(2)
# finish = time.time()
# res = finish - start
# print(res)
#
# start = time.monotonic()
# time.sleep(2)
# finish = time.monotonic()
# res = finish - start
# print(res)

# def x(sym1, sym2, numb):
#     for i in range(numb):
#         if i % 2 == 0:
#             print(sym1, end='')
#         else:
#             print(sym2, end='')
#
#
# x('+', '-', 7)

# a = 1
# lt1 = [1, 2, 3]
# print(lt1, id(lt1))
# lt1.append(4)
# print(lt1, id(lt1))
# print(id(lt1[1]), id(a))

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# lst = tuple(lst)
# tpl = list(tpl)
# print(tpl)
# print(lst)
#
# s = tuple(input('->') for i in range(5))

# def slicer(tpl, el):
#     if el not in tpl:
#         return tuple()
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#
#
# a = (1, 2, 3)
# b = (1, 8, 3, 4, 8, 8, 9, 2)
# c = (1, 2, 8, 5, 1, 2, 9)
# print(slicer(a, 8))
# print(slicer(b, 8))
# print(slicer(c, 8))

#
# def numbers(first, second):
#     return tuple(randint(first, second) for i in range(10))
#
#
# a = numbers(0, 5)
# b = numbers(-5, 0)
# print(a)
# print(b)
# c = a + b
# print(c)
# print(c.count(0))

# def get_user():
#     name = 'tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)

# множества (set)

# s = {'1', '2', '3'}
# s = {1, 2, 3}
# print(s)
# print(type(s))

# def to_set(lst):
#     x = set(lst)
#     return x, len(x)


# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# print(r)
# # a = {i for i in r if 'a' in i}
# # a = ['A' if i[1:] == 'a' else 'B' + i[1:] for i in r]
# a = ['A' if i[1:] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)

# a = set(input('Первая строка: '))
# b = set(input('Вторая строка: '))
# c = a.union(b)
# print(c)

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# a = frozenset({'hello', 'World'})
# print(a)

# словарь
# s = ['a', 'b', 'c']
# d = {'one': 'a', 'two': 'b', 'three': 'c'}
# a = {1: 3, 2: 235, 3: 253}
# print(a[1])

# d = {i: i ** 2 for i in range(7)}
# print(d)

# x = {1: 3, 2: 7, 3: 5, 4: -1}
# res = 1
# for i in x:
#     res *= x[i]
# print(res)

# d = {i: input('-> ') for i in range(1, 5)}
# print(d)
# del d[int(input('Удалите'))]
# print(d)

# x = {
#     1: ['Core-i3-4330 - ', 9, ' шт. по 4500руб'],
#     2: ['Core-i5-4670K - ', 3, ' шт. по 8500руб'],
#     3: ['AMD FX-6300 - ', 6, ' шт. по 3700руб'],
#     4: ['Pentium G3220 - ', 8, ' шт. по 2100руб'],
#     5: ['Core-i5-3450 - ', 5, ' шт. по 6400руб']
# }
#
#
# def port():
#     for j in x:
#         print(f'{j}) {x[j][0]}{x[j][1]}{x[j][2]}')
#
#
# port()
#
# while True:
#     i = int(input('№: '))
#     if i == 0:
#         break
#     else:
#         x[i][1] = int(input('Количество: '))
#
# port()

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x.copy()
# z.update(y)
# z = x | y
# print(z)

# x = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# # y = dict()
# # y['name'] = x.pop('name')
# # y['salary'] = x.pop('salary')
# x["location"] = x.pop('city')
# print(x)
#
# x1 = {}

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# x = dict()
# s = None
# for i in a:
#     if type(i) is str:
#         x[i] = []
#         s = i
#     else:
#         x[s].append(i)
# print(x)

# x = {
#     'John': {
#         'N': 3056,
#         'S': 8463,
#         'E': 8441,
#         'W': 2694
#     },
#     'Tom': {
#         'N': 4832,
#         'S': 6786,
#         'E': 4737,
#         'W': 3612
#     },
#     'Anne': {
#         'N': 5239,
#         'S': 4802,
#         'E': 5820,
#         'W': 1859
#     },
#     'Fiona': {
#         'N': 3904,
#         'S': 3645,
#         'E': 8821,
#         'W': 2451
#     }
# }
# for i in x:
#     print(i)
#     for j in x[i]:
#         print(f'{j} : {x[i][j]}')
# try:
#     name = input('Имя: ')
#     region = input('Регион: ')
#     print(x[name][region])
#     x[name][region] = int(input('Новое значение: '))
#     print(x[name])
# except (ValueError, KeyError):
#     print('Ошибка')

# d = dict(zip([1, 2, 3], ['one', 'two', 'three', ]))
# print(d)
# one = {1: 1, 2: 2, 3: 3}
# two = {4: 4, 5: 5, 6: 6}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, v1, '->', k2, v2)

# pairs = [(2, 'one'), (3, 'two'), (1, 'three')]
# a, b = zip(*pairs)
# print(a)
# print(b)
#
# data = list(zip(a, b))
# print(data)
# data.sort()
# print(data)
# data = dict(data)
# print(data)
# f = {v: k for k, v in data.items()}
# f = list(f.items())
# print(f)

# one = {'apple': 0.45, 'orange': 0.35}
# two = {'pepper': 0.25, 'onion': 0.55}
# print({**one, **two})
#
# for k, v in {**one, **two}.items():
#     print(k, '->', v)
# a = [1, 2, 3]
# for i, color in enumerate(a, start=1):
#     print(i, color)

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))


# def to_dict(*args):
#     return dict(zip(args, args))
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))

# def func(**args):
#     return args
#
#
# print(func(a=1, b=2, c=3))


# def func(*args):
#     print(*args)
#     return args
#
#
# print(func(1, 2, 3, 'abc'))\


# def info(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#
#
# info(surname="Sharma", name="Irina", age=22, phone=1234567890)
# info(surname="Wood", name="Igor", email="igor@mail.ru", country="Russia", age=25, phone=6789012345)


# def add(a):
#     x = 2
#
#     def add_same():
#         print('x =', x)
#     add_same()
#
#     return a + x
#
#
# print(add(3))
# names = dir(builtins)
# for i in names:
#     print(i, end=', ')

# def i(**arg):
#     for k, v in arg.items():
#         print(k, v)
#
#
# i(s=2, d=4, f=6)
#
# def func():
#     a = 6
#
#     def func2(b):
#         a = 4
#         print(('summ:', a + b))
#
#     print('a =', a)
#     func2(4)
#
#
# func()

# x = 25
#
#
# def func():
#     global t
#     a = 30
#
#     def loo():
#         nonlocal a
#         a = 35
#
#     loo()
#     t = a
#
#
# func()
#
# c = x + t
# print(c)

# name = []
# ball = []
# for i in range(int(input('Количество студентов: '))):
#     name.append(input(f'{i + 1}-й студент: '))
#     ball.append(int(input('Балл: ')))
# all_n = dict(zip(name, ball))
#
# res = 0
# for i in ball:
#     res += i
# res = res / len(ball)
#
# print(f'Средний балл: {round(res)}. Студенты с баллом выше среднего:')
#
# for k, v in all_n.items():
#     if v > res:
#         print(k)

# x = 1
#
#
# def fn1():
#     global x
#     x = 25
#
#     def fn2():
#         # nonlocal x
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x', x)
#
#     fn2()
#     print('fn1.x', x)
#
#
# fn1()
# print(x)

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))

# Замыкание
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# a = outer(5)
# print(a(10))

# def func1():
#     a = 1
#     b = 'lime'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a
#         c.append(4)
#         a = a + 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func1(city):
#     c = 0
#
#     def func2():
#         nonlocal c
#         c += 1
#         print(city, c)
#
#     return func2
#
#
# res = func1('Москва')
# res()
# res()
# res()
# res1 = func1('Сочи')
# res1()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }


# def outer(lower, upper):
#     def inner(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return inner
#
#
# d_A = outer(80, 100)
# d_B = outer(70, 80)
# d_C = outer(50, 70)
# d_D = outer(0, 50)
#
# print('A', d_A(students))
# print('B', d_B(students))
# print('C', d_C(students))
# print('D', d_D(students))

# def outer(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.mul = mul
#     replace.sub = sub
#     return replace
#
#
# obj = outer(5, 2)
# print(obj.add())
# print(obj.sub())
# print(obj.mul())

# lambda - выражения
# func = lambda x, y: x + y
# print(func(3, 4))
# print((lambda x, y: x + y)(3, 4))
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# c = {
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# }
# for i in c:
#     print('abc__',i(2))

# print((lambda x: lambda y: lambda z: x + y + z)(1)(2)(3))

# d = {'b': 25, 'a': 15, 'c': 24}
# lst = list(d.items())
# lst.sort(key=lambda i: i[1])
# print(lst)
#
# new_d = sorted(d.items(), key=lambda i: i[1])
# print(new_d)

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
# print(sorted(players, key=lambda item: item['last name']))
# print(sorted(players, key=lambda item: item['rating'], reverse=True))
# print(max(players, key=lambda item: item['rating']))

# area = {
#     'circle': lambda r: 3.14 * r ** 2,
#     'triangle': lambda a, b: a * b
# }
# print((lambda a, b, c: a if b > a < c else b if c > b < a else c)(4, 2, 3))


# map(func,*iter),filter(func,*iter)
# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 3, 4, -5]
#
# print(list(map(mult, lst)))
# print(list(map(lambda t: t * 2, lst)))
# print((lambda a, b, c: min([a, b, c]))(3, 7, 1))

# s1 = [1, 2, 3]
# s2 = [4, 5, 6]
# s3 = list(map(lambda x, y: x + y, s1, s2))
# print(s3)

# b = [randint(1, 40) for i in range(10)]
# res = list(filter(lambda s: 10 <= s <= 20, b))
# print(res)

# декоратор

# def hello():
#     return 'hello'
#
#
# def super_func(func):
#     print('hello,s')
#     print(func())
#
#
# super_func(hello)

# def my_decorator(func):
#     def wrap():
#         print('code before')
#         func()
#         print('code after')
#
#     return wrap
#
#
# @my_decorator
# def func_test():
#     print('hello')
#
#
# # test = my_decorator(func_test)
# # test()
#
# func_test()


# def fist_func(arg1):
#     def second_func(fn):
#         def three_func(arg3):
#             fn(arg1)
#             print(arg1 * arg3)
#
#         return three_func
#
#     return second_func
#
#
# @fist_func(3)
# def fn(r):
#     print("Результат:", end=" ")
#
#
# fn(5)

# def decor(fn):
#     def wrap(args1, args2):
#         print(args1, args2)
#         fn(args1, args2)
#
#     return wrap
#
#
# @decor
# def print_name(first, last):
#     print('my name', first, last)
#
#
# print_name('ira', 'zdez')

# def decor(fn):
#     def wrap(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @decor
# def print_name(*names, study='python'):
#     print(*names, 'study', study)
#
#
# print_name('ira', 'jora', 'dima')
# print_name('ira', 'jora', 'dima', study='JS')


# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor('сложение: ', '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor('вычитание: ', '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def decor(numb):
#     def deco(fn):
#         def wrap(arg):
#             return fn(arg) * numb
#
#         return wrap
#
#     return deco
#
#
# @decor(3)
# def number(a):
#     return a
#
#
# print(number(5))


# def typed(*args, **kwargs):
#     def wrapped(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError('Некорректный тип данных', f_args[i])
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapped
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z


# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, 'doge'))
# # print(typed_fn(3.6, 4.3, 5))
#
# print(typed_fn2('hell', 'hell', '!'))

# def change(x, c_old, c_new):
#     str_ = ''
#     for i in x:
#         if i == c_old:
#             str_ += c_new
#             continue
#         str_ += i
#     return str_
#
#
# str1 = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования."
# str2 = change(str1, 'N', 'P')
# print(str1)
# print(str2)

# s = 'Test string for me'
# arr = [ord(i) for i in s]
# print('ASCII коды', arr)
# x = [int(sum(arr) / len(arr))] + arr
# print(x)

# print(chr(92))
# print(chr(158346))

# a, b = 122, 97
# if a < b:
#     a, b = b, a
# arr = [chr(i) for i in range(b, a + 1)]
# print(''.join(arr))

# str_ = ''.join([chr(i) for i in range(10)])
# print(type(str_))
# print(str_)


def func(a):
    numb = ''
    while a > 0:
        numb = str(a % 2) + numb
        a = a // 2
    print(numb)


while True:
    x = int(input('-> '))
    if x == 0:
        break
    func(x)
