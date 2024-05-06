from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def teste(request):
    search = 'milamoskovic'
    r = requests.get(f'https://api.jamendo.com/v3.0/tracks/?client_id=4241b06f&format=jsonpretty&limit=all&imagesize=600&audioformat=mp32&search={search}')

    response = r.json()
    
    print(response)

class SearchTracks(APIView):
    
    def get(self, resquest):
        search = resquest.GET.get('search', '')
        boost = resquest.GET.get('boost', '')
        lang = resquest.GET.get('lang', 'en')
        limit = resquest.GET.get('limit', '100')
        id = resquest.GET.get('id', '')
        tags = resquest.GET.get('tags', '')
        offset = resquest.GET.get('offset', '')
        fuzzytags = resquest.GET.get('fuzzytags', '')
        
        try:
            r = requests.get(f'https://api.jamendo.com/v3.0/tracks/?client_id=4241b06f&format=jsonpretty&limit={limit}&imagesize=600&audioformat=mp32&search={search}&boost={boost}&id={id}&tags={tags}&offset={offset}&fuzzytags={fuzzytags}')
            
            if r.status_code == 200:
                response = r.json()
                return Response(response, status=status.HTTP_200_OK)
            
            else:
                Response({'error': 'Failed to fetch data'}, status=r.status_code)
        
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    
class Albums(APIView):
    
    def get(self, request):
        artist_name = request.GET.get('search', '')
        order = request.GET.get('order', '')
        limit = request.GET.get('limit', '100')
        idAlbum = request.GET.get('id', '')
        
        try:
            r = requests.get(f'https://api.jamendo.com/v3.0/albums/tracks/?client_id=4241b06f&format=jsonpretty&limit={limit}&imagesize=600&audioformat=mp32&artist_name={artist_name}&order={order}&id={idAlbum}')

            if r.status_code == 200:
                response = r.json()
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Failed to fetch data'}, status=r.status_code)
            
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
                
    
class Artists(APIView):
    
    def get(self, request):
        artist_name = request.GET.get('search', '')
        order = request.GET.get('order', '')
        limit = request.GET.get('limit', '100')
        
        try: 
            r = requests.get(f'https://api.jamendo.com/v3.0/artists/tracks/?client_id=4241b06f&format=jsonpretty&limit={limit}&order={order}&namesearch={artist_name}&imagesize=600&audioformat=mp32')
            
            if r.status_code == 200:
                response = r.json()
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Failed to fetch data'}, status=r.status_code)
        
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
