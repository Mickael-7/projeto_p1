import pygame as pg
import constantes as cs
from pygame.locals import *
import random as rd
from sys import exit

class Jogo():

    pg.init()
    tela = pg.display.set_mode(cs.TAMANHO_TELA)
    largura, altura = cs.TAMANHO_TELA
    relogio = pg.time.Clock()
    janela = pg.display.set_caption('Snake')
jg = Jogo()
class Cobra:

    def __init__(self):
        self.x, self.y = jg.largura/2, jg.altura/2
        self.deslocamento = 1
        self.xdir = self.deslocamento
        self.ydir = 0
        self.corpo = [pg.Rect(self.x - cs.TAMANHO_QUADRADO, self.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)]
        self.cabeca = pg.Rect(self.x, self.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)
        self.delay = 90
        self.time = 0
        
    def delta_time(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.delay:
            self.time = time_now
            return True
        return False
    def morte(self):
        global maca
        self.x, self.y = jg.largura/2, jg.altura/2
        self.corpo = [pg.Rect(self.x - cs.TAMANHO_QUADRADO, self.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)]
        self.cabeca = pg.Rect(self.x, self.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)
        self.xdir = 1
        self.ydir = 0
        self.dead = False
        maca = Maca()
    def atualizar(self):
        for quadrado in self.corpo:
            if cobra.cabeca.x == quadrado.x and cobra.cabeca.y == quadrado.y:
                self.morte()
            
            if self.cabeca.x not in range(0, jg.largura) or self.cabeca.y not in range(0, jg.largura):
                self.morte()
        self.corpo.append(self.cabeca)
        
        for i in range(len(self.corpo) - 1):
            self.corpo[i].x, self.corpo[i].y = self.corpo[i + 1].x, self.corpo[i + 1].y
        
        self.cabeca.x += self.xdir * cs.TAMANHO_QUADRADO
        self.cabeca.y += self.ydir * cs.TAMANHO_QUADRADO
        self.corpo.remove(self.cabeca)

    def movimento(self):
        

        if event.key == pg.K_w or event.key == pg.K_UP:
            if cobra.ydir == cobra.deslocamento:
                pass
            else:
                cobra.xdir = 0
                cobra.ydir = - cobra.deslocamento

        elif event.key == pg.K_s or event.key == pg.K_DOWN:
            if cobra.ydir == -cobra.deslocamento:
                pass
            else:
                cobra.xdir = 0
                cobra.ydir = cobra.deslocamento
        elif event.key == pg.K_d or event.key == event.key == pg.K_RIGHT:
            if cobra.xdir == -cobra.deslocamento:
                pass
            else:
                cobra.xdir = cobra.deslocamento
                cobra.ydir = 0
        elif event.key == pg.K_a or event.key ==  pg.K_LEFT:
            if cobra.xdir == cobra.deslocamento:
                pass
            else:
                cobra.xdir = - cobra.deslocamento
                cobra.ydir = 0


class Maca:

    def __init__(self):
        self.x = int(rd.randint(0, jg.largura) / cs.TAMANHO_QUADRADO) * cs.TAMANHO_QUADRADO
        self.y = int(rd.randint(0, jg.largura) / cs.TAMANHO_QUADRADO) * cs.TAMANHO_QUADRADO
        self.retangulo = pg.Rect(self.x, self.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)

    def atualizarMaçã(self):
        pg.draw.rect(jg.tela, 'red', self.retangulo)


def desenhoGrade():
    for x in range(0, jg.largura, cs.TAMANHO_QUADRADO):
        for y in range(0, jg.altura, cs.TAMANHO_QUADRADO):
            rect = pg.Rect(x, y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)
            pg.draw.rect(jg.tela, '#3c3c3b', rect, 1)


def desenhar_pontuacao(pontuacao):
    fonte = pg.font.SysFont('Helveitica', 50)
    texto = fonte.render(f'Pontos: {pontuacao}', True, (255, 0, 0))
    jg.tela.blit(texto, [0, 0])


class Musicas():
    def __init__(self):

        self.musica_Colisao = pg.mixer.Sound("music/smw_stomp.wav")

    def musica_fundo(self):
        pg.mixer_music.set_volume(0.15)
        pg.mixer.music.load("music/nymzaro - Drunk on the Light.mp3")
        pg.mixer.music.play(-1)

desenhoGrade()
cobra = Cobra()
maca = Maca()

musicas = Musicas()
musicas.musica_fundo()
while True:
    jg.tela.fill('black')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN:
            cobra.movimento()

    if cobra.delta_time():
        cobra.atualizar()
        

    desenhoGrade()

    maca.atualizarMaçã()

    pg.draw.rect(jg.tela, "green", cobra.cabeca)


    for quadrado in cobra.corpo:
        pg.draw.rect(jg.tela, "green", quadrado)
    if cobra.cabeca.x == maca.x and cobra.cabeca.y == maca.y:
        cobra.corpo.append(pg.Rect(quadrado.x, quadrado.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO))
        maca = Maca()
        '''musicas.musica_Colisao.play()'''
    desenhar_pontuacao(len(cobra.corpo) - 1)
    
    pg.display.flip()
    jg.relogio.tick(30)