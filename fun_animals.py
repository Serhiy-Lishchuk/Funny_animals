import pygame
import random

MAX_X = 1366
MAX_Y = 768
MAX_ANIMALS = 100
ANIMAL_SIZE = 64
animals = []


class Animal():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img_num = random.randint(1, 4)
        self.image_filename = "animal" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.image_filename).convert()
        self.image = pygame.transform.scale(self.image(ANIMAL_SIZE, ANIMAL_SIZE))

    def move_animal(self):
        self.y = self.y + self.speed
        if self.y > MAX_Y:
            self.y = 0 - ANIMAL_SIZE
        i = random.randint(1, 3)
        if i == 1:
            self.x += 1
            if self.x > MAX_X:
                self.x = 0 - ANIMAL_SIZE
        elif i == 2:
            self.x -= 1
            if self.x < 0 - ANIMAL_SIZE:
                self.x = MAX_X

    def draw_animal(self):
        screen.blit(self.image, (self.x, self.y))


def initialized_animal(max_animals, animals):
    for a in range(0, max_animals):
        x = random.randint(0, MAX_X)
        y = random.randint(0, MAX_Y)
        animals.append(Animal(x, y))
