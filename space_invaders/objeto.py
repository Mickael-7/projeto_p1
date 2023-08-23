import pygame


class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, tam, color, x, y):
        super().__init__()
        self.image = pygame.Surface((tam,tam))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))


shape = [
'  xxxxxxx',
' xxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',
'xxx     xxx',
'xx       xx']