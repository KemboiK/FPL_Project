from django.http import JsonResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, PlayerViewSet, CoachViewSet

def home(request):
    return JsonResponse({"message": "Welcome to the Fantasy Premier League API!"})

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'coaches', CoachViewSet)

urlpatterns = [
    path('', home, name='home'),  # Root URL
    path('api/', include(router.urls)),  # API routes
    path('', include(router.urls)),  # Allow direct access (e.g., /players/)
]
