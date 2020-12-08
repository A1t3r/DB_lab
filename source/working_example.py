import database as db
from sqlalchemy import create_engine, MetaData
from sqlalchemy_utils import create_database

# создаем связь
engine = create_engine('postgresql+psycopg2://postgres:password@localhost/lab1')
conn = engine.connect()  # создаем транзакцию
result = conn.execute("select * from ПРОКАТ")
print(result)
for i in list(result):
    print(i)

# query = ''' #пример создания пользователя
# CREATE USER if not exists test with password 'test'  # скл код этого дела
# ''' #
# result = conn.execute(query) # ну тут и так понятно

conn.execute("commit")  # заканчиваем открытую транзакцию
# result = conn.execute("create database heh") # теперь можно создать базу данных

# conn.execute("create table custs (id serial primary key, surname varchar(15));")

metadata = MetaData()

# metadata.reflect(engine)
# print(metadata.tables.keys())

conn.execute("""
create table if not exists Course
(
	id serial primary key,
	name varchar(20)
);
""")
conn.execute("commit")


# insert password
#db=db.Database('heh', 'postgres', password)