from itertools import count
import pygame
import random
 
pygame.init()   #starts pygame and all subparts of pygame

WIDTH, HEIGHT = 1200, 700
WIDTH_MAP, HEIGHT_MAP = 1170, 670
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agario.io")

#border coordinates
LEFTBORDER = (WIDTH - WIDTH_MAP)/2
RIGHTBORDER = (WIDTH + WIDTH_MAP)/2
BOTTOMBRODER = (HEIGHT - HEIGHT_MAP)/2
UPPERBORDER = (HEIGHT + HEIGHT_MAP)/2

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50,205,50)
PURPLE = (138, 43, 226)

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
    playerCell = pygame.draw.circle(mapBorders, PURPLE, (WIDTH/2, HEIGHT/2), 30)
    #playerCell
    #pygame.display.update()

def drawFoodCells():
    global countFoodCellsOnScreen
    for i in range(40):
        if countFoodCellsOnScreen == numberOfFoodCells:
            continue
        pygame.draw.circle(mapBorders, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (random.randint(LEFTBORDER, RIGHTBORDER), random.randint(BOTTOMBRODER, UPPERBORDER)), 5)
        countFoodCellsOnScreen = 1 + countFoodCellsOnScreen

    
def main():
    clock = pygame.time.Clock()

    #game loop
    while True:
        clock.tick(FPS)     #controls the speed of loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        drawFoodCells()
        drawPlayerCell()
        drawWindow()

if __name__ == "__main__":
    main()