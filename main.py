import telebot, messages, writer, reader, parse
from secret import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, messages.start)

@bot.message_handler(commands=["add"])
def add(message):
    bot.send_message(message.chat.id, messages.enter_note)
    bot.register_next_step_handler(message, get_note)

def get_note(message):
    note = message.text
    writer.write(note)
    bot.send_message(message.chat.id, messages.save)

@bot.message_handler(commands=["showall"])
def show_all(message):
    msg = reader.get_notes()
    bot.send_message(message.chat.id, msg, parse_mode="HTML")

@bot.message_handler(commands=["show"])
def show(message):
    bot.send_message(message.chat.id, messages.enter_id)
    bot.register_next_step_handler(message, show_note)

def show_note(message):
    note_id = message.text
    msg = reader.get_note(note_id)
    bot.send_message(message.chat.id, msg, parse_mode="HTML")

@bot.message_handler(commands=["del"])
def delete(message):
    bot.send_message(message.chat.id, messages.enter_id)
    bot.register_next_step_handler(message, del_note)

def del_note(message):
    writer.delete(message.text)
    bot.send_message(message.chat.id, messages.deleted) 

@bot.message_handler(commands=["edit"])
def edit(message):
    bot.send_message(message.chat.id, messages.enter_new_note)
    bot.register_next_step_handler(message, edit_note)

def edit_note(message):
    index, msg = parse.message_parser(message.text)
    writer.editing(index, msg)
    bot.send_message(message.chat.id, messages.edited)

bot.infinity_polling()