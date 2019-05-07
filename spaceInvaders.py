# Space Invaders game
import turtle
import os
import math

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

# Create Invaders
invader = turtle.Turtle("circle")
invader.color("red")
invader.penup()
invader.speed(0)
invader.setposition(-200, 250)

invaderSpeed = 2

# player bullet
bullet = turtle.Turtle("triangle")
bullet.color("yellow")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletSpeed = 20

# bullet states
# ready - ready to fire
# fire - bullet is fired and moving
bulletState = "ready"

# Move player left and right
def moveLeft():
    playerX = player.xcor()
    playerX -= playerSpeed
    # boundry check
    if playerX < -280:
        playerX = -280
    player.setx(playerX)

def moveRight():
    playerX = player.xcor()
    playerX += playerSpeed
    # boundry check
    if playerX > 280:
        playerX = 280
    player.setx(playerX)

def fireBullet():
    # bullet state is global if it needs to change
    global bulletState

    if bulletState == "ready":
        bulletState = "fire"
        # move bullet above player
        playerX = player.xcor()
        playerY = player.ycor() + 10
        bullet.setposition(playerX, playerY)
        bullet.showturtle()

# checking if bullet hit invader
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))

    if distance < 15:
        return True
    else:
        return False

# Keyboard Bindings
turtle.listen()
# player movement
turtle.onkey(moveLeft, "Left")
turtle.onkey(moveRight, "Right")
# bullet shooter
turtle.onkey(fireBullet, "space")

# Game loop
while True:
    # move invader
    invaderX = invader.xcor()
    invaderX += invaderSpeed
    invader.setx(invaderX)

    # move invader down (boundry check)
    if invader.xcor() > 280:
        invaderY = invader.ycor()
        invaderY -= 40
        invaderSpeed *= -1
        invader.sety(invaderY)

    if invader.xcor() < -280:
        invaderY = invader.ycor()
        invaderY -= 40
        invaderSpeed *= -1
        invader.sety(invaderY)

    # move bullet
    if bulletState == "fire":
        bulletY = bullet.ycor()
        bulletY += bulletSpeed
        bullet.sety(bulletY)
    # bullet boundries
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletState = "ready"

    # check for collision btwn invader and bullet
    if isCollision(bullet, invader):
        # reset bullet
        bullet.hideturtle()
        bulletState = "ready"
        bullet.setposition(0, -400)
        # reset invader
        invader.setposition(-200, 250)

    # check for collision btwn invader and player
    if isCollision(player, invader):
        player.hideturtle()
        invader.hideturtle()
        print("Game Over")
        break


# Exit window
window.exitonclick()
