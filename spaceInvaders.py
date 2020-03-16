# Space Invaders game
# last commit was today
import turtle
import os
import math
import random

# Screen set up
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.bgpic('/Users/isabel/PycharmProjects/spaceInvaders/space_invader.gif')
# window.bgpic('spaceInvaders-master\space_invader.gif')

# register shapes
turtle.register_shape("/Users/isabel/PycharmProjects/spaceInvaders/invader.gif")
# turtle.register_shape('spaceInvaders-master\invader.gif')
turtle.register_shape("/Users/isabel/PycharmProjects/spaceInvaders/player.gif")
# turtle.register_shape('spaceInvaders-master\player.gif')

# Screen border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

# loop draws border
for side in range(4):
    border_pen.fd(600)
    border_pen.left(90)

# border_pen.hideturtle()

# game Over
game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.color("white")
game_over_pen.penup()
game_over_string = "Game Over"
won_game_string = "You Won!"
game_over_pen.hideturtle()

# Scoring
score = 0
ADDED_POINTS = 10 # default score when hit invader

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
score_string = "Score: %s" % score
score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create player
player = turtle.Turtle("/Users/isabel/PycharmProjects/spaceInvaders/player.gif")
# player = turtle.Turtle('spaceInvaders-master\player.gif')
player.color("blue")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15

# Create Invaders
number_of_invaders = random.randint(5, 10)  # random ints
# create empty list of invaders
invaders = []  # lists

# add invaders to list
for i in range(number_of_invaders):  # for loops
    # create invader
    invaders.append(turtle.Turtle("/Users/isabel/PycharmProjects/spaceInvaders/invader.gif"))
    # invaders.append(turtle.Turtle('spaceInvaders-master\invader.gif'))

number_of_invaders = len(invaders)

for invader in invaders:
    invader.color("red")
    invader.penup()
    invader.speed(0)
    invaderX = random.randint(-200, 200)
    invaderY = random.randint(100, 250)
    invader.setposition(invaderX, invaderY)

invader_speed = 2

# player bullet
bullet = turtle.Turtle("triangle")
bullet.color("yellow")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 20

# bullet states
# ready - ready to fire
# fire - bullet is fired and moving
bullet_state = "ready"


# Move player left and right
def move_left():  # functions
    player_x = player.xcor()
    player_x -= player_speed
    # boundary check
    if player_x < -280:
        player_x = -280
    player.setx(player_x)


def move_right():  # functions
    player_x = player.xcor()
    player_x += player_speed
    # boundary check
    if player_x > 280:
        player_x = 280
    player.setx(player_x)


def fire_bullet():  # functions
    # bullet state is global if it needs to change
    global bullet_state

    if bullet_state == "ready":  # if else statements
        os.system("afplay /Users/isabel/PycharmProjects/spaceInvaders/laser.wav&")
        bullet_state = "fire"
        # move bullet above player
        player_x = player.xcor()
        player_y = player.ycor() + 10
        bullet.setposition(player_x, player_y)
        bullet.showturtle()


# checking if bullet hit invader
def is_collision(t1, t2):  # function
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))

    if distance < 15:
        return True
    else:
        return False


def end_game():
    if number_of_invaders == 0:
        return True


# Keyboard Bindings
turtle.listen()
# player movement
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
# bullet shooter
turtle.onkey(fire_bullet, "space")

# Game loop
while True:  # whiles loops
    for invader in invaders:  # for loops
        # move invader
        invader_x = invader.xcor()
        invader_x += invader_speed
        invader.setx(invader_x)

        # move invader down (boundry check)
        if invader.xcor() > 280:  # if else statements
            for i in invaders:  # for loops
                # move them down
                invader_y = i.ycor()
                invader_y -= 40
                i.sety(invader_y)
            # change direction
            invader_speed *= -1

        if invader.xcor() < -280:  # if else statements
            for i in invaders:  # for loops
                # move them down
                invader_y = i.ycor()
                invader_y -= 40
                i.sety(invader_y)
            # change direction
            invader_speed *= -1

        # check for collision btwn invader and bullet
        if is_collision(bullet, invader):  # if else statements
            os.system("afplay /Users/isabel/PycharmProjects/spaceInvaders/explosion.wav&")
            # reset bullet
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)

            # update invaders list
            if number_of_invaders != 0:  # if else statements
                # Delete enemy and update number
                invaders.remove(invader)
                invader.hideturtle()
                number_of_invaders -= 1

            # update score
            score += ADDED_POINTS
            score_string = "Score: %s" % score
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
            game_over_pen.clear()

        # check for collision btwn invader and player
        if is_collision(player, invader):  # if else statements
            os.system("afplay /Users/isabel/PycharmProjects/spaceInvaders/explosion.wav&")
            player.hideturtle()
            invader.hideturtle()
            game_over_pen.write(game_over_string, False, align="center", font=("Arial", 14, "normal"))
            break

        if end_game():
            game_over_pen.write(won_game_string, False, align="center", font=("Ariel", 14, "normal"))
            turtle.done()
            break

    # move bullet
    if bullet_state == "fire":  # if else statements
        bullet_y = bullet.ycor()
        bullet_y += bullet_speed
        bullet.sety(bullet_y)
    # bullet boundaries
    if bullet.ycor() > 275:  # if else statements
        bullet.hideturtle()
        bullet_state = "ready"

# Exit window
window.exitonclick()

# go out one border come out the other
# go up and down
# miss invader comes back from the top