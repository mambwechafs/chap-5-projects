import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")

# Load game assets
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")
background_img = pygame.image.load("background.png")
explosion_sound = pygame.mixer.Sound("explosion.wav")

# Player properties
player_x = 370
player_y = 480
player_speed = 5

# Enemy properties
enemy_x = random.randint(0, window_width - 64)
enemy_y = random.randint(50, 150)
enemy_speed = 2

# Bullet properties
bullet_x = 0
bullet_y = 480
bullet_speed = 10
bullet_state = "ready"

# Game loop
running = True
while running:
    # Fill the window with the background image
    window.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_x += player_speed
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    bullet_state = "fire"

    # Update player position
    player_x = max(0, min(window_width - 64, player_x))
    window.blit(player_img, (player_x, player_y))

    # Update enemy position
    enemy_x += enemy_speed
    if enemy_x <= 0 or enemy_x >= window_width - 64:
        enemy_speed *= -1
        enemy_y += 40
    window.blit(enemy_img, (enemy_x, enemy_y))

    # Update bullet position
    if bullet_state == "fire":
        window.blit(bullet_img, (bullet_x + 16, bullet_y))
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = "ready"

    # Collision detection
    if bullet_state == "fire" and enemy_x <= bullet_x <= enemy_x + 64 and enemy_y <= bullet_y <= enemy_y + 64:
        explosion_sound.play()
        bullet_y = 480
        bullet_state = "ready"
        enemy_x = random.randint(0, window_width - 64)
        enemy_y = random.randint(50, 150)

    pygame.display.update()

# Quit the game
pygame.quit()
