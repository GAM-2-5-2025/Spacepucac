import pygame
import random
import sys
from player import Player


class Game:
    def __init__(self):
        player_sprite = Player((window_width/2,window_height),window_width,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    #VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
        self.objects = pygame.sprite.Group()
        self.spawn_timer = pygame.time.get_ticks()
        
    def stvori_objekt(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_timer > 1000:  
            self.objects.add(Objekti(window_width))
            self.spawn_timer = current_time
    ##AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            
    def run(self):
        self.player.update()
        self.player.draw(screen)

        #VVVVVVVVVVVVVVV
        self.stvori_objekt()
        self.objects.update()
        self.objects.draw(screen)
        #AAAAAAAAAAAAAAAAAAAAAA

#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
class Objekti(pygame.sprite.Sprite):
    def __init__(self, window_width):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))  
        self.rect = self.image.get_rect(
            midtop=(random.randint(0, window_width), -30)
        )
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > window_height:  
            self.kill()  
##AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

if __name__ == '__main__':
    pygame.init()

    window_width = 700
    window_height = 700

    clock = pygame.time.Clock()


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
        y=y+0.1
        vrhy = vrhy+0.1
        screen.blit(pozadina,(x,y))
        screen.blit(pozadina,(x,vrhy))
        game.run()
        
        if vrhy>=0:
            y=0
            vrhy=-window_height
            

        pygame.display.update()
        clock.tick(60)


    pygame.quit()
