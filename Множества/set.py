"""
Реализуйте функцию union для множеств из python, не используя готовую функцию union. Можете использовать этот контест для проверки своего решения.
Формат входных данных
Строка 1: множество A целых чисел, записанных через пробел, или строка EMPTY
Строка 2: множество B целых чисел, записанных через пробел, или строка EMPTY
Формат выходных данных
Объединение множеств A и B: набор целых чисел, записанных в порядке возрастания через пробел.
Если результат операции -- пустое множество, напечатайте EMPTY.
"""
def union(set_a, set_b):
    result = []

    # Добавляем из первого множества все элементы
    for elem in set_a:
        result.append(elem)

    # Добавляем из второго множества все элементы, которых нет в результате
    for elem in set_b:
        result.append(elem)

    result = set(result)
    result = sorted(result)
    return result


 # Читаем первое множество
line_a = input().strip()
if line_a == "EMPTY":
    set_a = []
else:
    set_a = list(map(int, line_a.split()))

    # Читаем второе множество
line_b = input().strip()
if line_b == "EMPTY":
    set_b = []
else:
    set_b = list(map(int, line_b.split()))

    # Получаем объединение
union_set = union(set_a, set_b)

if not union_set:
    print("EMPTY")
else:
    print(" ".join(map(str, union_set)))



"""
Реализуйте функцию instersection для множеств из python, не используя готовую функцию intersection. Можете использовать этот контест для проверки своего решения.
Формат входных данных
Строка 1: множество A целых чисел, записанных через пробел, или строка EMPTY
Строка 2: множество B целых чисел, записанных через пробел, или строка EMPTY
Формат выходных данных
Пересечение множеств A и B: набор целых чисел, записанных в порядке возрастания через пробел.
Если результат операции -- пустое множество, напечатайте EMPTY.
"""
def intersection(set_a, set_b):
    result = []

    for elem in set_a:
        if elem in set_b and elem not in result:
            result.append(elem)

    return sorted(result)


# Читаем первое множество
line_a = input().strip()
if line_a == "EMPTY":
    set_a = []
else:
    set_a = list(map(int, line_a.split()))

# Читаем второе множество
line_b = input().strip()
if line_b == "EMPTY":
    set_b = []
else:
    set_b = list(map(int, line_b.split()))

inter_set = intersection(set_a, set_b)

if not inter_set:
    print("EMPTY")
else:
    print(" ".join(map(str, inter_set)))

"""
Реализуйте функцию difference для множеств из python, не используя готовую функцию difference. Можете использовать этот контест для проверки своего решения.
Формат входных данных
Строка 1: множество A целых чисел, записанных через пробел, или строка EMPTY
Строка 2: множество B целых чисел, записанных через пробел, или строка EMPTY
Формат выходных данных
Разность множеств A и B: набор целых чисел, записанных в порядке возрастания через пробел.
Если результат операции -- пустое множество, напечатайте EMPTY.
"""
def difference(set_a, set_b):
    result = []

    for elem in set_a:
        if elem not in set_b and elem not in result:
            result.append(elem)

    return sorted(result)

line_a = input().strip()
if line_a == "EMPTY":
    set_a = []
else:
    set_a = list(map(int, line_a.split()))

line_b = input().strip()
if line_b == "EMPTY":
    set_b = []
else:
    set_b = list(map(int, line_b.split()))

diff_set = difference(set_a, set_b)

if not diff_set:
    print("EMPTY")
else:
    print(" ".join(map(str, diff_set)))


"""
Реализуйте отображение trueSQRT, которое возвращает по положительному числу X два значения квадратного корня из Х.
Формат входных данных
Строка 1: число X>=0  типа float или int
Формат выходных данных
Два числа A и B типа float, записанные через пробел.
"""
import math

def trueSQRT(X):
    root = math.sqrt(X)
    return -root, root


X = float(input().strip())
A, B = trueSQRT(X)
if A == 0 :
    print(0)
else:
    print(A, B)

"""
Вам дан набор данных людей, в котором указаны имена, даты рождения и средний чек в магазине. Отсортируйте эти данные по каждому из полей и выведите результат.
Формат входных данных
Строка 1: N, целое положительное число, количество строк в данных
Строки 2..N+1: запись данных (имя, средний чек, дата рождения в формате DD.MM.YYYY)
Формат выходных данных
Строки 1..N: записи, отсортированные по полю имя
знак #
Строки N+2..2N+1: записи, отсортированные по полю чек
знак #
Строки 2N+2..3N+2: записи, отсортированные по полю дата
"""
from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, "%d.%m.%Y")


N = int(input())
data = []
for _ in range(N):
    line = input().strip()
    name, check_str, date_str = line.split()
    check = float(check_str)
    date = date_str  # сохраним строку, а для сортировки используем дату из parse_date
    data.append((name, check, date, line))  # сохраним оригинальную строку для вывода

# Сортируем по имени
sorted_by_name = sorted(data, key=lambda x: x[0])

# Сортируем по среднему чеку
sorted_by_check = sorted(data, key=lambda x: x[1])

# Сортируем по дате (парсим дату)
sorted_by_date = sorted(data, key=lambda x: parse_date(x[2]))

# Вывод результатов
for record in sorted_by_name:
    print(record[3])
print("#")
for record in sorted_by_check:
    print(record[3])
print("#")
for record in sorted_by_date:
    print(record[3])



"""
В этом задании вам нужно вычислить образ данного множества при заданном отображении F(x) = x^5 + 1.
Формат входных данных
Строка 1: элементы множества через пробел, числа типа int
Формат выходных данных
Строка: элементы образа через пробел, числа типа int в порядке возрастания
"""

line = input().strip()
if line == "":
    input_set = set()
else:
    input_set = set(map(int, line.split()))

image_set = set()
for x in input_set:
    image_set.add(x**5 + 1)

print(" ".join(str(num) for num in sorted(image_set)))