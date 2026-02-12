import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption(("second program with basic shapes"))
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.circle(screen , RED , (100,100),20)
    pygame.draw.line(screen , GREEN , (50 ,50) ,(500 , 50) , 2)
    pygame.draw.rect(screen , GREEN , (200 , 100 , 200 , 100) , 2)
    pygame.draw.polygon(screen  , GREEN , [(150,300) , (250,300),(200,400)],2)
    pygame.display.flip()
pygame.quit()
