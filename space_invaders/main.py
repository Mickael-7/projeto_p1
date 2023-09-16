import pygame
import sys
import objeto
import os
import igor
from player import Player
from alien import Aliens
from boss import Boss
from random import choice
from laser import Laser


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


class Game:
    def __init__(self):
        player_sprite = Player((largura/2, altura), largura, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.som_morte = pygame.mixer.Sound('music/invaderkilled_.mp3')
        self.som_vida_player = pygame.mixer.Sound('music/explosion.wav')
        self.musica_fundo = pygame.mixer_music.load('music/Battle Special.mp3')
        self.boss_hit = pygame.mixer.Sound('music/video-game-hit-noise-001-135821.mp3')
        self.kill = 0
        self.lives = 3
        self.y_creditos = 0

        boss_sprite = Boss((300, 35))
        self.boss = pygame.sprite.GroupSingle(boss_sprite)
        self.boss_direcao = 1.5
        self.life_boss = 5
        self.boss_lasers = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.alien_setup(rows=6, cols=8)
        self.alien_direcao = 1

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

    def boss_posicao(self):
        for boss in self.boss:
            if boss.rect.right >= largura:
                self.boss_direcao = -2

            elif boss.rect.left <= 0:
                self.boss_direcao = 1.5

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
            laser_sprite = Laser(random_alien.rect.center, 6, altura, 'red')
            self.alien_lasers.add(laser_sprite)

    def boss_shoot(self):
        if self.boss.sprites():
            for boss in self.boss:
                laser_boss = Laser(boss.rect.center, 8, altura, 'green')
                self.boss_lasers.add(laser_boss)

    def colisao(self):
        kill_boss = False
        if self.life_boss <= 0:
            kill_boss = True

        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                if pygame.sprite.spritecollide(laser, self.blocos, True):
                    laser.kill()

        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                if pygame.sprite.spritecollide(laser, self.aliens, True):
                    laser.kill()
                    self.kill += 1
                    self.som_morte.play()

        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                if pygame.sprite.spritecollide(laser, self.boss, kill_boss):
                    laser.kill()
                    self.kill += 10
                    self.life_boss -= 1
                    self.boss_hit.play()

        if self.aliens:
            for aliens in self.aliens:
                pygame.sprite.spritecollide(aliens, self.blocos, True)
                if pygame.sprite.spritecollide(aliens, self.player, True):
                    self.lives = 0
                    self.som_morte.play()
                if aliens.rect.y >= 630:
                    self.lives = 0

        if self.alien_lasers:
            for laser in self.alien_lasers:
                if pygame.sprite.spritecollide(laser, self.blocos, True):
                    laser.kill()

                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1
                    self.som_vida_player.play()

        if self.boss_lasers:
            for laserB in self.boss_lasers:
                if pygame.sprite.spritecollide(laserB, self.blocos, True):
                    laserB.kill()

                if pygame.sprite.spritecollide(laserB, self.player, False):
                    laserB.kill()
                    self.lives -= 1
                    self.som_vida_player.play()

    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(tela)
        self.player.draw(tela)

        self.boss.draw(tela)
        self.boss_posicao()
        self.boss.update(self.boss_direcao)
        self.boss_lasers.update()
        self.boss_lasers.draw(tela)

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
    fonte3 = pygame.font.SysFont('arial', 20, True, True)
    fonte2 = pygame.font.SysFont('arial', 15, True, True)
    pygame.mixer.music.play(-1)

    alienL = pygame.USEREVENT + 1
    pygame.time.set_timer(alienL, 700)
    som_de_perdedor = 1
    som_de_vencedor = 1
    bossL = pygame.USEREVENT + 1
    pygame.time.set_timer(bossL, 900)

    while True:

        if game.lives > 0 and game.kill < 108:

            pontos = f'PONTOS: {game.kill}'
            vidas = f'VIDAS: {game.lives}'
            texto_formatado = fonte.render(pontos, True, (255, 255, 255))
            texto_formatado_2 = fonte.render(vidas, True, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == alienL:
                    game.alien_shoot()
                if event.type == bossL:
                    game.boss_shoot()

            tela.blit(bg, (0, 0))

            real_y = altura % bg.get_rect().height

            tela.blit(bg, (0, real_y - bg.get_rect().height))
            tela.blit(texto_formatado, (15, 20))
            tela.blit(texto_formatado_2, (520, 20))
            if real_y < 650:
                tela.blit(bg, (0, real_y))
            altura += 1

            game.run()

            pygame.display.flip()
            fps.tick(60)
        elif game.lives == 0 and game.kill < 108:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.mixer.music.unload()
            tela.blit(bg, (0, 0))

            if som_de_perdedor == 1:
                som_loser = pygame.mixer.Sound('music/Sound _Fail.mp3')
                som_loser.play()
                som_de_perdedor = 0

            loser2 = 'VOCÊ FALHOU COM SUA MISSÃO'
            loser3 = 'PRESSIONE "R" PARA TENTAR NOVAMENTE'
            loser = 'WASTED'

            texto_loser = fonte.render(loser, True, (255, 0, 0))
            texto_loser_2 = fonte2.render(loser2, True, (255, 255, 255))
            texto_loser_3 = fonte2.render(loser3, True, (255, 255, 255))

            tela.blit(texto_loser, (258, 220))
            tela.blit(texto_loser_2, (158, 300))
            tela.blit(texto_loser_3, (128, 350))

            tecla = pygame.key.get_pressed()
            pygame.display.flip()
            fps.tick(60)

            if tecla[pygame.K_r]:
                game.lives = 5
                game.run()
                restart_program()
        elif game.kill >= 108:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.mixer.music.unload()

            if som_de_vencedor == 1:
                som_vencedor = pygame.mixer.Sound('music/vencedor.mp3')
                som_vencedor.play()
                som_de_vencedor = 0


            tela.blit(bg, (0, 0))

            real_y = altura % bg.get_rect().height

            tela.blit(bg, (0, real_y - bg.get_rect().height))

            if real_y < 650:
                tela.blit(bg, (0, real_y))
            altura += 1

            game.y_creditos -= 1
            linhas = igor.credito.split('\n')
            y = 650
            for linha in linhas:
                texto_renderizado = fonte3.render(linha, True, 'yellow')
                tela.blit(texto_renderizado, (50, y + game.y_creditos))
                y += 30

            pygame.display.flip()
            fps.tick(60)
            if game.y_creditos <= -5755:
                pygame.quit()
                sys.exit()
                