import fire
from httpx import get


def dollar():
    response = get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/1').json
    return response


fire.Fire()