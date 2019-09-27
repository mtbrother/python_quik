# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import re
import shutil
import sys

def make_dir (name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print('{} - уже существует'.format(name))

def remove_dir (name):
    try:
        os.removedirs(name)
    except FileNotFoundError:
        print('{} - папки не существует'.format(name))

def start ():
    answer =''
    quantity_dirs = range(1, 10)

    while answer != '3':

        answer = input('Выберите пункт меню:\n'
                       '1. Создать папки dir_1 - dir_9\n'
                       '2. Удалить папки dir_1 - dir_9\n'
                       '3. Выход\n')
        if answer =='3':
            break
        if answer == '1':
            for i in quantity_dirs:
                i = str(i)
                make_dir('dir_' + i)
        elif answer == '2':
            for i in quantity_dirs:
                i = str(i)
                remove_dir('dir_' + i)

if __name__ == '__main__':
    start()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()
if __name__ == '__main__':
    list_dir(main_path)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def current_file_copy ():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'

if __name__ == '__main__':
    print(current_file_copy())