def kmhmps(a):  #СКОРОСТЬ
    return f"Итог перевода: {round(a/3.6, 2)} метров в секунду\n----------"

def mpskmh(a):
    return f"Итог перевода: {round(a * 3.6, 2)} километр в час\n----------"

def milphkmh(a):
    return f"Итог перевода: {round(a * 1.609, 2)} километр в час\n----------"

def kmhmilph(a):
    return f"Итог перевода: {round(a / 1.609, 2)} миль в час\n----------"



def kmm(a):  #РАССТОЯНИЕ
    return f"Итог перевода: {round(a * 0.621371, 2)} миль\n----------"

def mkm(a):
    return f"Итог перевода: {round(a / 0.621371, 2)} км\n----------"

def milkm(a):
    return f"Итог перевода: {round(a * 1.609, 2)} километров\n----------"

def kmmil(a):
    return f"Итог перевода: {round(a / 1.609, 2)} миль\n----------"


def CtoF(a):  #ТЕМПЕРАТУРА
    return f"Итог перевода: {round((a* 9/5) +32, 2)} Фаренгейт\n----------"

def KtoF(a):
    return f"Итог перевода: {round((a* 9/5) +32 - 273.15, 2)} Фаренгейт\n----------"

def FtoC(a):
    return f"Итог перевода: {round((a-32) * 5/9, 2)} Цельсия\n----------"

def KtoC(a):
    return f"Итог перевода: {round(a - 273.15, 2)} Цельсия\n----------"

def CtoK(a):
    return f"Итог перевода: {round(a + 273.15, 2)} Кельвин\n----------"

def FtoK(a):
    return f"Итог перевода: {round((a-32) * 5/9 + 273.15, 2)} Кельвин\n----------"

def sqkmToSqmil(a):  #Площадь
    return f"Итог перевода: {round(a/2.59, 2)} квадратных миль\n----------"

def sqmilToSqKm(a):
    return f"Итог перевода: {round(a * 2.59, 2)} квадратных километров\n----------"

def lTom3(a): #объем
    return f"Итог перевода: {round(a / 1000, 2)} кубических метров\n----------"

def m3ToL(a):
    return f"Итог перевода: {round(a * 1000, 2)}  литра\n----------"





print("=== Конвертер значений ===")

while True:
    a = float(input("Введите значение: "))
    ans = int(input("1. Скорость\n2. Расстояние\n 3. Температура\n4. Площадь\n5. Объем\n0.Выход\nВыберите вариант: "))
    if ans not in [0,1,2,3,4,5]:
        print("Неправильный ввод")
        print("----------")
    elif ans == 0:
        print("До свидания!")
        break
    else: #ans = int(input(""))
        if ans == 1:
            ans = int(input("1. Километры в час в метры в секунду\n2. Метры в секунду в километры в час\n3. Километры в час в мили в час\n4. Мили в час в километры в час.\nВыберите вариант: "))
            if ans not in [1, 2, 3, 4]:
                print("Неправильный ввод")
                print("----------")
            elif ans == 1:
                print(kmhmps(a))
            elif ans == 2:
                print(mpskmh(a))
            elif ans == 3:
                print(kmhmilph(a))
            elif ans == 4:
                print(milphkmh(a))
        elif ans == 2:
            ans = int(input("1. Километры в метры\n2. Метры в километры\n3. Километры в мили\n4. Мили в километры\nВыберите вариант: "))
            if ans not in [1, 2, 3, 4]:
                print("Неправильный ввод")
                print("----------")
            elif ans == 1:
                print(kmm(a))
            elif ans == 2:
                print(mkm(a))
            elif ans == 3:
                print(kmmil(a))
            elif ans == 4:
                print(milkm(a))
        elif ans == 3:
            ans = int(input("1. Цельсии в Фаренгейты\n2. Кельвины в Фаренгейты\n3. Фаренгейты в Цельсии\n4. Кельвины в Цельсии\n 5. Цельсии в Кельвины\n6. Цельсии в Кельвины\nВыберите вариант: "))
            if ans not in [1, 2, 3, 4, 5, 6]:
                print("Неправильный ввод")
                print("----------")
            elif ans == 1:
                print(CtoF(a))
            elif ans == 2:
                print(KtoF(a))
            elif ans == 3:
                print(FtoC(a))
            elif ans == 4:
                print(KtoC(a))
            elif ans == 5:
                print(CtoK(a))
            elif ans == 6:
                print(FtoK(a))
        elif ans == 4:
            ans = int(input("1. Квадратные километры в квадратные милы\n2. Квадратные мили в квадратные километры\nВыберите вариант: "))
            if ans not in [1, 2]:
                print("Неправильный ввод")
                print("----------")
            elif ans == 1:
                print(sqkmToSqmil(a))
            elif ans == 2:
                print(sqmilToSqKm(a))
        elif ans == 5:
            ans = int(input("1.Литры в квадратные метры\n2. Квадратные метры в литры\nВыберите вариант: "))
            if ans not in [1, 2]:
                print("Неправильный ввод")
                print("----------")
            elif ans == 1:
                print(lTom3(a))
            elif ans == 2:
                print(m3ToL(a))
