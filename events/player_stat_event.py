
from .base import Event

# player_stat

class PlayerStatEvent(Event):
    def __init__(self, timestamp, fields):
        super().__init__(timestamp, fields)