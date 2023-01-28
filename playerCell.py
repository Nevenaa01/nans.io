import random
import numpy as np
import eulerN
import constants
import rk4N

def drawPlayerCell(mapBorders, PURPLE, X_PLAYER_CELL, Y_PLAYER_CELL, pygame, PLAYER_SIZE):
    playerCell = pygame.draw.circle(mapBorders, PURPLE, (X_PLAYER_CELL, Y_PLAYER_CELL), PLAYER_SIZE)
    #playerCell
    #pygame.display.update()

def playerCellMoving(pygame, mapBorders, PURPLE, PLAYER_SIZE):
    F = 15
    m = 1

    dnfX = lambda x, s, ds: F/m

    startPoint = np.array([constants.X_PLAYER_CELL, constants.Y_PLAYER_CELL])

    a = constants.X_PLAYER_CELL
    b, _ = pygame.mouse.get_pos()
    print(pygame.mouse.get_pos())

    h = (b - a)/100 + 0.01

    #newPoint, _ = eulerN.eulerN(a, b, h, startPoint, dnfX, 0.0)
    newPoint1, _ = rk4N.rk4N(a, b, h, startPoint, dnfX, 0.0)
    constants.X_PLAYER_CELL = b
    _, constants.Y_PLAYER_CELL = pygame.mouse.get_pos()

    playerCell = pygame.draw.circle(mapBorders, PURPLE, (b, newPoint1[0]), PLAYER_SIZE)
    #playerCell = pygame.draw.circle(mapBorders, (0,0,0), (b, newPoint1[0]), PLAYER_SIZE)
    pygame.display.update()
