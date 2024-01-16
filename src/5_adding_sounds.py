import pygame as pg

#Initialize pygame
pg.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Adding Sounds!")

#Load sound effects
sound_1 = pg.mixer.Sound("./assets/basic_tutorial_assets/sound_1.wav")
sound_2 = pg.mixer.Sound("./assets/basic_tutorial_assets/sound_2.wav")

#Play sound effects
sound_1.play()
pg.time.delay(2000)
sound_2.play()

#Load background music

pg.mixer.music.load("./assets/basic_tutorial_assets/music.wav")

#Play and stop music (infinite, start_time)
pg.mixer.music.play(-1,0.0)

#Main game loop
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

#End the game
pg.quit()
