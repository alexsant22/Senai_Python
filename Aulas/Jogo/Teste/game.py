import random
import pygame
from player import Player
from obstacle import Obstacle

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Desviar dos Obstáculos")
        self.clock = pygame.time.Clock()
        self.running = True

        # Criando jogador com imagem
        self.player = Player(x=100, y=self.screen_height // 2, width=50, height=50, image_path='imagens/player.png')

        # Criando obstáculos
        self.obstacles = [
            Obstacle(x=self.screen_width + i * 300, y=random.randint(100, 400), width=50, height=50, color=(255, 0, 0), speed=3)
            for i in range(10)
        ]

        # Pontuação
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 30)

        # Velocidade dos obstáculos
        self.obstacle_speed = 3
        self.speed_increase_interval = 10

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def check_collisions(self):
        for obstacle in self.obstacles:
            if (self.player.x < obstacle.x + obstacle.width and
                self.player.x + self.player.width > obstacle.x and
                self.player.y < obstacle.y + obstacle.height and
                self.player.y + self.player.height > obstacle.y):
                return True
        return False

    def update_game(self):
        for obstacle in self.obstacles:
            obstacle.move()
            if obstacle.off_screen(self.screen_width):
                obstacle.reset_position(self.screen_width)
                self.score += 5

        if self.score % self.speed_increase_interval == 0 and self.score != 0:
            self.obstacle_speed += 0.5
            self.speed_increase_interval += 10

        for obstacle in self.obstacles:
            obstacle.speed = self.obstacle_speed

        # Atualizar a pontuação
        self.update_score()

        # Desenhar o jogador
        self.player.draw(self.screen)

        # Desenhar obstáculos
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        # Atualizar a tela
        pygame.display.update()

    def reset(self):
        self.player.reset_position(100, self.screen_height // 2)
        self.score = 0
        self.obstacle_speed = 3
        self.speed_increase_interval = 10
        self.obstacles = [
            Obstacle(x=self.screen_width + i * 300, y=random.randint(100, 400), width=50, height=50, color=(255, 0, 0), speed=self.obstacle_speed)
            for i in range(10)
        ]

    def game_loop(self):
        while self.running:
            self.handle_events()

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            if self.check_collisions():
                print("Game Over! Pontuação Final:", self.score)
                self.reset()

            self.screen.fill((0, 0, 0))  # Cor de fundo
            self.update_game()
            self.clock.tick(60)
