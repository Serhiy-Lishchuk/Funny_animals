import configparser
import os

path = os.path.realpath(os.path.dirname(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(path, 'config.ini'))

MAX_X = int(config.get('SCREEN', 'width'))
MAX_Y = int(config.get('SCREEN', 'height'))

MAX_ANIMALS = int(config.get('ANIMALS', 'quantity'))
ANIMAL_SIZE = int(config.get('ANIMALS', 'size'))

BG_COLOUR = config.get('BACKGROUND', 'colour')
