from datetime import datetime


def get_id():
    result = 0
    with open('id.csv', 'r') as f:
        result = int(f.readline())
    return result

def plus_id(id):
    id = id + 1
    with open('id.csv', 'w') as f:
        f.write(str(id))


def write(message):
    id = get_id()
    note = f'{id};{datetime.now().strftime("%d.%m.%Y | %H:%M")};{message}\n'
    with open('notes.csv', 'a', encoding='utf-8') as f:
        f.write(note)
    plus_id(id)

def editing(index, message):
    result = ''
    with open('notes.csv', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            item = line.split(';')
            if item[0] == index:
                result += f'{item[0]};{item[1]};{message}'
            else:
                result += f'{item[0]};{item[1]};{item[2]}'
    with open('notes.csv', 'w', encoding='utf-8') as fl:
        fl.write(result)    


def delete(index):
    result = ''
    with open('notes.csv', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            item = line.split(';')
            if item[0] == index:
                continue
            result += f'{item[0]};{item[1]};{item[2]}'
    with open('notes.csv', 'w', encoding='utf-8') as fl:
        fl.write(result)
