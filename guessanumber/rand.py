from random import *

while True:
    print("*** Угадай число ***")
    print("Попробуй угадать число от 1 до 100, которое я загадал на этот раз")
    x = randint(1,100)
    ans = int(input("Первая попытка:"))
    if x == ans:
        print(f"Правильно! Ты угадал с первой попытки")
    else:
        print("Неправильно!")
        if x > ans:
            print("Больше")
        else:
            print("Меньше")
        ans = int(input("Вторая попытка:"))
        if x == ans:
            print(f"Правильно! Ты угадал с второй попытки")
        else:
            print("Неправильно!")
            if x > ans:
                print("Больше")
            else:
                print("Меньше")
            ans = int(input("Третья попытка:"))
            if x == ans:
                print(f"Правильно! Ты угадал с третья попытки")
            else:
                print("Неправильно!")
                if x > ans:
                    print("Больше")
                else:
                    print("Меньше")
                ans = int(input("Четвертая попытка попытка:"))
                if x == ans:
                    print(f"Правильно! Ты угадал с четвертой попытки")
                else:
                    print("Неправильно!")
                    if x > ans:
                        print("Больше")
                    else:
                        print("Меньше")
                    ans = int(input("Пятая(последняя) попытка попытка:"))
                    if x == ans:
                        print(f"Правильно! Ты угадал с пятой попытки")
                    else:
                        print(f"Чтож, кажется удача не на твоей стороне. Правильный ответ:{x}")