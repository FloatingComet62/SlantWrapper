from pygame import Surface, draw, Rect
from objects import Base
from util import Color, Position, Dimension, Angle, DisplayMode


class Arc(Base):
    """ Pygame Arc """
    dimension: Dimension
    """ Dimensions of Arc """
    start_angle: Angle
    """ Starting angle of Arc """
    stop_angle: Angle
    """ Stopping angle of Arc """
    thickness: int
    """ Thickness of the Arc """

    def __init__(
        self,
        position: Position,
        dimension: Dimension,
        start_angle: Angle,
        stop_angle: Angle,
        color: Color,
        thickness: int = 1
    ):
        super().__init__(position, color)

        self.dimension = dimension
        self.start_angle = start_angle
        self.stop_angle = stop_angle
        self.thickness = thickness

    def display(self, screen: Surface, display_mode: DisplayMode):
        draw.arc(
            screen,
            self.color.toRGB(),
            Rect(
                self.position.x - (self.dimension.width/2 if display_mode == DisplayMode.CENTER else 0),
                self.position.y - (self.dimension.height/2 if display_mode == DisplayMode.CENTER else 0),
                self.dimension.width,
                self.dimension.height
            ),
            self.start_angle.radian,
            self.stop_angle.radian,
            self.thickness
        )
