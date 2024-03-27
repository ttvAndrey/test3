
import telebot
import requests
#from wordgame import get_word, get_hidden_word
import re 
from getwhaether import get_weather, WEATHER_API_KEY

bot = telebot.TeleBot(
    token="6441965213:AAEoatSNwCF6M_nHkDsUBHW6MUtKLMzC3Ts"
)

Get_city = False


@bot.message_handler(commands=["weather"])
def weather(message):
    global Get_city         
    bot.send_message(message.chat.id, "Отправьте название города!")
    Get_city = True


@bot.message_handler(func=lambda message: True)
def check(message):
    if Get_city:
        city = message.text
        answer = get_weather(city)
        print(answer)
        current = answer["current"]
        temp_c = current["temp_c"]
        bot.send_message(message.chat.id, temp_c)
        location = answer["location"]
        localtime = location["localtime"]
        bot.send_message(message.chat.id, localtime)
        current = answer["current"]
        condition = current["condition"]
        text = condition["text"]
        icon = condition["icon"]
        is_day = current["is_day"]
        
        # Uncomment the line below to send the downloaded image to the user
        download_and_send_image(bot, message.chat.id, icon, text, message.chat.id)
        
        if is_day == 1:
            bot.send_message(message.chat.id, "Сейчас день")
        else:
            bot.send_message(message.chat.id, "Сейчас ночь")
    else:
        bot.send_message(message.chat.id, "Привет!")


# Function to download an image from a URL and send it to the user
def download_and_send_image(bot, chat_id, image_url, text, message_id):
    try:
        response = requests.get("https:" + image_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        bot.send_message(chat_id, f"Ошибка при загрузке изображения: {str(e)}")
        return

    if response.status_code == 200:
        # Send the photo with caption
        bot.send_photo(chat_id, response.content, caption=text)
    else:
        bot.send_message(chat_id, "Ошибка при загрузке изображения")
