import pygame


class Bird:
    def __init__(self):
        self.image = pygame.image.load("assets/bird.png")
        self.image = pygame.transform.scale(self.image, (50, 40))

        self.x = 100
        self.y = 250

        self.velocity = 0
        self.gravity = 0.5
        self.flap_strength = -8

    def flap(self):
        self.velocity = self.flap_strength

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.image.get_width(),
            self.image.get_height()
        )