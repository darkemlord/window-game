import pygame as pg

#Initialize pygame
pg.init()

#Create a display surface and set its caption

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Drawing objects") #Set the window title

#Define colors as RBG tuples

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#Give a background color to the display
display_surface.fill(BLUE)

#Draw various shapes on our display
#Line(surface, color, starting point, ending point, thickness)
pg.draw.line(display_surface,RED,(0,0), (600,600), 5)
pg.draw.line(display_surface,GREEN,(0,600), (600,0), 5)

#Circle(surface, color, center, radius, thickness... 0 for fill)
pg.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH // 2,WINDOW_HEIGHT // 2), 50, 2)

#Rectangle(surface, color, (top-left x, top-left y, width, height))
pg.draw.rect(display_surface, CYAN, (500,0, 100, 100))

#The main game loop
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    #Update the display
    pg.display.flip()
#End the game
pg.quit()
