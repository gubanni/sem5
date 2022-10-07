import random
import os

def InputNumber(text, ostatok):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{text}, введите количество конфет, которое возьмете от 1 до {ostatok}: "))
            if number >= 1 and number <= ostatok:
                is_OK = True
            else:
                print(f"{text}, введите корректное количество конфет")
        except ValueError:
            print("Это не число!")
        
    return number

def InputNumberBot(text, ostatok):
    print(f"{text}, введите количество конфет, которое возьмете от 1 до {ostatok}: ")
    number = random.randint(1, ostatok)  
    print(number)
    return number

def player_vs_bot():
    candies_total = 2021
    max_take = 28
    count = 0
    player_1 = input('\nИмя первого игрока: ')
    player_2 = 'Bot'

    print('\nДля начала опеределим кто первый начнет игру.\n')

    x = random.randint(1, 2)
    if x == 1:
        first = player_1
        second = player_2
    else:
        first = player_2
        second = player_1
    print(f'{first} ты ходишь первым !')

    while candies_total > 0:
        if count == 0:
            kol_candies = min(candies_total, max_take)
            if first == 'Bot':
                if candies_total <= max_take:
                    step = candies_total
                else:
                    step = InputNumberBot(first, kol_candies)
            else:
                step = InputNumber(first, kol_candies)
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОсталось еще {candies_total}')
            count = 1
        else:
            print('Все кончились конфетки')

        if count == 1:
            kol_candies = min(candies_total, max_take)
            if second == 'Bot':
                if candies_total <= max_take:
                    step = candies_total
                else:
                    step = InputNumberBot(second, kol_candies)
            else:
                step = InputNumber(second, kol_candies)
            #step = InputNumber(second, kol_candies)
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОсталось еще {candies_total}')
            count = 0
        else:
            print('Игра окончена!')

    if count == 1:
        print(f'{second} ПОБЕДИЛ')
    if count == 0:
        print(f'{first} ПОБЕДИЛ')


player_vs_bot()