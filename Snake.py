import pygame
import random

# Initialization of Components and Colors
pygame.init()
pygame.font.init()
colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)
colorRed = (255, 0, 0)
displayWidth = 640
displayHeight = 480
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("PyGame SNAKE")
# highScoreFile = open("HighScore.txt", "r") # Opening The File Containing High Score in Read Mode
clock = pygame.time.Clock()

# Game Variables
gameOver = False
endGame = False
yMovement = True
xMovement = True
bodyLength = 1
playerScore = 0
# highScore = int(highScoreFile.read()) # Reading The High Score
highScore = 0
xVelocity = 0
yVelocity = 0
xPosition = round(displayWidth/2)
yPosition = round(displayHeight/2)
xFood = random.randint(35, displayWidth-35)
yFood = random.randint(25, displayHeight-25)
bodyList = []

def gameReset() :
    global gameOver, endGame, yMovement, xMovement, bodyLength, playerScore, xVelocity, yVelocity, xPosition, yPosition, xFood, yFood, bodyList
    gameOver = False
    endGame = False
    yMovement = True
    xMovement = True
    bodyLength = 1
    playerScore = 0
    xVelocity = 0
    yVelocity = 0
    xPosition = round(displayWidth/2)
    yPosition = round(displayHeight/2)
    xFood = random.randint(35, displayWidth-35)
    yFood = random.randint(25, displayHeight-25)
    bodyList = []

# Game Loop
while not endGame :

    # Checking Pressed Key
    for keyPress in pygame.event.get() :
        if keyPress.type == pygame.KEYDOWN :
            if keyPress.key == pygame.K_RIGHT and yMovement :
                xVelocity = 5
                yVelocity = 0  
                yMovement = False
                xMovement = True
            if keyPress.key == pygame.K_LEFT and yMovement:
                xVelocity = -5
                yVelocity = 0
                yMovement = False
                xMovement = True
            if keyPress.key == pygame.K_UP and xMovement:
                xVelocity = 0
                yVelocity = -5
                yMovement = True
                xMovement = False
            if keyPress.key == pygame.K_DOWN and xMovement:
                xVelocity = 0
                yVelocity = 5  
                yMovement = True
                xMovement = False
            if keyPress.key == pygame.K_SPACE and gameOver:
                gameReset()
            if keyPress.key == pygame.K_ESCAPE and gameOver:
                endGame = True

        if keyPress.type == pygame.QUIT :
            endGame = True
        
    xPosition = xPosition + xVelocity
    yPosition = yPosition + yVelocity

    # Score Counter and Random Food Spawner
    if abs(xPosition - xFood) < 7 and abs(yPosition - yFood) < 7 and not gameOver :
        playerScore = playerScore + 1
        xFood = random.randint(35, displayWidth-35)
        yFood = random.randint(25, displayHeight-25)
        bodyLength = bodyLength + 1
    
    # Colision Checking 1 (Wall Colision Checking)
    if xPosition < 1 or xPosition > 639 or yPosition < 1 or yPosition > 479 :
        gameOver = True

    # Colision Checking 2 (Self Colision Checking)
    for x in bodyList[:len(bodyList)-1] :
        if x == headList and (not xMovement or not yMovement):
            gameOver = True
    
    gameDisplay.fill(colorWhite)
    font = pygame.font.SysFont(None, 40)

    # Displaying Score and Game Over Message
    if not gameOver :
        text = font.render("{}".format(playerScore), True, (0, 0, 0))
        gameDisplay.blit(text, (320, 5))
        pygame.draw.rect(gameDisplay, colorRed, [xFood, yFood, 15, 15])
    else :
        # High Score Checking and Modifying
        if playerScore > highScore :
            # highScoreFile.close()
            # highScoreFile = open("HighScore.txt", "w") # Opening The File Containing High Score in Read Mode
            highScore = playerScore
            # highScoreFile.write(str(highScore)) # Writing The High Score

        text = font.render("Game Over! Your Score : {}".format(playerScore), True, (0, 0, 0))
        textRectangle = text.get_rect(center=(displayWidth/2, displayHeight/2 - 30))
        gameDisplay.blit(text, textRectangle)
        text = font.render("High Score : {}".format(highScore), True, (0, 0, 0))
        textRectangle = text.get_rect(center=(displayWidth/2, displayHeight/2))
        gameDisplay.blit(text, textRectangle)
        text = font.render("Press Space To Restart (OR) Esc To End", True, (0, 0, 0))
        textRectangle = text.get_rect(center=(displayWidth/2, displayHeight/2 + 30))
        gameDisplay.blit(text, textRectangle)
        xVelocity = yVelocity = 0

    # Snake Head Position Checking and Length Increasing
    headList = []
    headList.append(xPosition)
    headList.append(yPosition)
    bodyList.append(headList)

    # Drawing Snake and Maintaining Length
    if len(bodyList) > bodyLength :
        del bodyList[0]
    for x, y in bodyList :
        pygame.draw.rect(gameDisplay, colorBlack, [x, y, 15, 15])

    pygame.display.update()
    clock.tick(24)

# highScoreFile.close()
pygame.quit()
quit()

## Created by Joydeep Biswas ##
