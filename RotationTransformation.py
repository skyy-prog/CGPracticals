import pygame
import numpy as np
import math

def Rotate(points, angle, pivot=None):
    if pivot is None:
        pivot = (0, 0)

    px, py = pivot
    rad = math.radians(angle)

  
    rotation_matrix = np.array([
        [math.cos(rad), -math.sin(rad), px * (1 - math.cos(rad)) + py * math.sin(rad)],
        [math.sin(rad),  math.cos(rad), py * (1 - math.cos(rad)) - px * math.sin(rad)],
        [0, 0, 1]
    ])

    homo_points = [np.array([x, y, 1]) for x, y in points]
    trans_points = [rotation_matrix @ p for p in homo_points]

    return [(int(p[0]), int(p[1])) for p in trans_points]


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Rotation')

running = True


OGPOINT = [(200, 200), (300, 200), (300, 300), (200, 300)]

 
TransPoint = Rotate(OGPOINT, 45, (250, 250))

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.polygon(screen, (0, 0, 0), OGPOINT, 2)
    pygame.draw.polygon(screen, (255, 0, 0), TransPoint, 2)
    pygame.display.flip()

pygame.quit()
