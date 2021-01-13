import json
import os
import redis
import requests
import schedule
import time

APP_NAME = "music-client"
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
USER = "Abspen1"


API_ROOT = "http://ws.audioscrobbler.com/2.0/"

TOKEN = f"{API_ROOT}?method=auth.gettoken&api_key={API_KEY}&format=json"

RECENT_TRACKS = f"{API_ROOT}?method=user.getrecenttracks&user=rj&api_key={API_KEY}&format=json"

# "?method=user.getrecenttracks&user={USER}&api_key={API_KEY}&format=json"

########## Sleeper API Functions ###########


def get_token():
    r = requests.get(TOKEN)
    return json.loads(r.content)


def get_recent_tracks():
    payload = {'limit': 1, 'user': 'Abspen1', 'api_key': API_KEY}
    r = requests.get(RECENT_TRACKS, params=payload)
    return json.loads(r.content)


def main():
    jsonData = get_recent_tracks()
    data = jsonData['recenttracks']['track']
    for item in data:
        print(item['name'])
        print(item['artist']['#text'])


if __name__ == "__main__":
    main()

# schedule.every().day.at("06:00").do(main)

# while True:
#     try:
#         schedule.run_pending()
#         time.sleep(1)
#     except Exception as identifier:
#         print(identifier)
#         time.sleep(1)
