import fire
from httpx import get


def high():
    response = get('https://economia.awesomeapi.com.br/json/all/USD').json()
    return response['USD']['high']


fire.Fire(high)