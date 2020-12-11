from tkinter import *
from tkinter import messagebox as mb
from database import Database
from sqlalchemy import exc
from tkinter.ttk import Combobox
from queries import table_symbols_num

import variables as v


def show_data(data=[], data_maxlength=[], inplace=True):
    if inplace:
        main_lbox.delete(0, END)

    length = len(data_maxlength)
    amount = len(data)
    for row in data:
        format_string = ""
        for i in range(len(row)):
            buf = str(row[i])
            format_string += buf + " " * (data_maxlength[i] - len(buf)) + " "
        main_lbox.insert(END, format_string)

    # recoloring
    if amount >= 1:
        main_lbox.itemconfig(0, fg=v.sd_name_color)

    num = 1
    while num < amount:
        main_lbox.itemconfig(num, bg=v.sd_item_even, fg=v.sd_item_text_color)
        num += 2

    num = 2
    while num < amount:
        main_lbox.itemconfig(num, bg=v.sd_item_odd, fg=v.sd_item_text_color)
        num += 2

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
        show_data()
        return
    return


def reload_tables(database):
    if database[0] == None:
        mb.showerror("Error", "Connection doesn't exist")
        return

    database[0].reload()
    return


def clear_tables(database):
    if database[0] == None:
        mb.showerror("Error", "Connection doesn't exist")
        return

    database[0].clear_all_table()
    show_data()
    return


def update_window(database):
    if database[0] == None:
        mb.showerror("Error", "Connection doesn't exist")
        return
    database[0]._create_procedures()
    return


def pack_menu(database):
    db_menu = Menu()
    db_menu.add_command(label="Create", command=lambda: create_database_window(database))
    db_menu.add_command(label="Connect", command=lambda: connect_database_window(database))
    db_menu.add_command(label="Update procedures", command=lambda: update_window(database))
    db_menu.add_command(label="Delete", command=lambda: detele_database(database))

    table_menu = Menu()
    table_menu.add_command(label="Reload data", command=lambda: reload_tables(database))
    table_menu.add_command(label="Clear tables", command=lambda: clear_tables(database))

    main_menu = Menu()
    main_menu.add_cascade(label="Database", menu=db_menu)
    main_menu.add_cascade(label="Tables", menu=table_menu)

    root.config(menu=main_menu)


def root_settings():
    root.title("The most impressive application name")
    root.resizable(width=False, height=False)


# database
database = [None]

# root
root = Tk()
root_settings()
pack_menu(database)

# show panel
main_lbox = Listbox(width=v.width_listbox, height=v.height_listbox, font=("Courier", 9), selectmode=MULTIPLE)
main_lbox.pack(side=LEFT)


# ------------------------- tool functions ------------------------- #
def show_tools(tool_frame, database, main_lbox):
    Button(tool_frame, text='Show', width=v.tl_button_width, command=lambda: show_table(show_combox, database)).grid(row=0, column=0)
    show_combox = Combobox(tool_frame)
    show_combox['values'] = ('', 'Students', 'Groups', 'Schedule', 'Courses')
    show_combox.current(0)
    show_combox.grid(row=0, column=1)

    Button(tool_frame, text='Clear', width=v.tl_button_width, command=lambda: clear_table(clear_combox, database)).grid(row=1, column=0)
    clear_combox = Combobox(tool_frame)
    clear_combox['values'] = ('', 'Students', 'Groups', 'Schedule', 'Courses')
    clear_combox.current(0)
    clear_combox.grid(row=1, column=1)

    Button(tool_frame, text='Add', width=v.tl_button_width, command=lambda: add2_table(add_combox, database)).grid(row=2, column=0)
    add_combox = Combobox(tool_frame)
    add_combox['values'] = ('', 'Students', 'Groups', 'Schedule', 'Courses')
    add_combox.current(0)
    add_combox.grid(row=2, column=1)

    Button(tool_frame, text='Delete', width=v.tl_button_width, command=lambda: delete_data(main_lbox, database)).grid(row=3, column=0)
    chosen_label = Label(tool_frame, text="chosen: 0")
    chosen_label.grid(row=3, column=1)


def show_table(combox, database):
    table_name = combox.get()
    if table_name == "":
        return

    if table_name not in v.table_names:
        mb.showerror("Error", "{} doesn't exist".format(table_name))
        return

    if database[0] == None:
        mb.showerror("Error", "No connected database")
        return

    show_data(database[0].get_table(table_name), table_symbols_num[table_name])
    return


def clear_table(combox, database):
    table_name = combox.get()
    if table_name == "":
        return

    if table_name not in v.table_names:
        mb.showerror("Error", "{} doesn't exist".format(table_name))
        return

    if database[0] == None:
        mb.showerror("Error", "No connected database")
        return

    database[0].clear_table(table_name)

    show_data()
    return


def add2_database(window, entries, database, table_name):  # have to be finished!!!!!!!!!!!!!!!!!!
    values = []
    for item in entries:
        values.append(item)

    database[0].insert_into(table_name, values)
    show_data(database[0].get_table(table_name), table_symbols_num[table_name])
    window.destroy()
    return


def add2_table(combox, database):
    table_name = combox.get()
    if table_name == "":
        return

    if table_name not in v.table_names:
        mb.showerror("Error", "{} doesn't exist".format(table_name))
        return

    if database[0] == None:
        mb.showerror("Error", "No connected database")
        return

    window = Toplevel(root)
    window.title("Add to {}".format(table_name))
    entries = []

    number = len(v.table_column_names[table_name])
    num = 0
    for i in range(1, number):
        Label(window, padx=v.cd_pad, pady=v.cd_pad, text=v.table_column_names[table_name][i],
              width=v.cd_label_width).grid(row=i-1, column=0)
        ent = Entry(window, width=v.cd_entry_width)
        ent.grid(row=i-1, column=1, padx=v.cd_pad, pady=v.cd_pad)
        entries.append(ent)
        num += 1

    Button(window, text="Add",
           command=lambda: add2_database(window, entries, database, table_name)).grid(row=num, column=1,
                                                                            padx=v.cd_pad, pady=v.cd_pad)
    return


def delete_data(main_lbox, database):
    pass
######################################################################

# tools panel
tools_label = Label(text="tools", width=v.width_tools)
tools_label.pack(side=TOP)

tool_frame = Frame(root, padx=v.tl_frame_pad, pady=v.tl_frame_pad)
tool_frame.pack(side=TOP)

show_tools(tool_frame, database, main_lbox)

### test block
show_data([['Username', 'years', 'job'], ['vadim', 3, 'waiter'], ['peter', 18, 'jobfree'],
           ['vadim', 3, 'waiter'], ['peter', 18, 'jobfree']], [30, 5, 10])


def sdb():
    print(database)


Button(text="show database", command=sdb).pack()
#####

root.mainloop()
