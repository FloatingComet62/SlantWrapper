from pygame import mixer


class Sound:
    """
    WARNING: PYGAME SOUND SYSTEM IS SHIT\n
    Pygame sound
    """
    name: str
    """ Soundtrack file location """
    handler: mixer.Sound

    def __init__(self, name: str):
        self.name = name
        self.handler = mixer.Sound(self.name)

    def play(self, loops: int = 0, max_time: int = 0, fade_ms: int = 0):
        self.handler.play(loops, max_time, fade_ms)

    def stop(self):
        self.handler.stop()
