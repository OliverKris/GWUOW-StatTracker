# events/match_events.py

from .base import Event

# match_start, match_end
class MatchStartEvent(Event):
    """Event signaling the start of a match"""
    def __init__(self, timestamp, fields):
        super().__init__(timestamp, fields)
        self.map_name = fields[0]
        self.map_type = fields[1]
        self.team_1_name = fields[2]
        self.team_2_name = fields[3]
        self.event_type = "match_start"

    def __repr__(self):
        return (
            f"<MatchStartEvent timestamp={self.timestamp}, "
            f"map={self.map_name} ({self.map_type}), "
            f"teams={self.team_1_name} vs {self.team_2_name}>"
        )

class MatchEndEvent(Event):
    """Event signaling the end of a match"""
    def __init__(self, timestamp, fields):
        super().__init__(timestamp, fields)
        # fields = [round_number, team_1_score, team_2_score]
        self.round_number = int(fields[0])
        self.team_1_score = int(fields[1])
        self.team_2_score = int(fields[2])
        self.event_type = "match_end"

    def __repr__(self):
        return (
            f"<MatchEndEvent timestamp={self.timestamp}, "
            f"round={self.round_number}, "
            f"score={self.team_1_score}-{self.team_2_score}>"
        )