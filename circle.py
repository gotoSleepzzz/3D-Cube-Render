from turtle import *
from math import pi, cos, sin
from random import randint, uniform

width = 300


def Map(val, in_min, in_max, out_min, out_max):
    return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def setup():
    Screen().bgcolor('black')
    Screen().title('Draw Moon!')
    colormode(255)

    turtle = Turtle()
    turtle.pensize(3)
    turtle.speed(0)
    turtle.hideturtle()

    turtle.penup()
    turtle.goto(0, -300)
    turtle.pendown()
    turtle.pencolor(255, 255, 255)
    turtle.circle(width)
    turtle.pensize(1)
    turtle.pencolor(175, 175, 175)

    return turtle


def draw(turtle):
    diff = 2*pi/10
    i = 0
    while(i < 100000):
        rad1 = Map(randint(0, 9), 0, 9, 0, 2*pi) + uniform(-diff, diff)
        rad2 = Map(randint(0, 9), 0, 9, 0, 2*pi) + uniform(-diff, diff)
        i += 1

        x1 = width * cos(rad1)
        y1 = width * sin(rad1)

        x2 = width * cos(rad2)
        y2 = width * sin(rad2)

        try:
            turtle.penup()
            turtle.goto((x1, y1))

            # r = randint(1, 255)
            # g = randint(1, 255)
            # b = randint(1, 255)
            # turtle.pencolor(r, g, b)

            turtle.pendown()
            turtle.goto(x2, y2)
        except Exception as e:
            print(e)
            Screen().bye()
            break
    pass


def main():
    turtle = setup()
    draw(turtle)
    pass


if __name__ == "__main__":
    main()
