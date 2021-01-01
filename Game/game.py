from graphics import *
from Scripts.Utility import utilityFunctions as util
import Scripts.Game.GameLogic.gameLogic as glog
import random


class GameManager:
    """Defines constants for buttons, text, pieces, etc."""
    def __init__(self):
        self.playerType = 'computer'
        self.countPassed = 0
        self.CELL_PIXEL_DIMENSION = 30
        self.OFFSET_BOARD = 50
        self.IMAGE_X = 850
        self.IMAGE_Y = 600
        self.BACK_TO_MENU_X = 150
        self.BACK_TO_MENU_Y = 650
        self.TO_MOVE_X = 810
        self.TO_MOVE_Y = 150
        self.PASS_X = 490
        self.PASS_Y = 650
        self.SCORE_X = 810
        self.SCORE_Y = 300
        self.WHITE_X = 685
        self.WHITE_Y = 360
        self.BLACK_X = 935
        self.BLACK_Y = 360
        self.SCORE_WHITE_X = 685
        self.SCORE_WHITE_Y = 420
        self.SCORE_BLACK_X = 935
        self.SCORE_BLACK_Y = 420
        self.OFFSET_X = 100
        self.OFFSET_Y = 20
        self.PIECE_RADIUS = 10
        self.SCOREBOARD_OFFSET_X = 29
        self.SCOREBOARD_OFFSET_Y = 19
        self.SCORE_WHITE_X1 = self.SCORE_WHITE_X - self.SCOREBOARD_OFFSET_X
        self.SCORE_WHITE_Y1 = self.SCORE_WHITE_Y - self.SCOREBOARD_OFFSET_Y
        self.SCORE_WHITE_X2 = self.SCORE_WHITE_X + self.SCOREBOARD_OFFSET_X
        self.SCORE_WHITE_Y2 = self.SCORE_WHITE_Y + self.SCOREBOARD_OFFSET_Y
        self.SCORE_BLACK_X1 = self.SCORE_BLACK_X - self.SCOREBOARD_OFFSET_X
        self.SCORE_BLACK_Y1 = self.SCORE_BLACK_Y - self.SCOREBOARD_OFFSET_Y
        self.SCORE_BLACK_X2 = self.SCORE_BLACK_X + self.SCOREBOARD_OFFSET_X
        self.SCORE_BLACK_Y2 = self.SCORE_BLACK_Y + self.SCOREBOARD_OFFSET_Y

    """Draws the playing grid and buttons on the screen"""
    def draw_game(self, window, turn):
        self.score_white = 0
        self.score_black = 0

        glog.reset_board()
        util.reset_screen(window)
        for i in range(0, 18):
            for j in range(0, 18):
                cell_x1 = self.OFFSET_BOARD + i*self.CELL_PIXEL_DIMENSION
                cell_y1 = self.OFFSET_BOARD + j*self.CELL_PIXEL_DIMENSION
                cell_x2 = self.OFFSET_BOARD + (i+1)*self.CELL_PIXEL_DIMENSION
                cell_y2 = self.OFFSET_BOARD + (j+1)*self.CELL_PIXEL_DIMENSION
                cell = Rectangle(Point(cell_x1, cell_y1),
                                 Point(cell_x2, cell_y2))
                cell.setOutline('black')
                cell.draw(window)
        util.draw_image(window, "../Images/GoTable.png", self.IMAGE_X, self.IMAGE_Y)
        util.draw_bordered_text(window, "Back to menu", self.BACK_TO_MENU_X, self.BACK_TO_MENU_Y)
        util.draw_unbordered_text(window, "To move", self.TO_MOVE_X, self.TO_MOVE_Y)
        util.draw_bordered_text(window, "Pass turn", self.PASS_X, self.PASS_Y)
        util.draw_unbordered_text(window, "Score", self.SCORE_X, self.SCORE_Y)
        util.draw_unbordered_text(window, "White", self.WHITE_X, self.WHITE_Y)
        util.draw_unbordered_text(window, "Black", self.BLACK_X, self.BLACK_Y)
        util.draw_small_bordered_text(window, str(self.score_white),
                                      self.SCORE_WHITE_X, self.SCORE_WHITE_Y)
        util.draw_small_bordered_text(window, str(self.score_black),
                                      self.SCORE_BLACK_X, self.SCORE_BLACK_Y)

    """Handles mouse clicks"""
    def handle_mouse_click_game(self, window, turn):
        cell_dimension = 30
        valid_move_flag = False
        while valid_move_flag is False:
            mouse_data = window.getMouse()
            if util.check_inside(mouse_data.x, mouse_data.y,
                                 self.BACK_TO_MENU_X - self.OFFSET_X,
                                 self.BACK_TO_MENU_Y - self.OFFSET_Y,
                                 self.BACK_TO_MENU_X + self.OFFSET_X,
                                 self.BACK_TO_MENU_Y + self.OFFSET_Y):
                return (True, "Home")
            elif util.check_inside(mouse_data.x, mouse_data.y,
                                   self.PASS_X - self.OFFSET_X,
                                   self.PASS_Y - self.OFFSET_Y,
                                   self.PASS_X + self.OFFSET_X,
                                   self.PASS_Y + self.OFFSET_Y):
                return self.handle_pressed_on_passed()
            else:
                for i in range(0, 19):
                    for j in range(0, 19):
                        if self.check_inside_piece_spot(i, j, mouse_data.x, mouse_data.y) is True:
                            return self.handle_placed_a_piece(i, j, turn, window)
        return (True, "Game")

    """For computer its strategy is to make random moves"""
    def make_random_move(self, window):
        self.countPassed = 0
        valid_move_flag = False
        while valid_move_flag is False:
            random_move = random.randint(0, 19*19-1)
            line = random_move % 19
            col = random_move // 19
            if glog.check_valid_position(col, line) is True:
                valid_move_flag = True
                cell_x = self.OFFSET_BOARD + line * self.CELL_PIXEL_DIMENSION
                cell_y = self.OFFSET_BOARD + col * self.CELL_PIXEL_DIMENSION
                piece = Circle(Point(cell_x, cell_y), 10)
                piece.setFill('white')
                piece.draw(window)
                self.perform_game_logic(window, col, line, 'white')

                self.reset_scores_on_screen(window)
                return (True, "Game")

    """Handles case if user presses on 'pass turn' button"""
    def handle_pressed_on_passed(self):
        if self.countPassed != 1:
            self.countPassed = 1
        elif self.countPassed == 1:
            self.countPassed += 1
        if self.countPassed == 2:
            return (True, "Home")
        else:
            return (True, "PutPiece")

    """Handles case if user presses on place in the board"""
    def handle_placed_a_piece(self, i, j, turn, window):
        if glog.check_valid_position(j, i) is True:
            self.countPassed = 0
            piece_x = self.OFFSET_BOARD + i * self.CELL_PIXEL_DIMENSION
            piece_y = self.OFFSET_BOARD + j * self.CELL_PIXEL_DIMENSION
            piece = Circle(Point(piece_x, piece_y), self.PIECE_RADIUS)

            piece.setFill(turn)
            piece.draw(window)

            self.perform_game_logic(window, j, i, turn)
            self.reset_scores_on_screen(window)

            return (True, "PutPiece")
        else:
            valid_move_flag = False

    """Checks if the player pressed on an intersection of lines in the playing grid"""
    def check_inside_piece_spot(self, i, j, mouse_x, mouse_y):
        return util.check_inside\
            (
                mouse_x, mouse_y,
                self.OFFSET_BOARD + i * self.CELL_PIXEL_DIMENSION - 10,
                self.OFFSET_BOARD + j * self.CELL_PIXEL_DIMENSION - 10,
                self.OFFSET_BOARD + i * self.CELL_PIXEL_DIMENSION + 10,
                self.OFFSET_BOARD + j * self.CELL_PIXEL_DIMENSION + 10
            )

    """Redraws the scores on the screen after a piece is placed"""
    def reset_scores_on_screen(self, window):
        util.reset_part_screen(window,
                               self.SCORE_WHITE_X1, self.SCORE_WHITE_Y1,
                               self.SCORE_WHITE_X2, self.SCORE_WHITE_Y2)

        util.reset_part_screen(window,
                               self.SCORE_BLACK_X1, self.SCORE_BLACK_Y1,
                               self.SCORE_BLACK_X2, self.SCORE_BLACK_Y2)

        util.draw_small_bordered_text(window, str(self.score_white),
                                      self.SCORE_WHITE_X, self.SCORE_WHITE_Y)
        util.draw_small_bordered_text(window, str(self.score_black),
                                      self.SCORE_BLACK_X, self.SCORE_BLACK_Y)

    """Call gameLogic.py modules which handles the logic of the board"""
    def perform_game_logic(self, window, i, j, turn):
        (self.score_white, self.score_black) = glog.add_piece(i, j, turn, self.score_white, self.score_black)
        (self.score_white, self.score_black) = glog.eliminate_surrounded_pieces(self.score_white, self.score_black)
        glog.mark_eliminated_pieces(window)

    def set_player_type(self, player_type):
        self.playerType = player_type
        if self.playerType != 'computer' and self.playerType != 'player':
            self.playerType = 'computer'

    def get_player_type(self):
        return self.playerType
