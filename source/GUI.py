from tkinter import *
from tkinter import messagebox as mb
from database import Database
from sqlalchemy import exc

import variables as v


def show_data(data=[], data_maxlength=[]):
    length = len(data_maxlength)
    for row in data:
        format_string = ""
        for i in range(len(row)):
            buf = str(row[i])
            format_string += buf + " " * (data_maxlength[i] - len(buf)) + "|"
        main_lbox.insert(END, format_string)
    return


def create_database(window, entries, database):
    db_name = entries[0].get()
    db_username = entries[1].get()
    db_password = entries[2].get()
    host = entries[3].get()

    try:
        database[0] = Database(db_name, db_username, db_password, host)
        database[0].create_database(db_name, db_username, db_password, host)
    except exc.ProgrammingError as pe:
        database[0] = None
        answer = mb.askyesno(
            title="Error",
            message="{} \n\nDo you want to connect to database?".format(pe))
        if answer:
            connect_database_def(window, database)
        window.destroy()
        return
    except exc.OperationalError as oe:
        database[0] = None
        mb.showerror(
            "Error",
            "{}".format(oe))
        return

    window.destroy()
    return


def create_database_def(window, database):
    database[0] = Database(v.db_name, v.db_username, v.db_password)
    try:
        database[0].create_database(v.db_name, v.db_username, v.db_password)
    except exc.ProgrammingError as pe:
        database[0] = None
        answer = mb.askyesno(
            title="Error",
            message="{} \n\nDo you want to connect to database?".format(pe))
        if answer:
            connect_database_def(window, database)
        window.destroy()
        return
    window.destroy()
    return


def create_database_window(database):
    if database[0] != None:
        mb.showerror(
            "Error",
            "Database already exists")
        return 1
    window = Toplevel(root)
    window.title("Create database")
    entries = []

    num = 0
    for i in range(len(v.cd_names)):
        Label(window, padx=v.cd_pad, pady=v.cd_pad, text=v.cd_names[i], width=v.cd_label_width).grid(row=i, column=0)
        ent = Entry(window, width=v.cd_entry_width)
        ent.grid(row=i, column=1, padx=v.cd_pad, pady=v.cd_pad)
        entries.append(ent)
        num += 1

    Button(window, text="Create def",
           command=lambda: create_database_def(window, database)).grid(row=num, column=0)
    Button(window, text="Create",
           command=lambda: create_database(window, entries, database)).grid(row=num, column=1,
                                                                            padx=v.cd_pad, pady=v.cd_pad)
    return


def connect_database(window, entries, database):
    pass


def connect_database_def(window, database):
    database[0] = Database(v.db_name, v.db_username, v.db_password)
    try:
        database[0].connect(v.db_name, v.db_username, v.db_password)
    except exc.OperationalError as oe:
        database[0] = None
        mb.showerror(
            "Error",
            "{} \n\n Database does'n exist".format(oe))
        window.destroy()
        return
    window.destroy()
    return


def connect_database_window(database):
    if database[0] != None:
        mb.showerror(
            "Error",
            "Connection already exists")
        return 1
    window = Toplevel(root)
    window.title("Connect database")
    entries = []

    num = 0
    for i in range(len(v.cd_names)):
        Label(window, padx=v.cd_pad, pady=v.cd_pad, text=v.cd_names[i], width=v.cd_label_width).grid(row=i, column=0)
        ent = Entry(window, width=v.cd_entry_width)
        ent.grid(row=i, column=1, padx=v.cd_pad, pady=v.cd_pad)
        entries.append(ent)
        num += 1

    Button(window, text="Connect def", command=lambda: connect_database_def(window, database)).grid(row=num,
                                                                          column=0)
    Button(window, text="Connect",
           command=lambda: create_database(window, entries, database)).grid(row=num, column=1,
                                                                            padx=v.cd_pad, pady=v.cd_pad)
    return


def detele_database(database):
    if database[0] == None:
        mb.showerror(
            "Error",
            "No existing connection"
        )
        return
    answer = mb.askyesno(
        title="Attention",
        message="Do you want to delete database?")
    if answer:
        database[0].delete_database()
        database[0] = None
        return
    return


def fill_tables():
    pass  # there have to be database filling with data


def clear_tables():
    pass


def pack_menu(database):
    db_menu = Menu()
    db_menu.add_command(label="Create", command=lambda: create_database_window(database))
    db_menu.add_command(label="Connect", command=lambda: connect_database_window(database))
    db_menu.add_command(label="Delete", command=lambda: detele_database(database))

    table_menu = Menu()
    table_menu.add_command(label="Fill tables", command=lambda: fill_tables(database))
    table_menu.add_command(label="Clear tables", command=lambda: clear_tables(database))

    main_menu = Menu()
    main_menu.add_cascade(label="Database", menu=db_menu)
    main_menu.add_cascade(label="Tables", menu=table_menu)

    root.config(menu=main_menu)


def root_settings():
    root.title("The most impressive application name")


def show_tables_tool():
    pass


# database
database = [None]

# root
root = Tk()
root_settings()
pack_menu(database)

# show panel
main_lbox = Listbox(width=v.width_listbox, height=v.height_listbox, font=("Courier", 9))
main_lbox.pack(side=LEFT)

# tools panel
tools_label = Label(text="tools", width=v.width_tools, bg="red")
tools_label.pack(side=TOP)

tool_frame = Frame(root, bg='cyan')
tool_frame.pack(side=TOP)

show_tables_tool()

### test block
show_data([['Username', 'years', 'job'], ['vadim', 3, 'waiter'], ['peter', 18, 'jobfree']], [30, 5, 10])

def sdb():
    print(database)
Button(text="show database", command=sdb).pack()
#####

root.mainloop()
