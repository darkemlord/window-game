import pygame as pg

# Initialize pygame
pg.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Mouse movement!")

# Set game values
VELOCITY = 10

# Load in Images
dragon_image = pg.image.load("./assets/basic_tutorial_assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)

# Main loop game
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # Move based on mouse Clicks
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y
        # Drag the object when the mouse button is clicked
        if event.type == pg.MOUSEMOTION and event.buttons[0] == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y
    # Fill the display surface to cover old images
    display_surface.fill((0, 0, 0))
    # Blit the images on the display
    display_surface.blit(dragon_image, dragon_rect)

    # Update the display
    pg.display.update()
# End the game
pg.quit()
