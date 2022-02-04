# **************************************************************************** #
#                                                        __________            #
#                                                       | Hi there.|   ::.     #
#    gameoflife.py                                      |_______  _| :.:       #
#                                                     ::.::     \/      .:.    #
#    By: mae <maeyener@gmail.com>                   ...   C)  A____A           #
#                                                   :.:  ((  ( . w . )  .:.    #
#    Created: 2022/02/03 21:31:19 by mae               .:::::::U::::U:::       #
#    Updated: 2022/02/04 17:11:13 by mae                ..   :.: . . .:: :.    #
#                                                                              #
# **************************************************************************** #

import random
import numpy as np
from matplotlib import pyplot as plt

class Game:

	def __init__(self, width, height, generations):

		self.height = height 
		self.width = width
		self.generations = generations
		self.grid = np.zeros(width*height, dtype='int').reshape(width, height)
		
# We want to control the distribution ratio, so let's plug the 1's in like this
		for i in range(0, width):
			for j in range(0, height):
				if random.randint(0, 100) < 15:
					self.grid[i][j] = 1
				else:
					self.grid[i][j] = 0
		plt.figure()
		plotted_img = plt.imshow(self.grid, interpolation="nearest",
								cmap=plt.cm.gray)
		#plt.show()
	
	def count_live_neighbors(self, i, j):
		
		live_neighbors = 0
		# We put "+ 2" instead of "+ 1" because the range() function is exclusive
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
		
		#print("neighbors currently alive: {}".format(live_neighbors))
		return live_neighbors

	def run(self):

		counter = 1
		print(self.grid)
		while counter <= self.generations:
			for i in range(0, self.width):
				for j in range(0, self.height):
					live = self.count_live_neighbors(i, j)
					#print(live)
					if self.grid[i][j] == 1 and (live > 3 or live < 2):
						self.grid[i][j] = 0
					elif self.grid[i][j] == 0 and live == 3:
						self.grid[i][j] = 1
					# Might throw that one out, not sure it is necessary, just a placeholder for now
					else:
						pass
			print(self.grid, "\n\n\n")

			counter += 1

test_grid = Game(10, 10, 5)
test_grid.run()