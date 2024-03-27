WEATHER_API_KEY = "9821b007e4ee4e798dc83436231012"
import requests

def get_weather(city):
    """Функция для получения погоды по городу."""
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&lang=ru"
    response = requests.get(url).json()
    #return response
    current = response['current']
    condition = current['condition']['text']
    temp_c = current['temp_c']
    return f"Погода в {city}: {condition}, температура: {temp_c}°C"
if __name__=="__main__":
    # print(get_weather("Moscow"))
    a=get_weather("Dmitrovo")
    print(type(a))
    import json
    with open (r"C:\Users\Админ\Desktop\Python\Словари и json\погода в москве.json","w",encoding="utf-8") as f:
        json.dump(a,f)
        print(a.keys())
        b=a["current"]
        print(b.keys())
        print(b["temp_c"])