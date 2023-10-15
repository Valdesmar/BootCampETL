import requests
import json
import pandas as pd
import openai

from pathlib import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = str(os.getenv('openai_api_key'))

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "Você é um motorista de Vectra B 2.2 2002"
        },
        {
            "role": "user",
            "content": f"Crie uma mensagem para {user['name']} sobre os problemas do VectraB 2.2 2002 (máximo de 150 caracteres)"
        }
        ]
    )
    return completion.choices[0].message.content.strip('\"')


def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })


def update_user(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False


for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated? {success}!")

