table_names = frozenset(('Students', 'Groups', 'Schedule', 'Courses'))
table_symbols_num = {
    'Students': [4, 7, 15, 15, 15],
    'Groups': [4, 30],
    'Schedule': [7, 15, 7, 8, 8, 8, 30],
    'Courses': [4, 50]
}
###### TABLE CREATION QUERIES
create_table_students_query = """
create table Students
(
	id serial primary key,
	groupID integer,
	surname varchar(15),
	name varchar(15),
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
	weekday varchar(15),
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

######## INIT SELECT SQL

selection1 = '''
CREATE or replace
 FUNCTION selection(_tbl_type anyelement)
  RETURNS SETOF anyelement AS
$$
BEGIN
   RETURN QUERY 
   EXECUTE format('SELECT * FROM %%s',
    pg_typeof(_tbl_type));
END;
$$ LANGUAGE plpgsql;
'''


####### INIT INSERT SQL

insertion='''
CREATE or replace
 FUNCTION insertion(tbl text,_values text)
  RETURNS void AS
$$
BEGIN
   EXECUTE format('insert into %%s values(%%s)',
    tbl, _values);
END;
$$ LANGUAGE plpgsql;
'''


###### TRUNCATION

truncation = '''
CREATE or replace
 FUNCTION Truncation(table_ text)
  RETURNS void AS
$$
BEGIN
   EXECUTE format('Truncate %%s CASCADE', table_);
END;
$$ LANGUAGE plpgsql;
'''

### find functions
find_in_s_by_FI='''
CREATE or replace
  FUNCTION search_in_schedule_by_FI(_name text, _surname text)
  RETURNS table(
  	groupID integer,
	weekday varchar(15),
	daytime integer,
	courseID integer,
	type varchar(8),
	audience varchar(8),
	lecturer text
  ) AS
$$
BEGIN
   RETURN QUERY 
   select schedule.groupid, schedule.weekday, schedule.daytime, 
   schedule.courseID, schedule.type, schedule.audience, schedule.lecturer 
   from Schedule, Students where (
	Students.name = _name and Students.surname = _surname
	and Schedule.groupid = Students.groupid);
END;
$$ LANGUAGE plpgsql;
'''