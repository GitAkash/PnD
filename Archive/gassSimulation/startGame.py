import numpy as np
import constants as c
import matplotlib.pyplot as plt
import matplotlib as mpl


def cellCreation(xCoordinate, yCoordinate, xVelocity, yVelocity, radius, mass):
    c.cellVelocity = np.vstack((c.cellVelocity, [xVelocity, yVelocity]))
    c.cellCoordinates = np.vstack((c.cellCoordinates, [xCoordinate, yCoordinate]))
    c.cellCharacteristics = np.vstack((c.cellCharacteristics, [radius, mass]))
    return True

def cellsInit():
    cellCount = int(input("How many cells would you like to add?: "))
    for i in range(1, cellCount + 1):
        print(f"Cell: {i}")
        xCoordinate = float(input("x-coordinate: "))
        yCoordinate = float(input("y-coordinate: "))
        xVelocity = float(input("x-velocity: "))
        yVelocity = float(input("y-velocity: "))
        radius = float(input("Radius: "))
        mass = float(input("Mass: "))
        cellCreation(xCoordinate, yCoordinate, xVelocity, yVelocity, radius, mass)
    return print(c.cellCoordinates)


