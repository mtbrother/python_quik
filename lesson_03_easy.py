# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def people(name, age, city):
    print(name, str(age) + " год(а)", 'проживает в городе ' + city, sep=',')


people(name=input('Введите ваше имя: '), age=input('Введите ваш возраст: '),
       city=input('Введите город проживания: '))

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

numbers = [14, 25, 36]
print(max(numbers))


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_len(lst):
    count = len(max(lst, key=len))
    for element in lst:
        if len(element) == count:
            print(element)

max_len(['qwrf', 'jhgasgd', 'hgsdgv', 'hkasgdg'])
