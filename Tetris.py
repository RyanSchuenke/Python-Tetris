# Name: Ryan Schuenke
# Description: final project Tetris


from graphics import *
import random


def menu(window):
    """
    Function for creating the title menu
    :param: window - parameter that allows use of the window
    :return: setting - string that allows for the game to begin
    """
    # creates the window for text to appear in and the title
    title_box = Rectangle(Point(2.5,3.5),Point(15.5,18.5))
    title_box.setFill(color_rgb(255,255,255))
    title_box.draw(window)
    title = Text(Point(9,6),"TETRIS")
    title.setSize(32)
    title.draw(window)

    start = Text(Point(9,9),"Press Enter to Start")
    start.draw(window)
    
    # draws strings for what the game controls are
    control_z = Text(Point(9,11),"z: rotate counter clockwise")
    control_z.draw(window)
    control_x = Text(Point(9,12),"x: rotate clockwise            ")
    control_x.draw(window)
    control_direction = Text(Point(9,13),"move left : <-    ->: move right")
    control_direction.draw(window)
    control_down1 = Text(Point(9,14),"|")
    control_down2 = Text(Point(9,15),"V")
    control_down1.draw(window)
    control_down2.draw(window)
    control_down3 = Text(Point(9,16),"move down")
    control_down3.draw(window)
    control_drop = Text(Point(9,17),"Space: drop to floor")
    control_drop.draw(window)

    # when the player presses enter, the menu is undrawn and the game is allowed to begin
    while window.isOpen():
        key = window.getKey()
        if key == "Return":
            title.undraw()
            start.undraw()
            title_box.undraw()
            control_z.undraw()
            control_x.undraw()
            control_direction.undraw()
            control_down1.undraw()
            control_down2.undraw()
            control_down3.undraw()
            control_drop.undraw()
            return "Start"


def gameover(board, window):
    """
    A function that checks the conditions for losing the game and ends it
    :param: board - dictionary keeping track of the filled squares
            window - paramater allowing for the use of the game window
    :return: loss - variable for stating if the player has lost
    """
    # checks to see if the squares at the top of the box are filled, disallowing for any new pieces to fall.
    while board[9,2] != False or board[9,3] != False or board[10,2] != False or board[10,3] != False or board[11,2] != False or board[11,3] != False:
        
        # draws in the box the same sie as the title and prompts the user to press enter to return to the menu
        title_box = Rectangle(Point(2.5,3.5),Point(15.5,18.5))
        title_box.setFill(color_rgb(255,255,255))
        title_box.draw(window)
        end = Text(Point(9,6),"GAMEOVER")
        end.setSize(32)
        end.draw(window)
        control_prompt = Text(Point(9,9),"Press Enter to reset")
        control_prompt.draw(window)
        
        # gets the key pressed and returns false if enter is pressed
        key = window.getKey()
        if key == "Return":
            title_box.undraw()
            end.undraw()
            return False


def piece_bucket(tetromino_bag):
    """
    Function for creating the 7 piece cycle
    :param: tetromino_bag - list for the cycle of pieces
    :return: list for reverse order of pieces
    """
    
    tetromino_bag.pop() # removes the last item from the list
    
    # if the list is empty, a new one is made and shuffled, so the pieces fall in a cycle of all seven pieces
    if tetromino_bag == []:
        tetromino_bag = ["I", "O", "T", "J", "L", "S", "Z"]
        random.shuffle(tetromino_bag)
        return tetromino_bag
    
    #if there are still items in the list, it is returned with one less item on the end
    else:
        return tetromino_bag
    

