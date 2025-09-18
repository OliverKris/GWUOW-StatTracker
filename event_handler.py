# event_handler.py

from mappings.event_mapping import EVENT_TYPE_MAP
from events.match_events import MatchStartEvent, MatchEndEvent
# from events.round_events import RoundStartEvent, RoundEndEvent
# from events.combat_events import KillEvent, DamageEvent, HealingEvent

# Registry for event handlers
handlers = {}

def register(event_cls):
    """Decorator to register a handler for a given event class"""
    def wrapper(func):
        handlers[event_cls] = func
        return func
    return wrapper

# --- Context: store match, timeline, stats, etc ---
# The context is a dictionary passed to every handler
# Example: {"match": MatchObj, "timeline": TimelineObj, "stats": StatsManagerObj}

# --- Category-based default handlers ---
def handle_match_event(event, context):
    match = context.get("match")
    event_name =  event.__class__.__name__
    match event_name:
        case "MatchStartEvent":
            from match.match import Match
            context["match"] = Match(event)
        case "MatchEndEvent":
            if match:
                match.end_match(event)

def handle_round_event(event, context):
    match = context.get("match")
    if match:
        match.add_event(event)
    event_name = event.__class__.__name__
    match event_name:
        case "RoundStartEvent": 
            return
        case "RoundEndEvent":
            return
        case "SetupCompleteEvent":
            return
        case _:
            return

def handle_combat_event(event, context):
    return

def handle_player_event(event, context):
    return

def handle_objective_event(event, context):
    return

def handle_ultimate_event(event, context):
    return

# --- Dispatcher mapping category -> handler ---
CATEGORY_HANDLER_MAP = {
    "match_event": handle_match_event,
    "round_event": handle_round_event,
    "combat_event": handle_combat_event,
    "player_event": handle_player_event,
    "objective_event": handle_objective_event,
    "ultimate_event": handle_ultimate_event,
}

# --- Main dispatch function ---
def dispatch(event, context):
    # Determine event category
    for category, event_classes in EVENT_TYPE_MAP.items():
        if isinstance(event, tuple(event_classes)):
            handler = CATEGORY_HANDLER_MAP.get(category)
            if handler:
                handler(event, context)
            return

    # Default fallback
    print("Default fallback")
    return