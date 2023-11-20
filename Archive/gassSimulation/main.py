import box
import startGame
import constants


def run():
    startGame.cellsInit()

    print(constants.cellVelocity)
    print(constants.cellCoordinates)
    print(constants.cellCharacteristics)
    box.init()
    # box.draw()
    box.run()


if __name__ == '__main__':
    run()
