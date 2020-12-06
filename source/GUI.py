from tkinter import *
from database import Database

import variables as v


def create_database():
    pass

def detele_database():
    pass

def fill_tables():
    pass

def clear_tables():
    pass

def pack_menu():
    db_menu = Menu()
    db_menu.add_command(label="Create database", command=create_database)
    db_menu.add_command(label="Delete database", command=detele_database)

    table_menu = Menu()
    table_menu.add_command(label="Fill tables", command=fill_tables)
    table_menu.add_command(label="Clear tables", command=clear_tables)

    main_menu = Menu()
    main_menu.add_cascade(label="Database", menu=db_menu)
    main_menu.add_cascade(label="Tables", menu=table_menu)

    root.config(menu=main_menu)


def root_settings():
    pass


def pack_frame_data():
    frame_data.pack(side=LEFT)


def pack_frame_tools():
    frame_tools.pack()


root = Tk()
root_settings()
pack_menu()

frame_data = Frame(root, width=v.width_frame_data, height=v.height_frame_data, bg="darkred")
pack_frame_data()

frame_tools = Frame(root, width=v.width_frame_tools, height=v.height_frame_tools, bg="green", bd=20)
pack_frame_tools()

root.mainloop()
