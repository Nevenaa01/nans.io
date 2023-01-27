import random

BOJA_BOTA = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def drawBotCell(SIZE, WIDTH_MAP, HEIGHT_MAP, X_PLAYER_CELL, Y_PLAYER_CELL, pygame, mapBorders):
    x = random.randint(SIZE, WIDTH_MAP - 5*SIZE)
    y = random.randint(SIZE, HEIGHT_MAP - 5*SIZE)

    #giving player enough distance at start
    while True:
        if x + SIZE <= X_PLAYER_CELL and y + SIZE > Y_PLAYER_CELL:
            x = random.randint(SIZE, WIDTH_MAP - SIZE)
        elif x + SIZE > X_PLAYER_CELL and y + SIZE <= Y_PLAYER_CELL:
            y = random.randint(SIZE, HEIGHT_MAP - SIZE)
        elif x + SIZE <= X_PLAYER_CELL and y + SIZE <= Y_PLAYER_CELL:
            x = random.randint(SIZE, WIDTH_MAP - SIZE)
            y = random.randint(SIZE, HEIGHT_MAP - SIZE)
        else:
            break

    x_bot_cell= x
    y_bot_cell = y

    botCell = pygame.draw.circle(mapBorders, BOJA_BOTA, (x_bot_cell, y_bot_cell), SIZE)

    return x_bot_cell, y_bot_cell

def botCellMovement():
    F = 10      #force that keeps the cell moving
    m = 1

    dP = lambda t: F/m

    global x_bot_cell
    global y_bot_cell

    p = [x_bot_cell, y_bot_cell]

    ta = 0
    tb = 10
    h = (ta - tb)/1000

    t = np.arange(ta, tb + h, h)

    pNew, _ = methods.eulerN.eulerN(ta, tb, h, p, dP, 0.0)

    x_bot_cell, y_bot_cell = pNew

    botCell = pygame.draw.circle(mapBorders, BOJA_BOTA, (x_bot_cell, y_bot_cell), SIZE)