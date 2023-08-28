from pprint import pprint

import requests as req
import json
import config
from config import API

headers = config.authorize("65672d2975774ae5a02e3d6f07601576", "1c34205ae1a347c0825d88ee6ef97849")


def get_artist(artist_id):
    url = API + f"artists/{artist_id}"

    response = req.get(url, headers=headers).json()
    if "error" in response:
        error_message = response["error"]
        print("Erro encontrado:", error_message)
        exit()
    else:
        return response


def get_episodesfromshow(show_id, country_code="BR", limit=200):
    url = API + f"shows/{show_id}/episodes?market={country_code}&limit={limit}"

    response = req.get(url, headers=headers).json()
    if "error" in response:
        error_message = response["error"]
        print("Erro encontrado:", error_message)
        exit()
    else:
        return response


if __name__ == '__main__':
    orvalho = "1ONoMgsO9VQDbJxnNmTlLw"

    response = dict(get_episodesfromshow(orvalho))
    print(response)
    for i in response["items"]:
        print(i["name"])