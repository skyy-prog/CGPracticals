# import pygame
# def drawLine(surface , color , start ,end):
#     x1,y1 = start
#     x2,y2 = end
#     dx = x2-x1
#     dy = y2 - y1
#     steps = max(abs(dx) , abs(dy))
#     xIncrement = dx/steps
#     yInrement = dy/steps
#     x,y = x1,y1
#     for _ in range(steps+1):
#         surface.set_at((round(x) , round(y)) , color )
#         x += xIncrement
#         y += yInrement
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption('Daa algo')
# green = (0, 255, 0)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     drawLine(screen ,green , (130,90) , (50,200) )
# pygame.display.flip()
# pygame.quit()       

import pygame

# def DRAWLINE(surface, color, start, end):
#     x1, y1 = start
#     x2, y2 = end
#     dx = x2 - x1
#     dy = y2 - y1
#     steps = max(abs(dx), abs(dy))

#     Xincrement = dx / steps
#     Yincrement = dy / steps

#     x, y = x1, y1
#     for _ in range(steps + 1):
#         surface.set_at((round(x), round(y)), color)
#         x += Xincrement
#         y += Yincrement

# pygame.init()

# pygame.display.set_caption("DAA ALGO")
# screen = pygame.display.set_mode((500, 500))

# green = (0, 255, 0)
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     DRAWLINE(screen, green, (50, 200), (450, 200))
#     pygame.display.flip()

# pygame.quit()


def DRAWLINE(surface , color , start,end):
    x1,y1 = start
    x2,y2 = end
    dx = x2-x1
    dy = y2 - y1
    steps = max((abs(dx)  , abs(dy)))
    Xincrement = dx/steps
    Yincrement = dy/steps
    x,y = x1 , y2
    for _ in range(steps + 1):
        surface.set_at((round(x) , round(y)) , color)
        x += Xincrement
        y += Yincrement
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("DAA ALGO")
green = (0, 255, 0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    DRAWLINE(screen , green  , (400,600) , (50 ,300))
    pygame.display.flip()
pygame.quit()

