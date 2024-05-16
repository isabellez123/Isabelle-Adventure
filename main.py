import pygame
import random
from user_player import Player

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 28)
pygame.display.set_caption("Balloon Flight!")

FPS = 60

start_message = "Welcome to Isabelle's Awesome Adventure."
instruct_1 = "Use controls WASD for movement"
instruct_2 = "Make bold decisions and interact with characters. Click to start"
end_message = "Congrats! You've completed the journey."


# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
PLAYER_START_X = 20
PLAYER_START_Y = 440

#images
bg_1 = pygame.image.load("background.png")
bg_2 = pygame.image.load("background_2.png")
house = pygame.image.load("house.png")
tree = pygame.image.load("tree.png")

#rendering
display_end_message = my_font.render(end_message, True, (255, 0, 0))
display_start_message = my_font.render(start_message, True, (255, 0, 0))

my_font = pygame.font.SysFont('Arial', 15)
display_instruct_1 = my_font.render(instruct_1, True, (255, 255, 255))
display_instruct_2 = my_font.render(instruct_2, True, (255, 255, 255))

user_player = Player(PLAYER_START_X, PLAYER_START_Y)

INITIAL_HOUSE_X = 900
INITIAL_TREE_X = 1100
house_x = INITIAL_HOUSE_X
tree_x = INITIAL_TREE_X

# render the text for later

run = True
game_over = False
start_screen = True

# -------- Main Program Loop -----------
frame = 0
direction = "down"

while run:

    # -- start screen
    if start_screen:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_screen = False

        # -- start screen here
        screen.blit(bg_1, (0, 0))
        screen.blit(display_start_message, (200, 200))
        screen.blit(display_instruct_1, (200, 250))
        screen.blit(display_instruct_2, (200, 300))
        pygame.display.update()

    # -- game
    if not game_over and not start_screen:

        if house_x < -250:
            house_x = INITIAL_HOUSE_X

        if tree_x < -250:
            tree_x = INITIAL_TREE_X

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                user_player.move_player("right")
            if keys[pygame.K_a]:
                user_player.move_player("left")

        if user_player.rect.x <= 150:
            house_x = house_x - 2
            tree_x = tree_x - 2
            user_player.move_player(direction)

            screen.blit(bg_1, (0, 0))
            screen.blit(house, (house_x, 360))
            screen.blit(tree, (tree_x, 360))
            screen.blit(user_player.image, user_player.rect)
            pygame.display.update()


        if user_player.rect.x == 300:
            bg_1 = bg_2
            size = (800, 600)
            screen = pygame.display.set_mode(size)
            user_player.move_player(direction)

            screen.blit(bg_1, (0, 0))
            screen.blit(user_player.image, user_player.rect)
            pygame.display.update()

    # clock.tick(FPS)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
