from pygame import mixer

# WARNING: PYGAME SOUND SYSTEM IS SHIT
class Sound:
    name: str
    loops: int
    handler: mixer.Sound

    def __init__(self, name: str, loops: int):
        self.name = name
        self.loops = loops

    def play(self, loops: int = 0, max_time: int = 0, fade_ms: int = 0):
        self.handler = mixer.Sound(self.name)
        self.handler.play(loops, max_time, fade_ms)

    def stop(self):
        self.handler.stop()