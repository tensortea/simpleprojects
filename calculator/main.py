def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def divide(a,b):
    if a == 0 or b == 0:
        return "На ноль нельзя делить!"
    return a / b
def multiply(a,b):
    return a*b

while True:
    print("=======Калькулятор=======")
    ans = int(input("1. Сложить\n2.Отнять\n3.Умножить\n4.Разделить\n0.Выход\n\nВыберите пункт(0-4): "))
    if ans == 0:
        print("До свидания!")
    elif ans != 1 and ans != 2 and ans != 3 and ans != 4:
        print("Я Вас не понял, повторите, пожалуйста, еще раз...")
    else:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if ans == 1:
            print("Ответ:",add(a,b))
        if ans == 2:
            print("Ответ:",substract(a,b))
        if ans == 3:
            print("Ответ:",multiply(a,b))
        if ans == 4:
            print("Ответ:",divide(a,b))
