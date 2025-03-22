import pygame
import sys
from pieces import wP, bP, wR, bR, wKnight, bKnight, wB, bB, wQ, bQ, wK, bK
from tile_center_position import tile_center_position

#initialize pygame
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 800
BOARD_SIZE = 640
ROWS, COLS = 8, 8
SQUARE_SIZE = BOARD_SIZE // COLS
MARGIN_X = (WINDOW_WIDTH - BOARD_SIZE) // 2
MARGIN_Y = (WINDOW_HEIGHT - BOARD_SIZE) // 2


# Colors
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)
HIGHLIGHT = (200, 200, 50)  # Yellow highlight
BG_COLOR = (50, 50, 50)

# if value is 1 then its acccupied by white pieces if 2 then black pieces if 0 then empty
# 3 for kings either white king or black king
board_state = [
    2 , 2 , 2 , 2 , 3 , 2 , 2 , 2 ,
    2 , 2 , 2 , 2 , 2 , 2 , 2 , 2 ,
    0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,
    0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,
    0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,
    0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,
    1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,
    1 , 1 , 1 , 1 , 3 , 1 , 1 , 1  ]


# the game in string format stored in the list                          
board_pieces = [
    "bR" , "bKnight" , "bB" , "bQ" , "bK" , "bB" , "bKnight" , "bR" ,                      
    "bP" ,    "bP"   , "bP" , "bP" , "bP" , "bP" ,    "bP"   , "bP" ,
    "0"  ,     "0"   ,  "0" ,  "0" ,  "0" ,  "0" ,     "0"   ,  "0" ,
    "0"  ,     "0"   ,  "0" ,  "0" ,  "0" ,  "0" ,     "0"   ,  "0" ,
    "0"  ,     "0"   ,  "0" ,  "0" ,  "0" ,  "0" ,     "0"   ,  "0" ,
    "0"  ,     "0"   ,  "0" ,  "0" ,  "0" ,  "0" ,     "0"   ,  "0"  ,
    "wP" ,    "wP"   , "wP" , "wP" , "wP" , "wP" ,    "wP"   , "wP" ,
    "wR" , "wKnight" , "wB" , "wQ" , "wK" , "wB" , "wKnight" , "wR" 
    ]

white = ["wP" , "wR" , "wKnight" , "wB" , "wQ" , "wK"]
black = ["bP" , "bR" , "bKnight" , "bB" , "bQ" , "bK"]

def highlighted_tile_color_position(index1):
    row, col = divmod(index1, COLS)
    x = MARGIN_X + col * SQUARE_SIZE
    y = MARGIN_Y + row * SQUARE_SIZE
    highlight_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
    highlight_surface.fill((255, 255, 0, 100))  # Yellow with 100 alpha (transparency)
    screen.blit(highlight_surface, (x, y))

# Create window
def create_window():
    global screen
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Chess Game")

#function to draw the board
def draw_board():
    """Draws the chessboard centered on the screen."""
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BROWN
            x = MARGIN_X + col * SQUARE_SIZE
            y = MARGIN_Y + row * SQUARE_SIZE
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

"""draws pieces on the board iterates through the list of pieces and draws them on the board, 
using the x and y coordinates of the pieces
that are stored in another list called tile_center_position"""
def draw_pieces():
    for i in range(64):
        if board_pieces[i] == "bR":
            screen.blit(bR, (tile_center_position[i][0], tile_center_position[i][1]))
        elif board_pieces[i] == "bKnight":
            screen.blit(bKnight, (tile_center_position[i][0], tile_center_position[i][1]))
        elif board_pieces[i] == "bB":
            screen.blit(bB, (tile_center_position[i][0], tile_center_position[i][1]))
        elif board_pieces[i] == "bQ":
            screen.blit(bQ, (tile_center_position[i][0], tile_center_position[i][1]))
        elif board_pieces[i] == "bK":
            screen.blit(bK, (tile_center_position[i][0], tile_center_position[i][1]))
        elif board_pieces[i] == "bP":
            screen.blit(bP, (tile_center_position[i][0], tile_center_position[i][1]))
        elif board_pieces[i] == "wR":
            screen.blit(wR, (tile_center_position[i][0], tile_center_position[i][1]))
        elif board_pieces[i] == "wKnight":
            screen.blit(wKnight, (tile_center_position[i][0], tile_center_position[i][1]))
        elif board_pieces[i] == "wB":
            screen.blit(wB, (tile_center_position[i][0], tile_center_position[i][1]))
        elif board_pieces[i] == "wQ":
            screen.blit(wQ, (tile_center_position[i][0], tile_center_position[i][1]))
        elif board_pieces[i] == "wK":
            screen.blit(wK, (tile_center_position[i][0], tile_center_position[i][1]))
        elif board_pieces[i] == "wP":
            screen.blit(wP, (tile_center_position[i][0], tile_center_position[i][1]))
        elif board_pieces[i] == "0":
            continue

