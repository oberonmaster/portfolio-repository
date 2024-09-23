from telebot import *
from DataBase.history import db_history_of_using, history_of_using
from RapidApi.rapidapi_handler import IMDbAPIHandler

def start_new_bot(token):
    bot = telebot.TeleBot(token)

    # Keyboards
    # Клавиатура с основными командами
    start_keyboard = types.InlineKeyboardMarkup(row_width=1)
    top_10_movies_button = types.InlineKeyboardButton(text='Топ 10 фильмов по версиии IMDb', callback_data='top_10_movies',)
    top_10_series_button = types.InlineKeyboardButton(text='Топ 10 сериалов по версиии IMDb', callback_data='top_10_series')
    history_button = types.InlineKeyboardButton(text='Посмотреть историю запросов', callback_data='history')
    help_button = types.InlineKeyboardButton(text='Справка', callback_data='help')
    start_keyboard.add(top_10_movies_button, top_10_series_button, history_button, help_button)

    help_message = "Команда 'Топ 10 фильмов по версиии IMDb' " \
                   "\nПосле ввода команды пользователю выводится 10 лучших фильмов по рейтингу в обратном порядке" \
                   "\n\nКоманда 'Топ 10 сериалов по версиии IMDb' " \
                   "\nПосле ввода команды пользователю выводится 10 лучших сериалов по рейтингу в обратном порядке" \
                   "\n\nКоманда 'Посмотреть историю запросов' " \
                   "\nПосле ввода команды выводится краткая история запросов пользователя (последние десять запросов)"

    def send_top_content(message, content_type):
        """
        Отправляет пользователю топ-10 контента (фильмов или сериалов).
        :param message: Сообщение, на которое нужно ответить.
        :param content_type: Тип контента ('movies' или 'series').
        """
        handler = IMDbAPIHandler(content_type)
        content = handler.get_top_10()

        if content:
            for item in content:
                # Отправляем картинку контента
                if item['image_url']:
                    bot.send_photo(message.chat.id, item['image_url'])

                # Отправляем сообщение с названием, рейтингом и описанием
                content_text = f"{item['title']} - Rating: {item['rating']}\n\n{item['description']}"
                bot.send_message(message.chat.id, content_text)
        else:
            bot.send_message(message.chat.id, f"Не удалось получить список {content_type}. Попробуйте позже.")

        db_history_of_using(message.chat.id, content_type)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, "Привет! Я помогу тебе выбрать фильм или сериал на вечер по рейтингу IMBd! Что ты хочешь посмотреть?",
                         reply_markup=start_keyboard)

    @bot.message_handler(commands=['top_10_movies'])
    def send_top_10_movies(message):
        send_top_content(message, 'movies')

    @bot.message_handler(commands=['top_10_series'])
    def send_top_10_series(message):
        send_top_content(message, 'series')

    @bot.message_handler(commands=['history'])
    def send_history(message):
        history = history_of_using(message.chat.id)
        bot.send_message(message.chat.id, history)
        db_history_of_using(message.chat.id, 'history')

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.send_message(message.chat.id, help_message)

    @bot.message_handler(func=lambda message: True)
    def handle_unknown_command(message):
        bot.send_message(message.chat.id, "Я тебя не понимаю. Используй /start.")

    @bot.callback_query_handler(func=lambda call: True)
    def get_callback_message(call):
        if call.data == "top_10_movies":
            send_top_content(call.message, 'movies')
        elif call.data == "top_10_series":
            send_top_content(call.message, 'series')
        elif call.data == "history":
            send_history(call.message)
        elif call.data == "help":
            send_help(call.message)
        else:
            bot.send_message(call.message.chat.id, "Я тебя не понимаю. Используй /start.")

    bot.polling(none_stop=True)
