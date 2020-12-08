from sqlalchemy import create_engine, MetaData
import psycopg2
import queries as q
import parsers as pr

tables = ('Groups', 'Students', 'Courses', 'Schedule')


class Database:
    _parent_connect = None
    _connect = None
    _metadata = None
    _name = None
    _engine = None
    _conn_string = "host='{}' dbname='{}' user='{}' password='{}'"
    _id_dict = {
        'Student': 1,
        'Group': 1,
        'Schedule': 1,
        'Course': 1
    }

    def __init__(self, dbname, username, password, host='localhost'):  # стартовая инициализация
        engine = create_engine('postgresql+psycopg2://{}:{}@{}'.format(username, password, host))
        self._parent_connect = engine.connect()
        self._metadata = MetaData()
        self._parent_connect.execute("commit")
        # self.create_database(dbname, username, password)
        # self._create_tables()
        # self._create_procedures()  # create init postgres procedures
        # for table in tables:
        #    self.insert_into(table, pr.init_insert_parser("data/" + table + ".txt"))
        # self._parent_connect.execute("commit")
        return

    def __fill_tables(self):
        for table in tables:
            tmp = pr.init_insert_parser("data/" + table + ".txt")
            for record in tmp:
                self.insert_into(table, record)

    def _create_insert_(self, inserts):
        for sql in inserts:
            self._connect.execute(sql)
            self._connect.execute("commit")

    def _create_delete_(self):
        pass

    def _create_select_all_(self):
        pass

    def _create_procedures(self):
        self._create_insert_(q.total_insert)
        self._create_delete_()
        self._create_select_all_()

    def create_database(self, database_name, username, password, host='localhost'):  # создание бд
        if self._name == None:
            self._parent_connect.execute("create database {}".format(database_name))
            self._parent_connect.execute("commit")
            self._name = database_name

            engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(username, password, host, database_name))
            self._engine = engine
            self._connect = engine.connect()
            self._connect.execute("commit")

            self._create_tables()
            self._create_procedures()
            self.__fill_tables()
        else:
            raise ValueError("'{}' already exists".format(database_name))
        return

    def connect(self, database_name, username, password, host='localhost'):
        if self._name == None:

            engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(username, password, host, database_name))
            self._engine = engine
            self._connect = engine.connect()
            self._connect.execute("commit")

            self._name = database_name
        else:
            raise ValueError("Already connected to '{}'".format(self._name))
        return

    def delete_database(self):  # удаление бд
        if self._name != None:
            self._connect.close()
            self._engine.dispose()
            self._connect = None
            self._engine = None
            c = input("Press enter to drop base")
            self._parent_connect.execute("DROP DATABASE {};".format(self._name))
            self._parent_connect.execute("commit")
            self._name = None
        else:
            raise ValueError("Database does not exist")
        return

    def __del__(self):
        if self._connect != None: self._connect.close()
        if self._parent_connect != None: self._parent_connect.close()
        if self._engine != None: self._connect.close()
        return

    def _create_tables(self):  # создание таблиц
        self._connect.execute(q.create_table_courses_query)
        self._connect.execute(q.create_table_schedule_query)
        self._connect.execute(q.create_table_groups_query)
        self._connect.execute(q.create_table_students_query)
        self._connect.execute("commit")
        return

    def get_table(self, name):  # вывод содержимого таблицы
        self._metadata.reflect(self._engine)
        if name in self._metadata.tables.keys():
            return q.select_all_from(name)
        else:
            raise ValueError("Can't get from non-exist table '{}'".format(name))

    def clear_table(self, name):  # это частичная (очистили одну)
        self._metadata.reflect(self._engine)
        if name in self._metadata.tables.keys():
            return q.delete_all_from(name)
        else:
            raise ValueError("Can't delete from non-exist table {}".format(name))

    def clear_all_table(self, name):  # это полная (очистили все)
        for name in q.table_names:
            self.clear_table(name)
        return

    # функция частичной очистки одной из таблиц??? - частичная, значит очистить одну таблицу
    # а полная значит очистить все таблицы

    def insert_into(self, table_name, values):  # добавление данных
        connection = self._engine.raw_connection()
        cursor = connection.cursor()
        cursor.callproc("insert_{}".format(table_name), values)
        results = list(cursor.fetchall())
        cursor.close()
        connection.commit()
        connection.close()

    def search_by_group(self, group_name):  # Поиск по заранее выбранному(вами) текстовому не ключевому полю
        pass  # мы вроде решили, что ищем по названию группы

    def update_table(self, table):  # Обновление кортежа
        pass

    def delete_by_group(self, group_name):  # Удаление по заранее выбранному текстовому не ключевому полю
        pass

    def single_delete(self, record_id):  # Удаление конкретной записи, выбранной пользователем
        pass
