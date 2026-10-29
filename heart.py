import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("I Love You Heart")

t = turtle.Turtle()
t.color("hot pink")
t.fillcolor("red")
t.speed(3)

def draw_heart():
    t.begin_fill()
    t.left(140)
    t.forward(113)

    for _ in range(200):
        t.right(1)
        t.forward(1)

    t.left(120)

    for _ in range(200):
        t.right(1)
        t.forward(1)

    t.forward(113)
    t.end_fill()

draw_heart()

t.penup()
t.goto(0, 0)
t.pendown()
t.color("white")

t.write(
    "I Love You",
    align="center",
    font=("Arial", 24, "bold")
)

t.hideturtle()
turtle.done()