def generate_piece(piece, window):
    """
    function for creating the 7 different pieces
    :param: piece - letter indicating what piece to organize
            window - variable to allow use of the window
    :return: tetromino - list for the blocks in a piece
    """
    # creates a list containing the pieces that make up a tetromino
    tetromino = []
    block1 = Rectangle(Point(0,0), Point(1,1))
    block2 = Rectangle(Point(0,0), Point(1,1))
    block3 = Rectangle(Point(0,0), Point(1,1))
    block4 = Rectangle(Point(0,0), Point(1,1))
    tetromino = [block1, block2, block3, block4]
    for block in tetromino:
        block.draw(window)
    
    #moves the tetromino and sets the fill of each block according to what piece type it is
    if piece == "O":
        block1.move(9,1)
        block2.move(10,1)
        block3.move(9,2)
        block4.move(10,2)
        for block in tetromino:
            block.setFill(color_rgb(255,255,0))
    
    elif piece == "I":
        block1.move(8,2)
        block2.move(9,2)
        block3.move(10,2)
        block4.move(11,2)
        for block in tetromino:
            block.setFill(color_rgb(0,255,255))
    
    elif piece == "J":
        block1.move(8,1)
        block2.move(9,1)
        block3.move(10,1)
        block4.move(10,2)
        for block in tetromino:
            block.setFill(color_rgb(0,0,255))
    
    elif piece == "L":
        block1.move(8,2)
        block2.move(8,1)
        block3.move(9,1)
        block4.move(10,1)
        for block in tetromino:
            block.setFill(color_rgb(255,127,0))
    
    elif piece == "S":
        block1.move(8,2)
        block2.move(9,2)
        block3.move(9,1)
        block4.move(10,1)
        for block in tetromino:
            block.setFill(color_rgb(0,255,0))
    
    elif piece == "Z":
        block1.move(8,1)
        block2.move(9,1)
        block3.move(9,2)
        block4.move(10,2)
        for block in tetromino:
            block.setFill(color_rgb(255,0,0))
    
    elif piece == "T":
        block1.move(8,1)
        block2.move(9,1)
        block3.move(9,2)
        block4.move(10,1)
        for block in tetromino:
            block.setFill(color_rgb(128,0,128))
            
    # returns the list of the tetromino pieces
    return tetromino
        
    
def piece_control(rotation,tetromino,piece,board,window):
    """
    function for accepting user input
    :param: rotation - integer for the current rotation state of the piece
            tetromino - list containing the four blocks of a tetromino
            piece - string specifying the type of piece currently moveable
            board - dictionary containing the state of each tile of the game board, allowing for hcheking if it is filled
            window - parameter allowing for accessing the gae window
    :return: rotation - rotation state of the piece
    """
    # checks for input from the user whithout stopping the game
    key = window.checkKey()
    
    # if the user presses left, each block in the piece will move left as long as it isn't on the board edge or directly next to a filled square
    if key == "Left":
        for block in tetromino:
            if block.getP2().getX() == 5 or board[block.getP2().getX()-1,block.getP2().getY()] != False:
                return rotation
        for block in tetromino:
            block.move(-1,0)
            
    # if the user presses right, each block in the piece will move right as long as it isn't on the board edge or directly next to a filled square
    elif key == "Right":
        for block in tetromino:
            if block.getP2().getX() == 14 or board[block.getP2().getX()+1,block.getP2().getY()] != False:
                return rotation
        for block in tetromino:
            block.move(1,0)
            
    # if the user presses down, each block in the piece will move downwards by one square
    elif key == "Down":
        for block in tetromino:
            if block.getP2().getY() ==23:
                return rotation
        for block in tetromino:
            block.move(0,1)
    
    # if the user presses space, each block of the teranimo moves down by the least number of squares to the floor or filled square
    elif key == "space":
        drop_distance = 25
        for row in range(1,24): # iterates downward through the rows of the board
            for block in tetromino:
                
                # if there is a filled square below one of the blocks, the drop distance is checked to see if it would be less than the current value 
                if board[block.getP2().getX(),row] != False and (row-1-block.getP2().getY())< drop_distance:
                    # sets the drop distance to the number of tiles the piece needs to move down to touch the top of the filled square
                    drop_distance = row-1-block.getP2().getY()
                    
                # if there are no filled squares below the piece, the distance is checked to see how far it needs to fall to the floor
                elif (23-block.getP2().getY())< drop_distance:
                    
                    # sets the drop distance to be equal to the shortest distance a block in the piecce needs to fall to reach it
                    drop_distance = 23 - block.getP2().getY()
        
        # after finding the minimum distance a block needs to fall to be placed, each block is moved down by that much
        for block in tetromino:
            block.move(0,drop_distance)
            
    # if the z key is pressed, the rotation function is called and tries to rotate the piece counterclockwise
    elif key.lower() == "z":
        rotation = rotate(rotation,"L", piece,tetromino,board)
    
    # if the x key is pressed, the rotation function is called and tries to rotate the piece clockwise
    elif key.lower() == "x":
        rotation = rotate(rotation,"R", piece,tetromino,board)
    
    # if no key is pressed, the rotation is returned
    return rotation


