import random
import mathFormulas

numberOfFoodCells = 100
countFoodCellsOnScreen = 0

#foods[] ce biti niz koji ce cuvati (x_pozicija, y_pozicija, poluprecnik) svake hrane

def countVirusWithFood(x_food, y_food, listOfPosition, food_radius):
    count = 0
    
    i = 0
    for pos in listOfPosition:
        if (food_radius + 71 > mathFormulas.distance(x_food, y_food, listOfPosition[0][1][0], listOfPosition[0][1][1])):
            count += 1
        elif (food_radius + 71 > mathFormulas.distance(x_food, y_food, listOfPosition[1][1][0], listOfPosition[1][1][1])):
            count += 1
        elif (food_radius + 71 > mathFormulas.distance(x_food, y_food, listOfPosition[2][1][0], listOfPosition[2][1][1])):
            count += 1
        elif (food_radius + 71 > mathFormulas.distance(x_food, y_food, listOfPosition[3][1][0], listOfPosition[3][1][1])):
            count += 1
        elif (food_radius + 71 > mathFormulas.distance(x_food, y_food, listOfPosition[4][1][0], listOfPosition[4][1][1])):
            count += 1
        elif (food_radius + 71 > mathFormulas.distance(x_food, y_food, listOfPosition[5][1][0], listOfPosition[5][1][1])):
            count += 1
    
    return count

def drawFoodCells(pygame, mapBorders, LEFTBORDER, RIGHTBORDER, BOTTOMBORDER, UPPERBORDER, x_bot_cell, y_bot_cell, SIZE, X_PLAYER_CELL, Y_PLAYER_CELL, PLAYER_SIZE, listOfPositions):
    global countFoodCellsOnScreen
    foods = []
    for i in range(100):
        if countFoodCellsOnScreen == numberOfFoodCells:
            continue
        x_food = random.randint(LEFTBORDER, RIGHTBORDER)
        y_food = random.randint(BOTTOMBORDER, UPPERBORDER)
        food_radius = 5

        
        while (food_radius + PLAYER_SIZE > mathFormulas.distance(x_food, y_food, X_PLAYER_CELL, Y_PLAYER_CELL) or food_radius + SIZE > mathFormulas.distance(x_food, y_food, x_bot_cell, y_bot_cell) or countVirusWithFood(x_food, y_food, listOfPositions, food_radius) > 0):
            x_food = random.randint(LEFTBORDER, RIGHTBORDER)
            y_food = random.randint(BOTTOMBORDER, UPPERBORDER)
        pygame.draw.circle(mapBorders, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x_food, y_food), food_radius)
        countFoodCellsOnScreen = 1 + countFoodCellsOnScreen

        foods.append((x_food, y_food, food_radius))
    return foods

