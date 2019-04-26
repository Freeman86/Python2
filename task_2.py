a = int(input("Введите число: "))

even = 0
odd = 0

while a > 0:
    if (a % 10) % 2 == 0:
        even += 1
    elif (a % 10) % 2 == 1:
        odd += 1
    a = a // 10

print(f'Четных {even}, нечетных {odd}')