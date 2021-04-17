from Perceptron import Perceptron
import pygame
from Training import Point
import numpy as np
from sklearn.preprocessing import StandardScaler


def Surface(surface_width, surface_height):
    pygame.init()
    surf = pygame.display.set_mode((surface_width, surface_height))
    pygame.display.set_caption('Canvas')
    return surf


width = 800
height = 800


surface = Surface(width, height)
brain = Perceptron()

points = []
X = []
y = []
n_points = 10000
for i in range(n_points):
    p = Point(width, height)
    points.append(p)
    X.append([p.x, p.y])
    y.append(p.label)
X = np.array(X)
y = np.array(y)

sx = StandardScaler()
sx.fit(X)
# X = sx.transform(X)

draw_loop = True

while draw_loop:
    surface.fill((255, 255, 200))
    pygame.draw.line(surface, (0, 0, 0), (0, 0), (width, height))

    for point in points:
        point.show(surface)

    guess = brain.guess(X)
    conditions = guess.reshape(-1,) == y
    for i, con in enumerate(conditions):
        if con:
            pygame.draw.circle(surface, (0, 255, 0), center=(points[i].x, points[i].y), radius=6)
        else:
            pygame.draw.circle(surface, (255, 0, 0), center=(points[i].x, points[i].y), radius=6)

    brain.batch_gradient_descent_log_loss(X, y)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            draw_loop = False

    # for point in points:
    #     train_X = np.array([[point.x, point.y]])
    #     train_X = sx.transform(train_X)
    #     train_y = point.label
    #     guess = brain.guess(train_X)
    #
    #     if guess[0][0] == train_y:
    #         pygame.draw.circle(surface, (0, 255, 0), center=(point.x, point.y), radius=6)
    #     else:
    #         pygame.draw.circle(surface, (255, 0, 0), center=(point.x, point.y), radius=6)

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         for point in points:
        #             sample_X = np.array([[point.x, point.y]])
        #             sample_y = np.array([point.label])
        #             brain.stochastic_gradient_descent(sample_X, sample_y)



