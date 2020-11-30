table_names = frozenset(('Student', 'Group', 'Schedule', 'Course'))

create_table_student_query = """
create table Student
(
	id serial primary key,
	groupID integer,
	name varchar(10),
	surname varchar(15),
	classes_number integer,
	foreign key (groupID) references Group (id)
);
"""

create_table_group_query = """
create table Group
(
	id serial primary key,
	name string
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
	lecturer varchar(20)
	constraint couple primary key(group, weekday, time),
	foreign key (courseID) references Course (id)
);
"""  # !!!!!!!!!!!!!!!!!!!!!! тип поля time: time / numeric

create_table_course_query = """
create table Course
(
	id serial primary key,
	name varchar(40)
);
"""


def select_all_from(table_name):
    if table_name in table_names:
        return "select * from {}".format(table_name)
    else:
        raise ValueError("There is no table with name '{}'".format(table_name))


def delete_all_from(table_name):
    if table_name in table_names:
        return "delete from {}".format(table_name)
    else:
        raise ValueError("There is no table with name '{}'".format(table_name))
