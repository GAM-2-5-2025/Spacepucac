import pygame,sys
from player import Player


class Game:
    def __init__(self):
        player_sprite = Player((300,300))
        self.player = pygame.sprite.GroupSingle(player_sprite)
    def run(self):
        self.player.draw(screen)
    

if __name__ == '__main__':
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
    game = Game()
    
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((0,0,0))
        game.run()
        y=y+0.1
        vrhy = vrhy+0.1
        screen.blit(pozadina,(x,y))
        screen.blit(pozadina,(x,vrhy))
        if vrhy>=0:
            y=0
            vrhy=-window_height
            

        pygame.display.update()


    pygame.quit()
