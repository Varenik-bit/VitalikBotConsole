import time
import random
from colorama import init, Fore
from colorama import Back
from colorama import Style
import webbrowser
import keyboard
from pygame import mixer
import string
import art
import pyttsx3
import wikipedia
import cowsay
import pyscreenshot
import qrcode
import os
from translate import Translator


init(autoreset=True)


fg = 0
while fg != 1:
    print(Style.BRIGHT + '''Добро пожаловать! Выберите пункт меню:
        1. Вход
        2. Регистрация
        3. Гостевой вход''')

    user_auto = input()
    if user_auto == '1' or user_auto.lower() == 'вход':

        print('Введите имя:')
        login_name_e = input()

        print('Введите пароль:')
        password = input()

        with open('db_auto.txt', 'r', encoding='utf-8') as f:
            n = 0
            for line in f:
                n += 1
                if login_name_e in line:
                    le = n
                else:
                    pass
                if password in line:
                    if n - le == 1:
                        print('Вы успешно вошли в аккаунт!')
                        fg += 1
                    else:
                        print('Повторите попытку входа!!')
                else:
                    pass

    elif user_auto == '2' or user_auto.lower() == 'регистрация':

        print('Введите имя:')
        login_name_r = input()

        print('Введите пароль:')
        password = input()

        with open('db_auto.txt', 'a', encoding='utf-8') as f:
            f.write(login_name_r)
            f.write('\n')
            f.write(password)
            f.write('\n')
            f.write('-----------')
            f.write('\n')
        print('Регистрация прошла успешно!')
        break

    elif user_auto == '3' or user_auto.lower() == 'гостевой вход':
        break


