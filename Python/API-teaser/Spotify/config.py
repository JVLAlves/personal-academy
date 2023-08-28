
import json
import os
import time
import os.path as path
from datetime import datetime

import requests

API = "https://api.spotify.com/v1/"
url_token = "https://accounts.spotify.com/api/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials",
    "client_id": "your-client-id",
    "client_secret": "your-client-secret"
}

autorization_headers = {
    "Authorization": None
}


def authorize(client_scrt, client_id):

    if not path.exists(".token"):

        data["client_secret"] = client_scrt
        data["client_id"] = client_id

        response = requests.post(url_token, headers=headers, data=data)
        token = response.json()
        expires = token["expires_in"]
        print(expires)
        timestmp = to_timestamp(expires)
        token["expires_in"] = timestmp

        writedown_json(token, ".token")
        autorization_headers["Authorization"] = f"Bearer {token['access_token']}"

        return autorization_headers

    else:
        token = read_json(".token")
        print(token["expires_in"])
        expired = timestamp_expired(token["expires_in"])
        if expired:
            print("Token Expirado. Gerando outro...")
            os.remove(".token")
            authorize(client_scrt, client_id)
        else:
            print("Token Valido")
            autorization_headers["Authorization"] = f"Bearer {token['access_token']}"

            return autorization_headers


def writedown_json(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


def read_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data


def to_timestamp(segundos):
    timestamp = time.time() + segundos
    return timestamp


def timestamp_expired(timestmp):
    timestamp = float(timestmp)
    now = time.time()
    print(timestamp)

    print(datetime.strftime(datetime.fromtimestamp(timestmp), '%Y-%m-%d %H:%M:%S'))
    return timestamp < now
