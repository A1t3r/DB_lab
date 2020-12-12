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


# default
def_url = r"data\default.txt"


def db_base_name():
    with open(def_url) as f:
        for line in f:
            values = line.split(sep='#')
            if values[0] == 'db_base_name':
                return values[1]


def db_name():
    with open(def_url) as f:
        for line in f:
            values = line.split(sep='#')
            if values[0] == 'db_name':
                return values[1]


def db_username():
    with open(def_url) as f:
        for line in f:
            values = line.split(sep='#')
            if values[0] == 'db_username':
                return values[1]


def db_password():
    with open(def_url) as f:
        for line in f:
            values = line.split(sep='#')
            if values[0] == 'db_password':
                return values[1]


def db_host():
    with open(def_url) as f:
        for line in f:
            values = line.split(sep='#')
            if values[0] == 'db_host':
                return values[1]


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
                 'name'],
    'Groups': ['id',
               'title',
               'classes_number'],
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
