def init_insert_parser(file):  # парсеры написаны исходя из логики построения запроса инсерта
    #                               # которые описаны в queries
    output = []
    # storage = ('Students', 'Courses', 'Schedule', 'Groups')
    f = open(file, 'r', encoding='utf-8')
    id = -1
    if file == 'data/Students.txt':  # верну список кортежей вида: (ид, имя, фамилия)
        data = f.read()  # все прочитали
        text = data.split('\n')  # поделили строки
        for line in text:
            if len(line):
                if line.find(' ') + 1:  # проверяем имя фамилия ли это, .find() вернет -1 если не нашел пробел
                    tmp = line.split(' ')
                    output.append((id, tmp[0], tmp[1]))
                else:
                    id += 1
    elif file == 'data/Schedule.txt':  # TO DO
        pass
    else:  # верну список с названием курсов или групп
        data = f.read()
        tmp = data.split('\n')
        output = tmp
    return output

def personal_info_parser(file):
    f = open(file, 'r')
    data = f.read()
    tmp = data.split('\n')
    return tmp
