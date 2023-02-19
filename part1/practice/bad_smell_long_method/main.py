# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def base():
    data = _read(csv)
    sort_data = _sort(data)
    result = _filter(sort_data)
    return result

def _read(csv):
    spisok = csv.split('\n')
    return [i.split(';') for i in spisok]

def _sort(data):
    return sorted(data, key=lambda x: int(x[1]))

def _filter(data):
    z = []
    for i in data:
        if int(i[1]) > 10:
            z.append(i)
    return z


if __name__ == '__main__':
    print(base())
