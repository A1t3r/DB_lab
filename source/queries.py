table_names = frozenset(('Student', 'Group', 'Schedule', 'Course'))
###### TABLE CREATION QUERIES
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
######################

######## INIT SELECT SQL ----- NOT TESTED!!!

selection1 = '''
CREATE or replace
 FUNCTION selection(_tbl_type anyelement)
  RETURNS SETOF anyelement AS
$$
BEGIN
   RETURN QUERY 
   EXECUTE format('SELECT * FROM %%s -- pg_typeof returns regtype, quoted automatically',
    pg_typeof(_tbl_type));
END;
$$ LANGUAGE plpgsql;
'''


#######################


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
