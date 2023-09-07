import requests
import json
import pandas as pd

# from flask import Flask, jsonify, request

url = 'https://jsonplaceholder.typicode.com'


def get_id(id):
    response = requests.get(f'{url}/posts/{id}')
    return response.json() if response.status_code == 200 else False


def update_user(user):
    ...


user1 = json.dumps(get_id(1), indent=2)

print(user1)


url1 = 'http://127.0.0.1:5000'
response1 = requests.get(url1)

print(response1.content)

