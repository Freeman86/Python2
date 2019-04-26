a = int(input("Введите число: "))

def recursion(a):
    if (a // 10) == 0:
        print(a)
    else:
        print(a % 10)
        a = a // 10
        recursion(a)

recursion(a)
