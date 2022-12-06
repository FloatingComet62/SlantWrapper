from pygame import mixer

# WARNING: PYGAME SOUND SYSTEM IS SHIT
class BackgroundSound:
    name: str
    def __init__(self, name: str):
        self.name = name

    def play(self, loops: int = -1, max_time: int = 0, fade_ms: int = 0):
        mixer.music.load(self.name)
        mixer.music.play(loops, max_time, fade_ms)

    def stop(self):
        mixer.music.stop()