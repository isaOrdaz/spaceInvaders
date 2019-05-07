# Space Invaders game
import turtle
import os

# Screen set up
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")

# Screen border
borderPen = turtle.Turtle()
borderPen.speed(0)
borderPen.color("white")
borderPen.penup()
borderPen.setposition(-300, -300)
borderPen.pendown()
borderPen.pensize(3)
# loop draws border
for side in range(4):
    borderPen.fd(600)
    borderPen.left(90)

borderPen.hideturtle()

# Create player
player = turtle.Turtle("triangle")
player.color("blue")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerSpeed = 15

# Move player left and right
def moveLeft():
    newX = player.xcor() - playerSpeed
    player.setx()

def moveRight():
    player.setx(player.xcor() + playerSpeed)

# Keyboard Bindings
turtle.listen()
turtle.onkey(moveLeft, "Left")
turtle.onkey(moveRight, "Right")


# Exit window
window.exitonclick()
