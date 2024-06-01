import pygame

# Initialization of Components and Colors
pygame.init()
pygame.font.init()

# Game Constant Declaration
colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)
colorRed = (255, 0, 0)

displayWidth = displayHeight = 480
xOffset = offset = 25
yOffset = offset + 10
gameBoardWidth = displayWidth - offset
gameBoardHeight = (displayWidth - offset) + yOffset

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("PyGame TicTacToe")

playerFont = pygame.font.SysFont('Arial', 100)
font = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()

def gameReset():
    global gameOver, endGame, playerTurn, gameArray, gridArray
    
    gameOver = False
    endGame = False
    playerTurn = "X"
    gameArray = [[None, None, None], \
                [None, None, None], \
                [None, None, None]]
    gridArray = []
    
    gameDisplay.fill(colorWhite)
    drawGrid()
    

# Drawing Fixed UI Components    
def drawGrid():
    blockSize = (displayWidth - (2 * offset)) / 3
    for row in range(3):
        for column in range(3):
            rectangle = ((blockSize * row) + xOffset, (blockSize * column) + yOffset, blockSize, blockSize)
            pygame.draw.rect(gameDisplay, colorBlack, rectangle, 1)
            positionArray = (int(rectangle[0] + blockSize / 2), int(rectangle[1] + blockSize / 2))
            gridArray.append(positionArray)

def drawSymbol(row, column, xPosition, yPosition):
    global gameArray, playerTurn
    
    gameArray[row][column] = playerTurn
    
    text = playerFont.render(playerTurn, True, (0, 0, 0))
    textRectangle = text.get_rect(center=(xPosition, yPosition))
    gameDisplay.blit(text, textRectangle)
    
def rowChecker(clickPosition, row):
    match row:
        case 0:
            if(clickPosition[0] > xOffset and clickPosition[0] < gameBoardWidth / 3 + xOffset):
                return True
            else:
                return False
        case 1:
            if(clickPosition[0] > gameBoardWidth / 3 + xOffset and clickPosition[0] < 2 * gameBoardWidth / 3 + xOffset):
                return True
            else:
                return False
        case 2:
            if(clickPosition[0] > 2 * gameBoardWidth / 3 + xOffset and clickPosition[0] < gameBoardWidth):
                return True
            else:
                return False
            
def columnChecker(clickPosition, column):
    match column:
        case 0:
            if(clickPosition[1] > yOffset and clickPosition[1] < gameBoardHeight / 3 + yOffset):
                return True
            else:
                return False
        case 1:
            if(clickPosition[1] > gameBoardHeight / 3 + yOffset and clickPosition[1] < 2 * gameBoardHeight / 3 + yOffset):
                return True
            else:
                return False
        case 2:
            if(clickPosition[1] > 2 * gameBoardHeight / 3 + yOffset and clickPosition[1] < gameBoardHeight):
                return True
            else:
                return False

def playerWon():
    global gameArray
    
    for row in range(3):
        if(gameArray[row][0] == gameArray[row][1] == gameArray[row][2]) and gameArray[row][2] != None:
            pygame.draw.line(gameDisplay, (0, 255, 200), \
                ((gridArray[row][0] - 2 * offset), (gridArray[row][1])), \
                ((gridArray[row + 6][0] + 2 * offset), (gridArray[row + 6][1])), 5)
            return True
    for column in range(3):
        if(gameArray[0][column] == gameArray[1][column] == gameArray[2][column]) and gameArray[2][column] != None:
            pygame.draw.line(gameDisplay, (0, 255, 200), \
                ((gridArray[column][1] - (yOffset - offset)), (gridArray[column][0] - 2 * offset)), \
                ((gridArray[column + 6][1] - (yOffset - offset)), (gridArray[column + 6][0] + 2 * offset)), 5)
            return True
    if(gameArray[0][0] == gameArray[1][1] == gameArray[2][2]) and gameArray[1][1] != None:
        pygame.draw.line(gameDisplay, (0, 255, 200), \
                ((gridArray[0][1] - offset), (gridArray[0][0]) - offset), \
                ((gridArray[8][1] + offset), (gridArray[8][0]) + offset), 5)
        return True
    if(gameArray[2][0] == gameArray[1][1] == gameArray[0][2]) and gameArray[1][1] != None:
        return True
    return False
        
gameReset()

# Game Loop
while not endGame:

    for keyPress in pygame.event.get():
        if keyPress.type == pygame.QUIT:
            endGame = True
        if keyPress.type == pygame.KEYDOWN :
            if keyPress.key == pygame.K_SPACE and gameOver:
                gameReset()
            if keyPress.key == pygame.K_ESCAPE and gameOver:
                endGame = True
            
        if not gameOver:
            if pygame.mouse.get_pressed()[0]:
                clickPosition = pygame.mouse.get_pos()
                for row in range(3):
                    if(columnChecker(clickPosition, row)):
                        for column in range(3):
                            if(rowChecker(clickPosition, column)):
                                if(gameArray[row][column] == None):
                                    drawSymbol(row, column, gridArray[row + column * 3][0], gridArray[row + column * 3][1])
                                    # Changing Player         
                                    if playerTurn == 'X':
                                        playerTurn = 'O'
                                    elif playerTurn == 'O':
                                        playerTurn = 'X'
                            
        if(playerWon() and not gameOver):
            gameOver = True
            
            alphaRectangle = (xOffset, xOffset, gameBoardWidth, gameBoardHeight)
            shapeSurface = pygame.Surface(pygame.Rect(alphaRectangle).size, pygame.SRCALPHA)
            pygame.draw.rect(shapeSurface, (255, 255, 255, 175), shapeSurface.get_rect())
            gameDisplay.blit(shapeSurface, alphaRectangle)
            
            text = font.render("Game Over! Player {} Won!".format(playerTurn), True, (0, 0, 0))
            textRectangle = text.get_rect(center=(displayWidth/2, (xOffset + yOffset/3)/2))
            gameDisplay.blit(text, textRectangle)
            
    pygame.display.update()
    clock.tick(24)

pygame.quit()
quit()

## Created by Joydeep Biswas ##