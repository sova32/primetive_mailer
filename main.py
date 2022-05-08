import asyncio
import subprocess
import time
import sys
from random import random


import smtplib

from email_validator import validate_email, EmailNotValidError
from email.message import EmailMessage



targets = set({})
subject = None


def check_emails():
    global targets
    temp = targets
    targets = set({})

    print('Форматування адрес скриньок та перевірка на доступність домену...')

    f = open('checked_emails.txt', 'w')

    for target in temp:
        try:
            emailObject = validate_email(target)
            targets.add(target)
            f.write(target + '\n')
        except EmailNotValidError as errorMsg:
            # If `testEmail` is not valid print a human readable error message
            print(str(errorMsg))

    f.close()
    print('Перевірені та робочі скриньки збарежено у файл: checked_emails.txt')



def open_files():
    global targets
    global subject
    global text
    global error_message



    # targets.txt
    print('Відкриваю і обробляю targets.txt')
    try:
        file = open('targets.txt')
    except Exception as exc:
        print('Помилка! Код помилки: ', exc)
        error_message = 'Перевірте файл "targets.txt" та спробуйте ще раз.'
        close_programm(error_message)
    for line in file.readlines():
        line = line.replace(' ', '')
        line = line.replace('\n', '')
        targets.add(line)
    file.close()
    print('Однакові скриньки відфільтровано, видалені лишні символи.')

    # subject.txt
    print('Відкриваю і обробляю subject.txt')
    try:
        file = open('subject.txt')

        subject = file.readline()
        file.close()

    except Exception as exc:
        print('Помилка! Код помилки: ', exc)
        error_message = 'Перевірте файл "subject.txt" та спробуйте ще раз.'
        close_programm(error_message)



    # text.txt
    # print('Відкриваю і обробляю text.txt')
    # try:
    #     file = open('text.txt')
    # except Exception as exc:
    #     print('Помилка! Код помилки: ', exc)
    #     error_message = 'Перевірте файл "text.txt" та спробуйте ще раз.'
    #     close_programm(error_message)
    # for line in file.readlines():
    #     text.append(line)
    # file.close()



def close_programm(message):
    print(message)
    print('Програму завершено. Натисніть "Enter" ')
    input()
    sys.exit(0)


async def main():
    global error_message

    global targets
    global subject
    global text



    print('Слава Україні!')
    print('Русский военный корабль, иди нахуй!!!')
    sender = input('Від кого шлем листа (наприклад killtheputin@mordor.ru)?: ')

    open_files()
    check_emails()

    try:

        for target in targets:
            # +++ Основний цикл відправки +++

            # Open the plain text file whose name is in textfile for reading.
            with open('/run/media/vadiki/D_238_GB_WD/Projects/python/mail sender/text.txt') as fp:
                # Create a text/plain message
                msg = EmailMessage()
                msg.set_content(fp.read())

            # me == the sender's email address
            # you == the recipient's email address
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = target

            # Send the message via our own SMTP server.
            s = smtplib.SMTP('localhost')
            s.send_message(msg)
            s.quit()
            print('Чекаю 3 секунди...')
            time.sleep(3)
            # --- Основний цикл відправки ---


        error_message = 'Завдання виконано!\nСлава нації! Смерть рашиській педерації!'



    except Exception as e:
        print(e, type(e))
    finally:
        close_programm(error_message)


if __name__ == "__main__":
    asyncio.run(main())