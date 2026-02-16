# import pygame
# def DRAWLINE(surface , color , start,end):
#     x1,y1 = start
#     x2,y2 = end
#     dx = x2-x1
#     dy = y2 - y1
#     steps = max((abs(dx)  , abs(dy)))
#     Xincrement = dx/steps
#     Yincrement = dy/steps
#     x,y = x1 , y2
#     for _ in range(steps + 1):
#         surface.set_at((round(x) , round(y)) , color)
#         x += Xincrement
#         y += Yincrement
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("DAA ALGO")
# green = (0, 255, 0)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     DRAWLINE(screen , green  , (400,600) , (50 ,300))
#     pygame.display.flip()
# pygame.quit()

import pygame
def  DRAWDAALINE(surface, color , start ,end):
    x1,y1 = start
    x2,y2 = end
    dx = x2-x1
    dy = y2 - y1
    #  point to be noted we have to use abs and max to find steps
    steps = max((abs(dx) , abs(dy)))  
    Xincrement = dx/steps
    Yincrement = dy/steps
    x,y = x1,y1
    for _ in range(steps +1):
        surface.set_at((round(x) , round(y)) , color)
        x += Xincrement
        y+= Yincrement
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('DAA Algo')
GREEN = (0,240,230)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False#
    screen.fill((0,0,0))
    DRAWDAALINE(screen , GREEN , (200,300) , (50,300))
    pygame.display.flip()

pygame.quit()