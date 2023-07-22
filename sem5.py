"""
Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где: второе и третье число являются ключами. Первое число является значением
для первого ключа.
четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа.
"""
"""
a, b, c, *d = input("Введите символы с раделителем /: ").split("/")
print(res := {b: a, c:d})
"""

"""
Самостоятельно сохраните в переменной строку текста.
Создайте из строки словарь, где ключ — буква, а значение — код буквы.
Напишите преобразование в одну строку.
"""
"""
print(dct := {i: ord(i) for i in input("Ввкдите строку: ")})
"""
"""
Продолжаем развивать задачу 2. Возьмите словарь, который вы получили.
Сохраните его итераторатор. Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""
"""
a = iter(dct.items())
for i in range(5):
    print(*next(a))
"""
"""
Создайте генератор чётных чисел от нуля до 100.
Из последовательности исключите числа, сумма цифр которых равна 8. Решение в одну строку.
"""
"""
print(*(i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8))
"""
"""
Напишите программу, которая выводит на экран числа от 1 до 100.
При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
Вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz». *Превратите решение в генераторное выражение.
"""
"""
lst = (i for i in range(1, 101))
for num in lst:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
        
print(*("FizzBuzz" if not i % 15 else "Buzz" if not i % 5 else "Fizz" if not i % 3 else i for i in range(1, 101)))
"""
"""
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
отдельный пример таблицы умножения. Для вывода результата используйте «принт»
без перехода на новую строку.
"""
"""
print('\n\n'.join(('\n'.join(['\t\t\t'.join(
    [f'{x} x {y: >2} = {x*y:>3}' for x in range(2 + 4*k, 6+4*k)]) for y in range(2, 11)]) for k in range(2))))
"""
"""
Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило: «число является простым, если делится
нацело только на единицу и на себя».
"""

def simple_generator(n):
    count = 0
    current = 2
    while count < n:
        flag = True
        for i in range(2, current//2+1):
            if not current % i:
                flag = False
        current += 1
        if flag:
            count += 1
            yield current-1


generator = simple_generator(int(input("Введите число: ")))
print(*generator)
