import jwt
import datetime
import requests

WORKSPACE_KEY = "137b950f-aafb-4f4b-870f-0069eae14426"
WORKSPACE_SECRET = "9620d47acc1092abea9639f9131fd9eecc7019d658247558de9032eb31ed6c4f"
webhook_url = 'https://engine-api.integration.app/webhooks/app-events/c48fb67c-baa7-48fe-b5ba-ef37925d1017'

def genrerate_token(client):
    encoded_jwt = jwt.encode(
      {"id": client.id,  # Identifier of user or organization.
        "name": client.user.username,  # Human-readable name (it will simplify troubleshooting)
        "iss": WORKSPACE_KEY,
        # "fields": <user fields value>, # (optional) Any user fields you want to attach to your user.
        "exp": datetime.datetime.now() + datetime.timedelta(seconds=1440)
        }, WORKSPACE_SECRET, algorithm="HS256")
    return encoded_jwt

def send_to_i_app(client, name, phone, email, company_name):
    # encoded_jwt = jwt.encode(
    #   {"id": client.id,  # Identifier of user or organization.
    #     "name": client.user.username,  # Human-readable name (it will simplify troubleshooting)
    #     "iss": WORKSPACE_KEY,
    #     # "fields": <user fields value>, # (optional) Any user fields you want to attach to your user.
    #     "exp": datetime.datetime.now() + datetime.timedelta(seconds=1440)
    #     }, WORKSPACE_SECRET, algorithm="HS256")
    
    data = {
    'name': name,
    'email': email,
    'phone': phone,
    'organization': company_name
    }

    payload = {
        'user_id': client.id,
        'data': data,
    }

    response = requests.post(webhook_url, json=payload)

    if response.status_code == 200:
        print('Webhook successfully sent!')
    else:
        print('User hasnt connected an external app', response.status_code)
    