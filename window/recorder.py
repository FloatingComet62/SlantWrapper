from cv2 import VideoWriter, VideoWriter_fourcc
from numpy import array
from util import Dimension
from dataclasses import astuple


class Recorder:
    writer: VideoWriter
    data: list[list[list[list[int]]]]
    writing: bool

    def __init__(self, file_name: str, fps, dimension: Dimension):
        self.writing = False
        self.data = list()
        self.writer = VideoWriter(
            f"{file_name}.mp4",
            VideoWriter_fourcc(*'mp4v'),
            fps,
            astuple(dimension)
        )

    def start(self):
        self.writing = True

    def stop(self):
        for item in self.data:
            self.writer.write(array(item))
        self.writer.release()
        self.writing = False

    def frame_data(self, data: list[list[list[int]]]):
        self.data.append(data)
