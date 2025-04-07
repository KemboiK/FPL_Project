from django.db import models

class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    strength = models.IntegerField()

    def __str__(self):
        return self.name

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    web_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    element_type = models.IntegerField()
    total_points = models.IntegerField()
    selected_by_percent = models.FloatField()
    now_cost = models.FloatField()
    minutes = models.IntegerField()
    goals_scored = models.IntegerField()
    assists = models.IntegerField()
    clean_sheets = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.web_name

class Gameweek(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    deadline_time = models.DateTimeField()
    average_entry_score = models.IntegerField(null=True, blank=True)
    highest_score = models.IntegerField(null=True, blank=True)
    is_current = models.BooleanField()
    is_next = models.BooleanField()
    is_previous = models.BooleanField()

    def __str__(self):
        return self.name

class Fixture(models.Model):
    id = models.IntegerField(primary_key=True)
    kickoff_time = models.DateTimeField()
    team_h = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_fixtures")
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_fixtures")
    team_h_score = models.IntegerField(null=True, blank=True)
    team_a_score = models.IntegerField(null=True, blank=True)
    finished = models.BooleanField()

    def __str__(self):
        return f"{self.team_h} vs {self.team_a}"

class Coach(models.Model):  # Define Coach model
    name = models.CharField(max_length=100)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
