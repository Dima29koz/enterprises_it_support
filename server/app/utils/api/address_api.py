import requests

from server.app.utils.api.keys import key_dadata


def get_address_data(address: str) -> list:
    req = f'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address'
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token {key_dadata}",
    }
    data = '{ "query": "' + address + '" }'
    res = requests.post(req, headers=headers, data=data.encode('utf-8'))
    try:
        return res.json().get('suggestions')
    except Exception:
        return []
