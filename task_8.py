seq = int(input("Введите последовательность: "))
num = int(input("Введите число для поиска: "))
temp = ""
count = 0

while seq > 0:
    temp = seq % 10
    seq = seq // 10
    if temp == num:
        count += 1


print(count)