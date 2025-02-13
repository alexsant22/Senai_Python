import pygame
import random

class Obstacle:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x -= self.speed

    def off_screen(self, screen_width):
        return self.x + self.width < 0

    def reset_position(self, screen_width):
        self.x = screen_width
        self.y = random.randint(100, 400)  # Altura aleatória para o obstáculo
