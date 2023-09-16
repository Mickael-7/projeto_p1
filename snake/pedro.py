import pygame as pg
from pygame.locals import *
import random as rd
from sys import exit

pg.init()
tamanhoQuadrado = 25
TAMANHO_TELA = (600,600)
tela = pg.display.set_mode(TAMANHO_TELA)
largura, altura = TAMANHO_TELA
relogio = pg.time.Clock()

janela = pg.display.set_caption('Snake')

def randomizar():
    x = int(rd.randint(tamanhoQuadrado, largura) / tamanhoQuadrado) * tamanhoQuadrado
    y = int(rd.randint(tamanhoQuadrado, largura) / tamanhoQuadrado) * tamanhoQuadrado
    return x, y

class Cobra:
    # Método construtor
    def _init_(self):
        self.x, self.y = largura/2, altura/2
        self.deslocamento = 1
        self.xdir = self.deslocamento
        self.ydir = 0
        self.cabeca = pg.Rect(self.x, self.y, tamanhoQuadrado, tamanhoQuadrado)
        self.corpo = [self.cabeca.copy()]
        self.delay = 90
        self.time = 0
    
    # Função para controlar a velocidade da cobra
    def delta_time(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.delay:
            self.time = time_now
            return True
        return False
    
    # Função para resetar os padrões quando a cobra morre
    def resetar(self):
        global maca
        self.x, self.y = largura/2 - tamanhoQuadrado, altura/2 - tamanhoQuadrado
        self.cabeca = pg.Rect(self.x, self.y, tamanhoQuadrado, tamanhoQuadrado)
        self.corpo = [self.cabeca.copy()]
        self.xdir = 1
        self.ydir = 0
        self.dead = False
        maca = Maca()

    # Motivos para que a cobra morra
    def morte(self):
        if cobra.cabeca.collidelistall(self.corpo):
            self.resetar()
        if self.cabeca.x not in range(0, largura) or self.cabeca.y not in range(tamanhoQuadrado, altura):
            self.resetar()

    def atualizar(self):    
        self.corpo.append(self.cabeca)
        for i in range(len(self.corpo) - 1):
            self.corpo[i].x, self.corpo[i].y = self.corpo[i + 1].x, self.corpo[i + 1].y
        
        self.cabeca.x += self.xdir * tamanhoQuadrado
        self.cabeca.y += self.ydir * tamanhoQuadrado
        self.corpo.remove(self.cabeca)

    # Função para movimentar a cobra, tanto com WASD quanto com as setas
    def movimento(self):
        if event.key == pg.K_w or event.key == pg.K_UP:
            if cobra.ydir == cobra.deslocamento:
                pass
            else:
                cobra.xdir = 0
                cobra.ydir = -cobra.deslocamento
        
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
                cobra.xdir = -cobra.deslocamento
                cobra.ydir = 0


class Maca:
    def _init_(self):
        self.x, self.y = randomizar()
        self.retangulo = pg.Rect(self.x, self.y, tamanhoQuadrado, tamanhoQuadrado)

    def desenharmaçã(self):
        pg.draw.rect(tela, '#F78B8B', self.retangulo)


def desenhar_parede(x, y):
    pg.draw.rect(tela, 'black', (x, y, tamanhoQuadrado, tamanhoQuadrado))

def desenhoGrade():
    for x in range(0, largura, tamanhoQuadrado):
        for y in range(tamanhoQuadrado, altura, tamanhoQuadrado):
            rect = pg.Rect(x, y, tamanhoQuadrado, tamanhoQuadrado)
            pg.draw.rect(tela, "#586C51", rect, 1)

def desenhar_pontuacao(pontuacao):
    fonte = pg.font.SysFont('Helveitica', 30)
    frase = f"Pontos: {pontuacao}"
    texto = fonte.render(frase, True, (255, 255, 255))
    tela.blit(texto, [255, 4])

'''class Musicas():
    def _init_(self):

        self.musica_Colisao = pg.mixer.Sound("music/smw_stomp.wav")

    def musica_fundo(self):
        pg.mixer_music.set_volume(0.15)
        pg.mixer.music.load("music/nymzaro - Drunk on the Light.mp3")
        pg.mixer.music.play(-1)'''
cobra = Cobra()
maca = Maca()

'''musicas = Musicas()
musicas.musica_fundo()'''
while True:
    tela.fill("#9EE983")
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            cobra.movimento()

    pg.draw.rect(tela, "#586C51", (0, 0, 600, tamanhoQuadrado))
    cobra.morte()
    cobra.atualizar()
    
    pg.draw.rect(tela, "#586C51", cobra.cabeca)
    for quadrado in cobra.corpo:
        pg.draw.rect(tela, "#586C51", quadrado)
    
    desenhoGrade()

    maca.desenharmaçã()

    # Condição para a cobra crescer quando comer a maçã
    if cobra.cabeca.colliderect(maca.retangulo):
        cobra.corpo.append(pg.Rect(quadrado.x, quadrado.y, tamanhoQuadrado, tamanhoQuadrado))
        maca = Maca()
        '''musicas.musica_Colisao.play()'''
    x_parede, y_parede = randomizar()

    if len(cobra.corpo) >= 5:
        desenhar_parede(x_parede, y_parede)
    
    # Desenhar os pontos
    desenhar_pontuacao(len(cobra.corpo)*10 - 10)
    
    # Atualização da tela e fps do display
    pg.display.flip()
    relogio.tick(10)