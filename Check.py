import telebot, os
TOKEN = '1732275777:AAFOivba83GDsB-IHEQfnEdY7seYdKXm-CU'
chatid = '536240230'
tb = telebot.TeleBot(TOKEN)
os.system("echo Hello from the other side!")
tb.send_message(chatid, 'ТЕСТ')
