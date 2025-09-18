class PlayerStats:
    def __init__(self, name, team, hero=None):
        self.name = name
        self.team = team
        self.hero = hero

        # Combat stats
        self.eliminations = 0
        self.final_blows = 0
        self.deaths = 0
        self.all_damage = 0.0
        self.barrier_damage = 0.0
        self.hero_damage = 0.0
        self.healing_done = 0.0
        self.healing_received = 0.0
        self.self_healing = 0.0
        self.damage_taken = 0.0
        self.damage_blocked = 0.0

        # Assists
        self.defensive_assists = 0
        self.offensive_assists = 0

        # Ultimates
        self.ultimates_earned = 0
        self.ultimates_used = 0

        # Multi-kill stats
        self.multikill_best = 0
        self.multikills = 0
        self.solo_kills = 0

        # Objective / environment
        self.objective_kills = 0
        self.environmental_kills = 0
        self.environmental_deaths = 0

        # Accuracy
        self.critical_hits = 0
        self.critical_accuracy = 0.0
        self.scoped_accuracy = 0.0
        self.scoped_critical_accuracy = 0.0
        self.scoped_critical_kills = 0

        # Shots
        self.shots_fired = 0
        self.shots_hit = 0
        self.shots_missed = 0
        self.scoped_shots_fired = 0
        self.scoped_shots_hit = 0
        self.weapon_accuracy = 0.0

        # Time played
        self.hero_time_played = 0.0

    def update_from_event(self, event):
        """
        Update stats from an event like 'player_stat', 'kill', 'healing', etc.
        """
        # Example for a player_stat line
        if event.event_type == "player_stat":
            self.eliminations = event.eliminations
            self.final_blows = event.final_blows
            self.deaths = event.deaths
            self.all_damage = event.all_damage
            self.barrier_damage = event.barrier_damage
            self.hero_damage = event.hero_damage
            self.healing_done = event.healing_done
            self.healing_received = event.healing_received
            self.self_healing = event.self_healing
            self.damage_taken = event.damage_taken
            self.damage_blocked = event.damage_blocked
            self.defensive_assists = event.defensive_assists
            self.offensive_assists = event.offensive_assists
            self.ultimates_earned = event.ultimates_earned
            self.ultimates_used = event.ultimates_used
            self.multikill_best = event.multikill_best
            self.multikills = event.multikills
            self.solo_kills = event.solo_kills
            self.objective_kills = event.objective_kills
            self.environmental_kills = event.environmental_kills
            self.environmental_deaths = event.environmental_deaths
            self.critical_hits = event.critical_hits
            self.critical_accuracy = event.critical_accuracy
            self.scoped_accuracy = event.scoped_accuracy
            self.scoped_critical_accuracy = event.scoped_critical_accuracy
            self.scoped_critical_kills = event.scoped_critical_kills
            self.shots_fired = event.shots_fired
            self.shots_hit = event.shots_hit
            self.shots_missed = event.shots_missed
            self.scoped_shots_fired = event.scoped_shots_fired
            self.scoped_shots_hit = event.scoped_shots_hit
            self.weapon_accuracy = event.weapon_accuracy
            self.hero_time_played = event.hero_time_played

class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.heroes_played = {} # round_number -> list of heroes used
        self.stats = {} # round_number -> stats object