#this function identify on which tile the user clicked it return index.
def user_click_position(position):
    x, y = position  # Unpack the tuple

    # Adjust click position relative to the board
    x -= MARGIN_X
    y -= MARGIN_Y

    # Check if click is within the board boundaries
    if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
        col = x // SQUARE_SIZE
        row = y // SQUARE_SIZE
        index = row * COLS + col  # Calculate the index based on row-major order
        print(f"Mouse clicked at: ({position[0]}, {position[1]}), Index: {index}")
        return index


# needs to be modified 
def pieces_movement(user_first_click,user_second_click,test):
    #variable user_first_click stores users first click
    #variable user_second_click stores user second click
    #availabe_position stores the vector of availabe positions
    
    if int(user_second_click) in test:
        board_pieces[user_second_click] = board_pieces[user_first_click]
        board_pieces[user_first_click] = "0"
        board_state[user_second_click] = board_state[user_first_click]
        board_state[user_first_click] = 0
        draw_board()
        draw_pieces()
        


def highlight_square(index1):
    
    posibble_moves = []
    #global highlighted_square
    draw_board()
    draw_pieces()
    highlighted_tile_color_position(index1)


    # this will allow me to use the highlight algorithm without having to copy it for differet collor
    if board_pieces[index1] in white:
        var = board_pieces[index1]
        ally = 1
        enemy = 2
    elif board_pieces[index1] in black:
        var = board_pieces[index1]
        ally = 2
        enemy = 1

    else:
        posibble_moves.append(-1)
        return posibble_moves

    if var == "bP" and index1 in range(8, 16):  # "bP" first move    
        for step in (8, 16):  # Move 1 step (8) and 2 steps (16)
            if board_state[index1 + step]:  # Check if the target square is occupied
                break
            target_index = index1 + step

            highlighted_tile_color_position(target_index)
            posibble_moves.append(target_index)

        not_allowed_positions = [0,8,16,24,32,40,48,56]
        if (index1 + 7 <= 63) and (board_state[index1 + 7] == enemy) and (index1 not in not_allowed_positions) and (board_state[index1 + 7] != 3):
            
            highlighted_tile_color_position(index1 + 7)
            posibble_moves.append(index1 + 7)

        not_allowed_positions = [7,15,23,31,39,47,55,63]
        if (index1 + 9 <= 63) and (board_state[index1 + 9] == enemy) and (index1 not in not_allowed_positions) and (board_state[index1 + 9] != 3):
            
            highlighted_tile_color_position(index1 + 9)
            posibble_moves.append(index1 + 9)

        return posibble_moves


    elif var == "bP": #board_pieces[index1] == var:#"bP"
        if (index1 + 8 <= 63) and (board_state[index1 + 8] != ally) and (board_state[index1 + 8] != enemy):

            highlighted_tile_color_position(index1 + 8)
            posibble_moves.append(index1 + 8)
        
        not_allowed_positions = [0,8,16,24,32,40,48,56]
        if (index1 + 7 <= 63) and (board_state[index1 + 7] == enemy) and (index1 not in not_allowed_positions):
            
            highlighted_tile_color_position(index1 + 7)
            posibble_moves.append(index1 + 7)

        not_allowed_positions = [7,15,23,31,39,47,55,63]
        if (index1 + 9 <= 63) and (board_state[index1 + 9] == enemy) and (index1 not in not_allowed_positions):
            
            highlighted_tile_color_position(index1 + 9)

            posibble_moves.append(index1 + 9)
        return posibble_moves

    elif var == "wP" and index1 in range(48, 56):#"wP"
        #this algorthim will highlight the first posible move for each pawn.
        for step in (8, 16):  # Move 1 step (8) and 2 steps (16)
            if board_state[index1 - step]:
                break

            target_index = index1 - step
            highlighted_tile_color_position(target_index)
            posibble_moves.append(target_index)

        not_allowed_positions = [7,15,23,31,39,47,55,63]
        if (index1 - 7 >= 0) and (board_state[index1 - 7] == enemy) and (index1 not in not_allowed_positions) and (board_state[index1 - 7] != 3):
            
            highlighted_tile_color_position(index1 - 7)
            posibble_moves.append(index1 - 7)

        not_allowed_positions = [0,8,16,24,32,40,48,56]
        if (index1 - 9 >= 0) and (board_state[index1 - 9] == enemy) and (index1 not in not_allowed_positions) and (board_state[index1 - 9] != 3):
            
            highlighted_tile_color_position(index1 - 9)
            posibble_moves.append(index1 - 9)

        return posibble_moves

    #adawd
    elif var == "wP": #board_pieces[index1] == var:#"wP"
        if index1 - 8 >= 0 and (board_state[index1 - 8] != ally) and (board_state[index1 - 8] != enemy):
            
            highlighted_tile_color_position(index1 - 8)
            posibble_moves.append(index1 - 8)

        not_allowed_positions = [7,15,23,31,39,47,55,63]
        if (index1 - 7 >= 0) and (board_state[index1 - 7] == enemy) and (index1 not in not_allowed_positions):
            
            highlighted_tile_color_position(index1 - 7)
            posibble_moves.append(index1 - 7)

        not_allowed_positions = [0,8,16,24,32,40,48,56]
        if (index1 - 9 >= 0) and (board_state[index1 - 9] == enemy) and (index1 not in not_allowed_positions):
            
            highlighted_tile_color_position(index1 - 9)
            posibble_moves.append(index1 - 9)

        return posibble_moves
    


