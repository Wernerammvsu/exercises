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

