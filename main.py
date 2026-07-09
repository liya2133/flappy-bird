import pygame
from bird import Bird
from pipe import Pipe
from camera_thread import CameraThread

pygame.init()

# Screen settings
WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gesture Controlled Flappy Bird")

clock = pygame.time.Clock()

# Load images
background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

ground = pygame.image.load("assets/ground.png")
ground = pygame.transform.scale(ground, (500, 100))

# Game objects
bird = Bird()
tracker = CameraThread()   # <-- Add this line
pipes = [Pipe(600)]

pipe_timer = 0
score = 0

font = pygame.font.SysFont("Arial", 40)
game_over_font = pygame.font.SysFont("Arial", 55)
restart_font = pygame.font.SysFont("Arial", 25)

game_over = False

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            pass

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:

                    bird = Bird()
                    tracker = CameraThread()
                    pipes = [Pipe(600)]

                    pipe_timer = 0
                    score = 0
                    game_over = False

    if not game_over:

        if tracker.get_flap():
            bird.flap()

        bird.update()

        pipe_timer += 1

        if pipe_timer >= 90:
            pipes.append(Pipe(600))
            pipe_timer = 0

        # Move pipes and update score
        for pipe in pipes:

            pipe.update()

            if not pipe.passed and pipe.x + 80 < bird.x:
                pipe.passed = True
                score += 1

        # Remove off-screen pipes
        pipes = [pipe for pipe in pipes if pipe.x > -100]

        # Collision detection
        bird_rect = bird.get_rect()

        for pipe in pipes:

            top_rect, bottom_rect = pipe.get_rects()

            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                game_over = True

        # Ground collision
        if bird.y >= 560:
            game_over = True

    # Draw everything
    screen.blit(background, (0, 0))

    for pipe in pipes:
        pipe.draw(screen)

    bird.draw(screen)

    screen.blit(ground, (0, 600))

    # Score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    # Game Over
    if game_over:

        text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (70, 240))

        restart = restart_font.render("Press R to Restart", True, (255, 255, 255))
        screen.blit(restart, (140, 320))

    pygame.display.update()
tracker.stop()
pygame.quit()