import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, altura, cor):
        super().__init__()
        self.image = pygame.Surface((4, 16))
        self.image.fill(cor)
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.limite_y = altura

    def destruir(self):
        if self.rect.y <= -50 or self.rect.y >= self.limite_y + 50:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destruir()

