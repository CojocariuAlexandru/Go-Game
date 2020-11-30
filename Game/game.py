from graphics import *
from Scripts.Utility import utilityFunctions as util
import Scripts.Game.GameLogic.gameLogic as glog

def draw_game(window, turn):
    global score_white
    global score_black
    score_white = 0
    score_black = 0

    glog.reset_board()
    cell_dimension = 30
    util.reset_screen(window)
    for i in range(0, 18):
        for j in range(0, 18):
            cell = Rectangle(Point(50+i*cell_dimension, 50+j*cell_dimension), Point(50+(i+1)*cell_dimension, 50+(j+1)*cell_dimension))
            cell.setOutline('black')
            cell.draw(window)
    util.draw_image(window, "../Images/GoTable.png", 850, 600)
    util.draw_bordered_text(window, "Back to menu", 150, 650)
    util.draw_unbordered_text(window, "To move", 810, 150)
    util.draw_bordered_text(window, "Pass turn", 490, 650)
    util.draw_unbordered_text(window, "Score", 810, 300)
    util.draw_unbordered_text(window, "White", 685, 360)
    util.draw_unbordered_text(window, "Black", 935, 360)
    util.draw_small_bordered_text(window, str(score_white), 685, 420)
    util.draw_small_bordered_text(window, str(score_black), 935, 420)



def handle_mouse_click_game(window, turn):
    global count_passed
    global score_black
    global score_white
    cell_dimension = 30
    mouse_data = window.getMouse()
    if util.check_inside(mouse_data.x, mouse_data.y, 50, 630, 250, 670): # clicked on "back to menu"
        return (True, "Home")
    elif util.check_inside(mouse_data.x, mouse_data.y, 390, 630, 590, 670): # clicked on "pass turn"
        if count_passed != 1:
            count_passed = 1
        elif count_passed == 1:
            count_passed += 1
        if count_passed == 2:

            return (True, "Home")
        else:
            return (True, "PutPiece")
    else:
        count_passed = 0
        for i in range(0, 19):
            for j in range(0, 19):
                if util.check_inside(mouse_data.x, mouse_data.y, 50+i*cell_dimension-10, 50+j*cell_dimension-10, 50+i*cell_dimension+10, 50+j*cell_dimension+10):
                    piece = Circle(Point(50 + i * cell_dimension, 50 + j * cell_dimension), 10)
                    piece.setFill(turn)
                    piece.draw(window)
                    print(score_white, ' ', score_black)
                    perform_game_logic(window, j, i, turn)
                    print(score_white, ' ', score_black)
                    util.reset_part_screen(window, 685-29, 420-19, 685+29, 420+19)
                    util.reset_part_screen(window, 935-29, 420-19, 935+29, 420+19)
                    util.draw_small_bordered_text(window, str(score_white), 685, 420)
                    util.draw_small_bordered_text(window, str(score_black), 935, 420)
                    return (True, "PutPiece")
    return (True, "Game")

def perform_game_logic(window, i, j, turn):
    global score_white
    global score_black
    (score_white, score_black) = glog.add_piece(i, j, turn, score_white, score_black)
    (score_white, score_black) = glog.eliminate_surrounded_pieces(score_white, score_black)
    glog.mark_eliminated_pieces(window)