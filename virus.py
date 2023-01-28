import random

def drawViruses(mapBorders, LEFTBORDER, RIGHTBORDER, BOTTOMBORDER, UPPERBORDER, GREEN_VIRUS, pygame, x_bot_cell, y_bot_cell, X_PLAYER_CELL, Y_PLAYER_CELL, WIDTH_MAP, HEIGHT_MAP):
    
    listOfPositions = []

    xIncrement = WIDTH_MAP/3
    yIncrement = HEIGHT_MAP/2

    xOld = 30

    for i in range(6):

        if i < 3:
            firstWidth = random.uniform(xOld, xIncrement - 100)
            firstHeight = random.uniform(30, yIncrement - 100)
        else:
            firstWidth = random.uniform(xOld, xIncrement - 100)
            firstHeight = random.uniform(HEIGHT_MAP/2, yIncrement - 100)

        firstPoint = (firstWidth, firstHeight)
        secondPoint = (firstWidth + 100, firstHeight)
        thirdPoint = (firstWidth + 100, firstHeight + 100)
        fourthPoint = (firstWidth, firstHeight + 100)

        if firstPoint[0] < x_bot_cell and secondPoint[0] > x_bot_cell and firstPoint[1] > y_bot_cell and fourthPoint[1] < y_bot_cell:
            i -= 1
            continue


        listOfPositions.append(((firstWidth, firstHeight), (firstWidth + 50, firstHeight + 50), (firstWidth + 100, firstHeight)))
        

        pygame.draw.polygon(mapBorders, GREEN_VIRUS, (firstPoint, secondPoint, thirdPoint, fourthPoint))

        if i == 2:
            yIncrement = HEIGHT_MAP
            xIncrement = WIDTH_MAP/3
            xOld = 130
        else:
            xOld = xIncrement
            xIncrement += WIDTH_MAP/3

    return listOfPositions