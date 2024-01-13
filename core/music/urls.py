from django.urls import path
from . import views

urlpatterns = [
    path('tracks/', views.SearchTracks.as_view(), name='tracks'),
    path('artists/',views.Artists.as_view() ,name='artists'),
    path('albums/', views.Albums.as_view(), name='albums'),
    path('teste/', views.teste, name='teste')
    
]