"""
API Key: AIzaSyDHcfQ7QtZdk7q37-XGOHOg9SDEefxShos
"""
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle
import pprint
from datetime import *
import os
from pytz import *

def CreateEvent(title:str, duration:str):
    scopes = ["https://www.googleapis.com/auth/calendar.events", "https://www.googleapis.com/auth/calendar"]
    flow = InstalledAppFlow.from_client_secrets_file(
        "google/auth/client_secret_file.json", scopes=scopes)
    if not os.path.exists("google/auth/token.pkl"):
        credentials = flow.run_local_server()
        pickle.dump(credentials, open("google/auth/token.pkl", "wb"))
    else:
        credentials = pickle.load(open("google/auth/token.pkl", "rb"))

    service = build("calendar", "v3", credentials=credentials)
    service_built = service.calendarList().list().execute()
    ID = service_built["items"][0]["id"]


    format_ark = "%B %d, %Y, %H:%M"
    format_duration = "%Y-%m-%dT%H:%M:%S%z"
    dates = duration.replace(" (UTC-7)", "")
    print(dates)
    split_dates = dates.split(" – ")
    print(split_dates)
    start_str = split_dates[0]
    end_str = split_dates[1]

    now = datetime.today()
    start = datetime.strptime(start_str, format_ark)
    start = start.replace(tzinfo=utc)
    end = datetime.strptime(end_str, format_ark)
    end = end.replace(tzinfo=utc)

    now_date = now.astimezone(timezone("America/Sao_Paulo")).strftime(format_duration)
    start_date = start.astimezone(timezone("America/Sao_Paulo")).strftime(format_duration)
    end_date = end.astimezone(timezone("America/Sao_Paulo")).strftime(format_duration)

    event = {
        'summary': f'{title}',
        'location': '',
        'description': '',
        'start': {
            'dateTime': start_date,
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': end_date,
            'timeZone': 'America/Sao_Paulo',
        },
        'attendees': [
            {'email': f'{ID}'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 30},
            ],
        },
    }
    if end.day <= now.day or end.month < now.month or end.year < now.year:
        return False
    else:
        service.events().insert(calendarId=ID, body=event).execute()
        return True