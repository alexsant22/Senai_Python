import pygame
import random
import sys
import time

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pulo nas Plataformas")

# Definir cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (34, 177, 76)
AZUL = (0, 0, 255)

# FPS (frames por segundo)
FPS = 60
clock = pygame.time.Clock()

# Configuração do jogador
player_width = 50
player_height = 50
player_x = LARGURA // 2 - player_width // 2
player_y = ALTURA - player_height - 100  # Começa em uma plataforma fixa
player_velocidade = 5
pulo_forca = -12
gravidade = 0.5
player_velocidade_y = 0
em_pulo = False
jogo_iniciado = False  # O jogo não começa até o primeiro pulo

# Configuração das plataformas
plataforma_width = 100
plataforma_height = 20
plataformas = []

# Função para desenhar o jogador
def desenha_jogador(x, y):
    pygame.draw.rect(TELA, AZUL, (x, y, player_width, player_height))

# Função para desenhar as plataformas
def desenha_plataformas(plataformas):
    for p in plataformas:
        pygame.draw.rect(TELA, VERDE, (p[0], p[1], plataforma_width, plataforma_height))

# Função para criar novas plataformas
def cria_plataforma():
    largura = random.randint(50, LARGURA - plataforma_width - 50)
    altura = random.randint(100, ALTURA - 50)
    plataformas.append([largura, altura, time.time()])  # Adiciona o tempo de criação da plataforma

# Função para mover as plataformas (e desaparecer após um tempo)
def move_plataformas():
    global plataformas
    for p in plataformas:
        if time.time() - p[2] > 3:  # Plataforma desaparece após 3 segundos
            plataformas.remove(p)

# Função para detectar colisões com plataformas
def checa_colisao(x, y, plataformas):
    for p in plataformas:
        if p[0] < x + player_width and p[0] + plataforma_width > x:
            if p[1] < y + player_height and p[1] + plataforma_height > y:
                return p
    return None

# Função principal do jogo
def jogo():
    global player_x, player_y, player_velocidade_y, em_pulo, plataformas, jogo_iniciado

    # Cria a primeira plataforma fixa (na parte inferior da tela)
    plataformas.append([LARGURA // 2 - 50, ALTURA - 100, time.time()])  # Plataforma fixa onde o jogador começa

    # Variáveis do jogo
    player_y_velocidade = 0
    jogo_rodando = True

    while jogo_rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Verifica o pulo
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not em_pulo:  # Primeiro pulo
                    if not jogo_iniciado:
                        jogo_iniciado = True  # O jogo começa com o primeiro pulo
                    player_velocidade_y = pulo_forca
                    em_pulo = True

        if jogo_iniciado:
            # Atualiza a posição do jogador
            player_velocidade_y += gravidade
            player_y += player_velocidade_y

            # Verifica colisão com plataformas
            plataforma_colidida = checa_colisao(player_x, player_y, plataformas)

            if plataforma_colidida:
                if player_velocidade_y > 0:  # Colisão descendo
                    player_y = plataforma_colidida[1] - player_height  # Fixa o jogador na plataforma
                    player_velocidade_y = 0
                    em_pulo = False

            # Cria novas plataformas e move as existentes
            if random.randint(1, 100) <= 2:  # Chance de criar nova plataforma
                cria_plataforma()

            move_plataformas()

            # Verifica se o jogador caiu
            if player_y >= ALTURA:
                print("Você perdeu! Game Over.")
                jogo_rodando = False

        # Preenche a tela com a cor de fundo
        TELA.fill(PRETO)

        # Desenha o jogador e as plataformas
        desenha_jogador(player_x, player_y)
        desenha_plataformas(plataformas)

        # Atualiza a tela
        pygame.display.update()

        # Controla o FPS
        clock.tick(FPS)

# Executa o jogo
jogo()
