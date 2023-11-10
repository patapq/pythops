#!/usr/bin/env python3

# Глава 1

# Напишите функцию Python, принимающую название в качестве аргумента
# и выводящую его в консоль.
# Объявляем функцию с параметром
def print_arg(name):
    print(name)

print_arg('something')

# Напишите функцию Python, принимающую строку в качестве аргумента
# и выводящую в консоль информацию о ее регистре.
def case_info(s: str):
    if s.isupper(): # Проверка строки на верхний регистр
        print('String is in upper case')
    elif s.islower(): # Проверка на нижний регистр
        print('String is in lower case')
    else: 
        print('String is mixed case') # Смешанный регистр

case_info('HELLO')
case_info('hello')
case_info('hElLo')


# Напишите списковое включение для получения списка букв слова smogtether
# в верхнем регистре.
list_compr = [i.upper() for i in 'smogtether'] # Списковое включение
print(list_compr)


# Напишите генератор, попеременно возвращающий слова «Четное» и «Не-
# четное».
def even_odd_generator():
    count = 0
    while True:
        if count % 2 == 0:
            yield "Четное"
        else:
            yield "Нечетное"
        count += 1

gen = even_odd_generator()
print(next(gen)) # Возвращает следующее значение генератора
print(next(gen))
print(next(gen))


# Глава 3

# Напишите с помощью sys сценарий, который выводит текст «командная
# строка» только тогда, когда запущен из командной строки.

import sys

def cmd():
    print('командная строка')

# "командная строка" будет выведен только при запуске файла из командной строки
# python3 lr_1.py
# Вывод: командная строка
# При импорте import lr_1.py строка выведена не будет
if __name__ == '__main__':
    cmd()


# Создайте с помощью библиотеки click утилиту командной строки, прини-
# мающую в качестве аргумента название и выводящую его в случае, если оно
# не начинается с символа p.

import click

@click.command()
@click.option('--name', default='Name', help='Enter a name not starting with p')
def greet(name):
    if name[0] != 'p':
        print(name)

greet()
# python3 lr_1.py --name Artur
# Вывод: Artur

# Воспользуйтесь fire для обращения к методам в уже существующем сценарии
# Python из командной строки
import fire

def greet(greeting='Hiya', name='Tammy'):
    print(f'{greeting} {name}')

fire.Fire()
# fire позволяет вызвать любой метод из командной строки, вызвав его имя и передать параметры
# python3 lr_1.py greet --greeting Hello!
# python3 lr_1.py print_arg Cool