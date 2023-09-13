import pygame


class Boss(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('sprite/boss.png').convert_alpha()
        self.rect = self.image.get_rect(midtop=pos)
        self.speed = 5

    def update(self,direcao):
        self.rect.x += direcao

