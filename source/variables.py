# root
width_root = 600
height_root = 400

# listbox
width_listbox = 100
height_listbox = 20

# tools
width_tools = 25
tl_button_width = 9
tl_frame_pad = 3

# database
db_base_name = 'postgres'
db_name = 'schedule'
db_username = 'postgres'
db_password = '123'
db_host = 'localhost'

# create database
cd_label_width = 15
cd_entry_width = 20
cd_names = ['Database name', 'Username', 'Password', 'Host']
cd_pad = 10

# show data
sd_name_color = "gray0"
sd_item_text_color = "gray6"
sd_item_even = "gray85"
sd_item_odd = "gray97"

# tables
table_names = ['Students', 'Groups', 'Schedule', 'Courses']
table_column_names = {
'Students': ['id',
	'groupid',
	'surname',
	'name',
	'classes_number'],
    'Groups': ['id',
	'title'],
    'Schedule': ['groupid',
	'weekday',
	'daytime',
	'courseid',
	'type',
	'audience',
	'lecturer'],
    'Courses': ['id',
	'name']
}
