import pygame, sys, random
from pygame.locals import *
from Minesweeper.colors import *

BombLightImg = pygame.image.load('Images\\Bomb-light-ground.png')
BombDarkImg = pygame.image.load('Images\\Bomb-dark-ground.png')
BombRedImg = pygame.image.load('Images\\Bomb-red.png')
FlagLightImg = pygame.image.load('Images\\Flag-light-grass.png')
FlagDarkImg = pygame.image.load('Images\\Flag-dark-grass.png')
LightGrassImg = pygame.image.load('Images\\light-grass.png')
DarkGrassImg = pygame.image.load('Images\\dark-grass.png')
LightGroundImg = pygame.image.load('Images\\light-ground.png')
DarkGroundImg = pygame.image.load('Images\\dark-ground.png')

Light1Img = pygame.image.load('Images\\1-light-ground.png')
Dark1Img = pygame.image.load('Images\\1-dark-ground.png')
Light2Img = pygame.image.load('Images\\2-light-ground.png')
Dark2Img = pygame.image.load('Images\\2-dark-ground.png')
Light3Img = pygame.image.load('Images\\3-light-ground.png')
Dark3Img = pygame.image.load('Images\\3-dark-ground.png')
Light4Img = pygame.image.load('Images\\4-light-ground.png')
Dark4Img = pygame.image.load('Images\\4-dark-ground.png')
Light5Img = pygame.image.load('Images\\5-light-ground.png')
Dark5Img = pygame.image.load('Images\\5-dark-ground.png')
Light6Img = pygame.image.load('Images\\6-light-ground.png')
Dark6Img = pygame.image.load('Images\\6-dark-ground.png')
Light7Img = pygame.image.load('Images\\7-light-ground.png')
Dark7Img = pygame.image.load('Images\\7-dark-ground.png')
Light8Img = pygame.image.load('Images\\8-light-ground.png')
Dark8Img = pygame.image.load('Images\\8-dark-ground.png')

WinImg = pygame.image.load('Images\\win-black.png')
GameOverImg = pygame.image.load('Images\\game-over-red.png')
ResetImg = pygame.image.load('Images\\reset-brown.png')
BombsImg = pygame.image.load('Images\\bombs-brown.png')


