import turtle
max_length = 250
increment = 10


def draw_spiral(a_turtle, line_length):
    if line_length > max_length:
        return
    a_turtle.forward(line_length)
    a_turtle.right(90)
    draw_spiral(a_turtle, line_length + increment)


charlie = turtle.Turtle(shape="turtle")
charlie.pensize(5)
charlie.color("red")
draw_spiral(charlie, 10)
turtle.done
