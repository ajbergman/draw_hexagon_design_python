# draw a hexagon design with turtle
# Written by Alex Bergman




import turtle
import math
import time

def get_color_choice(choice):
    color_choice = input("Please enter your "+choice+" choice: ")
    while color_choice != 'red' and color_choice != 'blue'\
          and color_choice != 'green' and color_choice != 'yellow'\
          and color_choice != 'purple':
        print(color_choice,"is not a legal choice. ", end='')
        color_choice = input("Please enter your choice: ")
    return color_choice

def get_num_hexagons():
    num_hexagons = int(input("Please enter a number of hexagons per row: "))
    while num_hexagons < 4 or num_hexagons > 20:
        print("It should be between 4 and 20. ", end='')
        num_hexagons = int(input("Please try again: "))
    return num_hexagons

def draw_hexagon(x, y, side_len, pen, color):
    turtle.speed(10)
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(30)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(side_len)
    turtle.seth(90)
    turtle.forward(side_len)
    turtle.seth(150)
    turtle.forward(side_len)
    turtle.seth(210)
    turtle.forward(side_len)
    turtle.seth(270)
    turtle.forward(side_len)
    turtle.seth(330)
    turtle.forward(side_len)
    turtle.end_fill()
    turtle.up()
    
    turtle.goto(x,y)
    turtle.seth(30)
    turtle.color('black')
    turtle.down()
    turtle.forward(side_len)
    turtle.seth(90)
    turtle.forward(side_len)
    turtle.seth(150)
    turtle.forward(side_len)
    turtle.seth(210)
    turtle.forward(side_len)
    turtle.seth(270)
    turtle.forward(side_len)
    turtle.seth(330)
    turtle.forward(side_len)
    turtle.up
    return
        
print("Choices for colors to use are:\n  red\n  blue\n  green\n  yellow\n  purple\n")
first_color = get_color_choice("first")
second_color = get_color_choice("second")
num_hexagons = get_num_hexagons()



d = 500/num_hexagons
d_div = d / 2
side_length = d_div/(math.cos(math.pi/6))
x = -250 + d_div
y = -250
draw_hexagon(x,y,side_length,turtle,first_color)
draw_hexagon(x+d,y,side_length,turtle,second_color)

cnt_x = 2
cnt_y = 0
next_x = x + (2*d)
next_y = y
while cnt_y < num_hexagons:
    while cnt_x < num_hexagons:
        draw_hexagon(next_x,next_y,side_length,turtle,first_color)
        cnt_x += 1
        while cnt_x < num_hexagons:
            draw_hexagon(next_x + d,next_y,side_length,turtle,second_color)
            cnt_x += 1
            break
        next_x = next_x + (2*d)
    if cnt_y % 2 == 0:
        next_x = -250 + (2*d_div)
        color_1 = first_color
        first_color = second_color
        second_color = color_1
    else:
        next_x = x
    next_y = next_y + side_length + d_div*(math.sin(math.pi/6))
    cnt_y = cnt_y + 1
    cnt_x = 0
    color_1 = first_color
    first_color = second_color
    second_color = color_1
    

time.sleep(5)
turtle.bye()
