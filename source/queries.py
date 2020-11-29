table_names = frozenset(('Student', 'Group', 'Schedule', 'Course'))

create_table_student_query = """
to do
"""

create_table_group_query = """
to do
"""

create_table_schedule_query = """
to do
"""

create_table_course_query = """
to do
"""


def select_all_from(table_name):
    if table_name in table_names:
        return "select * from {}".format(table_name)
    else:
        raise ValueError("There is no table with name '{}'".format(table_name))
