import pygame
from user_player import Player

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 28)

FPS = 60

# messages

start_message = "Welcome to Isabelle's Adventure."
instruct_1 = "Use controls WASD for movement"
instruct_2 = "Make bold decisions and interact with characters. Click to start"
end_message = "Congrats! You've completed the journey."
dialogue_2 = "Brave choice. You may now move on to the challenge. Good luck!"
yes_box = "YES!"
no_box = "NO!"
game_over = "Womp Womp"
game_over2 = "boo hoo"

# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
PLAYER_START_X = 20
PLAYER_START_Y = 440

# images
bg_1 = pygame.image.load("background.png")
bg_2 = pygame.image.load("background_2.png")
bg_2 = pygame.transform.scale(bg_2, (1024, 600))
house = pygame.image.load("house.png")
tree = pygame.image.load("tree.png")
player_2 = pygame.image.load("player_2.png")
dialogue_box_1 = pygame.image.load("msg_box1.png")
curr_bg = bg_1

# rendering
display_end_message = my_font.render(end_message, True, (255, 0, 0))
display_start_message = my_font.render(start_message, True, (255, 0, 0))
textbox_1 = pygame.Rect(500, 300, 100, 60)
textbox_2 = pygame.Rect(200, 300, 100, 60)

my_font = pygame.font.SysFont('Arial', 15)
display_instruct_1 = my_font.render(instruct_1, True, (255, 255, 255))
display_instruct_2 = my_font.render(instruct_2, True, (255, 255, 255))
display_game_over2 = my_font.render(game_over2, True, (255, 255, 255))

my_font = pygame.font.SysFont('Arial', 50)

display_yes_box = my_font.render(yes_box, True, (255, 255, 255))
display_no_box = my_font.render(no_box, True, (255, 255, 255))
# display_dialogue_2 =
# display_game_over =
# display_game_won =

display_game_over = my_font.render(game_over, True, (255, 255, 255))

user_player = Player(PLAYER_START_X, PLAYER_START_Y)

INITIAL_HOUSE_X = 900
INITIAL_TREE_X = 1100
house_x = INITIAL_HOUSE_X
tree_x = INITIAL_TREE_X
PLAYER_2_START_X = 440
PLAYER_2_START_Y = 400
player_2_x = PLAYER_2_START_X
player_2_y = PLAYER_2_START_Y

# render the text for later

end_screen = False
move = True
new_background = False
run = True
game_over = False
start_screen = True
game_screen = False

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
                game_screen = True

        screen.fill((0, 0, 0))
        screen.blit(display_start_message, (200, 200))
        screen.blit(display_instruct_1, (200, 250))
        screen.blit(display_instruct_2, (200, 300))
        pygame.display.update()

    # -- game
    if not game_over and game_screen:

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
            keys = pygame.key.get_pressed()
            if move:
                if keys[pygame.K_d]:
                    user_player.move_player("right")
                    house_x = house_x - 15
                    tree_x = tree_x - 15
                if keys[pygame.K_a]:
                    user_player.move_player("left")
                    house_x = house_x + 10
                    tree_x = tree_x + 10
            mouse_pressed = pygame.mouse.get_pressed(3)
            if mouse_pressed[0] and not move:
                mouse_pos = pygame.mouse.get_pos()
                rectangle = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
                if textbox_2.contains(rectangle):
                    new_background = True
                    move = True
                    user_player.reset_player()
                if textbox_1.contains(rectangle):
                    end_screen = True
                    game_screen = False

        if user_player.rect.x >= 360:
            move = False

        if new_background:
            curr_bg = bg_2

        screen.blit(curr_bg, (0, 0))
        screen.blit(house, (house_x, 360))
        screen.blit(tree, (tree_x, 360))
        screen.blit(user_player.image, user_player.rect)
        if not move:
            color = (255, 192, 203)
            color_2 = (255, 0, 0)
            screen.blit(dialogue_box_1, (200, 100))
            pygame.draw.rect(screen, color, textbox_1)
            pygame.draw.rect(screen, color_2, textbox_2)
            screen.blit(display_no_box, (500, 300))
            # screen.blit(display_yes_box, (200, 300))
            screen.blit(player_2, (player_2_x, player_2_y))
        pygame.display.update()

    if end_screen:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
        screen.fill((0, 0, 0))
        screen.blit(display_game_over, (270, 250))
        screen.blit(display_game_over2, (300, 350))
        pygame.display.update()
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
