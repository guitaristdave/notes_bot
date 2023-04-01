
def get_notes():
    result = ''
    with open('notes.csv', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            item = line.split(';')
            result += f'<b>id:</b> {item[0]}\n<b>Дата:</b> {item[1]}\n<b>Заметка:</b> {item[2]}---\n'
    return result
    

def get_note(id):
    result = ''
    with open('notes.csv', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            item = line.split(';')
            if item[0] == id:
                result += f'<b>id:</b> {item[0]}\n<b>Дата:</b> {item[1]}\n<b>Заметка:</b> {item[2]}'
    if result == '':
        return 'Заметка не найдена'
    else:
        return result
    
