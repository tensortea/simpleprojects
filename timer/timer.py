import playsound
import time
from datetime import datetime
loc = datetime.now()
print(f"Добро пожаловать в Таймер. Текущее время - {loc.strftime("%H:%M")}.")
an = int(input("1. Звонок к определенному времени(например, к 16:45).\n2. Звонок через определенное время(например, через 10 минут.\nВыберите режим: "))

if an == 1:
    loc = datetime.now()
    amh = int(input("Выберите час: "))
    amm = int(input("Выберите минуту: "))
    if amh > 23 or amm > 59 or amh < 0 or amm < 0:
        print("Неправильное время!")
    else:
        amm = amm + amh*60
        lmm = int(loc.strftime("%M")) + int(loc.strftime("%H")) * 60
        print(f"Таймер установлен в {datetime.now()}")
        if (amm - lmm)*60 <= 0:
            time.sleep(1440 - (amm - lmm)*60)
            playsound.playsound("alarm.mp3")
        else:
            time.sleep((amm - lmm)*60)
            playsound.playsound("alarm.mp3")


elif an == 2:
    ams = int(input("Выберите время таймера в минутах: "))

    if ams > 1500:
        print("Для таких целей лучше воспользоваться календарём")
    elif ams > 0:
        print(f"Таймер установлен в {datetime.now()}")
        time.sleep(ams*60)
        playsound.playsound("alarm.mp3")
    else:
        print("Я Вас не понял, пожалуйста, запустите Таймер заново")