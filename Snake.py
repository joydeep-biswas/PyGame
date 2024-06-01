import pygame
import random

# Initialization of Components and Colors
pygame.init()
pygame.font.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
display_width = 640
display_height = 480
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("PyGame SNAKE")
# highScoreFile = open("HighScore.txt", "r") # Opening The File Containing High Score in Read Mode
clock = pygame.time.Clock()

# Game Variables
game_over = False
end_game = False
y_movement = True
x_movement = True
body_length = 1
player_score = 0
# high_score = int(high_score_file.read()) # Reading The High Score
high_score = 0
x_velocity = 0
y_velocity = 0
x_position = round(display_width / 2)
y_position = round(display_height / 2)
x_food = random.randint(35, display_width - 35)
y_food = random.randint(25, display_height - 25)
body_list = []
head_list = []

def game_reset() :
    global game_over, end_game, y_movement, x_movement, body_length, player_score, x_velocity, y_velocity, x_position, y_position, x_food, y_food, body_list
    game_over = False
    end_game = False
    y_movement = True
    x_movement = True
    body_length = 1
    player_score = 0
    x_velocity = 0
    y_velocity = 0
    x_position = round(display_width / 2)
    y_position = round(display_height / 2)
    x_food = random.randint(35, display_width - 35)
    y_food = random.randint(25, display_height - 25)
    body_list = []

def update_action(xv, yv, xm, ym):
    global x_velocity, y_velocity, x_movement, y_movement
    
    x_velocity = xv
    y_velocity = yv
    x_movement = xm
    y_movement = ym

game_reset()

# Game Loop
while not end_game:

    # Checking Pressed Key
    for key_press in pygame.event.get() :
        if key_press.type == pygame.KEYDOWN :
            if key_press.key == pygame.K_RIGHT and y_movement :
                update_action(5, 0, True, False)
            if key_press.key == pygame.K_LEFT and y_movement:
                update_action(-5, 0, True, False)
            if key_press.key == pygame.K_UP and x_movement:
                update_action(0, -5, False, True)
            if key_press.key == pygame.K_DOWN and x_movement:
                update_action(0, 5, False, True)
            if key_press.key == pygame.K_SPACE and game_over:
                game_reset()
            if key_press.key == pygame.K_ESCAPE and game_over:
                end_game = True

        if key_press.type == pygame.QUIT :
            end_game = True
        
    x_position = x_position + x_velocity
    y_position = y_position + y_velocity

    # Score Counter and Random Food Spawner
    if abs(x_position - x_food) < 7 and abs(y_position - y_food) < 7 and not game_over :
        player_score = player_score + 1
        x_food = random.randint(35, display_width - 35)
        y_food = random.randint(25, display_height - 25)
        body_length = body_length + 1
    
    # Collision Checking 1 (Wall Collision Checking)
    if x_position < 1 or x_position > 639 or y_position < 1 or y_position > 479 :
        game_over = True

    # Collision Checking 2 (Self Collision Checking)
    for x in body_list[:len(body_list) - 1] :
        if x == headList and (not x_movement or not y_movement):
            game_over = True
    
    game_display.fill(WHITE)
    font = pygame.font.SysFont(None, 40)

    # Displaying Score and Game Over Message
    if not game_over :
        text = font.render("{}".format(player_score), True, (0, 0, 0))
        game_display.blit(text, (320, 5))
        pygame.draw.rect(game_display, RED, [x_food, y_food, 15, 15])
    else :
        # High Score Checking and Modifying
        if player_score > high_score :
            # highScoreFile.close()
            # highScoreFile = open("HighScore.txt", "w") # Opening The File Containing High Score in Read Mode
            high_score = player_score
            # highScoreFile.write(str(highScore)) # Writing The High Score

        text = font.render("Game Over! Your Score : {}".format(player_score), True, (0, 0, 0))
        textRectangle = text.get_rect(center=(display_width / 2, display_height / 2 - 30))
        game_display.blit(text, textRectangle)
        text = font.render("High Score : {}".format(high_score), True, (0, 0, 0))
        textRectangle = text.get_rect(center=(display_width / 2, display_height / 2))
        game_display.blit(text, textRectangle)
        text = font.render("Press Space To Restart (OR) Esc To End", True, (0, 0, 0))
        textRectangle = text.get_rect(center=(display_width / 2, display_height / 2 + 30))
        game_display.blit(text, textRectangle)
        x_velocity = y_velocity = 0

    # Snake Head Position Checking and Length Increasing
    headList = []
    headList.append(x_position)
    headList.append(y_position)
    body_list.append(headList)

    # Drawing Snake and Maintaining Length
    if len(body_list) > body_length :
        del body_list[0]
    for x, y in body_list :
        pygame.draw.rect(game_display, BLACK, [x, y, 15, 15])

    pygame.display.update()
    clock.tick(24)

# highScoreFile.close()
pygame.quit()
quit()

## Created by Joydeep Biswas ##
