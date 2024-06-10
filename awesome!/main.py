import pygame
import time
from user_player import Player
from printword import PrintWord

# set up pygame modules1';d
pygame.init()
pygame.font.init()

FPS = 60
curr_idx = 0
letter_x = 200
num = 0
# messages

start_message = "Welcome to Isabelle's Adventure."
instruct_1 = "Use controls WASD for movement"
instruct_2 = "Make bold decisions and interact with characters. Click to start"
win_message = "WOOHOO! CONGRATS"
win_message2 = "He was a millionare in disguise and you passed the test."
win_message3 = "Thank you for being a good samaritan."
end_message = "Congrats! You've completed the journey."
# - background 1 stuff
bg1_dialogue_1 = "In order to complete this adventure, you must choose the correct options. Would you like to continue?"
bg1_option1 = "YES!"
bg1_option2 = "NO!"
# - background 2 stuff
bg2_dialogue_1 = "Help! My kids got lost. Please help me look for them!"
bg2_option1 = "Help Her "
bg2_option2 = " Don't Trust her"
# - background 3 stuff
bg3_dialogue_1 = "Good job! You found her kids! They're lost and hungry"
bg3_option1 = "Go back"
bg3_option2 = "Buy them food"
# - background 4 stuff
bg4_dialogue_1 = "Could you spare some change please?"
bg4_option1 = "Of course"
bg4_option2 = "no."
game_over = "WOMP WOMP"
game_over2 = "You made the wrong choice. Better luck next time >:)"

# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
PLAYER_START_X = 20
PLAYER_START_Y = 440

# images
bg_1 = pygame.image.load("background.png")
bg_2 = pygame.image.load("background_2.png")
bg_2 = pygame.transform.scale(bg_2, (1024, 600))
bg_3 = pygame.image.load("background_3.png")
bg_3 = pygame.transform.scale(bg_3, (800, 600))
bg_4 = pygame.image.load("background_4.png")
bg_4 = pygame.transform.scale(bg_4, (800, 600))
house = pygame.image.load("house.png")
tree = pygame.image.load("tree.png")
player_2 = pygame.image.load("player_2.png")
dialogue_box = pygame.image.load("msg_box2.png")

# rendering
my_font = pygame.font.SysFont('Arial', 20)

display_end_message = my_font.render(end_message, True, (255, 0, 0))
display_start_message = my_font.render(start_message, True, (255, 0, 0))
display_game_over2 = my_font.render(game_over2, True, (255, 255, 255))
display_win_message2 = my_font.render(win_message2, True, (255, 255, 255))
display_win_message3 = my_font.render(win_message3, True, (255, 255, 255))
textbox_1 = pygame.Rect(500, 300, 100, 60)
textbox_2 = pygame.Rect(200, 300, 100, 60)
n = 1
my_font = pygame.font.SysFont('Press Start 2Pd', 30)
display_game_over = my_font.render(game_over, True, (255, 255, 255))
display_win_message = my_font.render(win_message, True, (255, 255, 255))

