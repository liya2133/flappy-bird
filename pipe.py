import pygame
import random

class Pipe:
    def __init__(self, x):
        self.image = pygame.image.load("assets/pipe.png")
        self.image = pygame.transform.scale(self.image, (80, 500))

        self.x = x
        self.gap = 180
        self.height = random.randint(150, 450)

        self.speed = 4

        self.passed = False

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        top_pipe = pygame.transform.flip(self.image, False, True)

        screen.blit(
            top_pipe,
            (self.x, self.height - self.image.get_height())
        )

        screen.blit(
            self.image,
            (self.x, self.height + self.gap)
        )

    def get_rects(self):
        top_rect = pygame.Rect(
            self.x,
            self.height - self.image.get_height(),
            self.image.get_width(),
            self.image.get_height()
        )

        bottom_rect = pygame.Rect(
            self.x,
            self.height + self.gap,
            self.image.get_width(),
            self.image.get_height()
        )

        return top_rect, bottom_rect