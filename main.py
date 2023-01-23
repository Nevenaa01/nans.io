import pygame
 
pygame.init()   #starts pygame and all subparts of pygame

WIDTH, HEIGHT = 1200, 700
WIDTH_MAP, HEIGHT_MAP = 1170, 670
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agario.io")

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50,205,50)

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

    #game loop
    while True:
        clock.tick(FPS)     #controls the speed of loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        drawWindow()

if __name__ == "__main__":
    main()