table_names = frozenset(('Student', 'Group', 'Schedule', 'Course'))

create_table_student_query = """
create table Student
(
	id serial primary key,
	groupID integer,
	name varchar(15),
	surname varchar(20),
	classes_number integer,
	foreign key (groupID) references Group (id)
);
"""

create_table_group_query = """
create table Group
(
	id serial primary key,
	name text check (name is not null)
);
"""

create_table_schedule_query = """
create table Schedule
(
	groupID integer,
	weekday string,
	time time,
	courseID integer,
	audience varchar(4),
	lecturer text
	constraint couple primary key(group, weekday, time),
	foreign key (courseID) references Course (id)
);
"""  # !!!!!!!!!!!!!!!!!!!!!! тип поля time: time / numeric

create_table_course_query = """
create table Course
(
	id serial primary key,
	name text
);
"""


def insert_into_student(values, id):
    query = "insert into Student (id, groupID, name, surname) values"
    buf = ''
    for item in values:
        query += (buf + " (" + str(id) + ", " + item[0] + ", " + item[1] +
                  ", " + item[2] + ")")
        buf = ','
        id += 1
    return query


def insert_into_group(values, id):
    query = "insert into Group (id, name) values"
    buf = ''
    for item in values:
        query += buf + " (" + str(id) + ", " + item[0] + ")"
        buf = ','
        id += 1
    return query


def insert_into_schedule(values, empty=None):
    query = "insert into Student (groupID, weekday, time, courseID, audience, lecturer) values"
    buf = ''
    for item in values:
        query += (buf + " (" + item[0] + ", " + item[1] + ", " + item[2] +
                  ", " + item[3] + ", " + item[4] + ", " + item[5] + ")")
        buf = ','
        id += 1
    return query


def insert_into_course(values, id):
    query = "insert into Course (id, name) values"
    buf = ''
    for item in values:
        query += (buf + " (" + str(id) + ", " + item[0] + ")")
        buf = ','
        id += 1
    return query


def select_all_from(table_name):
    if table_name in table_names:
        return "select * from {}".format(table_name)
    else:
        raise ValueError("Can't select from non-existent table '{}'".format(table_name))


def delete_all_from(table_name):
    if table_name in table_names:
        return "delete from {}".format(table_name)
    else:
        raise ValueError("Can't clear non-existent table '{}'".format(table_name))


insert_dict = {
    'Student': insert_into_student,
    'Group': insert_into_group,
    'Schedule': insert_into_schedule,
    'Course': insert_into_course
}
