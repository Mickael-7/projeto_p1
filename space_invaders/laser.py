import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed,altura):
        super().__init__()
        self.image = pygame.Surface((4, 16))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.limite_y = altura

    def destruir(self):
        pass

    def update(self):
        self.rect.y += self.speed

