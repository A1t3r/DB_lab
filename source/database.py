class user:
    def __init__(self, name,  password):
        self.name=name
        self.password=password

    def get_user_inforamation(self):
        return self.name + " " + self.password

class Database:
    def __init__(self, url):
        pass

    def create_database(self):
        pass

    def delete_database(self):
        pass

    def create_tables(self):
        pass

    def get_table(self, name):
        pass

    def clear_table(self, name):
        pass

    # функция частичной очистки одной из таблиц???

    def insert_into(self, table_name, values):
        pass

    # Поиск по заранее выбранному(вами) текстовому не ключевому полю

    # Обновление кортежа

    # Удаление по заранее выбранному текстовому не ключевому полю

    # Удаление конкретной записи, выбранной пользователем


