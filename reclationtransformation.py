import numpy as np
import pygame
def reflect(points, axis='x'):
    if axis == 'x':
        reflectionMatrix = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
    elif axis == 'y':
        reflectionMatrix = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
    else:   
        reflectionMatrix = np.array([
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])

    homogeneousPoints = [np.array([x, y, 1]) for x, y in points]

    transformedPoints = [
        reflectionMatrix @ p for p in homogeneousPoints
    ]

    return [(p[0], p[1]) for p in transformedPoints]


def translate(points, tx=0, ty=0):
    return [(x + tx, y + ty) for x, y in points]

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Reflection Transformation')

OGPoints = [(200,200), (300,200), (300,300), (200,300)]
rePOINTS = reflect(OGPoints, 'x')
rePOINTS = translate(rePOINTS, 0, 400)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False 

    screen.fill((255,255,255))

    pygame.draw.polygon(screen, (0,0,0), OGPoints)
    pygame.draw.polygon(screen, (255,100,0), rePOINTS)

    pygame.display.flip()

pygame.quit()

 