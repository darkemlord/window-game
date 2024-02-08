import pygame as pg

# Initialize pygame
pg.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Continuos movement")

# Set game values
VELOCITY = 5

# Load images
dragon_image = pg.image.load("./assets/basic_tutorial_assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Set FPS and Clock
FPS = 60
clock = pg.time.Clock()

# Main game Loop
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Get a list of all keys currently pressed
    keys = pg.key.get_pressed()

    # Move the dragon continuously
    if keys[pg.K_LEFT]:
        dragon_rect.x -= VELOCITY
    if keys[pg.K_RIGHT]:
        dragon_rect.x += VELOCITY
    if keys[pg.K_UP]:
        dragon_rect.y -= VELOCITY
    if keys[pg.K_DOWN]:
        dragon_rect.y += VELOCITY

    # fill the background
    display_surface.fill((0, 0, 0))

    # Blit surface object
    display_surface.blit(dragon_image, dragon_rect)

    # Update the display
    pg.display.update()

    # Tick the clock
    clock.tick(FPS)
# End of the game
pg.quit()
