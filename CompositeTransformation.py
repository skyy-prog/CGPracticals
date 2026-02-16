import pygame
import numpy as np
import math

def composite(points, trans):
    composite_matrix = np.identity(3)

    for matrix in trans:
        composite_matrix = np.dot(composite_matrix, matrix)

    Homopoints = [np.array([x, y, 1]) for x, y in points]
    TransPoints = [composite_matrix.dot(p) for p in Homopoints]

    return [(int(p[0]), int(p[1])) for p in TransPoints]


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Composite')

RECT = [(180, 50), (320, 50), (320, 130), (180, 130)]

TRI = [
    (250, 220),  
    (220, 260),   
    (280, 260)    
]
translate_matrix = np.array([
    [1, 0, 0],
    [0, 1, 150],
    [0, 0, 1]
])

 
angle = 0   
rad = math.radians(angle)
rotation_matrix = np.array([
    [math.cos(rad), -math.sin(rad), 0],
    [math.sin(rad),  math.cos(rad), 0],
    [0, 0, 1]
])

 
scaling_matrix = np.array([
    [1.0, 0, 0],
    [0, 1.0, 0],
    [0, 0, 1]
])

 
triangle_bottom = composite(TRI, [scaling_matrix, rotation_matrix, translate_matrix])

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

 
    pygame.draw.polygon(screen, (0, 0, 0), RECT, 2)
 
    pygame.draw.polygon(screen, (255, 0, 0), triangle_bottom, 2)

    pygame.display.flip()

pygame.quit()
