import random

def drawViruses(mapBorders, LEFTBORDER, RIGHTBORDER, BOTTOMBORDER, UPPERBORDER, GREEN_VIRUS, pygame):
    for i in range(7):

        firstWidth = random.randint(LEFTBORDER, RIGHTBORDER)
        firstHeight = random.randint(BOTTOMBORDER, UPPERBORDER)

        #if firstWidth > WIDTH_MAP and firstHeight > HEIGHT_MAP:
        pygame.draw.polygon(mapBorders, GREEN_VIRUS, ((firstWidth, firstHeight), 
        (firstWidth + 50, firstHeight + 50), (firstWidth + 100, firstHeight)))

        #else:
           #i -= 1  #if its too close to the border get another set of coordinates