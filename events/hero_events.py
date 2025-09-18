# events/hero_events.py

from .base import Event

# Base class for all hero-related events
class HeroEvent(Event):
    def __init__(self, timestamp, fields):
        super().__init__(timestamp, fields)
        self.player_team = fields[0]
        self.player_name = fields[1]
        self.player_hero = fields[2]
        self.hero_time_played = fields[4]  # common to all hero events

# Hero spawn
class HeroSpawnEvent(HeroEvent):
    def __init__(self, timestamp, fields):
        super().__init__(timestamp, fields)
        self.previous_hero = fields[3]   # only in spawn
        self.event_type = "hero_spawn"
    
    def __repr__(self):
        return (
            f"<HeroSpawnEvent timestamp={self.timestamp}, "
            f"team={self.player_team}, "
            f"player={self.player_name}, "
            f"hero={self.player_hero}, "
            f"previous_hero={self.previous_hero}, "
            f"time_played={self.hero_time_played}>"
        )

# Hero swap
class HeroSwapEvent(HeroEvent):
    def __init__(self, timestamp, fields):
        super().__init__(timestamp, fields)
        self.previous_hero = fields[3]   # previous hero
        self.event_type = "hero_swap"

    def __repr__(self):
        return (
            f"<HeroSwapEvent timestamp={self.timestamp}, "
            f"team={self.player_team}, "
            f"player={self.player_name}, "
            f"new_hero={self.player_hero}, "
            f"previous_hero={self.previous_hero}, "
            f"time_played={self.hero_time_played}>"
        )
