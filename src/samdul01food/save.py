import requests
import json

def food_api(name):
    name = "햄버거"
    headers = {
        'accept': 'application/json',
    }

    params = {
        'name': name,
    }

    response = requests.get('http://127.0.0.1:8000/food', params=params, headers=headers)

    data = json.loads(response.text)
    print(data)
    return data

get_api(햄버거)


