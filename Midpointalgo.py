import pygame
# pygame.init()
# width, height = 600, 500
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Midpoint Circle Algorithm")

# WHITE = (45, 134, 155)
# BLACK = (0, 0, 0)

# def draw_circle_points(surface, color, cx, cy, x, y):  
#     surface.set_at((cx + x, cy + y), color)
#     surface.set_at((cx - x, cy + y), color)
#     surface.set_at((cx + x, cy - y), color)
#     surface.set_at((cx - x, cy - y), color)
#     surface.set_at((cx + y, cy + x), color)
#     surface.set_at((cx - y, cy + x), color)
#     surface.set_at((cx + y, cy - x), color)
#     surface.set_at((cx - y, cy - x), color)

# def midpoint_circle(surface, color, center, radius):
#     cx, cy = center
#     x, y = 0, radius
#     p = 1 - radius

#     while x <= y:
#         draw_circle_points(surface, color, cx, cy, x, y)
#         x += 1
#         if p < 0:
#             p += 2 * x + 1
#         else:
#             y -= 1
#             p += 2 * (x - y) + 1

# running = True
# while running:
#     screen.fill(WHITE)
 
#     midpoint_circle(screen, BLACK, (300, 250), 100)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.display.update()

# pygame.quit()

black= (127,50,103)
# def DRAWCIRCLE(surface , color , cx ,cy , x , y):
#     surface.set_at((cx + x , cy + y) , color)
#     surface.set_at((cx - x , cy + y) , color)
#     surface.set_at((cx + x , cy - y) , color)
#     surface.set_at((cx - x , cy - y) , color)
#     surface.set_at((cx + y , cy + x) , color)
#     surface.set_at((cx - y , cy + x) , color)
#     surface.set_at((cx + y , cy - x) , color)
#     surface.set_at((cx - y , cy - x) , color)

# def midCircle(surface , center  , radius):
#     cx , cy = center
#     x,y =  0,radius
#     p = 1-radius
#     while x <=y:
#         DRAWCIRCLE(surface , black  , cx , cy , x , y)
#         x+=1
#         if p<0:
#             p += 2 * x +1
#         else:
#             y-=1
#             p += 2 * (x-y)+1

# def DRAWLINE(surface , color  , cx,cy,x,y):
#     surface.set_at((cx + x , cy + y),color)
#     surface.set_at((cx - x , cy + y),color)
#     surface.set_at((cx + x , cy - y),color)
#     surface.set_at((cx - x , cy - y),color)
#     surface.set_at((cx + y , cy + x),color)
#     surface.set_at((cx - y , cy + x),color)
#     surface.set_at((cx + y , cy - x),color)
#     surface.set_at((cx - y , cy - x),color)
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
            p += 2 * x+100
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

