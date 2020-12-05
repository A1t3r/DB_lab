def init_insert_parser(file):  # парсеры написаны исходя из логики построения запроса инсерта
    #                               # которые описаны в queries
    output = []
    # storage = ('Students', 'Courses', 'Schedule', 'Groups')
    f = open(file, 'r', encoding='utf-8')
    id = -1
    data = f.read()  # все прочитали
    text = data.split('\n')  # поделили строки
    text.pop(0)  # убрали описание
    if file == 'data/Students.txt':  # верну список кортежей вида: (ид, имя, фамилия)
        for line in text:
            if len(line):
                if line.find(' ') + 1:  # проверяем имя фамилия ли это, .find() вернет -1 если не нашел пробел
                    tmp = line.split(' ')
                    output.append((id, tmp[0], tmp[1]))
                else:
                    id += 1
    elif file == 'data/Schedule.txt':
        for line in text:
            if len(line):
                tmp = line.split(' ')
                t1 = tuple(tuple(tmp[:-4]))  # сейчас будут махинации, чтобы последние строчки идентифицировать как одну
                tmpstr = ' '
                tmpstr = tmpstr.join(tmp[-4:])  # это последние 4
                tmp = tmp[:-4]
                tmp.append(tmpstr)  # сделали объединение в один лист и конвертим в кортеж
                output.append(tuple(tmp))
    else:
        output = text
    return output

def personal_info_parser(file):
    f = open(file, 'r')
    data = f.read()
    tmp = data.split('\n')
    return tmp
