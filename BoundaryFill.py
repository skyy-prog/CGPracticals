import pygame
green = (0,0,0)

def FillBoundary(surface , color , cx,cy,x,y):
    surface.set_at((cx+x , cy+y ) , color)
    surface.set_at((cx-x , cy+y ) , color)
    surface.set_at((cx+x , cy-y ) , color)
    surface.set_at((cx-x , cy-y ) , color)
    surface.set_at((cx+y , cy+x  ) , color)
    surface.set_at((cx-y , cy+x ) , color)
    surface.set_at((cx+y , cy-x ) , color)
    surface.set_at((cx-y , cy-x ) , color)

def CalBoundaryFILL(surface ,center , radius ):
    cx,cy = center
    x,y = 0,radius
    p = 1-radius
    while x<=y:
        FillBoundary(surface , green , cx , cy , x,y)
        x+=1
        if p <0:
            p+= 289 * x+1
        else:
            # y -=1
            p += 2 * (x-y)+1
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('FiLLboundary')
green = (0,255,0)
running = True
while running:
    screen.fill((120,155,00))
    CalBoundaryFILL(screen , (300, 250) , 100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
     




   
