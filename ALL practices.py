# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption('First one')
# runing = True
# while runing :
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             runing = False
#     screen.fill((0,0,0))
#     pygame.display.flip()
# pygame.quit()

# import pygame
# screeen= pygame.display.set_mode((500,500))
# pygame.display.set_caption('basis shapes')
# BLUE = (0,0,255)
# RED = (120,0,90)
# running = True
# while running :
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             running = False
#     screeen.fill((255,255,255))
#     pygame.draw.circle(screeen , BLUE  , (130,120) , 100)
#     pygame.draw.line(screeen, RED , (50,90) , (300,450) , 2)
#     pygame.draw.rect(screeen , BLUE , [220,159,200,90] , 2)
#     pygame.draw.polygon(screeen, RED, [ (250, 420),   
#     (220, 460),  
#     (280, 460) ],2)
#     pygame.display.flip()
# pygame.quit()


# import pygame
# def DAA(surface, color , start ,end):
#     x1,y1 = start
#     x2,y2 = end
#     dx = x2-x1
#     dy = y2-y1
#     steps = max((abs(dx)  , abs(dy)))
#     Xincrement = dx/steps
#     Yincrement =dy/steps
#     x,y = x1,y1
#     for _  in range(steps+1):
#         surface.set_at((round(x) , round(y)) ,color)
#         x += Xincrement
#         y += Yincrement
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption('DAAAA algo')
# BLUE= (0,0,255)
# running = True
# while running :
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             running = False
#     screen.fill((255,255,255))
#     DAA(screen, BLUE, (300, 400), (100, 200))
#     pygame.display.flip()
# pygame.quit()

# import pygame
# def BREHEMSEN(surface , color , start,end):
#     x1,y1 = start
#     x2,y2 = end
#     dx = abs(x2-x1)
#     dy = abs(y2-y1)
#     steep = dy > dx
#     if steep:
#         x1,y1 = y1,x1
#         x2,y2 = y2 , x2
#     if x1 > x2:
#         x1,x2 = x2,x1
#         y1,y2 = y2,y1
#     dx = x2-x1
#     dy = abs(y2-y1)
#     error = dx//2
#     ysteep = 1 if y1 < y2 else -1
#     y = y1
#     for x in range(x1 , x2+1):
#         if steep:
#             surface.set_at((y,x) , color)
#         else:
#             surface.set_at((x,y) , color)
#         error -= dy
#         if error < 0:
#             y += ysteep
#             error += dx
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption('BRESEHMANS')
# running = True
# BLUE = (0,0,255)
# while running:
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             running = False
#     screen.fill((255,255,255))
#     BREHEMSEN(screen,  BLUE , (400,300) , (100,100))
#     pygame.display.flip()
# pygame.quit()


# import pygame
# def MINPOINT(surface , color , cx,cy , x,y):
#     surface.set_at((cx+x  , cy + y) ,color)
#     surface.set_at((cx-x  , cy + y) ,color)
#     surface.set_at((cx+x  , cy - y) ,color)
#     surface.set_at((cx-x  , cy - y) ,color)
#     surface.set_at((cx+y  , cy + x) ,color)
#     surface.set_at((cx-y  , cy + x) ,color)
#     surface.set_at((cx+y  , cy - x) ,color)
#     surface.set_at((cx-y  , cy - x) ,color)
# BLUE = (0,0,255)
# def secondMIS(surface , center , radius):
#     cx,cy = center
#     x,y = 0,radius
#     p = 1-radius
#     while x<= y:
#         MINPOINT(surface , BLUE , cx , cy , x , y )
#         x+=1
#         if p < 0:
#             p += 289* x+1
#         else:
#             # y -=1
#             p += 2 * (x-y) +1
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption('MIDPOINT ALGO')
# running = True
# while running:
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             running = False
#     screen.fill((255,255,255))
#     secondMIS(screen , (200,200) , 100)
#     pygame.display.flip()
# pygame.quit()

# import pygame
# import numpy as np
# def Translate(point , tx  , ty):
#     TranslateARRAY = np.array([
#         [1,0,tx],
#         [0,1,ty],
#         [0,0,1]
#     ])
#     HomoPOINT = [np.array([x,y,1]) for x,y in point]
#     TransPOINT = [TranslateARRAY @ p for p in HomoPOINT]
#     return [((int(p[0]) , int(p[1])) for p in TransPOINT)]
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption('ROTATION')
# running = True
# BLUE = (0,0,255)
# OGPOINT = [(200,200) , (200,100) , (100,100) , (100,200)]
# Transpoint = Translate(OGPOINT , 150,100)
# while running :
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             running = False
#     screen.fill((0,0,0))
#     pygame.draw.polygon(screen)


 