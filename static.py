

"""Game Configuration - Menu"""
# game modes
PLAY_AGAINST_FRIEND = "Play Against Friend"
PLAY_AGAINST_PC = "Play Against Computer"

BOARD_MODE_REGULAR = "Regular Board"
BOARD_MODE_EATEN = "Eaten Board"

# board size
MIN_ROW_NUM = 1
MAX_ROW_NUM = 15
MIN_COL_NUM = 1
MAX_COL_NUM = 15

# labels
MENU_TITLE = "Menu - Chomp Game"
HEAD_TITLE = "Welcome to Chomp Game!"
INPUT_NOT_VALID_MSG = "Please note- \nRows should be numbers between {}-{}, and columns should be numbers between {}-{}."
INPUT_NOT_VALID_TITLE = "Input Requirements"
BOARD_MODE_TITLE = "Choose Board Mode- "
PLAY_AGAINST_TITLE = "Choose Your Opponent- "
BOARD_SIZE_TITLE = "Choose Board Size- "
START_BUTTON = "Start Game!"

"""Display Configuration - GameObject and Cell"""
# cell colors
LIVE = '#9f8170'
DEAD = '#f0f8ff'
POISON = 'IndianRed1'
CHOSEN = '#00cdcd'

# cell size
CELL_SIZE = 75
SMALL_CELL_SIZE = 35

# event triggers
LEFT_MOUSE_BUTTON = "<Button-1>"
LEFT_MOUSE_BUTTON_RELEASE = "<ButtonRelease-1>"

# labels
INSTRUCTIONS_TITLE = "Instructions"
INSTRUCTIONS = "Chomp is a two-player strategy game, played on a rectangular board that made up of cells. \n" \
               "The players take it in turns to choose cell, than removing it along with the cells above it, and to " \
               "its right. \nBut be careful- The lower left cell is poisoned, so whoever touched it- loses the " \
               "game. \n\nGood Luck!"
GAME_TITLE = "Chomp Game"
GAME_OVER_MSG = "The Winner is Player {}! \nPlayer {} Lost :("
GAME_OVER_TITLE = "Game Over"
TURN_LABEL = "Turn: Player {}"