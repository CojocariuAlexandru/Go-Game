from graphics import *

def adjust_window(length, width):
    global window
    window = GraphWin("Go Game", length, width)

def start_game():
    global window
    game_run_flag = True
    game_state = "Home"

    while game_run_flag == True:
        if game_state == "Home":
            game_drawn_flag = False
            draw_home()
            (game_run_flag, game_state) = handle_mouse_click_home()
        elif game_state == "Game":
            if game_drawn_flag == False:
                turn = 'black'
                draw_game(turn)
                game_drawn_flag = True

            piece = Circle(Point(810, 200), 20)
            piece.setFill(turn)
            piece.draw(window)
            (game_run_flag, game_state) = handle_mouse_click_game(turn)

            if game_state == 'PutPiece':
                game_state = 'Game'
                if turn == 'white':
                    turn = 'black'
                else:
                    turn = 'white'

    window.close()

def handle_mouse_click_home():
    global window
    mouse_data = window.getMouse()
    if check_inside(mouse_data.x, mouse_data.y, 400, 180, 600, 220):
        return (True, "Game")
    elif check_inside(mouse_data.x, mouse_data.y, 400, 260, 600, 300):
        return (False, 'Home')
    return (True, "Home")

def handle_mouse_click_game(turn):
    global window
    cell_dimension = 30
    mouse_data = window.getMouse()
    if check_inside(mouse_data.x, mouse_data.y, 50, 630, 250, 670): # clicked on "back to menu"
        return (True, "Home")
    else:
        for i in range(0, 19):
            for j in range(0, 19):
                if check_inside(mouse_data.x, mouse_data.y, 50+i*cell_dimension-10, 50+j*cell_dimension-10, 50+i*cell_dimension+10, 50+j*cell_dimension+10):
                    piece = Circle(Point(50 + i * cell_dimension, 50 + j * cell_dimension), 10)
                    piece.setFill(turn)
                    piece.draw(window)
                    return (True, "PutPiece")
    return (True, "Game")

def check_inside(x_click, y_click, x_box, y_box, x_box2, y_box2):
    if x_click >= x_box and x_click <= x_box2:
        if y_click >= y_box and y_click <= y_box2:
            return True
    return False

def draw_game(turn):
    global window
    cell_dimension = 30
    reset_screen()
    for i in range(0, 18):
        for j in range(0, 18):
            cell = Rectangle(Point(50+i*cell_dimension, 50+j*cell_dimension), Point(50+(i+1)*cell_dimension, 50+(j+1)*cell_dimension))
            cell.setOutline('black')
            cell.draw(window)
    draw_image("../Images/GoTable.png", 850, 600)
    draw_bordered_text("Back to menu", 150, 650)
    draw_unbordered_text("To move", 810, 150)

def reset_screen():
    global window
    reset_green = Rectangle(Point(0, 0), Point(1000, 700))
    reset_green.setFill(color_rgb(0, 100, 0))
    reset_green.draw(window)

def draw_home():
    global window
    reset_screen()
    draw_unbordered_text("Go Game", 500, 60)
    draw_bordered_text("Play", 500, 200)
    draw_bordered_text("Quit", 500, 280)
    draw_image("../Images/GoTable.png", 850, 600)

def draw_unbordered_text(title, x, y):
    global window
    text_box = Text(Point(x, y), title)
    text_box.setTextColor('white')
    text_box.setSize(35)
    text_box.setFace('helvetica')
    text_box.draw(window)

def draw_bordered_text(title, x, y):
    global window
    text_border = Rectangle(Point(x-100, y-20), Point(x+100, y+20))
    text_border.setOutline('white')
    text_border.draw(window)

    text_box = Text(Point(x, y), title)
    text_box.setTextColor('white')
    text_box.setSize(20)
    text_box.setFace('helvetica')
    text_box.draw(window)

def draw_image(path, x, y):
    global window
    image = Image(Point(x, y), path)
    image.draw(window)

adjust_window(1000, 700)
start_game()