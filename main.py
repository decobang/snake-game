import math
import pygame
import time
import random
from food_object import Food

from snake_object import Snake

class Main:
	def __init__(self):

		# define constants
		self.SCREEN_WIDTH = 800
		self.SCREEN_HEIGHT = 800
		self.GRID_SIZE = 10

		# define colors
		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.RED = (255, 0, 0)
		self.GREEN = (0, 255, 0)
		self.BLUE = (0, 0, 255)

		# initialize pygame
		pygame.init()

		# set the window title
		pygame.display.set_caption("Snakey Snake")

		# create the screen and set width and height
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		
		self.fps = pygame.time.Clock()

		self.snake_direction = "RIGHT"
		self.change_direction = self.snake_direction
				
		# create snake object
		self.snake_object = Snake(self.screen, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.change_direction, self.WHITE)

		# create food object
		self.food_object = Food(self.screen, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.GREEN)
		self.food_object.setRandomPosition()
		
		self.is_game_running = True
		self.is_game_over = False

		self.playerScore = 0
		self.game_font = "monospace"

	def resetScreen(self):

		print("Resetting screen")

		self.snake_direction = "RIGHT"
		self.change_direction = self.snake_direction
		self.snake_object.resetSnakePosition()
		self.snake_object.is_snake_dead = False

		self.food_object.setRandomPosition()

		self.playerScore = 0

		self.is_game_running = True

		# time.sleep(1)

		self.startGame()

	def gamerOver(self, _final_score):
		self.is_game_running = False
		self.final_score = _final_score

		time.sleep(1)

		self.screen.fill(self.BLACK)
		pygame.display.update()

		self.game_font = pygame.font.SysFont("monospace", 50)
		game_over_surface = self.game_font.render("Game Over", True, self.RED)
		game_over_rect = game_over_surface.get_rect()
		game_over_rect.midtop = (self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2)

		self.final_score_font = pygame.font.SysFont("monospace", 30)
		final_score_surface = self.final_score_font.render("Final Score: {0}".format(self.final_score), True, self.WHITE)
		final_score_rect = final_score_surface.get_rect()
		final_score_rect.midtop = (self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2 + 50)

		self.screen.blit(game_over_surface, game_over_rect)
		self.screen.blit(final_score_surface, final_score_rect)
		
		pygame.display.update()

		print("Game Over")

		time.sleep(3)

		self.resetScreen()

	def showScore(self, _score, _size):
		score_font = pygame.font.SysFont("monospace", _size)
		score_surface = score_font.render("Score: {0}".format(_score), True, self.WHITE)
		score_rect = score_surface.get_rect()
		score_rect.midtop = 75, 20

		self.screen.blit(score_surface, score_rect)

	# draw the grid
	def drawGrid(self):
		for x in range(0, self.SCREEN_WIDTH, self.GRID_SIZE):
			pygame.draw.line(self.screen, self.WHITE, (x, 0), (x, self.SCREEN_HEIGHT))
		for y in range(0, self.SCREEN_HEIGHT, self.GRID_SIZE):
			pygame.draw.line(self.screen, self.WHITE, (0, y), (self.SCREEN_WIDTH, y))

	# handle events
	def eventHandler(self):
		for event in pygame.event.get():

			# checks if the user wants to quit the game
			if event.type == pygame.QUIT:
				self.is_game_running = False
			elif event.type == pygame.KEYDOWN:
				if event.key in [pygame.K_ESCAPE, pygame.K_q]:
					self.is_game_running = False

				# checks which key was pressed and changes the direction
				if event.key in [pygame.K_UP, pygame.K_w]:
					self.change_direction = "UP"
				if event.key in [pygame.K_DOWN, pygame.K_s]:
					self.change_direction = "DOWN"
				if event.key in [pygame.K_LEFT, pygame.K_a]:
					self.change_direction = "LEFT"
				if event.key in [pygame.K_RIGHT, pygame.K_d]:
					self.change_direction = "RIGHT"

		# checks if the direction is opposite to the current direction
		if self.change_direction == "UP" and self.snake_direction != "DOWN":
			self.snake_direction = "UP"
		if self.change_direction == "DOWN" and self.snake_direction != "UP":
			self.snake_direction = "DOWN"
		if self.change_direction == "LEFT" and self.snake_direction != "RIGHT":
			self.snake_direction = "LEFT"
		if self.change_direction == "RIGHT" and self.snake_direction != "LEFT":
			self.snake_direction = "RIGHT"

	def checkSnakeAndFoodCollision(self, _snake_position, _food_position):
		
		self.snake_object.snake_body.insert(0, list(_snake_position))

		if _snake_position[0] == _food_position[0] and _snake_position[1] == _food_position[1]:
			self.food_object.food_spawn = False
			self.playerScore += 1
		else:
			self.snake_object.snake_body.pop()

		if not self.food_object.food_spawn:
			self.food_object.setRandomPosition()
		
		self.food_object.food_spawn = True
			

	# main loop
	def startGame(self):

		print("Starting game")

		self.screen.fill(self.BLACK)
		pygame.display.update()

		# loop will run until is_game_running is False
		while self.is_game_running == True:
			if self.snake_object.is_snake_dead:
				self.gamerOver(self.playerScore)

			# call event handler
			self.eventHandler()

			# fill the screen with black
			self.screen.fill(self.BLACK)
			
			# calls the drawSnake method from the snake object
			self.snake_object.drawSnake()

			# calls the moveSnake method from the snake object
			self.snake_object.moveSnake(self.snake_direction)
			
			
			self.checkSnakeAndFoodCollision(self.snake_object.snake_position, self.food_object.food_position)

			self.food_object.drawFood()
			self.showScore(self.playerScore, 20)
			# update the whole screen
			pygame.display.update()

			# refreshes the screen after every 24 frames per second
			self.fps.tick(25)


# checks if the file is being run directly
if __name__ == "__main__":

	# create an instance of the Main class
	game = Main()

	# call the main loop method from the Main class
	game.startGame()