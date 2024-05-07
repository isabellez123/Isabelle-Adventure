import pygame
import random
import time
from fox import Fox
from fox_2 import Fox2
from coin import Coin
from redcoin import Red_coin
from bomb import Bomb

start_time = time.time()
red_coin_start = time.time()
red_coin_countdown = -1
# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Coin Collector!")
# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

name = "Collect coins as fast as you can!"
message = "Collision not detected"
r = 50
g = 0
b = 100

# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))

#initializing the objects

f = Fox(40, 60)
c = Coin(200, 85)
rc = Red_coin(200, 85)
f_2 = Fox2(40, 40)
# b = Bomb(200, 300)

score = 0
start = False
game_end = False
lose = False
red_coin_timer = 0
top_score = False
red_coin = False
bomb = 0

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

file = open("highscore", "r")
high_score = file.readline().strip()
print(int(high_score))

# -------- Main Program Loop -----------
while run:
    instruct_1 = my_font.render("Use ASWD to move", True, (255, 255, 255))
    instruct_2 = my_font.render("You have 10 seconds to collect 10 coins", True, (255, 255, 255))
    instruct_3 = my_font.render("Click anywhere on the screen to begin!", True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP and not start:  # Check for mouse click to start the game
            start = True

    if not start:
        screen.fill((r, g, b))
        screen.blit(f.image, f.rect)
        screen.blit(instruct_1, (150, 60))
        screen.blit(instruct_2, (150, 110))
        screen.blit(instruct_3, (150, 160))
        pygame.display.update()

    elif not game_end:
        countdown = 12
        elapsed_time = time.time() - start_time
        timer = countdown - elapsed_time
        timer = round(timer, 2)
        render_elapsed_time = my_font.render("Time: " + str(timer), True, (255, 255, 255))

        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_d]:
            f.move_direction("right")
        if keys[pygame.K_a]:
            f.move_direction("left")
        if keys[pygame.K_w]:
            f.move_direction("up")
        if keys[pygame.K_s]:
            f.move_direction("down")

        # blue fox

        if keys[pygame.K_RIGHT]:
            f_2.move_direction("right")
        if keys[pygame.K_LEFT]:
            f_2.move_direction("left")
        if keys[pygame.K_UP]:
            f_2.move_direction("up")
        if keys[pygame.K_DOWN]:
            f_2.move_direction("down")


        # collision
        if f.rect.colliderect(c.rect) or f_2.rect.colliderect(c.rect):
            message = "Collision detected"
            display_message = my_font.render(message, True, (255, 255, 255))
            x = random.randint(1, 400)
            y = random.randint(1, 300)
            c.set_location(x, y)
            score = score + 10
            render_score = my_font.render(str(score), True, (255, 255, 255))
        else:
            message = "Collision not detected"
            display_message = my_font.render(message, True, (255, 255, 255))

        # if f.rect.colliderect(b.rect):
        #     score = score - 10
        #     bomb = bomb + 1
        #     x_new = random.randint(445)
        #     y_new = random.randint(0, 280)
        #     b.set.location(x_new, y_new)
        #     display_bomb_count = my_font.render(("Bomb count is: ") + str(bomb), True, (255,255,255))
        #     render_score = my_font.render(str(score), True, (255, 255, 255))
        #
        # if bomb == 5:
        #     game_end = True

        if red_coin_countdown < 0:
            if random.randint(1, 30) == 1:
                x = random.randint(1, 400)
                y = random.randint(1, 300)
                rc.set_location(x, y)
                red_coin_start = time.time()
                red_coin_countdown = random.randint(3, 10)  # Randomize time for red coin appearance

        red_coin_elapsed_time = time.time() - red_coin_start
        red_coin_countdown = red_coin_countdown - red_coin_elapsed_time

        if f.rect.colliderect(rc.rect) or f_2.rect.colliderect(rc.rect):
            message = "Collision with red coin detected!"
            score = score + 25
            red_coin = False
            display_message = my_font.render(message, True, (255, 255, 255))
            rc.set_location(-100, -100)  # Move the red coin off-screen


        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False

        if timer <= 0 :
            game_end = True

            end_message = my_font.render("Game over, you win!", True, (255, 255, 255))
            screen.fill((r, g, b))
            screen.blit(end_message, (200, 150))
            pygame.display.update()

        else:
            if red_coin_countdown < 0:
                red_coin_countdown -= 1

            render_score = my_font.render("Score: " + str(score), True, (255, 255, 255))
            screen.fill((r, g, b))
            screen.blit(display_name, (0, 0))
            screen.blit(render_score, (0, 100))
            screen.blit(display_message, (0, 15))
            screen.blit(render_elapsed_time, (0, 150))
            screen.blit(rc.image, rc.rect)
            screen.blit(f_2.image, f_2.rect)
            screen.blit(f.image, f.rect)
            screen.blit(c.image, c.rect)
            pygame.display.update()

    # game ends
    if game_end == True:
        # high score stuff

        highscore_display = my_font.render("HIGHSCORE: " + str(high_score), True, (255, 255, 255))

        score_display = my_font.render(" YOUR SCORE: " + str(score), True, (255, 255, 255))
        screen.fill((r, g, b))
        screen.blit(highscore_display, (100, 100))
        screen.blit(score_display, (200, 200))
        pygame.display.update()
# Once we have exited the main program loop we can stop the game engine:
if int(high_score) < score:
    n = open("highscore", "w")
    n.write(str(score))

pygame.quit()
