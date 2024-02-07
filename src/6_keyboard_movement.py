import pygame as pg

# Initialize pygame
pg.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Discrete movement")

# Set game values
VELOCITY = 10

# Load in Images

dragon_image = pg.image.load("./assets/basic_tutorial_assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH // 2
dragon_rect.bottom = WINDOW_HEIGHT

print(dragon_image)
# Main loop game
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Check for discrete movements
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pg.K_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pg.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pg.K_DOWN:
                dragon_rect.y += VELOCITY
    # Fill the display surface to cover old images
    display_surface.fill((0, 0, 0))
    # Blit the images on the display
    display_surface.blit(dragon_image, dragon_rect)

    # Update the display
    pg.display.update()
# End the game
pg.quit()
