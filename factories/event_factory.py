from mappings.event_mapping import EVENT_CLASS_MAP

def create_event(timestamp, event_type, fields):
    """
    Factory function to create an event instance based on event_type.
    Falls back to generic Event if unknown.
    """
    event_class = EVENT_CLASS_MAP.get(event_type)
    if event_class:
        return event_class(timestamp, fields)
    else:
        print(f"Warning: Unknown event type of type '{event_type}', at {timestamp}")
        return None