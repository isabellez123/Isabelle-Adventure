import pygame


class PrintWord:

    def __init__(self, screen, string, frames_until_next_letter):
        self.frames_until_next_letter = frames_until_next_letter
        self.curr_idx = 0
        self.frames_passed = 0
        self.string = []
        self.letter_status = []
        for i in range(len(string)):
            self.string.append(string[i])
            self.letter_status.append(False)
        self.screen = screen
        self.printed = False

    def update(self):
        if self.curr_idx == len(self.string):
            self.printed = True
        if not self.printed:
            if self.frames_passed == self.frames_until_next_letter:
                self.letter_status[self.curr_idx] = True
                self.curr_idx += 1
                self.frames_passed = 0
        self.frames_passed += 1

    def print_letter_by_letter(self, x, y, font_size, next_line):
        x_value = x
        displacement = font_size * 0.5
        for i in range(len(self.letter_status)):
            if self.letter_status[i]:
                if x > next_line:
                    x = x_value
                    y += font_size
                my_font = pygame.font.SysFont('Arial', font_size)
                letter = my_font.render(self.string[i], True, (255, 255, 255))
                self.screen.blit(letter, (x, y))
                x += displacement

    def reset(self):
        for i in range(len(self.letter_status)):
            self.letter_status[i] = False
            self.printed = False
            self.curr_idx = 0
            self.frames_passed = 0