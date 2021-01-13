import json
import os
import redis
import requests
import schedule
import time

APP_NAME = "music-client"
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
USER = os.getenv("USER")

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


def recent():
    jsonData = get_recent_tracks()
    data = jsonData['recenttracks']['track']

    # Only runs once since we have limit of 1 on the call
    for item in data:
        name = item['name']
        artist = item['artist']['#text']
        image = item['image']
        for value in image:
            if value['size'] == 'medium':
                img = value['#text']

    dictionary = {"Name": name, "Artist": artist, "Image": img}
    return dictionary


def check_recent():
    current = recent()
    client = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379, db=11,
                         password=os.getenv("REDIS_PASS"))

    name = client.hget('current-track', 'Name').decode('utf-8')
    artist = client.hget('current-track', 'Artist').decode('utf-8')
    img = client.hget('current-track', 'Image').decode('utf-8')

    if name == current['Name'] and artist == current['Artist'] and img == current['Image']:
        print(f"{USER} hasn't listened to music in the past hour")
        return
    print('doing the update')
    # Do the update to README and update current


def init():
    client = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379, db=11,
                         password=os.getenv("REDIS_PASS"))
    current = recent()
    client.hset('current-track', 'Name', current['Name'])
    client.hset('current-track', 'Artist', current['Artist'])
    client.hset('current-track', 'Image', current['Image'])
    print(current)


if __name__ == "__main__":
    init()
    check_recent()

schedule.every().hour.do(check_recent)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as identifier:
        print(identifier)
        time.sleep(1)
