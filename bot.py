import telebot
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from logic import gen_pass


TOKEN = "TOKEN"



bot = telebot.TeleBot(TOKEN) #объект бота, через которого мы будем работать

class UserStates(StatesGroup):
    MAIN = State()
    MENU = State()
    NAME = State()
    PHONE = State()




@bot.message_handler(commands=['start', 'hello'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот, который поможет тебе.')
    text = ""
    for i in list: text += i
    bot.send_message(message.chat.id, text)
    bot.set_state(message.from_user.id, UserStates.MAIN, message.chat.id)

@bot.state_handlers(UserStates.MAIN)
def main(message, state):
    bot.send_message(message.chat.id, 'Выбери действие:')
    bot.send_message(message.chat.id, '1. Сгенерировать Имя')
    bot.send_message(message.chat.id, '2. Сгенерировать Телефон')
    bot.set_state(message.from_user.id, UserStates.MENU, message.chat.id)

@bot.state_handlers(UserStates.MENU)
def menu(message, state):
    if message.text == '1':
        bot.set_state(message.from_user.id, UserStates.NAME, message.chat.id)
    else:
        bot.send_message(message.chat.id, 'Выбери действие:')
        bot.send_message(message.chat.id, '1. Сгенерировать Имя')
        bot.send_message(message.chat.id, '2. Сгенерировать Телефон')
        bot.set_state(message.from_user.id, UserStates.MENU, message.chat.id)





@bot.message_handler(commands=['gen_pass'])
def gen_pass_handler(message):
    pass

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text == 'пока':
        bot.send_message(message.chat.id, 'Пока!')
    else:
        bot.send_message(message.chat.id, f"Я прочитал: {message.text}")

@bot.message_handler(content_types=['photo'])
def send_photo(message):
    bot.send_message(message.chat.id, 'Прикольная фотка!')

@bot.message_handler(content_types=['video'])
def send_video(message):
    bot.send_message(message.chat.id, 'Интересное видео!')

@bot.message_handler(content_types=['voice'])
def send_audio(message):
    bot.send_message(message.chat.id, 'Классный голос!')







bot.polling() #запуск бота - всегда в конце
