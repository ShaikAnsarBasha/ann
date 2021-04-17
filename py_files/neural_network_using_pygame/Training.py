import random
import pygame


def generate_point(width, height):
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    if x > y:
        return x, y, 1
    elif x < y:
        return x, y, 0
    else:
        return generate_point(width, height)


class Point:
    def __init__(self, width, height):
        self.x, self.y, self.label = generate_point(width, height)

    def show(self, surface):
        pygame.draw.circle(surface, (0, 0, 150, 255), center=(self.x, self.y), radius=11)







        # if self.label == 1:
        #     pygame.draw.ellipse(surface, (0, 0, 255), (self.x, self.y, 15, 15))
        # else:
        #     pygame.draw.ellipse(surface, (255, 0, 0), (self.x, self.y, 15, 15))
