from sqlalchemy import MetaData, Table, Integer, String, Column, Text, DateTime, Boolean
from sqlalchemy.orm import mapper
from datetime import datetime
from model.py import *

metadata = MetaData()

db = Table('post', metadata,
    Column('id', Integer(), primary_key=True),
    Column('group', String(200), nullable=False)
    Column('created_on', DateTime(), default=datetime.now)
)

class User(object):
    pass

mapper(User, db)

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Устанавливаем соединение с postgres
connection = psycopg2.connect(user="postgres", password="1111")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создаем курсор для выполнения операций с базой данных
cursor = connection.cursor()
sql_create_database =
# Создаем базу данных
cursor.execute('create database sqlalchemy_tuts')
# Закрываем соединение
cursor.close()
connection.close()