# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

number = int(input('Введите число от 0 до 9: '))
while True:
    if 0 < number < 10:
        print('Число в квадрате = ', number ** 2)
        break
    else:
        number = int(input('Введите число от 0 до 9: '))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

a = int(input('Введите значение а: '))
b = int(input('Введите значение b: '))
a, b = b, a
print('a =', a)
print('b =', b)
