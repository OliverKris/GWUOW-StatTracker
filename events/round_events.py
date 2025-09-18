# events/round_events.py

from events.base import Event

class RoundStartEvent(Event):
    """Signifies the start of a round"""
    def __init__(self, timestamp, fields):
        super().__init__(timestamp, fields)
        self.round_number = fields[0]
        self.capturing_team = fields[1]
        self.team_1_score = fields[2]
        self.team_2_score = fields[3]
        self.objective_index = fields[4]
        self.event_type = "round_start"

    def __repr__(self):
        return (
            f"<RoundStartEvent timestamp={self.timestamp}, "
            f"round_number={self.round_number}, "
            f"capturing_team={self.capturing_team}, "
            f"team_1_score={self.team_1_score}, "
            f"team_2_score={self.team_2_score}, "
            f"objective_index={self.objective_index}>"
        )

class RoundEndEvent(Event):
    """Signifies the end of a round"""
    def __init__(self, timestamp, fields):
        super().__init__(timestamp, fields)
        self.round_number = fields[0]
        self.capturing_team = fields[1]
        self.team_1_score = fields[2]
        self.team_2_score = fields[3]
        self.objective_index = fields[4]
        self.team_1_progress = fields[5]
        self.team_2_progress = fields[6]
        self.match_time_remaining = fields[7]
        self.event_type = "round_end"

    def __repr__(self):
        return (
            f"<RoundEndEvent timestamp={self.timestamp}, "
            f"round_number={self.round_number}, "
            f"capturing_team={self.capturing_team}, "
            f"team_1_score={self.team_1_score}, "
            f"team_2_score={self.team_2_score}, "
            f"objective_index={self.objective_index}, "
            f"team_1_progress={self.team_1_progress}, "
            f"team_2_progress={self.team_2_progress}, "
            f"match_time_remaining={self.match_time_remaining}>"
        )

class SetupCompleteEvent(Event):
    """Signifies that round setup is complete"""
    def __init__(self, timestamp, fields):
        super().__init__(timestamp, fields)
        self.round_number = fields[0]
        self.match_time_remaining = fields[1]
        self.event_type = "setup_complete"

    def __repr__(self):
        return (
            f"<SetupCompleteEvent timestamp={self.timestamp}, "
            f"round_number={self.round_number}, "
            f"match_time_remaining={self.match_time_remaining}>"
        )
