# !/usr/bin/python 
# -*- coding: utf-8 -*-
from configparser import ConfigParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from json import dumps
from logging import basicConfig, getLogger, error
from smtplib import SMTP


import asyncio
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from apps.model.models import (
    db, Users, ApplicationTos, Cars

)

# Старт журналирования
log = basicConfig(filemode='log/error.log')

# ------------------------------------------------
# Создание таблиц перед запуском приложения
# ------------------------------------------------
db.connect()
db.create_tables([Users, ApplicationTos, Cars])
db.close()

# Конфиг который хранит данные для старта
conf = ConfigParser()
conf.read('config.ini')

# Точка старта бота
bot = Bot(token=conf['Bot']['token'])
dp = Dispatcher(bot)


data = {}
json_obj = {"inline_keyboard": []}


class Request:
    '''
    Данный класс отправляет заявку на почту.
    '''
    pass


class App:
    '''
    Класс обрабатывает только текст, инлайн события не принимает. Так-же
    имеет один главный метод.
    '''
    def __init__(self):
        self.start = "Здравствуйте, какая у вас марка машины?"
        self.is_phone_text = "Введите номер телефона, что бы мы с вами могли связаться."
        self.is_email = [
            "Вы можете добавть дополнительно почту.",
            "Введите электронную почту."
        ]
        self.sendler = "Отправить заявку?"

    async def main(self, bot, msg):
        if msg.text == '/start':
            keyboard = json_obj['inline_keyboard'].append([
                {'text': 'Ford', 'callback_data': 'Ford'}, {'text': 'Lincoln', 'callback_data': 'Lincoln'}
            ])
            await bot.send_message(chat_id=msg.from_user.id, text=self.start, reply_markup=dumps(json_obj))
            del json_obj['inline_keyboard'][:]


    async def email_user(self, bot, msg):
        global data
        if "@" in msg.text:
            data['email'] = msg.text
            json_obj['inline_keyboard'].append([{"text": "Отправить", "callback_data": "Отправить"}])
            await bot.send_message(chat_id=msg.from_user.id, text=self.is_email[1], reply_markup=dumps(json_obj))
    

    async def if_email(self, bot, msg):
        global data
        if 'volume_enjine' in data and 'model' in data and 'mark' in data:
            try:
                data['user_number'] = int(str(msg.text).replace(' ', '').replace('-', '').replace('+', '').strip())

                json_obj['inline_keyboard'].append([
                    {"text": "Пропустить", "callback_data": "Пропустить"}
                ])
                await bot.send_message(chat_id=msg.from_user.id, text=self.is_email[0], reply_markup=dumps(json_obj))
            except:
                await bot.send_message(chat_id=msg.from_user.id, text=self.is_phone_text)
            # удаление
            del json_obj['inline_keyboard'][:]
            

