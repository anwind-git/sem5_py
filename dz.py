"""
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из
трёх элементов: путь, имя файла, расширение файла.
"""
print("--------------------------")
print("dz1")
print("--------------------------")


def split_path(path):
    import os

    file_name, ext = os.path.splitext(os.path.basename(path))

    return os.path.dirname(path), file_name, ext


path = "/home/user/documents/example.txt"
print(split_path(path))

"""
Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии
"""
print("--------------------------")
print("dz2")
print("--------------------------")

names = ['Вася', 'Петя', 'Вова']
amounts = [100, 200, 300]
prizes = ['10.5%', '15%', '20.25%']

result_dict = {name: amount * float(prize.strip('%')) / 100 for name, amount, prize in zip(names, amounts, prizes)}

print(result_dict)

"""
Создайте функцию генератор чисел Фибоначчи
"""
print("--------------------------")
print("dz3")
print("--------------------------")


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
print([next(fib) for _ in range(10)])