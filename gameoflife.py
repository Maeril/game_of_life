# **************************************************************************** #
#                                                        __________            #
#                                                       | Hi there.|   ::.     #
#    gameoflife.py                                      |_______  _| :.:       #
#                                                     ::.::     \/      .:.    #
#    By: mae <maeyener@gmail.com>                   ...   C)  A____A           #
#                                                   :.:  ((  ( . w . )  .:.    #
#    Created: 2022/02/03 21:31:19 by mae               .:::::::U::::U:::       #
#    Updated: 2022/02/04 15:57:36 by mae                ..   :.: . . .:: :.    #
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
        
# I want to control the distribution ratio so let me go ahead and plug the ones
# in like this
        for i in range(0, width):
            for j in range(0, height):
                if (random.randint(0, 100) < 10):
                    self.grid[i][j] = 1
                else:
                    self.grid[i][j] = 0
        plt.figure()
        plotted_img = plt.imshow(self.grid, interpolation="nearest",
                                cmap=plt.cm.gray)
        plt.show()


test_grid = Game(80, 80, 10)