class Application:
    '''
    Класс обрабатывает только инлайн события, предназначен для формирования 
    заявки.
    '''
    def __init__(self) -> None:
        self.is_mark_text = "Выберите марку машины"
        self.is_model_text = "Выберите модель:"
        self.is_volume_enjine_text = "Укажите объём двигателя:"
        self.is_phone_text = "Введите номер телефона, что бы мы с вами могли связаться."
        self.is_email = [
            "Вы можете добавть дополнительно почту.",
            "Введите электронную почту."
            ]
        self.sendler = "Заявка отправлена, с вами скоро свяжутся."
    
    
    async def mark_car(self, bot, msg):
        global data
        d=[]
        for x in db.execute_sql('SELECT name FROM cars;').fetchall():
            d.append(x[0])

        if msg.data in set(d):
            l=[]
            row = db.execute_sql(f'SELECT model_car FROM cars WHERE name="{msg.data}";')
            for i in row.fetchall():
                l.append(i[0])
            
            data['mark'] = msg.data
            for j in set(l):
                json_obj['inline_keyboard'].append([{'text': j, 'callback_data': j}])

            await bot.send_message(chat_id=msg.from_user.id, text=self.is_mark_text, reply_markup=dumps(json_obj))
            # удаление
            del json_obj['inline_keyboard'][:]


    async def model_car(self, bot, msg):
        global data
        d=[]
        for x in db.execute_sql('SELECT model_car FROM cars;').fetchall():
            d.append(x[0])

        if msg.data in set(d):
            l=[]
            row = db.execute_sql(f'SELECT year_car FROM cars WHERE model_car="{msg.data}";')
            for i in row.fetchall():
                l.append(i[0])
            
            data['model'] = msg.data
            for j in set(l):
                json_obj['inline_keyboard'].append([{'text': j, 'callback_data': j}])

            await bot.send_message(chat_id=msg.from_user.id, text=self.is_model_text, reply_markup=dumps(json_obj))
            # удаление
            del json_obj['inline_keyboard'][:]


    async def year_car(self, bot, msg):
        global data
        d=[]
        for x in db.execute_sql('SELECT year_car FROM cars;').fetchall():
            d.append(x[0])

        if msg.data in set(d):
            l=[]
            row = db.execute_sql(f'SELECT volume_engine FROM cars WHERE year_car="{msg.data}";')
            for i in row.fetchall():
                l.append(i[0])
            
            data['year'] = msg.data
            for j in set(l):
                json_obj['inline_keyboard'].append([{'text': j, 'callback_data': j}])

            await bot.send_message(chat_id=msg.from_user.id, text=self.is_volume_enjine_text, reply_markup=dumps(json_obj))
            # удаление
            del json_obj['inline_keyboard'][:]


    async def phone_user(self, bot, msg):
        global data
        d=[]
        for x in db.execute_sql('SELECT volume_engine FROM cars;').fetchall():
            d.append(str(x[0]))

        if msg.data in set(d):
            data['volume_enjine'] = msg.data
            await bot.send_message(chat_id=msg.from_user.id, text=self.is_phone_text)


    async def send(self, bot, msg, _f=False):
        global data
        if msg.data == "Пропустить" or _f == True:
            '''
            Отправка заяки на почту и в лс + проверка
            на наличие почты.
            '''
            data['user'] = msg.from_user.first_name

            json_obj['inline_keyboard'].append([{"text": "Начать заново", "callback_data": "Начать заново"}])
            await bot.send_message(chat_id=msg.from_user.id, text=self.sendler, reply_markup=dumps(json_obj))
            

            # Фотрмирование сообщения
            if 'email' in data:
                text = f"Имя: {data['user']}\nПочта: {data['email']}\nНомер телефона: {data['user_number']}\n"
                text += f"Марка: {data['mark']}\nМлодель: {data['model']}\n"
                text += f"Год: {data['year']}\nОбъём двигателя: {data['volume_enjine']}\n"
            else:
                text = f"Имя: {data['user']}\nНомер телефона: {data['user_number']}\n"
                text += f"Марка: {data['mark']}\nМлодель: {data['model']}\n"
                text += f"Год: {data['year']}\nОбъём двигателя: {data['volume_enjine']}\n"

            # Отправка данных на почту
            server = SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(user='vuacheslav.mir@gmail.com', password='amritta3113')
            message = MIMEMultipart()
            message['From'] = conf['Mail']['login']
            message['To'] = "gleblarionov46@gmail.com"
            message['Subject'] = "Заявка от бота!"
            message.attach(MIMEText(text, 'plain'))
            server.sendmail(message['From'], message['To'], message.as_string())
            server.quit()

            # Отправка в ЛС
            await bot.send_message(chat_id='549779784', text=text)
            # удаление
            del json_obj['inline_keyboard'][:]


    async def callback_email_user(self, bot, msg):
        global data
        if msg.data == " Пропустить":
            await self.send(bot=bot, msg=msg, _f=True)


@dp.message_handler(content_types=['text'])
async def main(msg):
    # Принимаем обычный текст
    await App().main(bot=bot, msg=msg)
    await App().if_email(bot=bot, msg=msg)
    await App().email_user(bot=bot, msg=msg)

@dp.callback_query_handler(lambda call: True)
async def callback(msg):
    # Читаем Inline кнопки
    await Application().mark_car(bot=bot, msg=msg)
    await Application().model_car(bot=bot, msg=msg)
    await Application().year_car(bot=bot, msg=msg)
    await Application().phone_user(bot=bot, msg=msg)
    await Application().callback_email_user(bot=bot, msg=msg)
    await Application().send(bot=bot, msg=msg)


# Запуск
if __name__ == '__main__':
	executor.start_polling(dp)
