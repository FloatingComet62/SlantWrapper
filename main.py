import pygame

from objects.rectangle import Rectangle
from objects.circle import Circle
from objects.text import Text
from window import Window
from util import Dimension, Color, Position

window = Window("Pong", Dimension(700, 500), Color.from_hex("#303030"), 60)
player = Rectangle(Position(10, 250), Dimension(10, 50), Color.from_hex("#eeeeee"))
ai = Rectangle(Position(680, 250), Dimension(10, 50), Color.from_hex("#eeeeee"))
ball = Circle(Position(350, 250), 5, Color.from_hex("#ffffff"))
scoreText = Text("Score: 0", Position(350, 20), 20, Color.from_hex("#ffffff"))
window.addObjs([player, ai, ball, scoreText])

ball_velocity = [5, 5]
score = 0
playing = True


def main():
    global ball_velocity
    global score
    global playing

    if playing:
        player.position.y = window.mouse[1] - player.dimension.height / 2
    else:
        if window.keys[pygame.K_r]:
            playing = True
            ball.position = Position(250, 250)
            ball_velocity = [5, 5]
            scoreText.score = 0
            window.background_color = Color.from_hex("#303030")

    ai.position.y = ball.position.y - ai.dimension.height / 2
    ball.position = ball.position.offset(ball_velocity[0], ball_velocity[1])
    scoreText.string = f"Score: {score}"

    if ball.position.y >= window.dimensions.height or ball.position.y <= 0:
        ball_velocity[1] = -ball_velocity[1]
    if ball.position.x >= window.dimensions.width - 20:
        ball_velocity[0] = -ball_velocity[0]

    if ball.position.x <= 20:
        if player.position.y <= ball.position.y <= (player.position.y + player.dimension.height):
            ball_velocity[0] = -ball_velocity[0]
            scoreText.score += 1
            return True

        # GAME OVER
        ball_velocity = [0, 0]
        window.background_color = Color.from_hex("#f57b42")
        playing = False

    return True


window.display(main)
