import turtle
import random

my_screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_screen.colormode(255)
screen_size_multiplier =0.97
screen_width,screen_height=my_screen.screensize()
my_screen.bgcolor("pink")

free = random.randint(0,100)

def draw_head_and_body(scale):
    my_turtle.pd()
    my_turtle.circle(scale*5)
    my_turtle.right(90)
    my_turtle.fd(scale*8)
    my_turtle.left(90)
    my_turtle.pu()

def draw_hat(scale):
    my_turtle.pd()
    my_turtle.fd(scale*5)
    my_turtle.left(90)
    my_turtle.circle(scale*5,extent=-180)
    my_turtle.right(90)
    my_turtle.fd(scale*3)
    my_turtle.left(180)
    my_turtle.fd(scale*17)
    my_turtle.pu()
    
def draw_arms(scale):
    free = random.uniform(20, 160)
    my_turtle.pd()
    my_turtle.setheading(270)
    my_turtle.left(free)
    my_turtle.fd(scale*8)
    my_turtle.left(180)
    my_turtle.fd(scale*8)
    my_turtle.setheading(270)
    my_turtle.right(free)
    my_turtle.fd(scale*8)
    my_turtle.left(180)
    my_turtle.fd(scale*8)
    my_turtle.setheading(270)
    my_turtle.pu()

def draw_body(scale):
    my_turtle.pd()
    my_turtle.fd(free)
    my_turtle.pu()

def draw_legs(scale):
    my_turtle.pd()
    my_turtle.fd(scale*9)
    my_turtle.right(180)
    my_turtle.fd(scale*9)
    my_turtle.right(90)
    my_turtle.fd(scale*9)
    my_turtle.right(180)
    my_turtle.pu()
    my_turtle.fd(scale*9)
    my_turtle.setheading(90)
    my_turtle.fd(free)
    my_turtle.fd(scale*8)
    my_turtle.right(90)
    my_turtle.circle(scale*5,extent=-180)

def make_human(red,green,blue,scale):
    my_turtle.pd()
    my_turtle.fillcolor(red,green,blue)
    draw_head_and_body(scale)
    draw_arms(scale)
    draw_body(scale)
    my_turtle.right(45)
    draw_legs(scale)
    my_turtle.begin_fill()
    draw_hat(scale)
    my_turtle.end_fill()
    my_turtle.pu()
    my_turtle.setposition(0,0)
    my_turtle.setheading(0)
    
    
def random_human():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    scale = random.randint(1,10)
    my_turtle.pu()
    x_position = random.randint(int(-1*screen_size_multiplier*screen_width),\
                                int(screen_size_multiplier*screen_width))
    y_position = random.randint(int(-1*screen_size_multiplier*screen_height),\
                                int(screen_size_multiplier*screen_height))
    my_turtle.setposition(x_position,y_position)
    make_human(red,green,blue,scale)


def lots_of_random_people():
    my_turtle.speed(10)
    for num in range(random.randint(1,20)):
        random_human()
