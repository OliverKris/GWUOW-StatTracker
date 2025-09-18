# match.py

from events.match_events import MatchStartEvent, MatchEndEvent
from timeline import Timeline

class Match:
    def __init__(self, start_event: MatchStartEvent):
        if not isinstance(start_event, MatchStartEvent):
            raise TypeError("Match must be initialized with a MatchStartEvent")

        self.start_event = start_event
        self.end_event: MatchEndEvent | None = None
        self.timeline = Timeline()
        self.timeline.add_event(start_event)

        self.teams = {
            "team_1": start_event.team_1_name,
            "team_2": start_event.team_2_name,
        }
        self.map_name = start_event.map_name
        self.map_type = start_event.map_type

        self.rounds = []   # can later hold Round objects

    def add_event(self, event):
        """Add any event into the match timeline."""
        self.timeline.add_event(event)

        if isinstance(event, MatchEndEvent):
            self.end_match(event)

    def end_match(self, end_event: MatchEndEvent):
        """Close the match properly with an end event."""
        if not isinstance(end_event, MatchEndEvent):
            raise TypeError("end_match must be called with a MatchEndEvent")
        self.end_event = end_event

    def duration(self):
        """Return match duration if ended (start → end timestamps)."""
        if not self.end_event:
            return None
        return f"{self.start_event.timestamp} → {self.end_event.timestamp}"

    def is_finished(self) -> bool:
        return self.end_event is not None

    def print_events(self):
        return print(self.timeline)

    def __repr__(self):
        status = "finished" if self.is_finished() else "in-progress"
        return (
            f"<Match {self.teams['team_1']} vs {self.teams['team_2']} "
            f"on {self.map_name} ({self.map_type}), "
            f"{len(self.timeline.events)} events, {status}>"
        )

    def summary(self):
        return {
            "map": self.map_name,
            "type": self.map_type,
            "team_1": self.teams["team_1"],
            "team_2": self.teams["team_2"],
            "events": len(self.timeline),
            "rounds": len(self.rounds),
            "duration": self.duration(),
        }