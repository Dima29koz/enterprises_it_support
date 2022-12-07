import requests

from server.app.utils.api.keys import key_weather


def get_weather(city_name: str):
    country_code = 'ru'
    limit = 1
    # base = 'http://api.openweathermap.org/'
    base = 'http://127.0.0.1/api_weather/'
    city_req = f'geo/1.0/direct?q={city_name},{country_code}&limit={limit}&appid={key_weather}'
    res = requests.get(base + city_req)
    res_json = res.json()

    lat = res_json[0].get('lat')
    lon = res_json[0].get('lon')
    units = 'metric'
    weather_req = f'data/2.5/weather?lat={lat}&lon={lon}&units={units}&appid={key_weather}'
    res = requests.get(base + weather_req)
    return res.json()
