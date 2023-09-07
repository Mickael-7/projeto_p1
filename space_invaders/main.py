import pygame
import sys
import objeto
from player import Player
from alien import Aliens
from random import choice
from laser import Laser


class Game:
    def __init__(self):
        player_sprite = Player((largura/2, altura), largura, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.kill = 0
        self.lives = 5

        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.alien_setup(rows=6, cols=8)
        self.alien_direcao = 1

        self.hit = 0

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

    def alien_setup(self, rows, cols, x_distancia=60, y_distancia=48, x_offset=70, y_offset=100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distancia + x_offset
                y = row_index * y_distancia + y_offset

                if row_index == 0:
                    alien_sprite = Aliens('redT', x, y)
                elif 1 <= row_index <= 2:
                    alien_sprite = Aliens('blueT', x, y)
                else:
                    alien_sprite = Aliens('whiteT', x, y)
                self.aliens.add(alien_sprite)

    def alien_posicao_check(self):
        all_aliens = self.aliens.sprites()
        for aliens in all_aliens:
            if aliens.rect.right >= largura:
                self.alien_direcao = -1
                self.alien_baixo(2)
            elif aliens.rect.left <= 0:
                self.alien_direcao = 1
                self.alien_baixo(2)

    def alien_baixo(self, distancia):
        if self.aliens:
            for aliens in self.aliens.sprites():
                aliens.rect.y += distancia

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6, altura)
            self.alien_lasers.add(laser_sprite)

    def colisao(self):
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                if pygame.sprite.spritecollide(laser, self.blocos, True):
                    laser.kill()

        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                if pygame.sprite.spritecollide(laser, self.aliens, True):
                    laser.kill()
                    self.kill += 1

        if self.aliens:
            for aliens in self.aliens:
                pygame.sprite.spritecollide(aliens, self.blocos, True)

        if self.alien_lasers:
            for laser in self.alien_lasers:
                if pygame.sprite.spritecollide(laser, self.blocos, True):
                    laser.kill()

                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        pygame.quit()
                        sys.exit()


    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(tela)
        self.player.draw(tela)

        self.aliens.draw(tela)
        self.alien_posicao_check()
        self.aliens.update(self.alien_direcao)
        self.alien_lasers.update()
        self.alien_lasers.draw(tela)
        self.blocos.draw(tela)

        self.colisao()


if __name__ == '__main__':
    pygame.init()
    largura = 600
    altura = 650
    tela = pygame.display.set_mode((largura, altura))
    fps = pygame.time.Clock()
    pygame.display.set_caption('space invaders')
    pygame_icon = pygame.image.load('sprite/jogador2.png')
    pygame.display.set_icon(pygame_icon)
    game = Game()
    bg = pygame.image.load('sprite/background.png').convert_alpha()
    bg = pygame.transform.scale(bg, (largura, altura))
    fonte = pygame.font.SysFont('arial', 15, True, True)
    fonte2 = pygame.font.SysFont('arial', 15, True, True)

    alienL = pygame.USEREVENT + 1
    pygame.time.set_timer(alienL, 700)

    while True:
        mensagem = f'PONTOS: {game.kill}'
        mensagem2 = f'VIDAS: {game.lives}'
        texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
        texto_formatado2 = fonte2.render(mensagem2, True, (255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == alienL:
                game.alien_shoot()

        tela.blit(bg, (0, 0))

        real_y = altura % bg.get_rect().height

        tela.blit(bg, (0, real_y - bg.get_rect().height))
        tela.blit(texto_formatado, (15, 20))
        tela.blit(texto_formatado2, (500,20))
        if real_y < 650:
            tela.blit(bg, (0, real_y))
        altura += 1

        game.run()

        pygame.display.flip()
        fps.tick(60)
