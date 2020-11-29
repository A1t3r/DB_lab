from sqlalchemy import create_engine
from sqlalchemy_utils import create_database

# создаем связь
engine = create_engine('postgresql+psycopg2://postgres:123@localhost/postgres')
conn = engine.connect() # создаем транзакцию
result = conn.execute("select * from aircrafts")
print(result)
print(list(result))

conn.execute("commit") # заканчиваем открытую транзакцию
result = conn.execute("create database heh") # теперь можно создать базу данных
