import pygame as pg

# Initialize pygame
pg.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Blitting Text")
running = True

# Define colors as RBG tuples
BLACK = (0, 0, 0)
DARK_GREEN = (10, 50, 10)
GREEN = (0, 255, 0)

# See all available system fonts
fonts = pg.font.get_fonts()

# Load fonts
system_font = pg.font.SysFont("calibri", 64)
custom_font = pg.font.Font("./assets/basic_tutorial_assets/AttackGraffiti.ttf", 32)

# Define Text
system_text = system_font.render("Dragons Rule!", True, GREEN, DARK_GREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
custom_text = custom_font.render("Move the dragoon soon!", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100)

# The main game loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Blit to display
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    # Update the display
    pg.display.update()
# End game
pg.quit()
