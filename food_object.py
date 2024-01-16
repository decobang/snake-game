# Description: This file contains the Food class which is used to create a food object for the snake game.

# imports the required modules
import math
import random
import pygame

class Food:
    # initialize the food object and set the required parameters
    def __init__(self, _screen, _screenWidth, _screenHeight, _color = pygame.Color("red")):
        self.color = _color
        self.screen = _screen
        self.screenWidth = _screenWidth
        self.screenHeight = _screenHeight
        self.food_position = []
        self.food_spawn = False

    # set the food position to a random position
    def setRandomPosition(self):
        self.food_position = [random.randrange(1, math.floor(self.screenWidth / 10)) * 10, random.randrange(1, math.floor(self.screenHeight / 10)) * 10]
    
    # draw the food on the screen
    def drawFood(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.food_position[0], self.food_position[1], 10, 10))
        