def rotate(rotation, direction, piece_type, tetromino, board):
    """
    :param: rotation - parameter that contains an integer specifying the current piece's rotation state
            direction - string specifying the direction the piece will attempt to be rotated
            piece_type - string specifying which piece is trying to be rotated
            tetromino - a list containing the blocks that make up each piece
            board - a dictionary containing the current state of each tile on the board
    :return: rotation - variable containing an integer for the piece's new rotation
    """
    # firstly, the piece type is checked
    if piece_type == "I":
        # the rotation is then checked and the squares that the block is going to move into are checked next to verify they are in the board
        # if the square isn't in the board, no rotation occurs since the piece would be rotating out of the grid
        if (rotation == 0 and (tetromino[3].getP2().getX(),tetromino[3].getP2().getY()+1) in board and
            (tetromino[3].getP2().getX(),tetromino[3].getP2().getY()-1) in board and
            (tetromino[3].getP2().getX(),tetromino[3].getP2().getY()-2) in board):
            
            # nexxt, the squares that the piece will move into are checked to make sure they are empty
            if (board[tetromino[3].getP2().getX(),tetromino[3].getP2().getY()+1] == False and
                board[tetromino[3].getP2().getX(),tetromino[3].getP2().getY()-1] == False and
                board[tetromino[3].getP2().getX(),tetromino[3].getP2().getY()-2] == False):
                
                # if all conditions are met, each piece is moved into its new position and the rotation is updated
                tetromino[0].move(2,-2)
                tetromino[1].move(1,-1)
                tetromino[3].move(-1,1)
                rotation = 1
        elif (rotation == 1 and (tetromino[3].getP2().getX()+1,tetromino[3].getP2().getY()) in board and
              (tetromino[3].getP2().getX()-1,tetromino[3].getP2().getY()) in board and
              (tetromino[3].getP2().getX()-2,tetromino[3].getP2().getY()) in board):
            if (board[tetromino[3].getP2().getX()+1,tetromino[3].getP2().getY()] == False and
                board[tetromino[3].getP2().getX()-1,tetromino[3].getP2().getY()] == False and
                board[tetromino[3].getP2().getX()-2,tetromino[3].getP2().getY()] == False):
                tetromino[0].move(-2,2)
                tetromino[1].move(-1,1)
                tetromino[3].move(1,-1)
                rotation = 0
    # the same general process is repeated for each piece type, rotation state, and going clockwise or counterclockwise
    
    elif piece_type == "J":
        if direction == "R":
            if (rotation == 0 and board[tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()+1] == False and
                board[tetromino[1].getP2().getX(),tetromino[1].getP2().getY()+1] == False
                and board[tetromino[1].getP2().getX(),tetromino[1].getP2().getY()-1] == False):
                tetromino[0].move(1,-1)
                tetromino[2].move(-1,1)
                tetromino[3].move(-2,0)
                rotation = 1
            elif rotation == 1 and (tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()) in board:
                if (board[tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()] == False and
                    board[tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()-1] == False and
                    board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()] == False):
                    tetromino[0].move(1,1)
                    tetromino[2].move(-1,-1)
                    tetromino[3].move(0,-2)
                    rotation = 2
            elif (rotation == 2 and board[tetromino[1].getP2().getX(),tetromino[1].getP2().getY()+1] == False and
                  board[tetromino[1].getP2().getX(),tetromino[1].getP2().getY()-1] == False and
                  board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()+1] == False):
                tetromino[0].move(-1,1)
                tetromino[2].move(1,-1)
                tetromino[3].move(2,0)
                rotation = 3
            elif rotation == 3 and (tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()) in board:
                if (board[tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()] == False and
                    board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()] == False and
                    board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()+1] == False):
                    tetromino[0].move(-1,-1)
                    tetromino[2].move(1,1)
                    tetromino[3].move(0,2)
                    rotation = 0
        elif direction == "L":
            if (rotation == 0 and board[tetromino[1].getP2().getX(),tetromino[1].getP2().getY()+1] == False and
                board[tetromino[1].getP2().getX(),tetromino[1].getP2().getY()-1] == False and
                board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()-1] == False):
                tetromino[0].move(1,1)
                tetromino[2].move(-1,-1)
                tetromino[3].move(0,-2)
                rotation = 3
            elif rotation == 3 and (tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()) in board:
                if (board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()] == False and
                    board[tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()] == False and
                    board[tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()-1] == False):
                    tetromino[0].move(1,-1)
                    tetromino[2].move(-1,1)
                    tetromino[3].move(-2,0)
                    rotation = 2
            elif (rotation == 2 and board[tetromino[1].getP2().getX(),tetromino[1].getP2().getY()-1] == False and
                  board[tetromino[1].getP2().getX(),tetromino[1].getP2().getY()+1] == False and
                  board[tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()+1] == False):
                tetromino[0].move(-1,-1)
                tetromino[2].move(1,1)
                tetromino[3].move(0,2)
                rotation = 1
            elif rotation == 1 and (tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()) in board:
                if (board[tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()] == False and
                    board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()] == False and
                    board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()+1] == False):
                    tetromino[0].move(-1,1)
                    tetromino[2].move(1,-1)
                    tetromino[3].move(2,0)
                    rotation = 0

    elif piece_type == "L":
        if direction == "R":
            if (rotation == 0 and board[tetromino[2].getP2().getX(),tetromino[2].getP2().getY()+1] == False and
                board[tetromino[2].getP2().getX(),tetromino[2].getP2().getY()-1] == False and
                board[tetromino[2].getP2().getX()-1,tetromino[2].getP2().getY()-1] == False):
                tetromino[0].move(0,-2)
                tetromino[1].move(1,-1)
                tetromino[3].move(-1,1)
                rotation = 1
            elif rotation == 1 and (tetromino[2].getP2().getX()+1,tetromino[2].getP2().getY()) in board:
                if (board[tetromino[2].getP2().getX()-1,tetromino[2].getP2().getY()] == False and
                    board[tetromino[2].getP2().getX()+1,tetromino[2].getP2().getY()] == False and
                    board[tetromino[2].getP2().getX()+1,tetromino[2].getP2().getY()-1] == False):
                    tetromino[0].move(2,0)
                    tetromino[1].move(1,1)
                    tetromino[3].move(-1,-1)
                    rotation = 2
            elif (rotation == 2 and board[tetromino[2].getP2().getX(),tetromino[2].getP2().getY()-1] == False and
                  board[tetromino[2].getP2().getX(),tetromino[2].getP2().getY()+1] == False and
                  board[tetromino[2].getP2().getX()+1,tetromino[2].getP2().getY()+1] == False):
                tetromino[0].move(0,2)
                tetromino[1].move(-1,1)
                tetromino[3].move(1,-1)
                rotation = 3
            elif rotation == 3 and (tetromino[2].getP2().getX()-1,tetromino[2].getP2().getY()) in board:
                if (board[tetromino[2].getP2().getX()+1,tetromino[2].getP2().getY()] == False and
                    board[tetromino[2].getP2().getX()-1,tetromino[2].getP2().getY()] == False and
                    board[tetromino[2].getP2().getX()-1,tetromino[2].getP2().getY()+1] == False):
                    tetromino[0].move(-2,0)
                    tetromino[1].move(-1,-1)
                    tetromino[3].move(1,1)
                    rotation = 0
        elif direction == "L":
            if (rotation == 0 and board[tetromino[2].getP2().getX(),tetromino[2].getP2().getY()-1] == False and
                board[tetromino[2].getP2().getX(),tetromino[2].getP2().getY()+1] == False and
                board[tetromino[2].getP2().getX()+1,tetromino[2].getP2().getY()+1] == False):
                tetromino[0].move(2,0)
                tetromino[1].move(1,1)
                tetromino[3].move(-1,-1)
                rotation = 3
            elif rotation == 3 and (tetromino[2].getP2().getX()-1,tetromino[2].getP2().getY()) in board:
                if (board[tetromino[2].getP2().getX()-1,tetromino[2].getP2().getY()] == False and
                    board[tetromino[2].getP2().getX()+1,tetromino[2].getP2().getY()] == False and
                    board[tetromino[2].getP2().getX()+1,tetromino[2].getP2().getY()-1] == False):
                    tetromino[0].move(0,-2)
                    tetromino[1].move(1,-1)
                    tetromino[3].move(-1,1)
                    rotation = 2
            elif (rotation == 2 and board[tetromino[2].getP2().getX(),tetromino[2].getP2().getY()+1] == False and
                  board[tetromino[2].getP2().getX(),tetromino[2].getP2().getY()-1] == False and
                  board[tetromino[2].getP2().getX()-1,tetromino[2].getP2().getY()-1] == False):
                tetromino[0].move(-2,0)
                tetromino[1].move(-1,-1)
                tetromino[3].move(1,1)
                rotation = 1
            elif rotation == 1 and (tetromino[2].getP2().getX()+1,tetromino[2].getP2().getY()) in board:
                if (board[tetromino[2].getP2().getX()+1,tetromino[2].getP2().getY()] == False and
                    board[tetromino[2].getP2().getX()-1,tetromino[2].getP2().getY()] == False and
                    board[tetromino[2].getP2().getX()-1,tetromino[2].getP2().getY()+1] == False):
                    tetromino[0].move(0,2)
                    tetromino[1].move(-1,1)
                    tetromino[3].move(1,-1)
                    rotation = 0
                
    elif piece_type == "S":
        if (rotation == 0 and board[tetromino[2].getP2().getX(),tetromino[2].getP2().getY()-1] == False and
            board[tetromino[2].getP2().getX()+1,tetromino[2].getP2().getY()+1] == False):
            tetromino[0].move(2,0)
            tetromino[1].move(1,-1)
            tetromino[3].move(-1,-1)
            rotation = 1
        elif (rotation == 1 and (tetromino[2].getP2().getX()-1,tetromino[2].getP2().getY()+1) in board and
              board[tetromino[2].getP2().getX()-1,tetromino[2].getP2().getY()+1] == False and
              board[tetromino[2].getP2().getX(),tetromino[2].getP2().getY()+1] == False):
            tetromino[0].move(-2,0)
            tetromino[1].move(-1,1)
            tetromino[3].move(1,1)
            rotation = 0
    
    elif piece_type == "Z":
        if (rotation == 0 and board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()] == False and
            board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()-1] == False):
            tetromino[0].move(1,1)
            tetromino[2].move(1,-1)
            tetromino[3].move(0,-2)
            rotation = 1
        elif (rotation == 1 and (tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()) in board and
              board[tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()] == False and
              board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()+1] == False):
            tetromino[0].move(-1,-1)
            tetromino[2].move(-1,1)
            tetromino[3].move(0,2)
            rotation = 0

    elif piece_type == "T":
        if direction == "R":
            if rotation == 0 and board[tetromino[1].getP2().getX(),tetromino[1].getP2().getY()+1] == False:
                tetromino[0].move(1,-1)
                tetromino[2].move(-1,-1)
                tetromino[3].move(-1,1)
                rotation = 1
            elif (rotation == 1 and (tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()) in board and
                  board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()] == False):
                tetromino[0].move(1,1)
                tetromino[2].move(1,-1)
                tetromino[3].move(-1,-1)
                rotation = 2
            elif rotation == 2 and board[tetromino[1].getP2().getX(),tetromino[1].getP2().getY()+1] == False:
                tetromino[0].move(-1,1)
                tetromino[2].move(1,1)
                tetromino[3].move(1,-1)
                rotation = 3
            elif (rotation == 3 and (tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()) in board and
                  board[tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()] == False):
                tetromino[0].move(-1,-1)
                tetromino[2].move(-1,1)
                tetromino[3].move(1,1)
                rotation = 0
        elif direction =="L": 
            if rotation == 0 and board[tetromino[1].getP2().getX(),tetromino[1].getP2().getY()-1] == False:
                tetromino[0].move(1,1)
                tetromino[2].move(1,-1)
                tetromino[3].move(-1,-1)
                rotation = 3
            elif (rotation == 3 and (tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()) in board and
                  board[tetromino[1].getP2().getX()-1,tetromino[1].getP2().getY()] == False):
                tetromino[0].move(1,-1)
                tetromino[2].move(-1,-1)
                tetromino[3].move(-1,1)
                rotation = 2
            elif rotation == 2 and board[tetromino[1].getP2().getX(),tetromino[1].getP2().getY()-1] == False:
                tetromino[0].move(-1,-1)
                tetromino[2].move(-1,1)
                tetromino[3].move(1,1)
                rotation = 1
            elif (rotation == 1 and (tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()) in board and
                  board[tetromino[1].getP2().getX()+1,tetromino[1].getP2().getY()] == False):
                tetromino[0].move(-1,1)
                tetromino[2].move(1,1)
                tetromino[3].move(1,-1)
                rotation = 0
    
    # the new current rotation is returned
    return rotation


