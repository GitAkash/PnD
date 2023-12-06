import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
import random

quantityCells = int(input("Cell Quantity: "))
boxSize = 100
cellCoordinates = np.zeros((1, 2), dtype='float64')[1:]
cellVelocities = np.zeros((1, 2), dtype='float64')[1:]

cellMass = 1
cellRadius = 5

for i in range(quantityCells):
    cellCoordinates = np.vstack((cellCoordinates, [random.randint(-40, 40), random.randint(-40, 40)]))
    cellVelocities = np.vstack((cellVelocities, [random.randint(-20, 20), random.randint(-20, 20)]))

print(
    f"Coordinates: \n {cellCoordinates} \n Velocity: \n {cellVelocities} \n Radius: \n {cellRadius} \n Mass: \n {cellMass}",
    end='')


def E_av():
    return np.sum(0.5 * cellMass * (cellVelocities[:, 0] ** 2 + cellVelocities[:, 1] ** 2)) / quantityCells


def lol(s):
    return (1 / E_av()) * s * np.exp((-0.5 * (s ** 2)) / E_av())


''' Setup the Box '''
matplotlib.use("QT5Agg")
fig, (box, hist3) = plt.subplots(1, 2)
ms = 2 * cellRadius * fig.gca().get_window_extent().height / boxSize * 72. / fig.dpi
line, = box.plot(cellCoordinates[:, 0], cellCoordinates[:, 1], marker='o', ms=ms, mfc='none', linestyle='None',
                 c='pink')
# hist2 = hist3.hist(np.sqrt(cellVelocities[:, 0] ** 2 + cellVelocities[:, 1] ** 2), bins=30, range=[0, 50])
# plt.xlim(-50, 50)
# plt.ylim(-50, 50)
box.set_xlim([-50, 50])
box.set_ylim([-50,50])
hist3.set_ylim([0, 50])
hist3.set_xlim([0, 50])


box.set_facecolor('grey')
plt.tight_layout()

plt.xlabel("Distribution")
plt.ylabel("Velocities")

'''
Cell also collides with walls, because it's 2D it's easy to calculate the angle the cells has to collide with.
'''


def wallCollisions():
    horizontalWall = ((cellCoordinates[:, 0] < -(boxSize / 2 - cellRadius / 2)) |
                      (cellCoordinates[:, 0] > boxSize / 2 - cellRadius / 2))
    verticalWall = ((cellCoordinates[:, 1] < -(boxSize / 2 - cellRadius / 2)) |
                    (cellCoordinates[:, 1] > boxSize / 2 - cellRadius / 2))
    cellVelocities[:, 1][verticalWall] *= -1
    cellVelocities[:, 0][horizontalWall] *= -1


'''
Cells also collide with each other, check if the cell radii are in range of each other,
if they are the cells collide and a collision will be performed.
'''


def cellCollisions():
    for cell1Coords, cell1Velocity, in zip(cellCoordinates, cellVelocities):
        for cell2Coords, cell2Velocity, in zip(cellCoordinates[1:], cellVelocities[1:]):
            xCell1 = cell1Coords[0];
            yCell1 = cell1Coords[1]
            xCell2 = cell2Coords[0];
            yCell2 = cell2Coords[1]
            dx = xCell1 - xCell2
            dy = yCell1 - yCell2

            if np.sqrt(dx ** 2 + dy ** 2) <= 0.8 * cellRadius and np.dot((cell1Coords - cell2Coords),
                                                                         (cell1Velocity - cell2Velocity)) < 0:
                d = np.linalg.norm(cell1Coords - cell2Coords) ** 2
                cell2VelocityOld = cell2Velocity
                cell1VelocityOld = cell1Velocity
                dv = np.dot((cell1VelocityOld - cell2VelocityOld), (cell1Coords - cell2Coords)) / d * (
                        cell1Coords - cell2Coords)
                cell1Velocity -= dv
                cell2Velocity += dv
                # cell2Velocity *= -cell1Velocity


# v = (-0.5 * (cellVelocities[:, 0] ** 2 + cellVelocities[:, 1] ** 2))
def update(i):
    cellCoordinates[:] += 0.1 * cellVelocities[:]
    cellCollisions()
    wallCollisions()
    line.set_data(cellCoordinates[:, 0], cellCoordinates[:, 1])
    sumfun = np.sum((np.sqrt(cellVelocities[:, 0] ** 2 + cellVelocities[:, 1] ** 2)))/quantityCells
    hist3.cla()
    # hist3.set_ylim([0, 1])
    # hist3.set_xlim([0, 50])
    s = np.sqrt((cellVelocities[:, 0] ** 2 + cellVelocities[:, 1] ** 2))
    # hist3.hist((np.sqrt(cellVelocities[:, 0] ** 2 + cellVelocities[:, 1] ** 2)), bins=30)
    hist3.plot(lol(np.sort(s)))
    print(s)
    return line, hist3


ani = animation.FuncAnimation(fig, update, frames=2000, repeat=True, interval=10, blit=True)
plt.show()
