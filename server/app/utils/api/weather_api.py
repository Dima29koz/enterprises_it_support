import requests

from server.app.utils.api.keys import key_weather


def get_weather(city_name: str):
    country_code = 'ru'
    limit = 1

    city_req = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit={limit}&appid={key_weather}'
    res = requests.get(city_req)
    res_json = res.json()

    lat = res_json[0].get('lat')
    lon = res_json[0].get('lon')
    units = 'metric'
    weather_req = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={units}&appid={key_weather}'
    res = requests.get(weather_req)
    return res.json()
