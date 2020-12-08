table_names = frozenset(('Student', 'Group', 'Schedule', 'Course'))

create_table_students_query = """
create table Students
(
	id serial primary key,
	groupID integer,
	name varchar(15),
	surname varchar(15),
	classes_number integer,
	foreign key (groupID) references Groups (id)
);
"""

create_table_groups_query = """
create table Groups
(
	id serial primary key,
	name varchar(30) check (name is not null)
);
"""

create_table_schedule_query = """
create table Schedule
(
	groupID integer,
	weekday varchar(20),
	daytime integer check (daytime >= 0 and daytime <= 8),
	courseID integer,
	type varchar(8),
	audience varchar(8),
	lecturer text,
	constraint couple primary key (groupID, weekday, daytime),
	foreign key (courseID) references Courses (id)
);
"""

create_table_courses_query = """
create table Courses
(
	id serial primary key,
	name text
);
"""

####### INIT INSERT SQL

insert_groups = '''
CREATE OR REPLACE
        FUNCTION insert_Groups(id integer,name varchar(30) )
        RETURNS void AS $$
        BEGIN
		insert into Groups values(id, name);
        END;
        $$ LANGUAGE plpgsql;
'''

insert_students = '''
CREATE OR REPLACE
        FUNCTION insert_Students(id integer, groupID integer, name varchar(20), surname varchar(20), classes_number integer)
        RETURNS void AS $$
        BEGIN
		insert into Students values(id, groupID, name, surname, classes_number);
        END;
        $$ LANGUAGE plpgsql;
'''

insert_courses = '''
CREATE OR REPLACE
        FUNCTION insert_Courses(id integer,name varchar(30) )
        RETURNS void AS $$
        BEGIN
		insert into Courses values(id, name);
        END;
        $$ LANGUAGE plpgsql;
'''

insert_schedule = '''
CREATE OR REPLACE
        FUNCTION insert_Schedule(groupID integer, weekday varchar(20), daytime integer, courseID integer, type varchar(8), audience varchar(8), lecturer text)
        RETURNS void AS $$
        BEGIN
		insert into Schedule values(groupID, weekday, daytime, courseID, type, audience, lecturer);
        END;
        $$ LANGUAGE plpgsql;
'''

total_insert = [insert_courses, insert_groups, insert_students, insert_schedule]

for i in range(len(total_insert)):
    total_insert[i] = total_insert[i].replace("\n", "")


#######

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
