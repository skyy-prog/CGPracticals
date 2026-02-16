import pygame
import numpy as np


def Scal(point , shx ,shy , pivot = None):
    if pivot == None:
        pivot =  (0,0)
    px , py = pivot
    scaling = np.array([
        [shx , 0 , px * (1-shx)],
        [0,shy , py * (1-shy)],
        [0,0,1]
    ])
    Homopoints = [np.array([x,y,1]) for x,y in point ]
    Tanspoint = [scaling @ p for p in Homopoints]
    return [(int(p[0]) , int(p[1])) for p in Tanspoint]
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('scaling transformation ')
OGPOINTS = [(200, 200), (300, 200), (300, 300), (200, 300)]
scaledPoint = Scal(OGPOINTS , 1.5 , 1.5 , (250,250))

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    pygame.draw.polygon(screen , (0,0,0) , OGPOINTS , 2)
    pygame.draw.polygon(screen , (0,0,255) , scaledPoint , 2)
    pygame.display.flip()
pygame.quit()

 