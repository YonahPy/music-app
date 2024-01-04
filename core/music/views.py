from django.shortcuts import render
import requests


def search_tracks(request):
    search = 'eminem'
    
    r = requests.get(f'https://api.jamendo.com/v3.0/tracks/?client_id=4241b06f&format=jsonpretty&limit=all&imagesize=600&audioformat=mp32&search={search}')

    response = r.json()
    print(response)
    
def albuns(request):
    artist_name = ''
    r = requests.get(f'https://api.jamendo.com/v3.0/albums/tracks/?client_id=4241b06f&format=jsonpretty&imagesize=600&audioformat=mp32&artist_name={artist_name}')

    response = r.json()
    print(response)
    
def artists(request):
    artist_name = ''
    r = requests.get(f'https://api.jamendo.com/v3.0/artists/tracks/?client_id=4241b06f&format=jsonpretty&order=popularity_total&namesearch={artist_name}&imagesize=600&audioformat=mp32')

    response = r.json()
    print(response)