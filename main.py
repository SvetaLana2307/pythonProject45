#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
Задача 1.
Напишите рекурсивную функцию fact, которая вычисляет факториал заданного числа x.
'''


def fact(x):
    if x <= 0:
        return 1
    else:
        return x * fact(x - 1)


print(fact(int(input("Введите число факториал, которого хотите узнать"))))

# In[ ]:


'''
Задача 2.
Создайте функцию filter_even, которая принимает на вход список целых чисел, и фильтруя, возвращает список,
содержащий только четные числа. Используйте filter для фильтрации и lambda.
'''


def filter_even(li):
    func = filter(lambda x: x % 2 == 0, li)
    list1 = list(func)
    return list1


string = (input("Введите цифры через пробел")).split()
string = [int(x) for x in string]

print(filter_even(string))

# In[ ]:


'''
Задача 3.
Напишите функцию square ,которая принимает на вход список целых чисел и
возвращает список с возведенными в квадрат элементами. Используйте map.
'''


def square(li):
    return list(map(lambda x: x * x, li))


# In[ ]:


'''
Задача 4.
Напишите функцию бинарного поиска bin_search, которая принимает на вход отсортированный список и элемент.
Функция должна возвращать индекс искомого элемента в списке.
'''


def bin_search(li, element):
    left = 0
    right = len(li)

    while (left + 1 < right):
        mid = (left + right) // 2

        if li[mid] <= element:
            left = mid
        else:
            right = mid

    if li[left] != element:
        return -1
    return left


# In[ ]:


'''
Задача 5.
Напишите функцию is_palindrome определяющую,является ли строка палиндромом. Палиндромами являются текстовые строки,
которые одинаково читаются слева направо и справа налево. В строках не учитываются знаки препинания,
пробельные символы и цифры; регистр не имеет значения.

На вход подается строка string.

Выведите YES, если строка является палиндромом и NO иначе.

Запрещается использовать reverse списка - list[::-1] и функцию reversed.
Чтобы учесть это ограничение, эту задачу рекомендуется решать используя технику решения задач "два указателя".
Один указатель читает только символы слева направо, а второй - справа налево.
'''


def is_palindrome(string):
    string_copy = ""
    string = string.strip()
    string = string.lower()
    for i in range(len(string)):
        if string[i].isalpha():
            string_copy += string[i]
    len_str = len(string_copy)
    for i in range(len(string_copy)):
        if string_copy[i] != string_copy[len_str - 1 - i] and (i < len_str - 1 - i):
            return "NO"
        return "YES"


print(is_palindrome(input("Введите строку ")))

# In[ ]:


'''
Задача 6.
Написать функцию calculate, которая принимает на вход текстовый файл содержащий строки следующего формата:

Формат файла: арифметическая операция целое число #1 целое число #2
Разделитель - 4 пробела

Функция должна вернуть 1 строку. Строка содержит набор из чисел, разделенных запятой.
После последнего числа запятая не ставится. Каждое число - результат операции:
"результирующее целое число" = "целое число #1" применить "арифметическая операция" "целое число #2"
'''


def calculate(path2file):
    output = ''

    with open(path2file) as f:

        for curLine in f.readlines():
            tokens = curLine.split('    ')
            op = tokens[0]
            x = int(tokens[1])
            y = int(tokens[2])
            prod = 0

            if op == '+':
                prod = x + y
            elif op == '-':
                prod = x - y
            elif op == '*':
                prod = x * y
            elif op == '//':
                prod = x // y if y != 0 else 'NAN'
            elif op == '%':
                prod = x % y if y != 0 else 'NAN'
            elif op == '**':
                prod = x ** y

            output += f"{prod},"

    return output


# In[ ]:


'''
Задача 7.

Написать функцию substring_slice,которой на вход поступают два текстовых файла.

Первый файл содержит строки текста.

