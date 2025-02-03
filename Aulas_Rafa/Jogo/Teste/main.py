import pygame
from game import Game

def main():
    pygame.init()

    # Definindo o tamanho da tela
    screen_width = 800
    screen_height = 600

    # Inicializando o jogo
    game = Game(screen_width, screen_height)

    # Loop principal do jogo
    game.game_loop()

    pygame.quit()

if __name__ == "__main__":
    main()
