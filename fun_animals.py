import pygame
import random
import sys

MAX_X = 1366
MAX_Y = 768
MAX_ANIMALS = 100
ANIMAL_SIZE = 64
animals = []
BG_COLOUR = (0, 0, 0)


class Animal():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img_num = random.randint(1, 4)
        self.image_filename = "animal" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.image_filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (ANIMAL_SIZE, ANIMAL_SIZE))

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


def initialized_animal(max_animals, animals_list):
    for a in range(0, max_animals):
        x = random.randint(0, MAX_X)
        y = random.randint(0, MAX_Y)
        animals_list.append(Animal(x, y))


def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()


def main():
    pygame.init()
    initialized_animal(MAX_ANIMALS, animals)

    while True:
        screen.fill(BG_COLOUR)
        check_for_exit()
        for a in animals:
            a.move_animal()
            a.draw_animal()
        pygame.display.flip()

if __name__ == '__main__':
    screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
    main()
