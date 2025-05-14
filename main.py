import pygame

pygame.init()

window_width = 1000
window_height = 700


pygame.display.set_mode((window_width, window_height))
screen = pygame.display.set_mode((window_width, window_height))

pozadina = pygame.image.load('pozadina.png').convert()

pozadina = pygame.transform.scale(pozadina, screen.get_size())

#glavno
run = True
x=0
y=0
vrhy=-window_height
while run:
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    y=y+0.1
    vrhy = vrhy+0.1
    screen.blit(pozadina,(x,y))
    screen.blit(pozadina,(x,vrhy))
    if vrhy>=0:
        y=0
        vrhy=-window_height
        

    pygame.display.update()


pygame.quit()
