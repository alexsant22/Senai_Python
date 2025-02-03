import pygame

class Player:
    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # Carregar a imagem do player
        self.image = pygame.image.load(r'img\\player.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  # Ajusta o tamanho da imagem

        self.vel = 10  # Velocidade do jogador

    def draw(self, screen):
        # Desenha a imagem na tela
        screen.blit(self.image, (self.x, self.y))

    def move(self, keys):
        # Movimentação somente para cima (W) e para baixo (S)
        if keys[pygame.K_w]:  # Tecla W para cima
            self.y -= self.vel
        if keys[pygame.K_s]:  # Tecla S para baixo
            self.y += self.vel

    def reset_position(self, x, y):
        self.x = x
        self.y = y
