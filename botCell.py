def drawBotCell():
    botCell = pygame.draw.circle(mapBorders, BOJA_BOTA, (random.randint(15, WIDTH_MAP - 15), random.randint(15, HEIGHT_MAP - 15)), 15)