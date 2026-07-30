import math
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def div(a,b):
    if b == 0:
        return "На ноль нельзя делить!"
    return a / b
def mult(a,b):
    return a*b


while True:
    print("=======Калькулятор=======")
    ans = int(input("1. Сложить\n2. Отнять\n3. Умножить\n4. Разделить\n5. Возвести в степень\n6. Квадратный корень\n7. Функции тригонометрии\n0. Выход\n\nВыберите пункт(0-7): "))
    if ans == 0:
        print("До свидания!")
        break
    elif ans not in [1,2,3,4, 5, 6, 7]:
        print("Я Вас не понял, повторите, пожалуйста, еще раз...")
    else:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if a == 3.14:
            a = math.pi
        elif b == 3.14:
            b = math.pi
        elif a == 2.71:
            a = math.e
        elif b == 2.71:
            b = math.e
        if ans == 1:
            print("Ответ:",plus(a,b))
        elif ans == 2:
            print("Ответ:",minus(a,b))
        elif ans == 3:
            print("Ответ:",mult(a,b))
        elif ans == 4:
            print("Ответ:",div(a,b))
        elif ans == 5:
            print(f"Ответ: {a**b}")
        elif ans == 6:
            print(f"Ответ: {math.sqrt(a)}; {math.sqrt(b)}")
        elif ans == 7:
            ans = int(input("1. Синус\n2. Косинус\n3. Тангенс\n4.Перевод радиан в градусы\n5. Перевод градусов в радианы\n6. АркСинус\n7. АркКосинус\n8. АркТангенс\nВыберите вариант(1-8): "))
            if ans == 1:
                print(f"Ответ: {math.sin(math.radians(a))}; {math.sin(math.radians(b))}")
            elif ans == 2:
                print(f"Ответ: {math.cos(math.radians(a))}; {math.cos(math.radians(b))}")
            elif ans == 3:
                print(f"Ответ: {math.tan(math.radians(a))}; {math.tan(math.radians(b))}")
            elif ans == 4:
                print(f"Ответ: {math.degrees(a)}; {math.degrees(b)}")
            elif ans == 5:
                print(f"Ответ: {math.radians(a)}; {math.radians(b)}")
            elif ans == 6:
                print(f"Ответ: {math.degrees(math.asin(a))}; {math.degrees(math.asin(b))}")
            elif ans == 7:
                print(f"Ответ: {math.degrees(math.acos(a))}; {math.degrees(math.acos(b))}")
            elif ans == 8:
                print(f"Ответ: {math.degrees(math.atan(a))}; {math.degrees(math.atan(b))}")
