'''import pygame


class Boss(pygame.sprite.Sprite):
    def __init__(self, pos, speed, x_inicio):
        super().__init__()
        self.image = pygame.image.load('sprite/boss.png').convert_alpha()
        self.rect = self.image.get_rect(midtop=pos)
        self.speed = speed
        self.x_inicio = x_inicio

    def movimento(self):
        if self.rect.right >= 600:
            self.rect.y = self.rect.right
            self.rect.x -= self.speed
        elif self.rect.right < 600 and self.rect.y < 298:
            self.rect.x += self.speed
            self.rect.y += self.speed






    def update(self):
        self.movimento()'''