while True:
    print(Fore.BLUE + 'Привет! Я твой ассистент Виталик! Выбери чем бы ты хотел заняться:')


    do_arr = ['Числовая угадай-ка', 'Камень, ножницы, бумага', 'Мини-калькулятор', 'Гугл-открывашка', 'Пианино', 'Генератор паролей', 'Красивый текст', 'Говорун слов', 'Википедиа', 'Корова говорунья', 'Скриншот', 'Генератор QR кода', 'Таймер помидоро', 'Выключатель компьютера']
    for i in do_arr:
        time.sleep(0.3)
        print(i)


    user_do = input(Fore.BLACK + Back.GREEN + 'Развлечение: ')
    user_do = user_do.lower()



    if user_do == 'мини-калькулятор':
        print('Тут ты можешь проводить математические расчеты! Для выхода из калькулятора введи любую букву!')
        while True:
            try:
                print(eval(input()))
            except:
                break



    if user_do == 'камень, ножницы, бумага':
        choice = ['камень', 'ножницы', 'бумага']
        user_ch = None

        while True:
            random_index = random.randint(0, len(choice) - 1)
            user_inp = input('Введите (камень, ножницы, бумага): ')

            if user_inp == choice[random_index]:
                print('НИЧЬЯ!')

            elif user_inp == 'ножницы' and choice[random_index] == 'бумага':
                print('ТЫ ВЫИГРАЛ!')
            elif user_inp == 'бумага' and choice[random_index] == 'ножницы':
                print('БОТ ВЫИГРАЛ!')

            elif user_inp == 'камень' and choice[random_index] == 'ножницы':
                print('ТЫ ВЫИГРАЛ!')
            elif user_inp == 'ножницы' and choice[random_index] == 'камень':
                print('БОТ ВЫИГРАЛ!')

            elif user_inp == 'бумага' and choice[random_index] == 'камень':
                print('ТЫ ВЫИГРАЛ!')
            elif user_inp == 'камень' and choice[random_index] == 'бумага':
                print('БОТ ВЫИГРАЛ!')

            user_ch = input('Желаешь продолжить игру?(ДА/НЕТ): ')
            if user_ch.upper() == 'ДА':
                continue
            elif user_ch.upper() == 'НЕТ':
                break
            else:
                print('НЕИЗВЕСТНАЯ КОМАНДА!')



    if user_do == 'числовая угадай-ка':

        while True:
            user_flagpl = 0
            if user_flagpl == 1:
                break

            print("Попробуй отгадать загаданное мной число")

            user_numpl1 = int(input('От какого числа я смогу загадывать: '))
            user_numpl2 = int(input('До какого числа я смогу загадывать: '))

            bot_numpl = random.randint(user_numpl1, user_numpl2)

            try_counter = 0

            print(f'Я загадал число от {user_numpl1} до {user_numpl2}! Попробуй угадать!')

            while True:
                try_counter += 1

                user_guess = int(input())

                if user_guess == bot_numpl:
                    print(f'ТЫ УГАДАЛ ЗА {try_counter} ПОПЫТОК! Это число {bot_numpl}!')
                    break
                else:
                    print('НЕ УГАДАЛ! Попробуй ещё раз!')

            while True:
                user_nextpl = input('ЖЕЛАЕШЬ ПРОДОЛЖИТЬ ИГРУ?(ДА/НЕТ) ')

                if user_nextpl.upper == 'ДА':
                    break

                elif user_nextpl.upper == 'НЕТ':
                    user_flagpl += 1
                    break

                else:
                    print('НЕИЗВЕСТНАЯ КОМАНДА!')
                    continue



    if user_do == 'гугл-открывашка':
        webbrowser.open(
            'https://google.com'
        )



    if user_do == 'пианино':
        mixer.init()

        do = mixer.Sound('notes/do.way')
        re = mixer.Sound('notes/re.way')
        mi = mixer.Sound('notes/mi.way')
        fa = mixer.Sound('notes/fa.way')
        sol = mixer.Sound('notes/sol.way')
        lja = mixer.Sound('notes/lja.way')
        si = mixer.Sound('notes/si.way')

        keymap = {
            'q': do,
            'w': re,
            'e': mi,
            'r': fa,
            't': sol,
            'y': lja,
            'u': si,
        }

        for key, note in keymap.items():
            keyboard.add_hotkey(key, note.play)
        while True:
            pass



    if user_do == 'генератор паролей':
        symbols = list(string.ascii_letters + string.digits)
        random.shuffle(symbols)
        n = int(input('Введите количество символов в пароле: '))
        password = ''.join(symbols[:n])
        print(password)



    if user_do == 'красивый текст':
        user_txt = input('Введите слово для вывода: ')
        art.tprint(user_txt)



    if user_do == 'говорун слов':
        engine = pyttsx3.init()
        user_say = input('Введите фразу которая будет произнесена: ')
        engine.say(user_say)



    if user_do == 'википедиа':
        user_known = input('О чем вы хотите узнать: ')
        print(wikipedia.search(user_known))
        user_knch = input('Выберите точную тему из предложенных: ')
        print(wikipedia.summary(user_knch))



    if user_do == 'корова говорунья':
        user_word = input('Какую фразу сказать корове: ')
        cowsay.cow(user_word)



    if user_do == 'скриншот':
        img = pyscreenshot.grab()
        img.save('test.png')



    if user_do == 'генератор QR кода':
        user_ht = input('Введите ссылку для QR кода: ')
        img = qrcode.make(user_ht)
        img.save('qr.png')



    if user_do == 'таймер помидоро':
        # Спрашиваем текст напоминания, который нужно потом показать пользователю
        print("О чём вам напомнить?")
        # Ждём ответа пользователя и результат помещаем в строковую переменную text
        text = str(input())
        # Спрашиваем про время
        print("Через сколько минут?")
        # Тут будем хранить время, через которое нужно показать напоминание
        local_time = float(input())
        # Переводим минуты в секунды
        local_time = local_time * 60
        # Ждём нужное количество секунд, программа в это время ничего не делает
        time.sleep(local_time)
        # Показываем текст напоминания
        print(text)



    if user_do == 'выключатель компьютера':

        user_time = int(input('Через сколько секунд хотите выключить компьютер: '))  # спрашиваем у пользователя через сколько выключить компьютер

        print(f'Компьютер будет выключен через {user_time} секунд!')  # выводим для удобства сообщение о времени выключения

        time.sleep(user_time)  # ставим таймер до выключения на время введённое пользователем

        os.system("shutdown -s -t 0")  # выключаем компьютер
