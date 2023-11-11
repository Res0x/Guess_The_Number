from random import randint
def is_valid(num):
    if num.isdigit():
        return True
    else:
        return False
def is_correct(txt):
    if txt == 'да' or txt == 'нет':
        return True
    return False
def play_game(rt):
    n = randint(1, rt)
    print('Угадайте число, которое я загадал')
    trys = input()
    while not is_valid(trys):
        print('Вы ввели не число, введите еще раз')
        trys = input()
    trys = int(trys)
    counter = 1
    while trys != n:
        if trys < n:
            print('Слишком мало, попробуйте еще раз')
        elif trys > n:
            print('Слишком много, попробуйте еще раз')
        trys = input()
        while not is_valid(trys):
            print('Вы ввели не число, введите еще раз')
            trys = input()
        trys = int(trys)
        counter += 1
    print(f'Вы угадали, за {counter} попыток поздравляем!')
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

print('Вы хотите сыграть в игру?')
ans = input().lower()
while not is_correct(ans):
    print('Введите да или нет')
    ans = input()
while ans == 'да':
    print('Добро пожаловать в числовую угадайку')
    print('Я загадаю число от 1 до того, которое вы сейчас введете')
    right_border = input()
    while not is_valid(right_border):
        print('Вы ввели не число, введите еще раз')
        right_border = input()
    right_border = int(right_border)
    play_game(right_border)
    print('Хотите сыграть еще раз?')
    ans = input().lower()
    while not is_correct(ans):
        print('Введите да или нет')
        trys = input()