from itertools import count
import numpy as np
import pygame
import random
import methods.eulerN
import botCell
import virus
import playerCell
import foodCell
 
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
PLAYER_SIZE = 17

#food
foods = []

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50,205,50)
GREEN_VIRUS = (0, 255, 0)
PURPLE = (138, 43, 226)


#borders of the map
mapBorders = pygame.Surface((WIDTH_MAP, HEIGHT_MAP))
mapBorders.fill(WHITE)

#so that the game can run at the same speed on every machine
FPS = 60

def drawWindow():
    WIN.fill(GREEN)
    WIN.blit(mapBorders, ((WIDTH - WIDTH_MAP)/2, (HEIGHT - HEIGHT_MAP)/2))
    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()

    global x_bot_cell, y_bot_cell
    global foods

    x_bot_cell, y_bot_cell = botCell.drawBotCell(SIZE, WIDTH_MAP, HEIGHT_MAP, X_PLAYER_CELL, Y_PLAYER_CELL, pygame, mapBorders)

    virus.drawViruses(mapBorders, LEFTBORDER, RIGHTBORDER, BOTTOMBORDER, UPPERBORDER, GREEN_VIRUS, pygame, x_bot_cell, y_bot_cell, X_PLAYER_CELL, Y_PLAYER_CELL, WIDTH_MAP, HEIGHT_MAP)

    playerCell.drawPlayerCell(mapBorders, PURPLE, X_PLAYER_CELL, Y_PLAYER_CELL, pygame, PLAYER_SIZE)

    foods = foodCell.drawFoodCells(pygame, mapBorders, LEFTBORDER, RIGHTBORDER, BOTTOMBORDER, UPPERBORDER, x_bot_cell, y_bot_cell, SIZE, X_PLAYER_CELL, Y_PLAYER_CELL, PLAYER_SIZE)

    #game loop
    while True:
        clock.tick(FPS)     #controls the speed of loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #botCellMovement()
        #playerCell.playerCellMoving(pygame, mapBorders, PURPLE, PLAYER_SIZE, X_PLAYER_CELL, Y_PLAYER_CELL)
        #u kretanju celije ce se proslediti foods mozda

        drawWindow()

if __name__ == "__main__":
    main()