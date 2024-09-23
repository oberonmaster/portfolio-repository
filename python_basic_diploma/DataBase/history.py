import os
import datetime
from peewee import *

# Получаем абсолютный путь к файлу базы данных
base_dir = os.path.dirname(os.path.abspath(__file__))  # Папка, в которой находится этот файл
db_path = os.path.join(base_dir, 'history.db')  # Путь к файлу базы данных

# создаем файл базы данных SQlite с абсолютным путем
db = SqliteDatabase(db_path)


# создаем класс таблицы
class HistoryTable(Model):
    history_user_id = IntegerField()  # id пользователя телеграм - целое число
    history_command = CharField()  # выполненая ботом команда - строка
    history_date = CharField()  # дата и время выполнения команды - строка

    class Meta:
        database = db


# Заполнение базы данных
def db_history_of_using(user_id: int, command: str):
    HistoryTable.create(history_user_id=user_id,
                        history_command=command,
                        history_date=datetime.datetime.now().strftime('%m.%d.%y %H:%M:%S'))


def history_of_using(user_id: int):
    message = str()

    messages = list()

    for action in HistoryTable.select().where(HistoryTable.history_user_id == user_id):
        messages.append(f"{action.history_command} : {action.history_date}")

    for i in messages[-1: -11:-1]:
        message += f"{i} \n"

    return message


# Создание таблицы, если она не существует
db.connect()
db.create_tables([HistoryTable], safe=True)