#white pawns are done now off to Rook 


    #Rook movement +y-y///+x-x
    elif var == "wR" or var == "bR": #board_pieces[index1] == var:#"wR"
        num = 8
        positive_y = index1
        while (positive_y >= 0) and (positive_y - 8 >= 0) and (board_state[positive_y - 8] != 3):
            positive_y -= num
            if board_state[positive_y] == ally:
                break
            if board_state[positive_y] == enemy:
                
                highlighted_tile_color_position(positive_y)
                posibble_moves.append(positive_y)
                break
            
            highlighted_tile_color_position(positive_y)
            posibble_moves.append(positive_y)

        
        negative_y = index1
        while (negative_y < 64) and (negative_y + 8 < 64) and (board_state[negative_y + 8] != 3):
            negative_y += num
            if board_state[negative_y] == ally:
                break
            if board_state[negative_y] == enemy:
                
                highlighted_tile_color_position(negative_y)
                posibble_moves.append(negative_y)
                break
            highlighted_tile_color_position(negative_y)
            posibble_moves.append(negative_y)
        

        positive_x = index1
        upper_bound = (positive_x // 8) * 8 + 7
        start_value = positive_x + 1
        for i in range(start_value, upper_bound + 1):
            if board_state[i] == ally or board_state[i] == 3:
                break

            if board_state[i] == enemy:
                
                highlighted_tile_color_position(i)
                posibble_moves.append(i)
                break
            highlighted_tile_color_position(i)
            posibble_moves.append(i)
        
        negative_x = index1
        lower_bound = (negative_x // 8) * 8 
        start_value = negative_x - 1
        for i in range(start_value, lower_bound - 1, -1):
            if board_state[i] == ally or board_state[i] == 3:
                break

            if board_state[i] == enemy:

                highlighted_tile_color_position(i)
                posibble_moves.append(i)
                break
            
            highlighted_tile_color_position(i)
            posibble_moves.append(i)

        return posibble_moves

    #knight movement
    elif var == "wKnight" or var == "bKnight":
        far_right_up = index1 - 6
        if (far_right_up >= 0) and ((index1 // 8) != (far_right_up // 8)) and (board_state[far_right_up] != ally) and (board_state[far_right_up] != 3):
            
            highlighted_tile_color_position(far_right_up)
            posibble_moves.append(far_right_up)

        mid_up_right = index1 - 15
        if (mid_up_right >= 0) and ((index1 // 8) >= (mid_up_right // 8) + 2) and (board_state[mid_up_right] != ally) and (board_state[mid_up_right] != 3):
            
            highlighted_tile_color_position(mid_up_right)
            posibble_moves.append(mid_up_right)

        mid_up_left = index1 - 17
        not_allowed_positions = [24,32,40,48,56]
        if((mid_up_left >= 0) and (index1 not in not_allowed_positions) and (board_state[mid_up_left] != ally) and (board_state[mid_up_left] != 3)):
            
            highlighted_tile_color_position(mid_up_left)
            posibble_moves.append(mid_up_left)

        far_left_up = index1 - 10
        not_allowed_positions = [ 
            0,1,2,3,4,5,6,7,
            8,9,16,17,24,25,
            32,33,40,
            41,48,49,56,57
            ]
        if((far_left_up >= 0) and (index1 not in not_allowed_positions) and (board_state[far_left_up] != ally) and (board_state[far_left_up] != 3)):
            highlighted_tile_color_position(far_left_up)
            posibble_moves.append(far_left_up)

        far_left_down = index1 + 6
        not_allowed_positions = [ 
            0,1,8,9,16,17,24,25,
            32,33,40,41,48,49,56,
            57,58,59,60,61,62,63
            ]
        
        if((far_left_down >= 0) and (index1 not in not_allowed_positions) and (board_state[far_left_down] != ally) and (board_state[far_left_down] != 3)):
            highlighted_tile_color_position(far_left_down)
            posibble_moves.append(far_left_down)

        mid_down_left = index1 + 15
        not_allowed_positions = [
            0,8,16,24,32,40,48,
            56,49,50,51,52,53,
            54,55,57,58,59,60,
            61,62,63
        ] 
        if((mid_down_left >= 0) and (index1 not in not_allowed_positions) and (board_state[mid_down_left] != ally) and (board_state[mid_down_left] != 3)):
            highlighted_tile_color_position(mid_down_left)
            posibble_moves.append(mid_down_left)


        mid_down_right = index1 + 17
        not_allowed_positions = [
            7,15,23,31,39,47,48,
            56,49,50,51,52,53,
            54,55,57,58,59,60,
            61,62,63
        ] 

        if((mid_down_right >= 0) and (index1 not in not_allowed_positions) and (board_state[mid_down_right] != ally) and (board_state[mid_down_right] != 3)):
            highlighted_tile_color_position(mid_down_right)
            posibble_moves.append(mid_down_right)

        far_right_down = index1 + 10
        not_allowed_positions = [
            6,7,14,15,22,23,30,31,38,39,
            46,47,54,55,56,57,58,59,60,
            61,62,63
        ]

        if((far_right_down >= 0) and (index1 not in not_allowed_positions) and (board_state[far_right_down] != ally) and (board_state[far_right_down] != 3)):
            
            highlighted_tile_color_position(far_right_down)
            posibble_moves.append(far_right_down)

        return posibble_moves
    
    #bishop movement
    elif var == "wB" or var == "bB":
        top_right = index1 - 7
        not_allowed_positions = [7,15,23,31,39,47,55,63]

        while((top_right >= 0) and((top_right + 7) not in not_allowed_positions) and(board_state[top_right] != ally)) and (board_state[top_right] != 3):
            
            highlighted_tile_color_position(top_right)
            posibble_moves.append(top_right)

            if board_state[top_right] == enemy:
                break
            
            top_right -= 7


        top_left = index1 - 9
        not_allowed_positions = [0,8,16,24,32,40,48, 56]

        while((top_left >= 0) and((top_left + 9) not in not_allowed_positions) and(board_state[top_left] != ally)) and (board_state[top_left] != 3):
            
            highlighted_tile_color_position(top_left)
            posibble_moves.append(top_left)

            if board_state[top_left] == enemy:
                break
            top_left -= 9


        bottom_left = index1 + 7
        not_allowed_positions = [0,8,16,24,32,40,48,56]

        while((bottom_left <= 63) and((bottom_left - 7 ) not in not_allowed_positions) and(board_state[bottom_left] != ally)) and (board_state[bottom_left] != 3):
            
            highlighted_tile_color_position(bottom_left)
            posibble_moves.append(bottom_left)

            if board_state[bottom_left] == enemy:
                break
            bottom_left += 7


        # this is what is breaking the program
        bottom_right = index1 + 9
        not_allowed_positions = [7,15,23,31,39,47,55,63]
        while((bottom_right <= 63) and((bottom_right - 9 ) not in not_allowed_positions) and(board_state[bottom_right] != ally)) and (board_state[bottom_right] != 3):
            
            highlighted_tile_color_position(bottom_right)
            posibble_moves.append(bottom_right)

            if(board_state[bottom_right] == enemy):
                break

            bottom_right += 9

    #queen movement
    elif var == "wQ" or var == "bQ":

        top_right = index1 - 7
        not_allowed_positions = [7,15,23,31,39,47,55,63]

        while((top_right >= 0) and((top_right + 7) not in not_allowed_positions) and(board_state[top_right] != ally)) and (board_state[top_right] != 3):
            
            highlighted_tile_color_position(top_right)
            posibble_moves.append(top_right)

            if board_state[top_right] == enemy:
                break
            top_right -= 7

        top_left = index1 - 9
        not_allowed_positions = [0,8,16,24,32,40,48, 56]

        while((top_left >= 0) and((top_left + 9) not in not_allowed_positions) and(board_state[top_left] != ally)) and (board_state[top_left] != 3):

            highlighted_tile_color_position(top_left)
            posibble_moves.append(top_left)

            if board_state[top_left] == enemy:
                break
            top_left -= 9


        bottom_left = index1 + 7
        not_allowed_positions = [0,8,16,24,32,40,48,56]

        while((bottom_left <= 63) and((bottom_left - 7 ) not in not_allowed_positions) and(board_state[bottom_left] != ally)) and (board_state[bottom_left] != 3):
            
            highlighted_tile_color_position(bottom_left)

            posibble_moves.append(bottom_left)

            if board_state[bottom_left] == enemy:
                break
            bottom_left += 7

        bottom_right = index1 + 9

        not_allowed_positions = [7,15,23,31,39,47,55,63]
        while((bottom_right <= 63) and((bottom_right - 9 ) not in not_allowed_positions) and(board_state[bottom_right] != ally)) and (board_state[bottom_right] != 3):

            highlighted_tile_color_position(bottom_right)
            posibble_moves.append(bottom_right)

            if board_state[bottom_right] == enemy:
                break
            bottom_right += 9


        num = 8
        positive_y = index1
        while positive_y >= 0 and (positive_y - 8 >= 0) and (board_state[positive_y - 8] != 3):
            positive_y -= num
            if board_state[positive_y] == ally:
                break
            if board_state[positive_y] == enemy:

                highlighted_tile_color_position(positive_y)
                posibble_moves.append(positive_y)
                break

            highlighted_tile_color_position(positive_y)
            posibble_moves.append(positive_y)

        
        negative_y = index1
        while negative_y < 64 and (negative_y + 8 < 64) and (board_state[negative_y + 8] != 3):
            negative_y += num
            if board_state[negative_y] == ally:
                break
            if board_state[negative_y] == enemy:

                highlighted_tile_color_position(negative_y)
                posibble_moves.append(negative_y)

                break

            highlighted_tile_color_position(negative_y)
            posibble_moves.append(negative_y)
        
        
        positive_x = index1
        upper_bound = (positive_x // 8) * 8 + 7
        start_value = positive_x + 1

        for i in range(start_value, upper_bound + 1):
            if board_state[i] == ally or board_state[i] == 3:
                break
            
            if board_state[i] == enemy:

                highlighted_tile_color_position(i)
                posibble_moves.append(i)
                break

            highlighted_tile_color_position(i)
            posibble_moves.append(i)
        

        negative_x = index1
        lower_bound = (negative_x // 8) * 8 
        start_value = negative_x - 1

        for i in range(start_value, lower_bound - 1, -1):
            if board_state[i] == ally or board_state[i] == 3:
                break

            if board_state[i] == enemy:
                highlighted_tile_color_position(i)
                posibble_moves.append(i)

                break
            highlighted_tile_color_position(i)
            posibble_moves.append(i)

        return posibble_moves
    
    #king movement
    elif var == "wK" or var == "bK":

        top = index1 - 8
        not_allowed_positions = [0,1,2,3,4,5,6,7]
        if(board_state[top] != ally) and (index1 not in not_allowed_positions) and (board_state[top] != 3):

            highlighted_tile_color_position(top)
            posibble_moves.append(top)

        top_left = index1 - 9
        not_allowed_positions = [0,1,2,3,4,5,6,7,8,16,24,32,40,48, 56]
        if (board_state[top_left] != ally) and (index1 not in not_allowed_positions) and (board_state[top_left] != 3):

            highlighted_tile_color_position(top_left)
            posibble_moves.append(top_left)

        left = index1 - 1
        not_allowed_positions = [0,8,16,24,32,40,48, 56]
        if (board_state[left] != ally) and (index1 not in not_allowed_positions) and (board_state[left] != 3):

            highlighted_tile_color_position(left)
            posibble_moves.append(left)

        bottom_left = index1 + 7
        not_allowed_positions = [0,8,16,24,32,40,48, 56,57,58,59,60,61,62,63]
        if(bottom_left <= 63) and (board_state[bottom_left] != ally) and (index1 not in not_allowed_positions) and (board_state[bottom_left] != 3):

            highlighted_tile_color_position(bottom_left)
            posibble_moves.append(bottom_left)

        bottom = index1 + 8
        not_allowed_positions = [56,57,58,59,60,61,62,63]
        if(bottom <= 63) and (board_state[bottom] != ally) and (index1 not in not_allowed_positions) and (board_state[bottom] != 3):

            highlighted_tile_color_position(bottom)
            posibble_moves.append(bottom)

        bottom_right = index1 + 9
        not_allowed_positions = [56,57,58,59,60,61,62,63,7,15,23,31,39,47,55]
        if(bottom_right <= 63) and (board_state[bottom_right] != ally) and (index1 not in not_allowed_positions) and (board_state[bottom_right] != 3):

            highlighted_tile_color_position(bottom_right)
            posibble_moves.append(bottom_right)

        right = index1 + 1
        not_allowed_positions = [63,7,15,23,31,39,47,55]
        if(right <= 63) and (board_state[right] != ally) and (index1 not in not_allowed_positions) and (board_state[right] != 3):

            highlighted_tile_color_position(right)
            posibble_moves.append(right)

        top_right = index1 - 7
        not_allowed_positions = [63,7,15,23,31,39,47,55,0,1,2,3,4,5,6,7]
        if(top_right >= 0) and (board_state[top_right] != ally) and (index1 not in not_allowed_positions) and (board_state[top_right] != 3):

            highlighted_tile_color_position(top_right)
            posibble_moves.append(top_right)
    
    else:
        posibble_moves.append(-1)
    return posibble_moves


# Main loop
def main():
    create_window()
    running = True
    screen.fill(BG_COLOR)
    draw_board()
    draw_pieces()

    test = []
    first_move_bool = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Close window when X is clicked
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click event
                #it gets first click and stores it in index1
                #then it checks if index1 is in the board boundaries if not it will wait till the user clicks on the board

                if first_move_bool:
                    index1 = user_click_position(event.pos)
                    if index1 is None:
                        continue
                    test = highlight_square(index1)
                    print(f"index1 : {index1}, and test is: {test}")
                    first_move_bool = False
                    

                elif first_move_bool == False:
                    index2 = user_click_position(event.pos)
                    if index2 is None:
                        continue
                    print(f"index2 : {index2}")
                    if index1 == index2:
                        draw_board()
                        draw_pieces()
                        test = []
                        first_move_bool = True
                        continue
                    if index2 not in test or (-1 in test):#check if the user second input is not in test"vector" then if its not assign index2 to index1
                        draw_board()
                        draw_pieces()
                        index1 = index2 
                        test = highlight_square(index2)
                        print(f"new index1 is old index2: {index1}, and new test is: {test}")
                        first_move_bool = False
                    elif index2 in test:
                        pieces_movement(index1,index2,test)
                        test = []
                        draw_board()
                        draw_pieces()
                        first_move_bool = True

        # Update the display
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

