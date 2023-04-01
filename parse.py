def message_parser(text):
    message_list = text.split()
    index = message_list[0]
    message = ''
    for i in range(1, len(message_list)):
        message += f'{message_list[i]} '
    message += '\n'
    return index, message