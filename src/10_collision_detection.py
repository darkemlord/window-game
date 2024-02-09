import pygame as pg, random

# Initialize pygame
pg.init()

# Display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Collision Detection")  # Set the window title

FPS = 60
clock = pg.time.Clock()

# Set game Values
LEVEL_UP = 1000
TIGER_APPEAR = 10
VELOCITY = 5
SCORE = 0

# Load sound effects
sound_1 = pg.mixer.Sound("./assets/basic_tutorial_assets/sound_1.wav")

# See All available system fonts
fonts = pg.font.get_fonts()

# Load Fonts

system_font = pg.font.SysFont("calibri", 20)

# Define text

system_text = system_font.render(f"Score: {SCORE}", True, "white")
system_text_rect = system_text.get_rect()
system_text_rect.topleft = (0, 0)

# Load images
dragon_image = pg.image.load("./assets/basic_tutorial_assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)

tiger_image = pg.image.load("./assets/basic_tutorial_assets/tiger.png")
tiger_image = pg.transform.scale(tiger_image, (32, 32))
tiger_rect = tiger_image.get_rect()
tiger_active = False
tiger_speed = 2

coin_image = pg.image.load("./assets/basic_tutorial_assets/coin.png")
coin_rect = coin_image.get_rect()
coins = [
    pg.Rect(
        random.randint(0, WINDOW_WIDTH - 32),
        random.randint(0, WINDOW_HEIGHT - 32),
        32,
        32,
    )
]
# Main loop game
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # Get a list of all keys currently being pressed down
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if keys[pg.K_RIGHT] and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    if keys[pg.K_UP] and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    if keys[pg.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY

    # Fill display surface
    display_surface.fill((0, 0, 0))

    # Check for collision between two rect
    for coin_rect in coins[:]:
        if dragon_rect.colliderect(coin_rect):
            SCORE += 1
            sound_1.play()
            new_coin_pos = pg.Rect(
                random.randint(0, WINDOW_WIDTH - 32),
                random.randint(0, WINDOW_HEIGHT - 32),
                32,
                32,
            )
            coins.append(new_coin_pos)
            coin_rect.left = random.randint(0, WINDOW_WIDTH - 32)
            coin_rect.top = random.randint(0, WINDOW_HEIGHT - 32)
            system_text = system_font.render(f"Score: {SCORE}", True, (255, 255, 255))

            # Reset to 1 every 100 multiple value and increase speed
            if SCORE % LEVEL_UP == 0:
                # Reset coins list
                coins = [
                    pg.Rect(
                        random.randint(0, WINDOW_WIDTH - 32),
                        random.randint(0, WINDOW_HEIGHT - 32),
                        32,
                        32,
                    )
                ]
                # Increase dragon speed
                VELOCITY += 1

    # ENEMY FLOW
    if SCORE >= TIGER_APPEAR and not tiger_active:
        tiger_active = True
        tiger_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    if tiger_active:
        if tiger_rect.x < dragon_rect.x:
            tiger_rect.x += tiger_speed
        elif tiger_rect.x > dragon_rect.x:
            tiger_rect.x -= tiger_speed
        if tiger_rect.y < dragon_rect.y:
            tiger_rect.y += tiger_speed
        elif tiger_rect.y > dragon_rect.y:
            tiger_rect.y -= tiger_speed

    if tiger_active:
        display_surface.blit(tiger_image, tiger_rect)

    if tiger_active and dragon_rect.colliderect(tiger_rect):
        SCORE = 0
        VELOCITY = 5
        tiger_active = False
        tiger_rect.center = (-100, -100)
        coins = [
            pg.Rect(
                random.randint(0, WINDOW_WIDTH - 32),
                random.randint(0, WINDOW_HEIGHT - 32),
                32,
                32,
            )
        ]

    for coin_rect in coins:
        display_surface.blit(coin_image, coin_rect)
        # pg.draw.rect(display_surface, (255, 255, 0), coin_rect, 1)

    # pg.draw.rect(display_surface, (0, 255, 0), dragon_rect, 1)
    # Blit assets
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(dragon_image, dragon_rect)

    # Update display
    pg.display.update()

    # Tick the  clock
    clock.tick(FPS)

# End game
pg.quit()
