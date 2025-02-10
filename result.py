import requests

def get_weather(city_name, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=ru'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        city = data.get('name', 'Неизвестно')
        country = data.get('sys', {}).get('country', 'Неизвестно')
        temperature = data.get('main', {}).get('temp', 'Нет данных')
        humidity = data.get('main', {}).get('humidity', 'Нет данных')
        pressure = data.get('main', {}).get('pressure', 'Нет данных')
        weather_description = data.get('weather', [{}])[0].get('description', 'Нет данных')
        wind_speed = data.get('wind', {}).get('speed', 'Нет данных')

        print(f"Погода в {city}, {country}:")
        print(f"Температура: {temperature}°C")
        print(f"Влажность: {humidity}%")
        print(f"Давление: {pressure} гПа")
        print(f"Описание: {weather_description}")
        print(f"Скорость ветра: {wind_speed} м/с")
    else:
        print(f"Ошибка запроса: {response.status_code}, {response.json()}")

if __name__ == "__main__":
    API_key = 'd2da61fb1b13f6c28141e0ea74febf44'
    city_name = input("Введите название города: ")
    get_weather(city_name, API_key)
