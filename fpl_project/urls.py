from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from .views import home, teams_list, players_list, fixtures_list, coaches_list

def home(request):
    return JsonResponse({"message": "Welcome to the Fantasy Premier League API!"})

urlpatterns = [
    path('', home, name='index'),  # Root URL
    path('admin/', admin.site.urls),
    path('api/', include('fpl.urls')),  

    # Web views
    path('teams/', teams_list, name='teams'),
    path('players/', players_list, name='players'),
    path('fixtures/', fixtures_list, name='fixtures'),
    path('coaches/', coaches_list, name='coaches'),
]
