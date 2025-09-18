# timeline.py

class Timeline:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        """Append an event to the timeline"""
        self.events.append(event)

    def __iter__(self):
        """Allow iteration over events in timeline"""
        return iter(self.events)

    def __len__(self):
        """Number of events in timeline"""
        return len(self.events)

    def __repr__(self):
        return f"<Timeline events={len(self.events)}>"

    def __str__(self):
        """Human-readable timeline (all events, one per line)"""
        if not self.events:
            return "Timeline[empty]"

        lines = [f"{i+1}. {str(event)}" for i, event in enumerate(self.events)]
        return "Timeline:\n" + "\n".join(lines)
