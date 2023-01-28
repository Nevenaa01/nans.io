import random
import mathFormulas

numberOfFoodCells = 100
countFoodCellsOnScreen = 0

#foods[] ce biti niz koji ce cuvati (x_pozicija, y_pozicija, poluprecnik) svake hrane

def drawFoodCells(pygame, mapBorders, LEFTBORDER, RIGHTBORDER, BOTTOMBORDER, UPPERBORDER, x_bot_cell, y_bot_cell, SIZE, X_PLAYER_CELL, Y_PLAYER_CELL, PLAYER_SIZE):
    global countFoodCellsOnScreen
    foods = []
    for i in range(100):
        if countFoodCellsOnScreen == numberOfFoodCells:
            continue
        x_food = random.randint(LEFTBORDER, RIGHTBORDER)
        y_food = random.randint(BOTTOMBORDER, UPPERBORDER)
        food_radius = 5
        
        while (food_radius + PLAYER_SIZE > mathFormulas.distance(x_food, y_food, X_PLAYER_CELL, Y_PLAYER_CELL) or food_radius + SIZE > mathFormulas.distance(x_food, y_food, x_bot_cell, y_bot_cell)): 
            x_food = random.randint(LEFTBORDER, RIGHTBORDER)
            y_food = random.randint(BOTTOMBORDER, UPPERBORDER)
        pygame.draw.circle(mapBorders, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x_food, y_food), food_radius)
        countFoodCellsOnScreen = 1 + countFoodCellsOnScreen

        foods.append((x_food, y_food, food_radius))

    return foods

