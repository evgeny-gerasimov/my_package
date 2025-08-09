import requests


def get_url(url: str) -> str:
    response = requests.get(url, timeout=10)
    return response.text