def main():
    global DISPLAYSURF, GRID, GRIDWIDTH, GRIDHEIGHT, NUMBOMBS, FLAGS, GAMEOVER
    GRIDWIDTH = 20
    GRIDHEIGHT = 20
    NUMBOMBS = 40
    GAMEOVER = False
    WIN = False
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((GRIDWIDTH * 20, GRIDHEIGHT * 20 + 50))
    pygame.display.set_caption('Minesweeper')

    GRID = [[0 for x in range(GRIDWIDTH)] for y in range(GRIDHEIGHT)]
    FLAGS = [[0 for x in range(GRIDWIDTH)] for y in range(GRIDHEIGHT)]
    assignBombs()

    while True:
        DISPLAYSURF.fill(SKY)
        DISPLAYSURF.blit(ResetImg, (10, 10))
        DISPLAYSURF.blit(BombsImg, (90, 10))
        for x in range(0, GRIDWIDTH * 20, 10):
            pygame.draw.polygon(DISPLAYSURF, GRASS_DARK, ((x, 50), (x + 5, 43), (x + 10, 50)))
        mouseClicked = False
        mousex = 0
        mousey = 0
        click = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                click = event.button

        if mouseClicked == True:
            row = int((mousey - 50) / GRIDWIDTH)
            col = int(mousex / GRIDWIDTH)

            # Evaluate space selected by the player
            if click == 1 and mousey >= 50 and GAMEOVER == False and WIN == False:
                if GRID[row][col] != 10:
                    GRID[row][col] = 9
                else:
                    GRID[row][col] = 99

            # Initiate reset sequence when button is pressed
            elif click == 1 and mousex in range(10, 90) and mousey in range(10, 40):
                resetBoard()
                GAMEOVER = False
                WIN = False

            # Add and remove flags when player right clicks
            elif click == 3 and mousey >= 50 and GAMEOVER == False and WIN == False:
                if GRID[row][col] == 0 or 10:
                    if FLAGS[row][col] == 0:
                        FLAGS[row][col] = 1
                    else:
                        FLAGS[row][col] = 0

        # If chosen square is clear, check nearby squares for bombs
        while True:
            for row in range(0, GRIDHEIGHT):
                for col in range(0, GRIDWIDTH):
                    minRow = row - 1
                    maxRow = row + 1
                    minCol = col - 1
                    maxCol = col + 1
                    if GRID[row][col] == 9:
                        if col == 0:
                            minCol = 0
                        elif col == GRIDWIDTH - 1:
                            maxCol = GRIDWIDTH - 1
                        if row == 0:
                            minRow = 0
                        elif row == GRIDWIDTH - 1:
                            maxRow = GRIDWIDTH - 1
                        nearby = 0
                        for y in range(minRow, maxRow + 1):
                            for x in range(minCol, maxCol + 1):
                                if GRID[y][x] == 10:
                                    nearby += 1
                        if nearby == 0:
                            nearby = 9
                            for y in range(minRow, maxRow + 1):
                                for x in range(minCol, maxCol + 1):
                                    if GRID[y][x] == 0:
                                        GRID[y][x] = 9
                        GRID[row][col] = nearby
            if 9 not in GRID:
                break

        # Draw board
        for row in range(0, GRIDHEIGHT):
            for col in range(0, GRIDWIDTH):
                if GRID[row][col] == 0 or GRID[row][col] == 10:
                    if FLAGS[row][col] == 1:
                        displaySquare(FlagLightImg, FlagDarkImg, row, col)
                    else:
                        displaySquare(LightGrassImg, DarkGrassImg, row, col)
                elif GRID[row][col] == 1:
                    displaySquare(Light1Img, Dark1Img, row, col)
                elif GRID[row][col] == 2:
                    displaySquare(Light2Img, Dark2Img, row, col)
                elif GRID[row][col] == 3:
                    displaySquare(Light3Img, Dark3Img, row, col)
                elif GRID[row][col] == 4:
                    displaySquare(Light4Img, Dark4Img, row, col)
                elif GRID[row][col] == 5:
                    displaySquare(Light5Img, Dark5Img, row, col)
                elif GRID[row][col] == 6:
                    displaySquare(Light6Img, Dark6Img, row, col)
                elif GRID[row][col] == 7:
                    displaySquare(Light7Img, Dark7Img, row, col)
                elif GRID[row][col] == 8:
                    displaySquare(Light8Img, Dark8Img, row, col)
                elif GRID[row][col] == 9:
                    displaySquare(LightGroundImg, DarkGroundImg, row, col)
                elif GRID[row][col] == 11:
                    displaySquare(FlagLightImg, FlagDarkImg, row, col)
                if GRID[row][col] == 99:
                    displaySquare(BombLightImg, BombDarkImg, row, col)
                    GAMEOVER = True

        if GAMEOVER == True:
            DISPLAYSURF.blit(GameOverImg, (100, 200))
        else:
            WIN = True
            for row in GRID:
                if 0 in row:
                    WIN = False

        if WIN == True:
            DISPLAYSURF.blit(WinImg, (100, 200))

        pygame.display.update()


# Alternate light and dark squares to display
def displaySquare(lightImg, darkImg, row, col):
    if col % 2 == 0 and row % 2 == 0 or col % 2 == 1 and row % 2 == 1:
        DISPLAYSURF.blit(lightImg, (col * 20, row * 20 + 50))
    else:
        DISPLAYSURF.blit(darkImg, (col * 20, row * 20 + 50))


# Reset board to begin a new game
def resetBoard():
    for row in range(0, GRIDHEIGHT):
        for col in range(0, GRIDWIDTH):
            GRID[row][col] = 0
            FLAGS[row][col] = 0
    assignBombs()


# Distribute bombs across the board
def assignBombs():
    for i in range(0, NUMBOMBS):
        num = -1
        while num < 0:
            num = random.randint(1, GRIDHEIGHT * GRIDWIDTH)
            if GRID[int(num / GRIDWIDTH) - 1][num % GRIDWIDTH - 1] != 10:
                GRID[int(num / GRIDWIDTH) - 1][num % GRIDWIDTH - 1] = 10
            else:
                num = -1


if __name__ == '__main__':
    main()
