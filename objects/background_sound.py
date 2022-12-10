from pygame import mixer


class BackgroundSound:
    """
    WARNING: PYGAME SOUND SYSTEM IS SHIT\n
    Pygame background music
    """
    name: str
    """ Soundtrack file location"""

    def __init__(self, name: str):
        self.name = name

    def play(self, loops: int = -1, max_time: int = 0, fade_ms: int = 0):
        """ Start playing the track """
        mixer.music.load(self.name)
        mixer.music.play(loops, max_time, fade_ms)

    def stop(self):
        """ Stop playing the track """
        mixer.music.stop()
