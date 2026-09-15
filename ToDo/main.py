import json
import os
import datetime

db = "tasks.json"

tasks = []


#команды
def save():
     with open(db, "w", encoding="utf-8") as f:
             json.dump(tasks, f, ensure_ascii=False, indent=2)


def add():
    text = input("Напишите вашу задачу: ")
    if text.strip() == '':
        print("Напишите задачу заново\n")
    else:
        nowt = datetime.datetime.now()
        tasks.append({"text": text, "done": False, "date": nowt.strftime("%H:%M %Y.%m.%d")})
        save()

def load():
    global tasks
    if os.path.exists(db):  
        with open(db, "r", encoding="utf-8") as f:
            tasks = json.load(f)

def show():
    global tasks

    if not tasks:
        print("Список пустой...")
        return
    for i, t in enumerate(tasks, start=1):
        check = "✔" if t["done"] else " "
        print(f"{i}. [{check}] {t['text']}  ({t['date']})")

def mark(a):
    global tasks
    if 1 <= a <= len(tasks):
        tasks[a-1]["done"] = True
        save()
        print("Отмечено как выполненое! ✔")
    else:
        print("Задачи с таким номером не существует...")

def delete(a):
    global tasks
    if 1 <= a <= len(tasks):
        tasks.pop(a-1)
        save()
    else:
        print("Задачи с таким номером не существует...")

load()
#основной цикл
while True:
    try:
        menu = int(input("1. Добавить задачу\n2. Показать задачи\n3. Отметить выполненную задачу\n4. Удалить\n0. Выход\nВыбор: "))
        if menu in [1,2,3,4,0]:
            if menu == 1:
                add()
                
            elif menu == 2:
                show()
            
            elif menu == 3:
                show()
                try:
                    ans = int(input("Выберите номер задачи: "))
                    mark(ans)
                except:
                    print("Попробуйте заново...")
            
            elif menu == 4:
                show()
                try:
                    ans = int(input("Выберите номер задачи: "))
                    delete(ans)
                except:
                    print("Попробуйте заново...")
                
            
            elif menu == 0:
                save()
                break
        else:
            print("Введите допустимое значение...")
    except ValueError:
        print("Неверное значение, попробуй написать цифру...")