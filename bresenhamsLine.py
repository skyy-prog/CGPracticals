 

# import pygame
# def BREHESEN(surface , color , start,end):
#     x1,y1 = start
#     x2,y2 = end
#     dx = abs(x2-x1)
#     dy = abs(y2-y1)
#     steep = dy > dx
#     if steep :
#         x1,y1 = y1,x1
#         x2,y2 = y2,x2
#     if x1 > x2:
#         x1,x2 = x2,x1
#         y1,y2 = y2,y1
#     dx = x2-x1
#     dy = abs(y2 - y1)
#     y = y1
#     error = dx//2
#     ysteep = 1 if y1 < y2 else -1
#     for x in range(x1 , x2+1):
#         if steep:
#             surface.set_at((y,x) , color)
#         else:
#             surface.set_at((x,y) , color)
#         error -= dy
#         if error < 0 :
#             y += ysteep
#             error += dx

# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption('BRESEHN')
# pygame.init()
# running = True
# Blue = (10,244,150)
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0,0,0))
#     BREHESEN(screen , Blue , (50,50) , (400,450))
#     pygame.display.flip()
# pygame.quit()



import pygame
def breshen(surface, color , start , end):
    x1,y1 = start
    x2,y2 = end
    dx = abs(x2-x1)
    dy = abs(y2 - y1)
    steep = dy > dx
    if steep :
        x1,y1 = y1, x1
        x2,y2  = y2 , x2
    if x1 >x2:
        x1,x2 = x2,x1
        y1 , y2 = y2 , y1
    dx = x2-x1
    dy = abs(y2 - y1)
    error = dx//2
    ysteep  = 1 if y1 < y2 else -1
    y = y1
    for x in range(x1, x2 + 1):
        if steep :
            surface.set_at((y,x) , color)
        else :
            surface.set_at((x,y) , color)
        error -= dy
        if error < 0:
            y += ysteep
            error += dx
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Brehensen')
blue= (0,233,190)
running  = True
while running:
    for evn in pygame.event.get():
        if evn.type == pygame.QUIT:
            running = False
    breshen(screen , blue , (200,200)  , (400 , 450))
    pygame.display.flip()
pygame.quit()