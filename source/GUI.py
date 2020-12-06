# from tkinter import *

# root = Tk()
# entry = Entry(root)
# root.mainloop()

# ============================================================================ #
#                                                                              #
#                        ПРОВЕРКА ФУНКЦИЙ БАЗЫ ДАННЫХ                          #
#                                                                              #
# ============================================================================ #

from database import Database


password = ''  # enter your password here
name_db = 'kekv'
username = 'postgres'

db = Database('postgres', username, password)
db.create_database(name_db, username, password)
# db.connect(name_db, username, password)
# c = input("Press enter to drop base")
db.delete_database()
