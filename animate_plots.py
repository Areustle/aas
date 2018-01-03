#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as pt
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation
import datetime
import csv
from math import floor

def cum_chart():

    data = np.loadtxt("/Users/areustle/Downloads/cumulative.csv",
            comments='#', delimiter=',', usecols=(1,2,3,4))

    dates = []
    with open('/Users/areustle/Downloads/cumulative.csv') as cvsfile:
        for row in csv.reader(cvsfile):
            if row[0][0] == "#":
                continue
            dates.append(datetime.datetime.strptime(row[0], "%Y-%m-%d"))

    fig, ax = pt.subplots()
    # ax.set_aspect('equal', 'box')
    ax.set_ylim(0, np.amax(data)+5)
    ax.set_xlim(dates[0],dates[-1])

    tot, = ax.plot_date([], [], '-', label='Total', animated=True)
    pho, = ax.plot_date([], [], '-', label='Photon', animated=True)
    evt, = ax.plot_date([], [], '-', label='Events', animated=True)
    spc, = ax.plot_date([], [], '-', label='Spacecraft', animated=True)
    location = mdates.MonthLocator(interval=6)
    ax.xaxis.set_major_locator(location)
    formatter = mdates.AutoDateFormatter(location)
    ax.xaxis.set_major_formatter(formatter)
    fig.autofmt_xdate()
    ax.tick_params(axis='x', direction='out', top='off')
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.legend(loc='upper left')
    pt.ylabel('Cumulative Data Downloaded (TB)')
    pt.xlabel('Date')
    pt.title(
        'Cumulative Amount of Data Downloaded (Total = %.2f TB)' % data[-1,0])


    # This function guides matplotlib in how to draw frames of the animation.
    def update(i):
        k = min(i, data.shape[0]/18 )
        j=k*18
        xdata = dates[0:j]
        tot.set_data(xdata, data[0:j,0])
        pho.set_data(xdata, data[0:j,1])
        evt.set_data(xdata, data[0:j,2])
        spc.set_data(xdata, data[0:j,3])
        # ax.relim(visible_only=True)
        return tot, pho, evt, spc,

    # Here we actually run the animation.
    ani = FuncAnimation(fig, update, frames=int(floor(data.shape[0]/18 * 1.1)), interval=1,
            blit=True)
    ani.save('cumulative_download.mp4', fps=30)
    # pt.show()
    pt.clf()

if __name__ == '__main__':

    cum_chart()
