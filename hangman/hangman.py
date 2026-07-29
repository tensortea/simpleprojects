import random

#переменные
secret = []
words = ["пайтон", "змея", "код", "число", "слово", "виселица", "пытка", "казнь"]
att = 0
ct = 0

#стадии
HANGMAN_STAGES = [
    ["  +---+", '  |   |', '  |', '  |','  |', '  |','========='],
    ["  +---+", '  |   |', '  |   O', r'  |','  |', '  |','========='],
    ["  +---+", '  |   |', '  |   O', r'  |   |', '  |', '  |', '========='],
    ["  +---+", '  |   |', '  |   O', r'  |   |\ ', r'  |', '  |', '========='],
    ["  +---+", '  |   |', '  |   O', r'  |  /|\ ', r'  |', '  |', '========='],
    ["  +---+", '  |   |', '  |   O', r'  |  /|\ ', r'  |    \ ', '  |', '========='],
    ["  +---+", '  |   |', '  |   O', r'  |  /|\ ', r'  |  / \ ', '  |', '=========']
]

print("Добро пожаловать на виселицу. Попробуйте отгадать слово за 6 попыток чтобы выжить")

word = random.choice(words)      #выбор слова
for _ in range(len(word)):  # шифрование слова
    secret.append("*")

#цикл игры
while True:
    ct = 0
    print('\n'.join(HANGMAN_STAGES[att]), sep='\n')    #состояние виселицы
    print(f"Загаданное слово: {''.join(secret)}, возможностей ошибиться: {6-att}")
    an = input("Введите букву: ")      #ввод буквы

    if an in word: #проверка(неполная)
        for i in range(len(word)):
            if word[i] == an:
                secret[i] = an

    else: # ошибка
        att += 1

    for i in range(len(word)):
        if word[i] == secret[i]:
            ct+=1

    if ct == len(word):
        print("Вы выиграли!")
        print('\n'.join(HANGMAN_STAGES[att]), sep='\n')
        break

    elif att == 6:
        print("Вы проиграли")
        print('\n'.join(HANGMAN_STAGES[att]), sep='\n')
        break
