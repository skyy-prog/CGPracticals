import pygame

black = (0,255,0)
 
def MINPOINT(surface ,colo , cx,cy , x,y):
    surface.set_at((cx+x , cy+y) , colo)
    surface.set_at((cx-x , cy+y) , colo)
    surface.set_at((cx+x , cy-y) , colo)
    surface.set_at((cx-x , cy-y) , colo)
    surface.set_at((cx+y , cy+x) , colo)
    surface.set_at((cx-y , cy+x) , colo)
    surface.set_at((cx+y , cy-x) , colo)
    surface.set_at((cx-y , cy-x) , colo)

def secondfunction(surface , center , radius):
    cx,cy = center 
    x,y = 0,radius
    p =1-radius
    while x<=y:
        MINPOINT(surface ,black , cx , cy,x,y)
        x+=1
        if p<0:
            p += 2 * x+1
        else:
            y -=1
            p+= 2 * (x-y)+1
 
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('MIdCIrcle')
running = True
while running:
    screen.fill((120,155,00))
    secondfunction(screen, (300, 250), 100)
    # secondfunction2(screen, (300, 250), 100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()

