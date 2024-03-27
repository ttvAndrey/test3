import requests
city=input("Введите названия города!\n")
print(f"{city} это самый лчший город на земле!")
# url="https://books.toscrape.com/"
# response=requests.get(url)
# print(response.text)
open_token="319a5bf65a1011e0e506786796e8e69e"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_token}&units=metric&lang=ru"
response=requests.get(url)
print(response.text)