from twython import Twython
import requests

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

url = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'application/json'}
joke_msg = requests.get(url, headers=headers).json().get('joke')
twitter.update_status(status=joke_msg)
print("Tweeted: " + joke_msg)
