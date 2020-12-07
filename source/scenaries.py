# ============================================================================ #
#                                                                              #
#                        ПРОВЕРКА ФУНКЦИЙ БАЗЫ ДАННЫХ                          #
#                                                                              #
# ============================================================================ #

from database import Database


password = ''  # enter your password here
scenario_num = 1  # choose any among 1, 2, 3
name_db = 'kekv'
username = 'postgres'

# args: (self, database_name, username, password, host='localhost') для всех
# db = Database('postgres', username, password)
# db.create_database(name_db, username, password)
# db.connect(name_db, username, password)

if scenario_num == 1:
    db = Database('postgres', username, password)
    db.create_database(name_db, username, password)
    c = input("Press enter to drop base")
    db.delete_database()  # пока не работает!!!

if scenario_num == 2:
    db.connect(name_db, username, password)
    c = input("Press enter to drop base")
    db.delete_database()  # пока не работает!!!

if scenario_num == 3:
    db = Database('postgres', username, password)
    db.create_database(name_db, username, password)