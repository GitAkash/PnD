import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

matplotlib.use("TkAgg")

import constants as c

time = 0

fig, box = plt.subplots()
ms = 2 * c.cellCharacteristics[:, 0] * fig.gca().get_window_extent().height / c.boxSize * 72. / fig.dpi
line, = box.plot(c.cellCoordinates[:, 0], c.cellCoordinates[:, 1], marker="o", mfc='none')


def wallCollisions(cellCoordinates, cellVelocity, cellRadius, boxSize):
    mask = ((cellCoordinates[:, 0] < boxSize / 2 - cellRadius) |
            (cellCoordinates[:, 1] > boxSize / 2 - cellRadius) |
            (cellCoordinates[:, 0] < boxSize / 2 - cellRadius) |
            (cellCoordinates[:, 1] > boxSize / 2 - cellRadius))

    return c.cellVelocity[mask]


def init():
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    fig.gca().set_aspect('equal', 'box')
    return line,


def update(i):
    global time
    time += 0.5
    c.cellCoordinates[:] += time * c.cellVelocity[:]
    wallCollisions(c.cellCoordinates, c.cellVelocity, c.cellCharacteristics[:, 1], c.boxSize)
    line.set_data(c.cellCharacteristics[:, 0], c.cellCoordinates[:, 1])
    return line,


def run():
    ani = animation.FuncAnimation(fig=fig, func=update, frames=1000, repeat=False, interval=100, blit=True)
    plt.show()
