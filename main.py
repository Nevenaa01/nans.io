from itertools import count
import numpy as np
import pygame
import random
import methods.eulerN
 
pygame.init()   #starts pygame and all subparts of pygame

WIN = pygame.display.set_mode()
WIDTH, HEIGHT = WIN.get_size()
WIDTH_MAP, HEIGHT_MAP = WIDTH - 30, HEIGHT - 30

pygame.display.set_caption("Agar.io")

#border coordinates
LEFTBORDER = (WIDTH - WIDTH_MAP)/2
RIGHTBORDER = (WIDTH + WIDTH_MAP)/2
BOTTOMBORDER = (HEIGHT - HEIGHT_MAP)/2
UPPERBORDER = (HEIGHT + HEIGHT_MAP)/2

#position and size of player cell and bot cell
X_PLAYER_CELL = WIDTH_MAP/2
Y_PLAYER_CELL = HEIGHT_MAP/2
x_bot_cell = 0
y_bot_cell = 0
SIZE = 15

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50,205,50)
GREEN_VIRUS = (0, 255, 0)
PURPLE = (138, 43, 226)
BOJA_BOTA = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#borders of the map
mapBorders = pygame.Surface((WIDTH_MAP, HEIGHT_MAP))
mapBorders.fill(WHITE)

#food
numberOfFoodCells = 100
countFoodCellsOnScreen = 0

#player cell
#playerCell = pygame.draw.circle(mapBorders, PURPLE, (WIDTH/2, HEIGHT/2), 30)

#so that the game can run at the same speed on every machine
FPS = 60

def drawWindow():
    WIN.fill(GREEN)
    WIN.blit(mapBorders, ((WIDTH - WIDTH_MAP)/2, (HEIGHT - HEIGHT_MAP)/2))
    pygame.display.update()

def drawPlayerCell():
    playerCell = pygame.draw.circle(mapBorders, PURPLE, (X_PLAYER_CELL, Y_PLAYER_CELL), 30)
    #playerCell
    #pygame.display.update()



def drawBotCell():
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

    global x_bot_cell 
    x_bot_cell= x

    global y_bot_cell
    y_bot_cell = y

    botCell = pygame.draw.circle(mapBorders, BOJA_BOTA, (x_bot_cell, y_bot_cell), SIZE)

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


def drawViruses():
    for i in range(7):

        firstWidth = random.randint(LEFTBORDER, RIGHTBORDER)
        firstHeight = random.randint(BOTTOMBORDER, UPPERBORDER)

        #if firstWidth > WIDTH_MAP and firstHeight > HEIGHT_MAP:
        pygame.draw.polygon(mapBorders, GREEN_VIRUS, ((firstWidth, firstHeight), 
        (firstWidth + 50, firstHeight + 50), (firstWidth + 100, firstHeight)))

        #else:
           #i -= 1  #if its too close to the border get another set of coordinates

def drawFoodCells():
    global countFoodCellsOnScreen
    for i in range(40):
        if countFoodCellsOnScreen == numberOfFoodCells:
            continue
        pygame.draw.circle(mapBorders, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (random.randint(LEFTBORDER, RIGHTBORDER), random.randint(BOTTOMBORDER, UPPERBORDER)), 5)
        countFoodCellsOnScreen = 1 + countFoodCellsOnScreen

    
def main():
    clock = pygame.time.Clock()

    drawBotCell()
    drawViruses()
    
    #game loop
    while True:
        clock.tick(FPS)     #controls the speed of loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #botCellMovement()
        drawFoodCells()
        drawPlayerCell()
        
        drawWindow()

if __name__ == "__main__":
    main()