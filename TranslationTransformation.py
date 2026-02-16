import pygame
import numpy as np
def translate(point , tx,ty):
    translatedarray = np.array([
        [1,0,tx],
        [0,1,ty],
        [0,0,1]
    ])
    HomoPoint = [np.array([x,y,1]) for x,y in point]
    TransPoint = [translatedarray @p  for p in HomoPoint]
    return [(int(p[0]) ,int(p[1])) for p in TransPoint]
pygame.init()
OGPOINT = [
    (200, 200),
    (200, 100),
    (100, 100),
    (100, 200)
]
TransPOINT  = translate(OGPOINT , 150,100)
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Translation ')
running  =True
while running :
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    pygame.draw.polygon(screen, (0,0,0) , OGPOINT , 2)
    pygame.draw.polygon(screen, (0,0,0) , TransPOINT , 2)
    pygame.display.flip()
pygame.quit()

 