Второй файл содержит строки из двух целых неотрицательных чисел. Первое число в строке всегда меньше или равно второму.
Числа всегда меньше длины соответствующей строки первого файла.
Соответствующей - это значит 1-ая строка из 1-го файла соответствует 1-ой строке из 2-го файла,
а 123-я строка из 1-го файла соответствует 123-ей строке из 2-го файла.

Функция должна вернуть строку, состоящую из подстрок 1-го входного файла.
Подстроки разделены пробелами. Какие брать подстроки - написано во втором файле. В конце файла пробела нет.
'''


def substring_slice(path2file_1, path2file_2):
    output = ''

    with open(path2file_1) as f1, open(path2file_2) as f2:
        for curLine in f1.readlines():
            tokens = f2.readline().split()
            x1 = int(tokens[0])
            x2 = int(tokens[1])

            output += f"{curLine[x1:x2 + 1]} "

    return output


# In[ ]:


'''
Задача 8.

Написать функцию decode_ch,на вход которой поступает строка.
В ней хранится набор химических символов (He, O, H, Mg, Fe, ...). Без пробелов.
Нужно расшифровать химические символы в название химических элементов.
Функция должна вернуть строку - расшифровку

Для удобства, прилагается json файл, который ставит в соответствие химическому символу его химическое название.
'''

import json


def decode_ch(string_of_elements):
    output = ''

    with open('periodic_table.json', encoding='utf-8') as json_file:
        curElem = ''
        periodic_table = json.load(json_file)

        for i in range(len(string_of_elements)):
            curElem += string_of_elements[i]

            if i + 1 == len(string_of_elements) or string_of_elements[i + 1].isupper():
                output += periodic_table.get(curElem)
                curElem = ''

    return output


# In[ ]:


'''
Задача 9.

Создайте класс с названием Student.

При инициализации объекта подается два аргумента. Первый - имя студента. Второй - фамилия студента.

1. Создайте три атрибута объекта данного класса:
1)name имя студента
2)surname фамилия студента
3)fullname имя и фамилия студента через пробел

2. Создайте метод для экземпляра класса Student под названием greeting, который при вызове возвращает
строку Hello, I am Student Здесь и далее нужно только написать сам класс.

3. Добавьте новый атрибут класса под названием grades. При инициализации объекта соответственно
добавляется новый аргумент, в котором будет лежать список оценок данного студента, по дефолту
равный списку [3,4,5]. Создайте метод под названием mean_grade, который возвращает среднее всех
оценок студента (то есть среднее этого атрибута).

4. Сделайте метод is_otlichnik, который возвращает строку YES, если средняя оценок студента больше
или равна 4.5 и NO в противном случае. Примечание: этот метод должен вызывать метод mean_grade внутри себя.

5. На этот раз определим операцию сложения для двух студентов. Пусть такая операция возвращает строку следующего
вида: "Name1 is friends with Name2", где Name1 и Name2 - имена первого студента и второго (именно атрибут name).
То есть, если создать два экземпляра класса Student, то их сумма должна вернуть вышеописанную строку.

6. Теперь переопределим поведение нашего класса с функцией print.
Пусть при вызове функции print от экземпляра класса Student печатается его атрибут fullname.
'''

from functools import reduce


class Student:
    name = ''

    surname = ''

    fullname = ''

    grades = []

    def __init__(self, name, surname, grades=[3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = name + " " + surname
        self.grades = grades

    def greeting(self):
        return f'Hello, I am Student {self}'

    def mean_grade(self):
        return reduce(lambda x, y: x + y, self.grades) / len(self.grades)

    def is_otlichnik(self):
        return 'YES' if self.mean_grade() >= 4.5 else 'NO'

    def __add__(self, other):
        return f'{self.name} is friends with {other.name}'

    def __str__(self):
        return self.fullname


# In[ ]:


'''
Задача 10.

Определите класс исключений MyError, который принимает строковое сообщение
msg в качестве параметра при инициализации и также имеет атрибут msg.
'''


class MyError(Exception):
    msg = ''

    def __init__(self, msg):
        self.msg = msg

