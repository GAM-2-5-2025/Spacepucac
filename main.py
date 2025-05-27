import pygame
import random
import sys
from player import Player 

class Objekti(pygame.sprite.Sprite):
    def __init__(self, window_width):
        super().__init__()
        self.image = pygame.image.load('meteor.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(midtop=(random.randint(0, window_width), -30))
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > window_height:
            self.kill()

class Game:
    def __init__(self):
        player_sprite = Player((window_width / 2, window_height), window_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.objects = pygame.sprite.Group()
        self.spawn_timer = pygame.time.get_ticks()

    def stvori_objekt(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_timer > 1000:
            self.objects.add(Objekti(window_width))
            self.spawn_timer = current_time

    def check_collisions(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.objects, True):
            self.player.sprite.health -= 1
            if self.player.sprite.health <= 0:
                self.end_game()

    def end_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        self.player.update()
        self.player.draw(screen)
        self.stvori_objekt()
        self.objects.update()
        self.objects.draw(screen)
        self.check_collisions()
        self.player.sprite.lasers.update()
        self.player.sprite.lasers.draw(screen)


if __name__ == '__main__':
    pygame.init()

    window_width = 700
    window_height = 700
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()

    pozadina = pygame.image.load('pozadina.png').convert()
    pozadina = pygame.transform.scale(pozadina, screen.get_size())

    game = Game()

    run = True
    x = 0
    y = 0
    vrhy = -window_height

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((0, 0, 0))

        y += 0.1
        vrhy += 0.1
        screen.blit(pozadina, (x, y))
        screen.blit(pozadina, (x, vrhy))

        
        text_color = (255, 255, 255)
        font = pygame.font.SysFont("Arial", 30)
        
        text = font.render(f"Zdravlje: {game.player.sprite.health}", True, text_color)
        screen.blit(text, (10, 10))

        game.run()

        if vrhy >= 0:
            y = 0
            vrhy = -window_height

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
