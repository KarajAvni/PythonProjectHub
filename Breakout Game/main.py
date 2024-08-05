import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Bricks
bricks = []

def create_bricks():
    for i in range(-200, 250, 50):
        for j in range(150, 250, 50):
            brick = turtle.Turtle()
            brick.shape("square")
            brick.color("blue")
            brick.shapesize(stretch_wid=1, stretch_len=2)
            brick.penup()
            brick.goto(i, j)
            bricks.append(brick)

# Functions
def paddle_right():
    x = paddle.xcor()
    x += 30
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 30
    paddle.setx(x)

# Keyboard bindings
screen.listen()
screen.onkey(paddle_right, "Right")
screen.onkey(paddle_left, "Left")

# Create bricks
create_bricks()

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    # Paddle and ball collisions
    if (
        (ball.ycor() < -240 and ball.ycor() > -250)
        and (ball.xcor() > paddle.xcor() - 50)
        and (ball.xcor() < paddle.xcor() + 50)
    ):
        ball.sety(-240)
        ball.dy *= -1

    # Brick collisions
    for brick in bricks:
        if (
            (ball.ycor() > brick.ycor() - 25)
            and (ball.ycor() < brick.ycor() + 25)
            and (ball.xcor() > brick.xcor() - 25)
            and (ball.xcor() < brick.xcor() + 25)
        ):
            brick.hideturtle()
            bricks.remove(brick)
            ball.dy *= -1

    time.sleep(0.01)
