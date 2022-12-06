import requests

from server.app.utils.api.keys import key_dadata


def get_bank_data(query: str):
    req = f'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/bank'
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token {key_dadata}",
    }
    data = '{ "query": "' + query + '" }'
    res = requests.post(req, headers=headers, data=data)
    try:
        return res.json().get('suggestions')[0]
    except Exception:
        return {'data': None}
