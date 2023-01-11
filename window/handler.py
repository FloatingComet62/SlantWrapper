from dataclasses import dataclass


@dataclass
class Handler:
    event_type: int
    handler: ()