#start the letter by letter things
print_instruct_1 = PrintWord(screen, instruct_1, 1)
print_instruct_2 = PrintWord(screen, instruct_2, 1)
# - bg1
print_bg1_dialogue_1 = PrintWord(screen, bg1_dialogue_1, 1)
print_bg1_option1 = PrintWord(screen, bg1_option1, 3)
print_bg1_option2 = PrintWord(screen, bg1_option2, 3)
# - bg2
print_bg2_dialogue_1 = PrintWord(screen, bg2_dialogue_1, 1)
print_bg2_option1 = PrintWord(screen, bg2_option1, 3)
print_bg2_option2 = PrintWord(screen, bg2_option2, 3)
# - bg3
print_bg3_dialogue_1 = PrintWord(screen, bg3_dialogue_1, 1)
print_bg3_option1 = PrintWord(screen, bg3_option1, 3)
print_bg3_option2 = PrintWord(screen, bg3_option2, 3)
# - bg4
print_bg4_dialogue_1 = PrintWord(screen, bg4_dialogue_1, 1)
print_bg4_option1 = PrintWord(screen, bg4_option1, 3)
print_bg4_option2 = PrintWord(screen, bg4_option2, 3)

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
win_screen = False
move = True
new_background = False
run = True
game_over = False
start_screen = True
bg1 = False
bg2 = False
bg3 = False
bg4 = False


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
                bg1 = True
        print_instruct_1.update()
        screen.fill((0, 0, 0))
        screen.blit(display_start_message, (200, 200))
        print_instruct_1.print_letter_by_letter(200, 250, 15, 1000)
        if print_instruct_1.printed:
            print_instruct_2.update()
            print_instruct_2.print_letter_by_letter(200, 300, 15, 1000)
        pygame.display.update()

    # -- bg1
    if not game_over and bg1:
        draw_interval = 1000/FPS
        next_draw_time = time.time() * 1000 + draw_interval
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
            keys = pygame.key.get_pressed()
            if move:
                if keys[pygame.K_d]:
                    user_player.move_player("right")
                    tree_x = tree_x - 15
                if keys[pygame.K_a]:
                    user_player.move_player("left")
                    tree_x = tree_x + 10
            mouse_pressed = pygame.mouse.get_pressed(3)

            if mouse_pressed[0] and not move and print_bg1_option2.printed:
                mouse_pos = pygame.mouse.get_pos()
                rectangle = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
                if textbox_2.contains(rectangle):
                    bg2 = True
                    bg1 = False
                    move = True
                    user_player.reset_player()
                if textbox_1.contains(rectangle):
                    end_screen = True
                    game_over = True

        n = n + 1
        if user_player.rect.x >= 360:
            move = False

        screen.blit(bg_1, (0, 0))
        screen.blit(tree, (tree_x, 360))
        screen.blit(user_player.image, user_player.rect)
        if not move:
            color_1 = (255, 192, 203)
            color_2 = (255, 0, 0)
            screen.blit(dialogue_box, (200, 100))
            pygame.draw.rect(screen, color_1, textbox_1)
            pygame.draw.rect(screen, color_2, textbox_2)
            print_bg1_dialogue_1.update()
            print_bg1_dialogue_1.print_letter_by_letter(220, 120, 15, 658)
            if print_bg1_dialogue_1.printed:
                print_bg1_option1.update()
                print_bg1_option1.print_letter_by_letter(200, 300, 50, 300)
            if print_bg1_option1.printed:
                print_bg1_option2.update()
                print_bg1_option2.print_letter_by_letter(500, 300, 50, 600)
        pygame.display.update()

        remaining_time = next_draw_time - time.time() * 1000

        if remaining_time > 0:
            time.sleep(remaining_time / 1000)

    # - bg2
    if not game_over and bg2:
        draw_interval = 1000 / FPS
        next_draw_time = time.time() * 1000 + draw_interval
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
            keys = pygame.key.get_pressed()
            if move:
                if keys[pygame.K_d]:
                    user_player.move_player("right")
                if keys[pygame.K_a]:
                    user_player.move_player("left")
            mouse_pressed = pygame.mouse.get_pressed(3)

            if mouse_pressed[0] and not move and print_bg2_option2.printed:
                mouse_pos = pygame.mouse.get_pos()
                rectangle = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
                if textbox_2.contains(rectangle):
                    bg3 = True
                    bg2 = False
                    move = True
                    user_player.reset_player()
                if textbox_1.contains(rectangle):
                    end_screen = True
                    game_over = True

        if user_player.rect.x >= 360:
            move = False

        screen.blit(bg_2, (0, 0))
        screen.blit(user_player.image, user_player.rect)
        if not move:
            color_1 = (255, 192, 203)
            color_2 = (255, 0, 0)
            screen.blit(dialogue_box, (200, 100))
            pygame.draw.rect(screen, color_1, textbox_1)
            pygame.draw.rect(screen, color_2, textbox_2)
            print_bg2_dialogue_1.update()
            print_bg2_dialogue_1.print_letter_by_letter(220, 120, 15, 658)
            if print_bg2_dialogue_1.printed:
                print_bg2_option1.update()
                print_bg2_option1.print_letter_by_letter(200, 300, 50, 300)
            if print_bg2_option1.printed:
                print_bg2_option2.update()
                print_bg2_option2.print_letter_by_letter(500, 300, 50, 600)
        pygame.display.update()

        remaining_time = next_draw_time - time.time() * 1000

        if remaining_time > 0:
            time.sleep(remaining_time / 1000)

    # - bg3
    if not game_over and bg3:
        draw_interval = 1000 / FPS
        next_draw_time = time.time() * 1000 + draw_interval
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
            keys = pygame.key.get_pressed()
            if move:
                if keys[pygame.K_d]:
                    user_player.move_player("right")
                if keys[pygame.K_a]:
                    user_player.move_player("left")
            mouse_pressed = pygame.mouse.get_pressed(3)

            if mouse_pressed[0] and not move and print_bg2_option2.printed:
                mouse_pos = pygame.mouse.get_pos()
                rectangle = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
                if textbox_2.contains(rectangle):
                    end_screen = True
                    game_over = True
                if textbox_1.contains(rectangle):
                    bg4 = True
                    bg3 = False
                    move = True
                    user_player.reset_player()

        if user_player.rect.x >= 360:
            move = False

        screen.blit(bg_3, (0, 0))
        screen.blit(user_player.image, user_player.rect)
        if not move:
            color_1 = (255, 192, 203)
            color_2 = (255, 0, 0)
            screen.blit(dialogue_box, (200, 100))
            pygame.draw.rect(screen, color_1, textbox_1)
            pygame.draw.rect(screen, color_2, textbox_2)
            print_bg3_dialogue_1.update()
            print_bg3_dialogue_1.print_letter_by_letter(220, 120, 15, 658)
            if print_bg3_dialogue_1.printed:
                print_bg3_option1.update()
                print_bg3_option1.print_letter_by_letter(200, 300, 50, 300)
            if print_bg3_option1.printed:
                print_bg3_option2.update()
                print_bg3_option2.print_letter_by_letter(500, 300, 50, 600)
        pygame.display.update()

        remaining_time = next_draw_time - time.time() * 1000

        if remaining_time > 0:
            time.sleep(remaining_time / 1000)

    # - bg4
    if not game_over and bg4:
        draw_interval = 1000 / FPS
        next_draw_time = time.time() * 1000 + draw_interval
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
            keys = pygame.key.get_pressed()
            if move:
                if keys[pygame.K_d]:
                    user_player.move_player("right")
                if keys[pygame.K_a]:
                    user_player.move_player("left")
            mouse_pressed = pygame.mouse.get_pressed(3)

            if mouse_pressed[0] and not move and print_bg2_option2.printed:
                mouse_pos = pygame.mouse.get_pos()
                rectangle = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
                if textbox_2.contains(rectangle):
                    win_screen = True
                    game_over = True
                if textbox_1.contains(rectangle):
                    end_screen = True
                    game_over = True

        if user_player.rect.x >= 360:
            move = False

        screen.blit(bg_4, (0, 0))
        screen.blit(user_player.image, user_player.rect)
        if not move:
            color_1 = (255, 192, 203)
            color_2 = (255, 0, 0)
            screen.blit(dialogue_box, (200, 100))
            pygame.draw.rect(screen, color_1, textbox_1)
            pygame.draw.rect(screen, color_2, textbox_2)
            print_bg4_dialogue_1.update()
            print_bg4_dialogue_1.print_letter_by_letter(220, 120, 15, 658)
            if print_bg4_dialogue_1.printed:
                print_bg4_option1.update()
                print_bg4_option1.print_letter_by_letter(200, 300, 50, 300)
            if print_bg4_option1.printed:
                print_bg4_option2.update()
                print_bg4_option2.print_letter_by_letter(500, 300, 50, 600)
        pygame.display.update()

        remaining_time = next_draw_time - time.time() * 1000

        if remaining_time > 0:
            time.sleep(remaining_time / 1000)

    if end_screen:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
        screen.fill((255, 0, 0))
        screen.blit(display_game_over, (270, 250))
        screen.blit(display_game_over2, (150, 350))
        pygame.display.update()

    if win_screen:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
        screen.fill((0, 255, 0))
        screen.blit(display_win_message, (270, 250))
        screen.blit(display_win_message2, (100, 300))
        screen.blit(display_win_message3, (100, 350))
        pygame.display.update()
# Once we have exited the main program loop we can stop the game engine:

pygame.quit()