def piece_place(tetromino, piece, board):
    """
    :param: tetromino - list of the blocks in the tetromino
            piece - string for the current piece type
            board - dictionary keeping track of the presence of pieces in each game tile
    :return: tetromino - returns either an empty list if the piece places or the list containing the blocks of the tetromino
    """
    
    for block in tetromino:
        
        # if one of the blocks in the tetromino is on the floor, the board state is updated and an empty list is returned
        if block.getP2().getY() == 23:
            for block in tetromino:
                board[block.getP2().getX(),block.getP2().getY()] = piece
            return []
        
        # if one of the blocks in the tetromino is directly above a filled square, the board state is updated and an empty list is returned
        elif board[block.getP2().getX(),block.getP2().getY()+1] != False:
            for block in tetromino:
                board[block.getP2().getX(),block.getP2().getY()] = piece
            return []
    
    # if the current tetromino is not in a position to be placed, it is returned
    return tetromino


def line_clear(score, grid, board, window):
    """
    a function to clear lines when the row is full
    :param: score - number of current line clears to be updated
            grid - dictionary for each tile of the game board, allowing for it to change color
            board - dictionary keeping track of whether the square of the game board is filled or not
            window - paramater allowing for the accessing of the game window
    :return: score - new number of line clears
    """
    # iterates through each row going downwards, so all subsequent lines are cleared
    for row in range(4,24):
        filled = 0
        for column in range(5,15):
            
            # if one of the columns is not filled, checking restarts on the next row down
            if board[column, row] == False:
                    break
            filled +=1
            
            # checks to see if all ten columns in a row are empty before clearing a line.
            if filled == 10:
                
                
                for row in range(row,4, -1): # iterates upward through the board.
                    for col in range (5,15): # iterates across for each tile in the column
                        
                        # changes the value of the tile to be equal to the block that is directly above it
                        board[col,row] = board[col,row-1]
                        
                        # sets the filled color of the game board tile to be coressponding to the correct color for the piece above it
                        if board[col,row] == False:
                            grid[col,row].setFill(color_rgb(255,255,255))
                            grid[col,row].undraw()
                            grid[col,row].draw(window)
                        if board[col,row] == "O":
                            grid[col,row].setFill(color_rgb(255,255,0))
                            grid[col,row].undraw()
                            grid[col,row].draw(window)
                        elif board[col,row] == "I":
                            grid[col,row].setFill(color_rgb(0,255,255))
                            grid[col,row].undraw()
                            grid[col,row].draw(window)
                        elif board[col,row] == "J":
                            grid[col,row].setFill(color_rgb(0,0,255))
                            grid[col,row].undraw()
                            grid[col,row].draw(window)
                        elif board[col,row] == "L":
                            grid[col,row].setFill(color_rgb(255,127,0))
                            grid[col,row].undraw()
                            grid[col,row].draw(window)
                        elif board[col,row] == "S":
                            grid[col,row].setFill(color_rgb(0,255,0))
                            grid[col,row].undraw()
                            grid[col,row].draw(window)
                        elif board[col,row] == "Z":
                            grid[col,row].setFill(color_rgb(255,0,0))
                            grid[col,row].undraw()
                            grid[col,row].draw(window)
                        elif board[col,row] == "T":
                            grid[col,row].setFill(color_rgb(128,0,128))
                            grid[col,row].undraw()
                            grid[col,row].draw(window)
                        else:
                            grid[col,row].setFill(color_rgb(255,255,255))
                            grid[col,row].undraw()
                            grid[col,row].draw(window)
                            board[col,row] = False
                
                # adds one to the score every time a line is full and cleared and returns it
                score +=1
    return score


