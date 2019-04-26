while True:
    c = input("Введите знак: ")
    if c == "0":
        print("До свидания!")
        break
    elif c == '/' or c == '*' or c == '-' or c == '+':
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        if c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c == '/':
            if a == 0 or b == 0:
                print("Введите ненулевое значение")
            else:
                print(a / b)
        elif c == '*':
            print(a * b)
    else:
        print("Введите коректное значения знака!")