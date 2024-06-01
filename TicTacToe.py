import pygame

# Initialization of Components and Colors
pygame.init()
pygame.font.init()

# Game Constant Declaration
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

display_width = display_height = 480
x_offset = y_offset = offset = 0
game_board_width = display_width - offset
game_board_height = (display_width - offset) + y_offset

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("PyGame TicTacToe")

symbol_font = pygame.font.SysFont('Arial', 100)
font_1 = pygame.font.SysFont('Arial', 25)
font_2 = pygame.font.SysFont('Arial', 16)
clock = pygame.time.Clock()

def game_reset():
    global game_over, end_game, player_turn, game_array, grid_array

    game_over = False
    end_game = False
    player_turn = "X"
    game_array = [[None, None, None],
                  [None, None, None],
                  [None, None, None]]
    grid_array = []

    game_display.fill(WHITE)
    draw_grid()


# Drawing Fixed UI Components    
def draw_grid():
    blockSize = (display_width - (2 * offset)) / 3
    for row in range(3):
        for column in range(3):
            rectangle = ((blockSize * row) + x_offset, (blockSize * column) + y_offset, blockSize, blockSize)
            pygame.draw.rect(game_display, BLACK, rectangle, 1)
            positionArray = (int(rectangle[0] + blockSize / 2), int(rectangle[1] + blockSize / 2))
            grid_array.append(positionArray)

def draw_symbol(row, column, xPosition, yPosition):
    global game_array, player_turn

    game_array[row][column] = player_turn

    text = symbol_font.render(player_turn, True, (0, 0, 0))
    text_rectangle = text.get_rect(center=(xPosition, yPosition))
    game_display.blit(text, text_rectangle)

def row_checker(click_position, row):
    match row:
        case 0:
            if(click_position[0] > x_offset and click_position[0] < game_board_width / 3 + x_offset):
                return True
            else:
                return False
        case 1:
            if(click_position[0] > game_board_width / 3 + x_offset and click_position[0] < 2 * game_board_width / 3 + x_offset):
                return True
            else:
                return False
        case 2:
            if(click_position[0] > 2 * game_board_width / 3 + x_offset and click_position[0] < game_board_width):
                return True
            else:
                return False

def column_checker(click_position, column):
    match column:
        case 0:
            if(click_position[1] > y_offset and click_position[1] < game_board_height / 3 + y_offset):
                return True
            else:
                return False
        case 1:
            if(click_position[1] > game_board_height / 3 + y_offset and click_position[1] < 2 * game_board_height / 3 + y_offset):
                return True
            else:
                return False
        case 2:
            if(click_position[1] > 2 * game_board_height / 3 + y_offset and click_position[1] < game_board_height):
                return True
            else:
                return False

def draw_menu(text_1, text_2):
    alphaRectangle = (x_offset, x_offset, game_board_width, game_board_height)
    shapeSurface = pygame.Surface(pygame.Rect(alphaRectangle).size, pygame.SRCALPHA)
    pygame.draw.rect(shapeSurface, (255, 255, 255, 175), shapeSurface.get_rect())
    game_display.blit(shapeSurface, alphaRectangle)

    text = font_1.render(text_1, True, (0, 0, 0))
    textRectangle = text.get_rect(center=(display_width / 2, (x_offset + y_offset / 3) / 2 + 14))
    game_display.blit(text, textRectangle)

    text = font_2.render(text_2, True, (0, 0, 0))
    textRectangle = text.get_rect(center=(display_width / 2, (x_offset + y_offset / 3) / 2 + 34))
    game_display.blit(text, textRectangle)

def draw_line(row_1, row_2, column_1, column_2):
    pygame.draw.line(game_display, (0, 255, 200),
                     ((grid_array[row_1][column_1] - 2 * offset), (grid_array[row_1][column_2])),
                     ((grid_array[row_2][column_1] + 2 * offset), (grid_array[row_2][column_2])), 5)
def player_won():
    global game_array

    for row in range(3):
        if(game_array[row][0] == game_array[row][1] == game_array[row][2]) and game_array[row][2] is not None:
            draw_line(row, row + 6, 0, 1)
            return True
    for column in range(3):
        if(game_array[0][column] == game_array[1][column] == game_array[2][column]) and game_array[2][column] is not None:
            draw_line(column, column + 6, 1, 0)
            return True
    if(game_array[0][0] == game_array[1][1] == game_array[2][2]) and game_array[1][1] is not None:
        draw_line(0, 8, 1, 0)
        return True
    if(game_array[2][0] == game_array[1][1] == game_array[0][2]) and game_array[1][1] is not None:
        draw_line(0, 8, 0, 1)
        return True
    return False

def is_tie():
    global game_array
    for i in range(3):
        for j in range(3):
            if(game_array[i][j] is None):
                return True
    return False


def switch_player():
    global player_turn

    if player_turn == 'X':
        player_turn = 'O'
    elif player_turn == 'O':
        player_turn = 'X'


game_reset()

# Game Loop
while not end_game:

    for key_press in pygame.event.get():
        if key_press.type == pygame.QUIT:
            end_game = True
        if key_press.type == pygame.KEYDOWN :
            if key_press.key == pygame.K_SPACE and game_over:
                game_reset()
            if key_press.key == pygame.K_ESCAPE and game_over:
                end_game = True

        if not game_over:
            if pygame.mouse.get_pressed()[0]:
                clickPosition = pygame.mouse.get_pos()
                for row in range(3):
                    if(column_checker(clickPosition, row)):
                        for column in range(3):
                            if(row_checker(clickPosition, column)):
                                if(game_array[row][column] == None):
                                    draw_symbol(row, column, grid_array[row + column * 3][0],
                                                grid_array[row + column * 3][1])
                                    # Changing Player
                                    switch_player()

        if(player_won() and not game_over):
            game_over = True
            switch_player()
            draw_menu("Game Over! Player {} Won!".format(player_turn), "SPACE to Reset, ESC to End")

        if not is_tie() and not game_over:
            game_over = True
            draw_menu("It's a Draw!", "SPACE to Reset, ESC to End")

    pygame.display.update()
    clock.tick(24)

pygame.quit()
quit()

## Created by Joydeep Biswas ##