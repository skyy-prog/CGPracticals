import pygame
import numpy as np
def scaling(points, sx, sy, pivot=None):
    if pivot is None:
        pivot = (0, 0)

    px, py = pivot

    scalingArray = np.array([
        [sx, 0, px * (1 - sx)],
        [0, sy, py * (1 - sy)],
        [0, 0, 1]
    ])

    HomoPoints = [np.array([x, y, 1]) for x, y in points]
    TransPoints = [scalingArray @ p for p in HomoPoints]

    return [(int(p[0]), int(p[1])) for p in TransPoints]


pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('scaling transformation ')

# Original Shape
OGPOINTS = [(200, 200), (300, 200), (300, 300), (200, 300)]

# Scaled Shape
scaledPoints = scaling(OGPOINTS, 1.5, 1.5, (250, 250))

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Original
    pygame.draw.polygon(screen, (0, 0, 0), OGPOINTS, 2)

    # Scaled
    pygame.draw.polygon(screen, (0, 0, 255), scaledPoints, 2)

    pygame.display.flip()

pygame.quit()



# import pygame
# import numpy as np

# def scaling(points, sx, sy, pivot=None):
#     if pivot is None:
#         pivot = (0, 0)

#     px, py = pivot

#     scalingArray = np.array([
#         [sx, 0, px * (1 - sx)],
#         [0, sy, py * (1 - sy)],
#         [0, 0, 1]
#     ])

#     HomoPoints = [np.array([x, y, 1]) for x, y in points]
#     TransPoints = [scalingArray @ p for p in HomoPoints]

#     return [(int(p[0]), int(p[1])) for p in TransPoints]


# pygame.init()
# screen = pygame.display.set_mode((500, 500))
# pygame.display.set_caption('Scaling Transformation')

# OGPOINTS = [(200, 200), (300, 200), (300, 300), (200, 300)]
# pivot = (250, 250)

# # Medium box
# scaledPoints1 = scaling(OGPOINTS, 1.5, 0.5, pivot)

# # Bigger box
# scaledPoints2 = scaling(OGPOINTS, 2, 2, pivot)

# running = True
# while running:
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             running = False

#     screen.fill((255, 255, 255))

#     # Original
#     pygame.draw.polygon(screen, (0, 0, 0), OGPOINTS, 2)

#     # Medium
#     # pygame.draw.polygon(screen, (255, 0, 0), scaledPoints1, 2)

#     # Bigger
#     pygame.draw.polygon(screen, (0, 0, 255), scaledPoints2, 2)

#     pygame.display.flip()

# pygame.quit()
