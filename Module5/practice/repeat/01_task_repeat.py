# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random

def gen_list(size, of, to):
    lst = []
    for i in range(size):
        lst.append(random.randint(of, to))
    return lst

print(gen_list(5, 1, 20))
