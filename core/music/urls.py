from django.urls import path
from . import views

urlpatterns = [
    path('tracks/', views.SearchTracks.as_view(), name='tracks'),
    path('artists/',views.Artists.as_view() ,name='artists'),
    path('albuns/', views.Albuns.as_view(), name='albuns'),
    path('teste/', views.teste, name='teste')
    
]