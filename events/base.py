# events/base.py

"""
Generic class for all match events
"""

class Event:
    def __init__(self, timestamp, raw_fields):
        self.timestamp = timestamp
        self.raw_fields = raw_fields
        self.event_type = None
    
    def __repr__(self):
        return f"<Event {self.event_type} at {self.timestamp}>"