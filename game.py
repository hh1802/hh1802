from random import randint

import pygame


class Ball(object):

    def __init__(self, center, color, radius, speed):
        self._center = center
        self._color = color
        self._radius = radius
        self._speed = speed

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    def move(self):
        x, y = self._center[0], self._center[1]
        sx, sy = self._speed[0], self._speed[1]
        self._center = x, y = x + sx, y + sy
        if x + self._radius >= 800 or x - self._radius <= 0:
            self._speed = -sx, sy
        if y + self._radius >= 600 or y - self._radius <= 0:
            self._speed = sx, -sy

    def eat(self, other):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self._color, self._center,
                           self._radius, 0)


def main():
    balls = []
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN \
                    and event.button == 1:
                color = random_color()
                radius = randint(10, 100)
                speed = randint(-10, 10), randint(-10, 10)
                ball = Ball(event.pos, color, radius, speed)
                balls.append(ball)
        refresh(screen, balls)
        clock.tick(24)
        for ball in balls:
            ball.move()
    pygame.quit()


def refresh(screen, balls):
    bg_color = (242, 242, 242)
    screen.fill(bg_color)
    for ball in balls:
        ball.draw(screen)
    pygame.display.flip()


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return red, green, blue


if __name__ == '__main__':
    main()
