# **************************************************************************** #
#                                                        __________            #
#                                                       | Hi there.|   ::.     #
#    gameoflife.py                                      |_______  _| :.:       #
#                                                     ::.::     \/      .:.    #
#    By: mae <maeyener@gmail.com>                   ...   C)  A____A           #
#                                                   :.:  ((  ( . w . )  .:.    #
#    Created: 2022/02/03 21:31:19 by mae               .:::::::U::::U:::       #
#    Updated: 2022/02/10 18:53:29 by mae                ..   :.: . . .:: :.    #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pygame as pg
from scipy import signal
import random
import sys

class GameOfLife:

	# Parameters are as follows: window width,
	# window height, cell scale.
	def __init__(self, w=600, h=400, s=5):

		self.w = w
		self.h = h
		self.s = s
		self.grid = np.zeros((w * h), dtype="int").reshape(w, h)

		# Init the base grid.
		# Plug the 1's like so to control distribution ratio
		for i in range(0, self.w):
			for j in range(0, self.h):
				if random.randint(0, 100) < 10:
					self.grid[i][j] = 1
				else:
					self.grid[i][j] = 0

	def map_live_neighbors(self):

		kernel = np.ones((3 * 3), dtype="int").reshape(3, 3)
		kernel[1, 1] = 0
		self.neighbor_map = signal.convolve2d(self.grid, kernel)[1:-1, 1:-1]


	def update(self):

		for i in range(0, self.w):
			for j in range(0, self.h):

				# Apply Conway's rules
				if self.grid[i][j] == 1 and (self.neighbor_map[i][j] > 3 
					or self.neighbor_map[i][j] < 2):
					self.grid[i][j] = 0
				elif self.grid[i][j] == 0 and self.neighbor_map[i][j] == 3:
					self.grid[i][j] = 1

	def run(self):

		pg.init()
		screen = pg.display.set_mode((self.w, self.h))
		clock = pg.time.Clock()
		pg.display.set_caption("John Conway's Game of Life")

		while True:

			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()

			# The cell value defines color. We change "1" to "97" to display a
			# more visible pink instead of the blue "1" yields.
			c_grid = self.grid.copy()
			c_grid[c_grid == 1] = 97
			
			surf = pg.surfarray.make_surface(c_grid)
			screen.blit(surf, (0,0))
			pg.display.flip()

			self.map_live_neighbors()
			self.update()
			clock.tick()

Game = GameOfLife()
Game.run()