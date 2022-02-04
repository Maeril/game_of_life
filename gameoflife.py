# **************************************************************************** #
#                                                        __________            #
#                                                       | Hi there.|   ::.     #
#    gameoflife.py                                      |_______  _| :.:       #
#                                                     ::.::     \/      .:.    #
#    By: mae <maeyener@gmail.com>                   ...   C)  A____A           #
#                                                   :.:  ((  ( . w . )  .:.    #
#    Created: 2022/02/03 21:31:19 by mae               .:::::::U::::U:::       #
#    Updated: 2022/02/04 18:07:22 by mae                ..   :.: . . .:: :.    #
#                                                                              #
# **************************************************************************** #

import sys
import time
import random
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

class Game:

	def __init__(self, width, height, generations):

		self.height = height 
		self.width = width
		self.generations = generations
		self.grid = np.zeros(width*height, dtype='int').reshape(width, height)

	def init_grid(self):
				
		# Plug the 1's like so to control distribution ratio
		for i in range(0, self.width):
			for j in range(0, self.height):
				if random.randint(0, 100) < 20:
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

	def	update(self, args=None):
		for i in range(0, self.width):
			for j in range(0, self.height):
				live = self.count_live_neighbors(i, j)
				#print(live)
				if self.grid[i][j] == 1 and (live > 3 or live < 2):
					self.grid[i][j] = 0
				elif self.grid[i][j] == 0 and live == 3:
					self.grid[i][j] = 1
				# Placeholder
				else:
					pass
		return (self.grid)		

	def run(self):

		#fig, ax = plt.subplots( )
		#img = ax.imshow(self.grid, interpolation='nearest' )
		#ani = animation.FuncAnimation( fig, func=self.update, 
		#						frames=self.generations, init_func=self.init_grid)
		#plt.show()

		i = 1
		self.grid = self.init_grid()
		print(self.grid, "\n\n\n")
		while i < self.generations:
			self.grid = self.update()
			print(self.grid, "\n\n\n")
			time.sleep(1)

test = Game(10, 10, 5)
test.run()