import pygame
import random

MAX_X = 1366
MAX_Y = 768
MAX_ANIMALS = 100
SHOW_SIZE = 64


class Animal():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img_num = random.randint(1, 4)
        self.image_filename = "animal" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.image_filename).convert()
        self.image = pygame.transform.scale(self.image(SHOW_SIZE, SHOW_SIZE))

    def move_animal(self):
        self.y = self.y + self.speed
        if self.y > MAX_Y:
            self.y = 0 - SHOW_SIZE
        i = random.randint(1, 3)
        if i == 1:
            self.x += 1
            if self.x > MAX_X:
                self.x = 0 - SHOW_SIZE
        elif i == 2:
            self.x -= 1
            if self.x < 0 - SHOW_SIZE:
                self.x = MAX_X

    def draw_animal(self):
        screen.blit(self.image, (self.x, self.y))
