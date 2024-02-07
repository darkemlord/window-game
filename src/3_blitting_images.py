import pygame as pg

# Initialize pygame
pg.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Blitting images")

# Create images

dragon_left_image = pg.image.load("./assets/basic_tutorial_assets/dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pg.image.load("./assets/basic_tutorial_assets/dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

# The main game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # Blit surface object at the given coordinates to our display
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    pg.draw.line(
        display_surface,
        "white",
        (WINDOW_WIDTH // 2, 0),
        (WINDOW_WIDTH // 2, WINDOW_HEIGHT),
        10,
    )

    # Update the display
    pg.display.update()
# End game
pg.quit()
