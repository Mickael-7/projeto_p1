import pygame as pg
import constantes as cs
import os
import random as rd
from sys import exit


class Jogo():
    def __init__(self):
        pg.init()
        self.tela = pg.display.set_mode(cs.TAMANHO_TELA)
        self.largura, self.altura = cs.TAMANHO_TELA
        self.relogio = pg.time.Clock()
        self.esta_rodando = True
        self.janela = pg.display.set_caption('Snake Game')
        self.imagem = pg.image.load('maca.jpg')
        self.fonte = pg.font.match_font(cs.FONTE)
        self.carregar_arquivos()

    def carregar_arquivos(self):
        diretorio_imagem = os.path.join(os.getcwd(), "imagens")
        self.diretorio_audios = os.path.join(os.getcwd(), "music")
        self.cobra_start_logo = os.path.join(diretorio_imagem, cs.COBRA_START_LOGO)
        self.cobra_start_logo = pg.image.load(self.cobra_start_logo).convert()

    def mostrar_texto(self, texto, cor, tamanho, x, y):
        # Exibe um texto na tela do jogo
        fonte = pg.font.SysFont(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto, texto_rect)
    def mostrar_start_logo(self, x, y):
        start_logo_rect = self.cobra_start_logo.get_rect()
        start_logo_rect.midtop = (x,y)
        self.tela.blit(self.cobra_start_logo, start_logo_rect)
    def mostrar_tela_start(self):
        pg.mixer.music.load(os.path.join(self.diretorio_audios,cs.MUSICA_START))
        pg.mixer_music.set_volume(0.10)
        pg.mixer.music.play()

        self.mostrar_start_logo(self.largura/2, 0)
        self.mostrar_texto(
            "-Precione  qualquer tecla para jogar",
             cs.PRETA,
            40,
            self.largura / 2,
            500
        )
        self.mostrar_texto(
            "Densolvolvido por: Nathan Dalbert e Pedro Ricardo",
            cs.PRETA,
            23,
            self.largura / 2,
            570
        )


        pg.display.flip()
        self.esperar_por_jogador()
    def esperar_por_jogador(self):
        esperando = True
        while esperando:
            self.relogio.tick(cs.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == pg.KEYDOWN:
                    esperando = False
                    pg.mixer_music.stop()


jg = Jogo()
jg.mostrar_tela_start()


class Cobra:

    def __init__(self):
        self.x, self.y = jg.largura / 2, jg.altura / 2
        self.deslocamento = 1
        self.xdir = self.deslocamento
        self.ydir = 0
        self.corpo = [pg.Rect(self.x, self.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)]
        self.cabeca = pg.Rect(self.x, self.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)
        self.delay = 90
        self.time = 0

    def delta_time(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.delay:
            self.time = time_now
            return True
        return False
        

    def reset(self):
        self.x, self.y = jg.largura / 2, jg.altura / 2
        self.corpo = [pg.Rect(self.x - cs.TAMANHO_QUADRADO, self.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)]
        self.cabeca = pg.Rect(self.x, self.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)
        self.xdir = 1
        self.ydir = 0
        self.delay = 90
        maca.reset()
        barreiras.barreiras.clear()

    def atualizar(self):
        for quadrado in self.corpo:
            if cobra.cabeca.x == quadrado.x and cobra.cabeca.y == quadrado.y:
                self.reset()
            for barreira in barreiras.barreiras:
                if cobra.cabeca.colliderect(barreira):
                  self.reset()
            if self.cabeca.x not in range(0, jg.largura) or self.cabeca.y not in range(cs.TAMANHO_QUADRADO, jg.largura):
                self.reset()
        
        
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
        elif event.key == pg.K_a or event.key == pg.K_LEFT:
            if cobra.xdir == cobra.deslocamento:
                pass
            else:
                cobra.xdir = - cobra.deslocamento
                cobra.ydir = 0


class Maca:

    def __init__(self):
        self.x = int(rd.randint(cs.TAMANHO_QUADRADO, jg.largura) / cs.TAMANHO_QUADRADO) * cs.TAMANHO_QUADRADO
        self.y = int(rd.randint(cs.TAMANHO_QUADRADO, jg.largura) / cs.TAMANHO_QUADRADO) * cs.TAMANHO_QUADRADO
        self.retangulo = pg.Rect(self.x , self.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)
    def reset(self):
        self.x = int(rd.randint(cs.TAMANHO_QUADRADO, jg.largura - cs.TAMANHO_QUADRADO) / cs.TAMANHO_QUADRADO) * cs.TAMANHO_QUADRADO
        self.y = int(rd.randint(cs.TAMANHO_QUADRADO, jg.altura - cs.TAMANHO_QUADRADO) / cs.TAMANHO_QUADRADO) * cs.TAMANHO_QUADRADO
        self.retangulo = pg.Rect(self.x, self.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)

    def maca_com_cimento(self):
        for barreira in barreiras.barreiras:
            if self.retangulo.colliderect(barreira):
                self.x = int(rd.randint(cs.TAMANHO_QUADRADO, jg.largura - cs.TAMANHO_QUADRADO) / cs.TAMANHO_QUADRADO) * cs.TAMANHO_QUADRADO
                self.y = int(rd.randint(cs.TAMANHO_QUADRADO, jg.altura - cs.TAMANHO_QUADRADO) / cs.TAMANHO_QUADRADO) * cs.TAMANHO_QUADRADO
                self.retangulo = pg.Rect(self.x, self.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)

    def atualizarMaçã(self):
        pg.draw.rect(jg.tela, 'red', self.retangulo)

def desenhoGrade():
    for x in range(0, jg.largura, cs.TAMANHO_QUADRADO):
        for y in range(cs.TAMANHO_QUADRADO, jg.altura, cs.TAMANHO_QUADRADO):
            rect = pg.Rect(x, y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO)
            pg.draw.rect(jg.tela, (42, 51, 26), rect, 1)


def desenhar_pontuacao(pontuacao):
    fonte = pg.font.SysFont('Helveitica', 30)
    frase = f"Pontos: {pontuacao}"
    texto = fonte.render(frase, True, (255, 255, 255))
    jg.tela.blit(texto, [255, 4])

class Musicas():
    def __init__(self):
        self.musica_Colisao = pg.mixer.Sound("music/smw_stomp.wav")

    def musica_fundo(self):
        pg.mixer_music.set_volume(0.15)
        pg.mixer.music.load("music/nymzaro - Drunk on the Light.mp3")
        pg.mixer.music.play(-1)

class Barreiras:
    def __init__(self, num_barreiras):
        self.barreiras = []
        self.num_barreiras = num_barreiras

    def gerar_barreiras(self):
        for i in range(self.num_barreiras):
            x = int(rd.randint(cs.TAMANHO_QUADRADO, jg.largura - cs.TAMANHO_QUADRADO) / cs.TAMANHO_QUADRADO) * cs.TAMANHO_QUADRADO
            y = int(rd.randint(cs.TAMANHO_QUADRADO, jg.altura - cs.TAMANHO_QUADRADO) / cs.TAMANHO_QUADRADO) * cs.TAMANHO_QUADRADO
            self.barreiras.append(pg.Rect(x, y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO))

    def barreira_tela(self):
        for macaxeira in self.barreiras:
            pg.draw.rect(jg.tela, cs.CINZA, macaxeira)


        
barreiras = Barreiras(1)
 
desenhoGrade()
cobra = Cobra()
maca = Maca()

musicas = Musicas()
musicas.musica_fundo()

while True:
    jg.tela.fill((155, 186, 89))
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
    barreiras.barreira_tela()
    jg.tela.blit(jg.imagem, (maca.x, maca.y))

    pg.draw.rect(jg.tela, (42, 51, 26), (0, 0, 600, cs.TAMANHO_QUADRADO))

    pg.draw.rect(jg.tela, (42, 51, 26), cobra.cabeca)
    for quadrado in cobra.corpo:
        pg.draw.rect(jg.tela, (42, 51, 26), quadrado)
    maca.maca_com_cimento()
    if cobra.cabeca.x == maca.x and cobra.cabeca.y == maca.y:
        cobra.corpo.append(pg.Rect(quadrado.x, quadrado.y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO))
        maca = Maca()
        x = int(rd.randint(cs.TAMANHO_QUADRADO, jg.largura - cs.TAMANHO_QUADRADO) / cs.TAMANHO_QUADRADO) * cs.TAMANHO_QUADRADO
        y = int(rd.randint(cs.TAMANHO_QUADRADO, jg.altura - cs.TAMANHO_QUADRADO) / cs.TAMANHO_QUADRADO) * cs.TAMANHO_QUADRADO
        barreiras.barreiras.append(pg.Rect(x, y, cs.TAMANHO_QUADRADO, cs.TAMANHO_QUADRADO))
        if len(cobra.corpo) >= 5:
            cobra.delay -= 1
        musicas.musica_Colisao.play()
    
    desenhar_pontuacao(len(cobra.corpo) * 10 - 10)
        
    pg.display.flip()
    jg.relogio.tick(cs.FPS)