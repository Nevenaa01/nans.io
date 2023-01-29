import random

BOJA_BOTA = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def drawBotCell(SIZE, WIDTH_MAP, HEIGHT_MAP, X_PLAYER_CELL, Y_PLAYER_CELL, pygame, mapBorders):
    x = random.randint(SIZE, WIDTH_MAP - SIZE)
    y = random.randint(SIZE, HEIGHT_MAP - SIZE)

    #giving player enough distance at start
    while True:
        if abs(y - Y_PLAYER_CELL) <= 8*SIZE:
            y = random.randint(SIZE, HEIGHT_MAP - SIZE)
        elif abs(x - X_PLAYER_CELL) <= 8*SIZE:
            x = random.randint(SIZE, WIDTH_MAP - SIZE)
        else:
            break


    botCell = pygame.draw.circle(mapBorders, BOJA_BOTA, (x, y), SIZE)

    return x, y

def botCellMovement():
    F = 10      #force that keeps the cell moving
    m = 1

    dP = lambda t: F/m

    global x_bot_cell
    global y_bot_cell

    botCell = pygame.draw.circle(mapBorders, BOJA_BOTA, (x_bot_cell, y_bot_cell), SIZE)