import pygame
scren = pygame.display.set_mode((500,500))
pygame.display.set_caption('second prac')
GREEN = (0,120,90)
RED = (0,0,255)
BLUE = (198 , 150,232)
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    scren.fill((255,255,255))
    pygame.draw.circle(scren , RED , (100,100),50)
    pygame.draw.line(scren , BLUE , (100,200) , (300,200) ,2 )
    pygame.draw.rect(scren , GREEN , (200,15,150,150) ,2)
    pygame.draw.polygon(scren , BLUE , [(150,300) , (250,300),(200,400)] ,2)
    pygame.display.flip()
pygame.quit()