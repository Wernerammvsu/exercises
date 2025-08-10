"""
Три пирата делят награбленные N монет. Первого устраивает a% добычи, второго b%, третьего c%.
Гарантируется, что a, b, c<=100.

Найдите все распределения награбленного, которые устроят всех пиратов.
Формат входных данных
Строка 1: N (>0 типа int), a (>=0, float), b (>=0, float), c (>=0, float)
Формат выходных данных
Строки 1..N: все распределения монет, в одной строке пишется через пробел количество монет у каждого: na, nb, nc.

Строки выводятся в лексикографическом (алфавитном) порядке.

Если удовлетворительных дележей нет, нужно написать EMPTY.
"""
import math


# Читаем входные данные
data = input().strip().split()
N = int(data[0])
a, b, c = map(float, data[1:4])

# Вычисляем минимальные количества монет для каждого пирата
min_na = math.ceil(a / 100 * N)
min_nb = math.ceil(b / 100 * N)
min_nc = math.ceil(c / 100 * N)

results = []

# Перебираем na от min_na до N - (min_nb + min_nc)
for na in range(min_na, N + 1):
    # nb от min_nb до N - na - min_nc
    for nb in range(min_nb, N - na + 1):
        nc = N - na - nb
        # nc должно быть не меньше min_nc и не отрицательным
        if nc >= min_nc:
            results.append((na, nb, nc))

# Проверяем есть ли удовлетворяющие распределения
if not results:
    print("EMPTY")
else:
# Сортируем по лексикографическому порядку (na, nb, nc)
    results.sort()
# Выводим результаты
    for res in results:
        print(*res)
"""
В этом задании вам предлагается найти и вывести все счастливые билеты, в которых 2*N цифр и максимально возможная цифра 
равна M. Счастливый билет -- это тот, в котором сумма левой половины билета равняется сумме правой половины.
Формат входных данных
Строка 1: N (>0 типа int, размер одной половины билета), M (>=0 типа int, максимально возможная цифра в одном месте)
Формат выходных данных
Строки 1..maxDig^(N+1): билеты, отсортированные в порядке возрастания суммы, в случае равенства -- 
по возрастанию в лексикографическом (алфавитном) порядке.
"""
def generate_sequences(N, M):
    from collections import defaultdict
    sum_dict = defaultdict(list)

    def backtrack(prefix, length, max_digit, current_sum):
        if length == 0:
            sum_dict[current_sum].append("".join(map(str, prefix)))
            return
        for digit in range(max_digit + 1):
            backtrack(prefix + [digit], length - 1, max_digit, current_sum + digit)

    backtrack([], N, M, 0)
    # Сортируем последовательности по лексикографическому порядку внутри каждой суммы
    for s in sum_dict:
        sum_dict[s].sort()
    return sum_dict


N, M = map(int, input().split())
left_parts = generate_sequences(N, M)
right_parts = generate_sequences(N, M)

for s in sorted(left_parts.keys()):
    for left_seq in left_parts[s]:
        for right_seq in right_parts[s]:
            # Выводим билет из левой и правой половины
            # Разделять цифры пробелом согласно примеру из условия
            print(" ".join(left_seq + right_seq))

"""
В этом задании вам нужно перечислить все размещения (повторения возможны) из множества 0..maxDig размера N.
Формат входных данных
Строка 1: N (>0 типа int, размер размещения), maxDig (>=0 типа int, максимально возможная цифра в одном месте)
Формат выходных данных
Строки 1..maxDig^(N+1): размещения, отсортированные в лексикографическом (алфавитном) порядке.
"""

N, maxDig = map(int, input().split())
base = maxDig + 1
total = base ** N  # Общее количество размещений

for num in range(total):
    digits = []
    x = num
    for _ in range(N):
        digits.append(str(x % base))
        x //= base
    digits.reverse()  # Потому что младшие цифры шли первыми
    print(" ".join(digits))


