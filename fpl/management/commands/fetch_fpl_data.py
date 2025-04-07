import requests
from django.core.management.base import BaseCommand
from fpl.models import Player, Team, Fixture, Gameweek

FPL_BOOTSTRAP_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
FPL_FIXTURES_URL = "https://fantasy.premierleague.com/api/fixtures/"

class Command(BaseCommand):
    help = "Fetch and store FPL data"

    def handle(self, *args, **kwargs):
        self.fetch_teams()
        self.fetch_players()
        self.fetch_gameweeks()
        self.fetch_fixtures()
        self.stdout.write(self.style.SUCCESS("✅ FPL data successfully fetched and stored!"))

    def fetch_teams(self):
        """Fetch and store teams"""
        response = requests.get(FPL_BOOTSTRAP_URL).json()
        teams_data = response["teams"]
        for team in teams_data:
            Team.objects.update_or_create(
                id=team["id"],
                defaults={
                    "name": team["name"],
                    "short_name": team["short_name"],
                    "strength": team["strength"],
                },
            )

    def fetch_players(self):
        """Fetch and store players"""
        response = requests.get(FPL_BOOTSTRAP_URL).json()
        players_data = response["elements"]
        for player in players_data:
            Player.objects.update_or_create(
                id=player["id"],
                defaults={
                    "first_name": player["first_name"],
                    "second_name": player["second_name"],
                    "web_name": player["web_name"],
                    "team_id": player["team"],
                    "element_type": player["element_type"],
                    "total_points": player["total_points"],
                    "selected_by_percent": player["selected_by_percent"],
                    "now_cost": player["now_cost"] / 10,
                    "minutes": player["minutes"],
                    "goals_scored": player["goals_scored"],
                    "assists": player["assists"],
                    "clean_sheets": player["clean_sheets"],
                    "yellow_cards": player["yellow_cards"],
                    "red_cards": player["red_cards"],
                },
            )

    def fetch_gameweeks(self):
        """Fetch and store gameweeks"""
        response = requests.get(FPL_BOOTSTRAP_URL).json()
        gameweeks_data = response["events"]
        for gw in gameweeks_data:
            Gameweek.objects.update_or_create(
                id=gw["id"],
                defaults={
                    "name": gw["name"],
                    "deadline_time": gw["deadline_time"],
                    "average_entry_score": gw["average_entry_score"],
                    "highest_score": gw["highest_score"],
                    "is_current": gw["is_current"],
                    "is_next": gw["is_next"],
                    "is_previous": gw["is_previous"],
                },
            )

    def fetch_fixtures(self):
        """Fetch and store fixtures"""
        response = requests.get(FPL_FIXTURES_URL).json()
        for fixture in response:
            Fixture.objects.update_or_create(
                id=fixture["id"],
                defaults={
                    "kickoff_time": fixture["kickoff_time"],
                    "team_h_id": fixture["team_h"],
                    "team_a_id": fixture["team_a"],
                    "team_h_score": fixture.get("team_h_score"),
                    "team_a_score": fixture.get("team_a_score"),
                    "finished": fixture["finished"],
                },
            )
