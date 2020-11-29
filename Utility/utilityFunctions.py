from graphics import *

def draw_unbordered_text(window, title, x, y):
    text_box = Text(Point(x, y), title)
    text_box.setTextColor('white')
    text_box.setSize(35)
    text_box.setFace('helvetica')
    text_box.draw(window)

def draw_bordered_text(window, title, x, y):
    text_border = Rectangle(Point(x-100, y-20), Point(x+100, y+20))
    text_border.setOutline('white')
    text_border.draw(window)

    text_box = Text(Point(x, y), title)
    text_box.setTextColor('white')
    text_box.setSize(20)
    text_box.setFace('helvetica')
    text_box.draw(window)

def reset_screen(window):
    reset_green = Rectangle(Point(0, 0), Point(1000, 700))
    reset_green.setFill(color_rgb(0, 100, 0))
    reset_green.draw(window)

def draw_image(window, path, x, y):
    image = Image(Point(x, y), path)
    image.draw(window)

def check_inside(x_click, y_click, x_box, y_box, x_box2, y_box2):
    if x_click >= x_box and x_click <= x_box2:
        if y_click >= y_box and y_click <= y_box2:
            return True
    return False