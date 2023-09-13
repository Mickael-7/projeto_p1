import pygame


class Aliens(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        imagem = 'sprite/'+color+'.png'
        self.image = pygame.image.load(imagem).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direcao):
        self.rect.x += direcao