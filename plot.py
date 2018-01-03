#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as pt
from matplotlib.animation import FuncAnimation

data = np.loadtxt("/Users/areustle/Downloads/cumulative.csv",
        comments='#', delimiter=',', usecols=(1,2,3,4))
fig, ax = pt.subplots()
# ax.set_aspect('equal', 'box')
ax.set_ylim(0, 350)
ax.set_xlim(0, 3039)
ln, = ax.plot([], [], animated=True)

# This function guides matplotlib in how to draw frames of the animation.
def update(j):
    # print range(0,j+1), data[0:j+1]
    ln.set_data(data[0,0:j+1],data[1,0:j+1])
    return ln,

# Here we actually run the animation.
ani = FuncAnimation(fig, update, frames=len(data)-1, interval=1, blit=True)
pt.show()
pt.clf()

