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
        
        try:
            r = requests.get(f'https://api.jamendo.com/v3.0/tracks/?client_id=4241b06f&format=jsonpretty&limit=all&imagesize=600&audioformat=mp32&search={search}')
            
            if r.status_code == 200:
                response = r.json()
                return Response(response, status=status.HTTP_200_OK)
            
            else:
                Response({'error': 'Failed to fetch data'}, status=r.status_code)
        
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    
class Albuns(APIView):
    
    def get(self, request):
        artist_name = request.GET.get('search', '')
        
        try:
            r = requests.get(f'https://api.jamendo.com/v3.0/albums/tracks/?client_id=4241b06f&format=jsonpretty&imagesize=600&audioformat=mp32&namesearch={artist_name}')

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
        
        try: 
            r = requests.get(f'https://api.jamendo.com/v3.0/artists/tracks/?client_id=4241b06f&format=jsonpretty&order=popularity_total&namesearch={artist_name}&imagesize=600&audioformat=mp32')
            
            if r.status_code == 200:
                response = r.json()
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Failed to fetch data'}, status=r.status_code)
        
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