def main():
    """
    Driver function for the tetris program
    """
    # creates the window and sets it to be evenly divided into squares
    win = GraphWin("Tetris", 468, 676, autoflush=False)
    win.setCoords(0, 26, 18, 0)
    
    speeds = [48,43,38,33,28,23,18,13,8,6,5,5,5,4,4,4,3,3,3,2,2,2,2,2,2,2,2,2] # list of possible fall speeds
    setting = False # ensures that the game doesn't start preemptively
    
    # while the window is open, the game runs and is able to be reset
    while win.isOpen():
        
        # fills the background of the screen each time the game starts, so it is consistent after a new game following a game over
        screen = Rectangle(Point(0,26),Point(18,0))
        screen.setFill(color_rgb(240,240,240))
        screen.draw(win)

        game_grid = dict()
        for col in range(5,15):
            for row in range(4,24):
                
                # fills the game with a board of empty square and places them in a dictionary with their coordinates as the key, so the color can be changed
                square = Rectangle(Point(col-1,row-1),Point(col,row))
                game_grid[col,row] = Rectangle(Point(col-1,row-1),Point(col,row))
                game_grid[col,row].setFill(color_rgb(256,256,256))
                game_grid[col,row].draw(win)

        board_state = dict() 
        for col in range(5,15):
            for row in range(0,24):
                
                # fills the board with false values, so each square is empty
                board_state[col,row] = False
                
        current_score = 0 # sets the starting number of line clears to zero
        
        #places an empty scoreboard
        scoreboard = Text(Point(16,22),("Score:", current_score))
        scoreboard.draw(win)
        bucket = [0] # creates the piece bucket containing one value for the first .pop
        
        # opens the controls menu and prompts the user to press enter to start
        setting = menu(win)
        
        # loop that runs as long as the player hasn't lost
        while setting != False:
            
            # checks the conditions for if the game is lost and changes setting to false if so
            setting = gameover(board_state, win) 
            if setting == False:
                break
            
            bucket = piece_bucket(bucket) # function call for making piece bucket
            current_piece = bucket[-1] # chooses the current piece from the last item in the bucket list
            tetracube = generate_piece(current_piece, win) # function call to make the tetracube list of each block component
            current_rotation = 0 # resets rotation
            
            # undraws, resets the score, and redraws it every time a piece is place
            scoreboard.undraw()
            scoreboard = Text(Point(16,22),("Score:", current_score))
            scoreboard.draw(win)
            
            # loop that runs while the current piece has not been placed on the ground, keeping it from being changed or reset
            while tetracube != []:
                for frame in range(1,61): # iterates through 60 frames per second
                    update(60)
                    
                    # function call that allows for moving of the piece, checking if the piece is on the ground yet after every movement
                    current_rotation = piece_control(current_rotation,tetracube,current_piece,board_state,win)
                    tetracube = piece_place(tetracube, current_piece, board_state)
                    
                    # if the piece was on the ground and placed, then the loop is exited and 
                    if tetracube == []:
                        break
                    
                    # when the score gets above 280, the speed is set to move the block down every frame.
                    if current_score>280:
                        for block in tetracube:
                            block.move(0,1)
                        tetracube = piece_place(tetracube, current_piece, board_state)
                        break
                    
                    # for every ten line clears, the speed increases to the next level in the speed list
                    # the block moves down when the frame is equal to the speed
                    elif frame == speeds[current_score//10]:
                        for block in tetracube:
                            block.move(0,1)
                        tetracube = piece_place(tetracube, current_piece, board_state)
                        break
                    
                # after a piece is placed, the conditions for a line clear are checked and the score is updated
                current_score = line_clear(current_score,game_grid,board_state,win)


main()