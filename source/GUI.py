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

URL = 'postgresql+psycopg2://postgres:123@localhost/postgres'


db = Database(URL)
db.create_database("hello_db")
c = input("Press anything to drop base")
db.delete_database()
