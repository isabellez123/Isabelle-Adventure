import pygame
import random
from balloon import Balloon

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 28)
pygame.display.set_caption("Balloon Flight!")

FPS = 500

start_message = "WELCOME TO BALLOON FIGHT."
instruct_1 = "Click the mouse to move the balloon up and down"
instruct_2 = "Dodge the Flying birds. Click to start!"
end_message = "You suck. Click to restart"


# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
BALLOON_START_X = 20
BALLOON_START_Y = 430

bg = pygame.image.load("background.png")
bg_2 = pygame.image.load("")
house = pygame.image.load("house.png")
tree = pygame.image.load("tree.png")

display_end_message = my_font.render(end_message, True, (255, 0, 0))
display_start_message = my_font.render(start_message, True, (255, 0, 0))

my_font = pygame.font.SysFont('Arial', 15)
display_instruct_1 = my_font.render(instruct_1, True, (255, 255, 255))
display_instruct_2 = my_font.render(instruct_2, True, (255, 255, 255))

balloon = Balloon(BALLOON_START_X, BALLOON_START_Y)

INITIAL_HOUSE_X = 900
INITIAL_TREE_X = 1100
house_x = INITIAL_HOUSE_X
tree_x = INITIAL_TREE_X

# render the text for later

# The loop will carry on until the user exits the game (e.g. clicks the close button).

run = True
game_over = False
start_screen = True

# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
points = 0
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
        screen.blit(bg, (0, 0))
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
                balloon.move_balloon("right")
            if keys[pygame.K_a]:
                balloon.move_balloon("left")
            if Balloon(100, 430):
                house_x = house_x - 30
                tree_x = tree_x - 30

            screen.blit(bg, (0, 0))
            screen.blit(house, (house_x, 360))
            screen.blit(tree, (tree_x, 360))
            screen.blit(balloon.image, balloon.rect)
            pygame.display.update()

            if Balloon(500,430):
                screen.blit(bg_2, (0, 0))

        balloon.move_balloon(direction)

        frame += 2

    # -- end screen
    if game_over:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                points = 0
                balloon.x = BALLOON_START_X
                balloon.y = BALLOON_START_Y
                house_x = INITIAL_HOUSE_X
                tree_x = INITIAL_TREE_X
                game_over = False

        # -- end screen here
        screen.blit(bg, (0, 0))
        screen.blit(display_end_message, (300, 300))
        pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
