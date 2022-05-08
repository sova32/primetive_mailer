# primetive_mailer

primetive_mailer

**Встановлення:**

git clone https://github.com/sova32/primetive_mailer.git
cd primetive_mailer
pip3 install email_validator

**Використання.**

cd primetive_mailer
python3 main.py

**Для пранків необхідно використовувати VPN!!!**

у папцы э три файла:
1. subject.txt - тема листа у одну строку. Программа читає лише саму першу строку, інше ігнорує
2. targets.txt - список поштових адрес. Кожна з нової строки
3. text.txt - текст листа.

Программа создає файл checked_emails.txt. Це виправлений та перевірений список поштових адрес. Кожного разу видаляється та записуються нові адреси.

На gmail.com приходить в спам.
На mail.ru приходить нормально.
