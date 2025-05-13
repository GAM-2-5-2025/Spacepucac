import pygame

pygame.init()
#namjestit prozor velicine
window_width = 1000
window_height = 700
game_display = pygame.display.set_mode((window_width, window_height))
#pozadina
pozadina = pygame.image.load('pozadina.png')

#pocetna pozicija
y = 0
#glavno
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #pomicanje pozadine
    y -=0.5
    #resetiranje slike
    if y == -1 * pozadina.get_height():
        y = 0
    game_display.blit(pozadina, (0, y))
    pygame.display.update()
pygame.quit()
