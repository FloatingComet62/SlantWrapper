from pygame import mixer


class Sound:
    """
    WARNING: PYGAME SOUND SYSTEM IS SHIT
    Pygame sound
    """
    name: str
    """ Soundtrack file location """
    handler: mixer.Sound

    def __init__(self, name: str, loops: int):
        self.name = name
        self.loops = loops

    def play(self, loops: int = 0, max_time: int = 0, fade_ms: int = 0):
        self.handler = mixer.Sound(self.name)
        self.handler.play(loops, max_time, fade_ms)

    def stop(self):
        self.handler.stop()
