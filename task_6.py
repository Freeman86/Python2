
import random

num = random.randint(0, 10)
att = 0

while True:
    a = int(input("Введите число: "))
    att += 1
    if a == num:
        print("Вы угадали!")
        break
    elif a > num:
        print("Ваше число больше")
    elif a < num:
        print("Ваше число меньше")
    elif att > 10:
        print("Вы не угадали!")
        break