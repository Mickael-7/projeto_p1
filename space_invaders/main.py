import pygame, sys
from player import Player
class Game:
    def __init__(self):
        player_sprite = Player((largura/2, altura),largura,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()

        self.player.draw(tela)

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
