import pygame
import sys
from player import Player
import objeto


class Game:
    def __init__(self):
        player_sprite = Player((largura/2, altura), largura, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.shape = objeto.shape
        self.bloco_tam = 6
        self.blocos = pygame.sprite.Group()
        self.obstaculos_qtd = 4
        self.obstaculos_x_pos = [num * (largura/self.obstaculos_qtd)for num in range(self.obstaculos_qtd)]
        self.criar_multi_obj(*self.obstaculos_x_pos, x_inicio=largura/15, y_inicio=480)

    def criar_obstaculos(self, x_inicio, y_inicio, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_inicio + col_index * self.bloco_tam + offset_x
                    y = y_inicio + row_index * self.bloco_tam
                    bloco = objeto.Obstaculo(self.bloco_tam, (241, 79, 80), x, y)
                    self.blocos.add(bloco)

    def criar_multi_obj(self, *offset, x_inicio, y_inicio):
        for offset_x in offset:
            self.criar_obstaculos(x_inicio, y_inicio, offset_x)

    def run(self):
        self.player.update()

        self.player.sprite.lasers.draw(tela)
        self.player.draw(tela)

        self.blocos.draw(tela)


if __name__ == '__main__':
    pygame.init()
    largura = 600
    altura = 650
    tela = pygame.display.set_mode((largura, altura))
    fps = pygame.time.Clock()
    pygame.display.set_caption('space invaders')
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tela.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        fps.tick(60)
