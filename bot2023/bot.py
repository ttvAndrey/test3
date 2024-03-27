import telebot
from wordgame import get_word, get_hidden_word
import re 
from constante import LEVELS

def has_cyrillic(text):
    return bool(re.search("[а-яА-Я]", text)) and len(text) == 1


token = "6904216016:AAFzJRnLGrZR36YtWk2OuQnqLOIM4dHNhTg"


class Bot(object):
    def __init__(self, token: str):
        self.bot = telebot.TeleBot(token)
        self.word = ""
        self.letters = []
        self.level = None
        @self.bot.message_handler(commands=["start"])
        def start(message):
            self.bot.send_message(message.chat.id, "Привет")

        @self.bot.message_handler(commands=["help"])
        def help(message):
            self.bot.send_message(
                message.chat.id,
                "Добро пожаловать в игру угадай слово! \nПравила этой игры просты:\n 1 нужно выбрать сложность уровня\n 2 нужно выбрать сколько тгр вы хотите сыграть\n 3 сыграть ещё раз и ещё раз",
            )

        @self.bot.message_handler(commands=["play"])
        def play(message):
            if self.level is None:
                self.bot.send_message(message.chat.id,
                    f"Введите уровень сложности: {list(LEVELS.keys())}!"
                    )
                return
            if self.word != "":
                self.bot.send_message(
                    message.chat.id,
                    "Вы уже играете, но если хотите сначало то нажмите на кнопку /restart",
                )
                return
            self.word = get_word()
            self.popitka=get_popitka(self.word, self.level)
            self.hidden_word = get_hidden_word(self.word)
            self.bot.send_message(message.chat.id, f"У вас есть {self.popitka} попыток")
            self.bot.send_message(message.chat.id, self.hidden_word)

        @self.bot.message_handler(commands=["restart"])
        def restart(message):
            self.word = ""
            self.hidden_word = ""
            self.letters = []
            self.popitka = 0
            self.level = None
        def check_level(message):
            if len(message.text)>2:
                return True
            return False
        def get_popitka(word: str, level: str) -> int:
            return len(word) + LEVELS[level]

        @self.bot.message_handler(func=lambda message: check_level(message))
        def set_level(message):
            if self.level is not None:
                return
            if message.text in LEVELS.keys():
                self.level=message.text
                self.bot.send_message(message.chat.id,
                    f"Ваш уровень сложности {self.level}, запустите игру нажав /play"
                    )
            else:
                self.bot.send_message(message.chat.id,
                    "Вы ввели не правильный уровень сложности"
                    )

        @self.bot.message_handler(func=lambda message: True)
        def check(message):
            if  self.level is None:
                return
            if has_cyrillic(message.text):
                self.bot.send_message(message.chat.id, "ok")
                print(message.text)
                oshibka = False
                l = message.text
                if l in self.letters:
                    self.bot.send_message(
                        message.chat.id, "Вы уже использовали эту букву!"
                    )
                    return
                if l in self.word:
                    self.bot.send_message(message.chat.id, "Вы угадали букву!")
                    for i, x in enumerate(self.word):
                        if x == l:
                            self.hidden_word = (
                                self.hidden_word[0:i] + l + self.hidden_word[i + 1 :]
                            )
                    self.bot.send_message(message.chat.id, self.hidden_word)
                else:
                    self.bot.send_message(message.chat.id, "Вы не угадали!")
                    oshibka = True
                    self.popitka-=1
                self.letters.append(l)
                if self.word == self.hidden_word:
                    self.bot.send_message(message.chat.id, "Вы победили!!!!")
                if self.popitka==0:
                    self.bot.send_message(message.chat.id, "Вы проиграли!!!!\n Хотите сыграть ещё нажмите на кнопку /restart")
            else:
                self.bot.send_message(message.chat.id, "Вы ввели не коректный текст!")


bot = Bot(token).bot
bot.infinity_polling()
