import pygame
def Drawline(surface , color, start ,end)                                        :
    x1,y1 = start
    x2,y2 = end
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    steep = dy > dx
    if steep:
        x1,y1 = y1,x1
        x2,y2 = y2,x2
    if x1 > x2:
        x1,x2 = x2,x1
        y1,y2 = y2,y1
    dx = x1-x2
    dy = abs(y2-y1)
    error = dx//2
    ysteeep = 1 if y1 < y2 else -1
    y = y1
    for x in range(x1, x2+1):
        if steep:
            surface.set_at((y,x) , color)
        else:
            surface.set_at((x,y) , color)
        error -= dy
        if error < 0                                                                      :
            y += ysteeep
            error += dx

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Bresenhams')
green = (0,255,0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            Drawline(screen  , green , (50,50) , (450 ,400))
    pygame.display.flip()
pygame.quit
 