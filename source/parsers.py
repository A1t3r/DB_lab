def init_insert_parser(file):  # парсеры написаны исходя из логики построения запроса инсерта
    #                               # которые описаны в queries
    output = []
    # storage = ('Students', 'Courses', 'Schedule', 'Groups')
    f = open(file, 'r', encoding='utf-8')
    id = -1
    data = f.read()  # все прочитали
    text = data.split('\n')  # поделили строки
    text.pop(0)  # убрали описание
    num_of_classes = 0
    if file == 'data/Students.txt':  # верну список кортежей вида: (ид, имя, фамилия)
        stud_id = 0
        for line in text:
            if len(line):
                if line.find(' ') + 1:  # проверяем имя фамилия ли это, .find() вернет -1 если не нашел пробел
                    tmp = line.split(' ')
                    output.append((stud_id, id, tmp[0], tmp[1]))
                    stud_id += 1
                else:
                    id += 1
    elif file == 'data/Schedule.txt':  # Верну кортеж вида
        for line in text:  # (id группы|День недели|Номер пары|Тип занятия|Аудитоия|Преподаватель)
            if len(line):
                tmp = tuple(line.split(','))
                output.append(tmp)
                num_of_classes+=1
    else:
        id = 0
        for item in text:
            if(file == 'data/Groups.txt'):
                text[id] = [id, text[id], 9]
            else:
                text[id] = [id, text[id]]
            id += 1
        output = text
    return output


def personal_info_parser(file):
    f = open(file, 'r')
    data = f.read()
    tmp = data.split('\n')
    return tmp

# init_insert_parser("data/Students.txt")
