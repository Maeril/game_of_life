# **************************************************************************** #
#                                                        __________            #
#                                                       | Hi there.|   ::.     #
#    gameoflife.py                                      |_______  _| :.:       #
#                                                     ::.::     \/      .:.    #
#    By: mae <maeyener@gmail.com>                   ...   C)  A____A           #
#                                                   :.:  ((  ( . w . )  .:.    #
#    Created: 2022/02/03 21:31:19 by mae               .:::::::U::::U:::       #
#    Updated: 2022/02/05 02:49:43 by mae                ..   :.: . . .:: :.    #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pygame as pg
import random
import sys

class GameOfLife:

	def __init__(self, w, h):

		self.height = h
		self.width = w
		self.grid = np.zeros((w * h), dtype='int').reshape(w, h)
				
		# Init the base grid.
		# Plug the 1's like so to control distribution ratio
		for i in range(0, self.width):
			for j in range(0, self.height):
				if random.randint(0, 100) < 10:
					self.grid[i][j] = 1
				else:
					self.grid[i][j] = 0
					
	def count_live_neighbors(self, i, j):
		
		live_neighbors = 0

		# Create a contextual map of the neighbors.
		# Skip (0, 0) as it indicates current position, i.e. not a neighbor.
		neighbor_map = [(-1, -1), (-1, 0), (-1, 1), 
						(0, -1), (0, 1), 
						(1, -1), (1, 0), (1, 1)]
	
		# Using the remainder operation '%' allows us to find our way in that 
		# "local neighbor map" contextually.
		for _i, _j in neighbor_map:
			if self.grid[(i + _i) % self.width][(j + _j) % self.height]:
				live_neighbors += 1
		return (live_neighbors)

	def update(self, screen):
		
		for i in range(0, self.width):
			for j in range(0, self.height):
				
				live = self.count_live_neighbors(i, j)

				# Apply Conway's
				if self.grid[i][j] == 1 and (live > 3 or live < 2):
					self.grid[i][j] = 0
				elif self.grid[i][j] == 0 and live == 3:
					self.grid[i][j] = 1

				# Display the live cell
				if self.grid[i][j] == 1:
					pg.draw.rect(screen, (255, 255, 255),
									[(i * 5), (j * 5), 5, 5])

		return (self.grid)		

	def run(self):

		pg.init()
		screen = pg.display.set_mode((self.width, self.height))
		clock = pg.time.Clock()
		pg.display.set_caption("John Conway's Game of Life")

		while True:
			clock.tick(60)
			screen.fill((0, 0, 0))

			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
			
			self.grid = self.update(screen)

			pg.display.update()


Game = GameOfLife(400, 600)
Game.run()