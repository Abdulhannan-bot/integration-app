import requests

webhook_url = 'https://engine-api.integration.app/webhooks/app-events/c48fb67c-baa7-48fe-b5ba-ef37925d1017'

user_id = 2
data = {
    'name': 'Alaister Moody',
    'email': 'alistermoody@gmail.com',
    'phone': '1233211234',
    'organization': 'Apple'
}

payload = {
    'user_id': user_id,
    'data': data,
}

response = requests.post(webhook_url, json=payload)

if response.status_code == 200:
    print('Webhook successfully sent!')
else:
    print('Failed to send webhook. Status code:', response.status_code)
