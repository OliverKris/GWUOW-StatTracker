# mappings/events.py

from events.match_events import MatchStartEvent, MatchEndEvent
from events.round_events import RoundStartEvent, RoundEndEvent, SetupCompleteEvent
from events.player_stat_event import PlayerStatEvent
# from events.combat_events import KillEvent, DamageEvent, HealingEvent
# from events.objective_events import PointProgressEvent, PayloadProgressEvent, ObjectiveCapturedEvent
from events.hero_events import HeroSpawnEvent, HeroSwapEvent
# from events.ultimate_events import UltimateChargedEvent, UltimateStartEvent, UltimateEndEvent
# from events.special_events import MercyRezEvent, EchoDuplicateStartEvent, EchoDuplicateEndEvent, DvaDemechEvent, DvaRemechEvent, RemechChargedEvent

# Map string -> Event class
EVENT_CLASS_MAP = {
    # Match events
    "match_start": MatchStartEvent,
    "match_end": MatchEndEvent,
    
    # Round events
    "round_start": RoundStartEvent,
    "round_end": RoundEndEvent,
    "setup_complete": SetupCompleteEvent,
    
    # Player / hero events
    "hero_spawn": HeroSpawnEvent,
    "hero_swap": HeroSwapEvent,
    
    # # Combat events
    # "kill": KillEvent,
    # "damage": DamageEvent,
    # "healing": HealingEvent,
    
    # # Objective / progress
    # "point_progress": PointProgressEvent,
    # "payload_progress": PayloadProgressEvent,
    # "objective_captured": ObjectiveCapturedEvent,
    
    # # Ultimate events
    # "ultimate_charged": UltimateChargedEvent,
    # "ultimate_start": UltimateStartEvent,
    # "ultimate_end": UltimateEndEvent,
    
    # # Special events
    # "mercy_rez": MercyRezEvent,
    # "echo_duplicate_start": EchoDuplicateStartEvent,
    # "echo_duplicate_end": EchoDuplicateEndEvent,
    # "dva_demech": DvaDemechEvent,
    # "dva_remech": DvaRemechEvent,
    # "remech_charged": RemechChargedEvent,
    
    # Player stats
    "player_stat": PlayerStatEvent,
}

# Group classes into categories
EVENT_TYPE_MAP = {
    "match_event": [MatchStartEvent, MatchEndEvent],
    "round_event": [RoundStartEvent, RoundEndEvent, SetupCompleteEvent],
    # "combat_event": [KillEvent, DamageEvent, HealingEvent, DvaDemechEvent],
    "player_event": [PlayerStatEvent, HeroSpawnEvent, HeroSwapEvent],
    # "objective_event": [PointProgressEvent, PayloadProgressEvent, ObjectiveCapturedEvent],
    # "ultimate_event": [UltimateChargedEvent, UltimateStartEvent, UltimateEndEvent],
}
