import pygame


class Player_2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("player_2.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
        self.image = pygame.transform.scale(self.image, scale_size)

# class test(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#
#         self.image = pygame.image.load("testImage.png").convert()
#         self.image.set_colorkey((255,255,255))
#         self.image_scaled = pygame.image.load(self.image, (size, size))
#         self.rect = self.image_scaled.get_rect()