from sqlalchemy import create_engine, MetaData
import queries as q


class Database:
    _engine = None
    _connect = None
    _metadata = None
    _id_dict = {
        'Student': 1,
        'Group': 1,
        'Schedule': 1,
        'Course': 1
    }

    def __init__(self, url):  # стартовая инициализация
        self._engine = create_engine(url)
        self._connect = self._engine.connect()
        self._metadata = MetaData()
        # can we use engine.execute() instead?
        return

    def create_database(self):  # создание бд
        pass

    def delete_database(self):  # удаление бд
        pass

    def _create_tables(self):  # создание таблиц
        pass

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
        self._metadata.reflect(self._engine)
        if table_name in self._metadata.tables.keys() and table_name in q.table_names:
            length = len(values)
            query = q.insert_dict[table_name](values, self._id_dict[table_name])
            self._id_dict[table_name] += length
            return query
        else:
            raise ValueError("Can't delete from non-exist table {}".format(table_name))

    def search_by_group(self, group_name):  # Поиск по заранее выбранному(вами) текстовому не ключевому полю
        pass  # мы вроде решили, что ищем по названию группы

    def update_table(self, table):  # Обновление кортежа
        pass

    def delete_by_group(self, group_name):  # Удаление по заранее выбранному текстовому не ключевому полю
        pass

    def single_delete(self, record_id):  # Удаление конкретной записи, выбранной пользователем
        pass
