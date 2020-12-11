# ============================================================================ #
#                                                                              #
#                        ПРОВЕРКА ФУНКЦИЙ БАЗЫ ДАННЫХ                          #
#                                                                              #
# ============================================================================ #

from database import Database


password = ''  # enter your password here
scenario_num = 6  # choose any among 1, 2, 3
name_db = 'heh'
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
    db = Database(name_db, username, password)
    db.create_database(name_db, username, password)
   # db.connect(name_db, username, password)
  #  c = input("Press enter to drop base")
    db.delete_database()  # пока не работает!!!

if scenario_num == 3:
    db = Database('postgres', username, password)
    db.create_database(name_db, username, password)

if scenario_num == 4:
    db = Database(name_db, username, password)
    db.create_database(name_db, username, password)
    print(db.get_table("Students"))
    print(db.get_table("Courses"))
    print(db.get_table("Groups"))
    print(db.get_table("Schedule"))
    db.delete_database()

if scenario_num == 5:
    db = Database(name_db, username, password)
    db.create_database(name_db, username, password)
    print(db.get_table("Students"))
    print(db.get_table("Courses"))
    print(db.get_table("Groups"))
    print(db.get_table("Schedule"))
    db.clear_table("Schedule")
    print(db.get_table("Schedule"))
    db.clear_all_table()
    print(db.get_table("Students"))
    print(db.get_table("Courses"))
    print(db.get_table("Groups"))
    db.delete_database()

if scenario_num == 6:
    db = Database(name_db, username, password)
    db.create_database(name_db, username, password)
    db.update_table('Schedule',['audience', 'lecturer'],['aud 228','zhmih'],['groupid', 'weekday', 'daytime'],[0,'Понедельник',1])
    print(db.get_table("Students"))
    print(db.get_table("Courses"))
    print(db.get_table("Groups"))
    print(db.get_table("Schedule"))
    print(db.search_by_FI('Антон','Коркунов'))
    db.delete_database()