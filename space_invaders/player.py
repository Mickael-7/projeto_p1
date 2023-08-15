import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, limite, speed):
        super().__init__()
        self.image = pygame.image.load('sprite/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.max_x = limite
        self.ready = True

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed


    def recarga(self):
        pass

    def limite(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x:
            self.rect.right = self.max_x

    def update(self):
        self.get_input()
        self.limite()
