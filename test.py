import requests

headers = {
  "Authorization": "Bearer YOUR_TOKEN_HERE"
}

response = requests.get('https://api.tellonym.me/tells?limit=10', headers=headers)

questions = response.json()['tells']

print(questions)

