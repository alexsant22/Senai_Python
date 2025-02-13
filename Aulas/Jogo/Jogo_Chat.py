import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Mini Geometry Dash")

# Definir cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)

# Definir FPS (frames por segundo)
FPS = 60
clock = pygame.time.Clock()

# Configurações do personagem
personagem_width = 50
personagem_height = 50
personagem_x = 100
personagem_y = ALTURA - personagem_height
velocidade_pulo = -15
gravidade = 0.5
pulo = False

# Obstáculos
obstaculo_width = 50
obstaculo_height = 50
obstaculo_velocidade = 5
obstaculos = []

# Função para desenhar o personagem
def desenha_personagem(x, y):
    pygame.draw.rect(TELA, AZUL, (x, y, personagem_width, personagem_height))

# Função para criar obstáculos
def cria_obstaculo():
    altura = random.randint(100, ALTURA - 100)
    obstaculos.append([LARGURA, altura])

# Função para mover obstáculos
def move_obstaculos():
    global obstaculos
    for obstaculo in obstaculos:
        obstaculo[0] -= obstaculo_velocidade
    obstaculos = [obstaculo for obstaculo in obstaculos if obstaculo[0] > -obstaculo_width]
    return obstaculos

# Função para detectar colisões
def checa_colisao(x, y, obstaculos):
    for obstaculo in obstaculos:
        if x + personagem_width > obstaculo[0] and x < obstaculo[0] + obstaculo_width:
            if y + personagem_height > obstaculo[1] and y < obstaculo[1] + obstaculo_height:
                return True
    return False

# Função principal do jogo
def jogo():
    global personagem_y, pulo, obstaculos

    # Variáveis do jogo
    personagem_y_velocidade = 0
    jogo_rodando = True

    while jogo_rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Verifica o pulo
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not pulo:
                    personagem_y_velocidade = velocidade_pulo
                    pulo = True

        # Atualiza a física do personagem
        if pulo:
            personagem_y_velocidade += gravidade
            personagem_y += personagem_y_velocidade
            if personagem_y >= ALTURA - personagem_height:
                personagem_y = ALTURA - personagem_height
                pulo = False

        # Move obstáculos
        obstaculos = move_obstaculos()

        # Adiciona novos obstáculos
        if random.randint(1, 100) <= 2:  # Chance de gerar novo obstáculo
            cria_obstaculo()

        # Verifica colisões
        if checa_colisao(personagem_x, personagem_y, obstaculos):
            print("Game Over!")
            jogo_rodando = False

        # Preenche a tela com uma cor de fundo
        TELA.fill(PRETO)

        # Desenha o personagem e os obstáculos
        desenha_personagem(personagem_x, personagem_y)
        for obstaculo in obstaculos:
            pygame.draw.rect(TELA, BRANCO, (obstaculo[0], obstaculo[1], obstaculo_width, obstaculo_height))

        # Atualiza a tela
        pygame.display.update()

        # Controla o FPS
        clock.tick(FPS)

# Executa o jogo
jogo()