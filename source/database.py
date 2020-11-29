class user:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def get_user_information(self):
        return self.name + " " + self.password


class Database:
    def __init__(self, url):
        pass

    def create_database(self):  # создание бд
        pass

    def delete_database(self):  # удаление бд
        pass

    def create_tables(self):  # создание таблицы
        pass

    def get_table(self, name):  # вывод содержимого таблицы
        pass

    def clear_table(self, name):  # это частичная (очистили одну)
        pass

    def clear_all_table(self, name):  # это полная (очистили все)
        # for table in tables:
        #   clear_table(table)
        pass

    # функция частичной очистки одной из таблиц??? - частичная, значит очистить одну таблицу
    # а полная значит очистить все таблицы

    def insert_into(self, table_name, values):  # добавление данных
        pass

    def search_by_group(self, group_name):# Поиск по заранее выбранному(вами) текстовому не ключевому полю
        pass  # мы вроде решили, что ищем по названию группы

    def update_table(self, table):# Обновление кортежа
        pass

    def delete_by_group(self, group_name):# Удаление по заранее выбранному текстовому не ключевому полю
        pass
    def single_delete(self, record_id):# Удаление конкретной записи, выбранной пользователем
        pass