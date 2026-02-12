import pygame
import numpy as np

def shear(points, shx, shy, pivot=None):
    if pivot is None:
        pivot = (0, 0)

    px, py = pivot

 
    shearing = np.array([
        [1, shx, -py * shx],
        [shy, 1, -px * shy],
        [0, 0, 1]
    ])

     
    homoPoints = [np.array([x, y, 1]) for x, y in points]

     
    transPoint = [shearing @ p for p in homoPoints]

    return [(int(p[0]), int(p[1])) for p in transPoint]


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Shearing Points')

 
OGPOINTS = [(200, 200), (300, 200), (200, 0)]

 
sharedPoint = shear(OGPOINTS, 0.5, 0.2, (250, 250))

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((205, 255, 255))
 
    pygame.draw.polygon(screen, (0, 0, 0), OGPOINTS, 2)
 
    pygame.draw.polygon(screen, (255, 0, 0), sharedPoint, 2)

    pygame.display.flip()

pygame.quit()
