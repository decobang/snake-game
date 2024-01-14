
import math
import random

import pygame


class Food:
    def __init__(self, _screen, _screenWidth, _screenHeight, _color = pygame.Color("red")):
        self.color = _color
        self.screen = _screen
        self.screenWidth = _screenWidth
        self.screenHeight = _screenHeight
        self.food_position = []
        self.food_spawn = False

    def setRandomPosition(self):
        self.food_position = [random.randrange(1, math.floor(self.screenWidth / 10)) * 10, random.randrange(1, math.floor(self.screenHeight / 10)) * 10]
       
    def drawFood(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.food_position[0], self.food_position[1], 10, 10))
        