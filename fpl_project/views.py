from django.shortcuts import render
from fpl.models import Team, Player, Fixture, Coach  # Import models

def home(request):
    return render(request, 'home.html')

def teams_list(request):
    teams = Team.objects.all()  # Fetch all teams from the database
    return render(request, 'teams.html', {'teams': teams})  # Pass teams to template

def players_list(request):
    players = Player.objects.all()  # Fetch all players from the database
    return render(request, 'players.html', {'players': players})

def fixtures_list(request):
    fixtures = Fixture.objects.all()  # Fetch all fixtures from the database
    return render(request, 'fixtures.html', {'fixtures': fixtures})

def coaches_list(request):
    coaches = Coach.objects.all()  # Fetch all coaches from the database
    return render(request, 'coaches.html', {'coaches': coaches})
