from django.urls import path
from . import views

urlpatterns = [
    path('teste/', views.search_tracks, name='teste'),
    
]