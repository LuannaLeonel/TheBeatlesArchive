import requests
from random import randint

'''
Python script that returns a random Beatles song!

Using the the-beatles-api to get the songs data
https://github.com/vrandall66/the-beatles-api

'''
try:
    songs = requests.get("https://the-beatles-api.herokuapp.com/api/v1/songs").json()
    random_number = randint(0, len(songs))
    song = songs[random_number]
    print(f'Today you should listen "{song.get("trackName")}"!')
except expression as identifier:
    print("Something went wrong...")
