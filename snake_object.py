# Description: This file contains the snake object class. 
# This class is responsible for the snake's movement, collision detection, and drawing the snake on the screen.

# import pygame module
import pygame 

class Snake:

    # initialize the snake object and set the required parameters
    def __init__(self, _screen, _screenWidth, _screenHeight, _changeTo, _color):
        self.screen = _screen
        self.screenWidth = _screenWidth
        self.screenHeight = _screenHeight
        self.changeToDirection = _changeTo
        self.color = _color
        self.is_snake_dead = False

        # set the initial position of the snake and the snake body
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

    # reset the snake position and snake body
    def resetSnakePosition(self):
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        

    # move the snake based on the direction
    def moveSnake(self, _direction):
        self.changeToDirection = _direction

        if self.changeToDirection == 'UP':
            self.snake_position[1] -= 10
        if self.changeToDirection == 'DOWN':
            self.snake_position[1] += 10
        if self.changeToDirection == 'LEFT':
            self.snake_position[0] -= 10
        if self.changeToDirection == 'RIGHT':
            self.snake_position[0] += 10

        self.is_snake_dead = self.checkSnakeCollisions()

    # check if the snake collides with the wall or itself and return True or False
    def checkSnakeCollisions(self):
        if self.snake_position[0] < 0 or self.snake_position[0] > self.screenWidth - 10:
            return True
        elif self.snake_position[1] < 0 or self.snake_position[1] > self.screenHeight - 10:
            return True

        for block in self.snake_body[1:]:
            if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
                return True
        
    # increase the snake body when it eats the food and draw the snake on the screen
    def drawSnake(self):
        for pos in self.snake_body:
            pygame.draw.rect(self.screen, self.color, pygame.Rect(pos[0], pos[1], 10, 10))

        