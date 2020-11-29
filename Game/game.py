from graphics import *
from Scripts.Utility import utilityFunctions as util
import Scripts.Game.GameLogic.gameLogic as glog

def draw_game(window, turn):
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


def handle_mouse_click_game(window, turn):
    cell_dimension = 30
    mouse_data = window.getMouse()
    if util.check_inside(mouse_data.x, mouse_data.y, 50, 630, 250, 670): # clicked on "back to menu"
        return (True, "Home")
    else:
        for i in range(0, 19):
            for j in range(0, 19):
                if util.check_inside(mouse_data.x, mouse_data.y, 50+i*cell_dimension-10, 50+j*cell_dimension-10, 50+i*cell_dimension+10, 50+j*cell_dimension+10):
                    piece = Circle(Point(50 + i * cell_dimension, 50 + j * cell_dimension), 10)
                    piece.setFill(turn)
                    piece.draw(window)
                    perform_game_logic(window, j, i, turn)
                    return (True, "PutPiece")
    return (True, "Game")

def perform_game_logic(window, i, j, turn):
    glog.add_piece(i, j, turn)
    glog.eliminate_surrounded_pieces()
    glog.mark_eliminated_pieces(window)