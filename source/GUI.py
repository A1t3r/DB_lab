from tkinter import *
from tkinter import messagebox as mb
from database import Database

import variables as v


def create_database():
    pass


def create_database_def():
    pass


def create_database_window():
    window = Toplevel(root)
    window.title("Create database")
    entries = dict()

    num = 0
    for i in range(len(v.cd_names)):
        Label(window, padx=v.cd_pad, pady=v.cd_pad, text=v.cd_names[i], width=v.cd_label_width).grid(row=i, column=0)
        ent = Entry(window, width=v.cd_entry_width)
        ent.grid(row=i, column=1, padx=v.cd_pad, pady=v.cd_pad)
        entries['ent1'] = ent
        num += 1

    Button(window, text="Create def", command=create_database_def).grid(row=num,
                                                                        column=0)  # might be deleted when p'll be finished
    Button(window, text="Create", command=create_database).grid(row=num, column=1, padx=v.cd_pad, pady=v.cd_pad)


def connect_database():
    pass


def connect_database_def():
    pass


def connect_database_window():
    window = Toplevel(root)
    window.title("Connect database")
    entries = dict()

    num = 0
    for i in range(len(v.cd_names)):
        Label(window, padx=v.cd_pad, pady=v.cd_pad, text=v.cd_names[i], width=v.cd_label_width).grid(row=i, column=0)
        ent = Entry(window, width=v.cd_entry_width)
        ent.grid(row=i, column=1, padx=v.cd_pad, pady=v.cd_pad)
        entries['ent1'] = ent
        num += 1

    Button(window, text="Connect def", command=connect_database_def).grid(row=num,
                                                                          column=0)  # might be deleted when p'll be finished
    Button(window, text="Connect", command=connect_database).grid(row=num, column=1, padx=v.cd_pad, pady=v.cd_pad)


def detele_database():
    answer = mb.askyesno(
        title="Attention",
        message="Do you want to delete database?")
    if answer:
        pass  # there have to be deleting database


def fill_tables():
    pass  # there have to be database filling with data


def clear_tables():
    pass


def pack_menu():
    db_menu = Menu()
    db_menu.add_command(label="Create", command=create_database_window)
    db_menu.add_command(label="Connect", command=connect_database_window)
    db_menu.add_command(label="Delete", command=detele_database)

    table_menu = Menu()
    table_menu.add_command(label="Fill tables", command=fill_tables)
    table_menu.add_command(label="Clear tables", command=clear_tables)

    main_menu = Menu()
    main_menu.add_cascade(label="Database", menu=db_menu)
    main_menu.add_cascade(label="Tables", menu=table_menu)

    root.config(menu=main_menu)


def root_settings():
    root.title("The most impressive application name")


def show_tables_tool():
    pass


# root
root = Tk()
root_settings()
pack_menu()

# database
database = None

# show panel
main_lbox = Listbox(width=v.width_listbox, height=v.height_listbox)
main_lbox.pack(side=LEFT)

# tools panel
tools_label = Label(text="tools", width=v.width_tools, bg="red")
tools_label.pack(side=TOP)

tool_frame = Frame(root, bg='cyan')
tool_frame.pack(side=TOP)

show_tables_tool()


root.mainloop()
