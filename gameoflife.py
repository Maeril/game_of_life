# **************************************************************************** #
#                                                        __________            #
#                                                       | Hi there.|   ::.     #
#    gameoflife.py                                      |_______  _| :.:       #
#                                                     ::.::     \/      .:.    #
#    By: mae <maeyener@gmail.com>                   ...   C)  A____A           #
#                                                   :.:  ((  ( . w . )  .:.    #
#    Created: 2022/02/03 21:31:19 by mae               .:::::::U::::U:::       #
#    Updated: 2022/02/05 01:34:24 by mae                ..   :.: . . .:: :.    #
#                                                                              #
# **************************************************************************** #

import sys
import time
import random
import numpy as np
import pygame

class Game:

	def __init__(self, width, height):

		self.height = height 
		self.width = width
		self.grid = np.zeros(width*height, dtype='int').reshape(width, height)

	def init_grid(self):
				
		# Plug the 1's like so to control distribution ratio
		for i in range(0, self.width):
			for j in range(0, self.height):
				if random.randint(0, 100) < 10:
					self.grid[i][j] = 1
				else:
					self.grid[i][j] = 0
		return (self.grid)
					
	def count_live_neighbors(self, i, j):
		
		live_neighbors = 0
		# We put "+ 2" instead of "+ 1" bc range() is exclusive
		for x in range(i - 1 , i + 2):
			for y in range(j - 1, j + 2):
				if x == i and y == j:
					continue
				if x != self.width and y != self.height:
					live_neighbors += self.grid[x][y]
				elif x == self.width and y != self.height:
					live_neighbors += self.grid[0][y]
				elif x != self.width and y == self.height:
					live_neighbors += self.grid[x][0]
				else:
					live_neighbors += self.grid[0][0]
		
		return (live_neighbors)

	def update(self, screen):
		
		for i in range(0, self.width):
			for j in range(0, self.height):
				
				live = self.count_live_neighbors(i, j)

				if self.grid[i][j] == 1 and (live > 3 or live < 2):
					self.grid[i][j] = 0
				elif self.grid[i][j] == 0 and live == 3:
					self.grid[i][j] = 1

				if self.grid[i][j] == 1:
					pygame.draw.rect(screen, (255, 255, 255), [(i * 5), (j * 5), 5, 5])

		return (self.grid)		

	def run(self):

		pygame.init()
		screen = pygame.display.set_mode((self.width, self.height))
		clock = pygame.time.Clock()
		pygame.display.set_caption("John Conway's Game of Life")

		self.grid = self.init_grid()
		# print(self.grid, "\n\n\n")
		
		while True:
			clock.tick(60)
			screen.fill((0, 0, 0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			
			# self.draw_grid(screen)
			self.grid = self.update(screen)

			pygame.display.update()


test = Game(500, 500)
test.run()