# **************************************************************************** #
#                                                        __________            #
#                                                       | Hi there.|   ::.     #
#    gameoflife.py                                      |_______  _| :.:       #
#                                                     ::.::     \/      .:.    #
#    By: mae <maeyener@gmail.com>                   ...   C)  A____A           #
#                                                   :.:  ((  ( . w . )  .:.    #
#    Created: 2022/02/03 21:31:19 by mae               .:::::::U::::U:::       #
#    Updated: 2022/02/09 23:07:34 by mae                ..   :.: . . .:: :.    #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pygame as pg
import random
import sys

class GameOfLife:

	# Parameters are as follows: window width,
	# window height, cell scale.
	def __init__(self, w=600, h=400, s=5):

		self.w = w
		self.h = h
		self.s = s
		self.grid = np.zeros((w * h), dtype='int').reshape(w, h)

		# Init the base grid.
		# Plug the 1's like so to control distribution ratio
		for i in range(0, self.w):
			for j in range(0, self.h):
				if random.randint(0, 100) < 10:
					self.grid[i][j] = 1
				else:
					self.grid[i][j] = 0

	def count_live_neighbors(self, i, j):

		live_neighbors = 0
		# Create a contextual map of the neighbors.
		# Skip (0, 0) as it indicates current position,
		# i.e. not a neighbor.
		neighbor_map = [(-1, -1), (-1, 0), (-1, 1),
						(0, -1), (0, 1),
						(1, -1), (1, 0), (1, 1)]

		# Using the remainder operation '%' allows us to find our way
		# in that "local neighbor map" contextually.
		for _i, _j in neighbor_map:
			if self.grid[(i + _i) % self.w][(j + _j) % self.h]:
				live_neighbors += 1
		return (live_neighbors)

	def update(self):

		# Here, we create a second grid to edit while preserving
		# the original one until the end of the loop.
		new_grid = self.grid.copy()

		for i in range(0, self.w):
			for j in range(0, self.h):

				l = self.count_live_neighbors(i, j)

				# Apply Conway's rules
				if self.grid[i][j] == 1 and (l > 3 or l < 2):
					new_grid[i][j] = 0
				elif self.grid[i][j] == 0 and l == 3:
					new_grid[i][j] = 1

		# The new grid replaces the precedent one.
		self.grid = new_grid.copy()

	def run(self):

		pg.init()
		screen = pg.display.set_mode((self.w, self.h))
		surf = pg.Surface((self.w, self.h))
		clock = pg.time.Clock()
		pg.display.set_caption("John Conway's Game of Life")

		while True:
			# screen.fill((41, 5, 59))

			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()

			surf = pg.surfarray.make_surface(self.grid)
			# surf = pg.transform.scale2x(surf)
			screen.blit(surf, (0,0))
			pg.display.flip()

			self.update()
			clock.tick()

Game = GameOfLife()
Game.run()