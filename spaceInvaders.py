# # Space Invaders
# import math
# import os
# import random
# import turtle
#
# # Set up the screen
# mainScreen = turtle.Screen()
# mainScreen.bgcolor("black")
# mainScreen.title("Space Invaders")
# mainScreen.bgpic("space_invader.png")
#
# # Register the shapes
# turtle.register_shape("invader.gif")
# turtle.register_shape("player.gif")
#
# # Draw border
# border_pen = turtle.Turtle()
# border_pen.speed(0)
# border_pen.color("white")
#
# border_pen.penup()
# border_pen.setposition(-300, -300)
# border_pen.pensize(3)
# border_pen.pendown()
#
# for side in range(4):
#     border_pen.fd(600)
#     border_pen.lt(90)
# border_pen.hideturtle()
#
# # Draw Pen for Win
# game_over_pen = turtle.Turtle()
# game_over_pen.speed(0)
# game_over_pen.color("green")
# game_over_pen.penup()
# game_over_pen.setposition(0, 0)
# game_over_pen.hideturtle()
# game_over_string = "Next Level"
#
# # Set the score to 0
# score = 0
#
# # Draw the score
# score_pen = turtle.Turtle()
# score_pen.speed(0)
# score_pen.color("white")
# score_pen.penup()
# score_pen.setposition(-290, 280)
# scorestring = "Score: %s" % score
# score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
# score_pen.hideturtle()
#
# # Create the player turtle
# player = turtle.Turtle()
# player.color("blue")
# player.shape("player.gif")
# player.penup()
# player.speed(0)
# player.setposition(0, -250)
# player.setheading(90)
#
# playerspeed = 15
#
# # Chose a number of enemies
# number_of_enemies = random.randint(5, 10)
# # Create an empty list of enemies
# enemies = []
#
# # Add enemies to the list
# for i in range(number_of_enemies):
#     # Create the enemy
#     enemies.append(turtle.Turtle())
#
# for enemy in enemies:
#     # Create invader
#     enemy.color("red")
#     enemy.shape("invader.gif")
#     enemy.penup()
#     enemy.speed(0)
#     x = random.randint(-200, 200)
#     y = random.randint(100, 250)
#     enemy.setposition(x, y)
#
# enemyspeed = 2
#
# # Create player's bullet
# bullet = turtle.Turtle()
# bullet.color("yellow")
# bullet.shape("circle")
# bullet.penup()
# bullet.speed(0)
# bullet.setheading(90)
# bullet.shapesize(0.5, 0.5)
# bullet.hideturtle()
#
# bulletspeed = 20
#
# # Define bullet state
# # ready - ready to fire
# # fire - bullet is firing
# bulletstate = "ready"
#
#
# # Move the player left and right
# def move_left():
#     x = player.xcor()
#     x -= playerspeed
#     if x < -280:
#         x = -280
#     player.setx(x)
#
#
# def move_right():
#     x = player.xcor()
#     x += playerspeed
#     if x > 280:
#         x = 280
#     player.setx(x)
#
#
# def fire_bullet():
#     # Declare bulletstate as a global if it needs changed
#     global bulletstate
#     if bulletstate == "ready":
#         os.system("afplay laser.wav&")
#         bulletstate = "fire"
#         # Move bullet to just above player
#         x = player.xcor()
#         y = player.ycor() + 10
#         bullet.setposition(x, y)
#         bullet.showturtle()
#
#
# def isCollision(t1, t2):
#     distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
#     if distance < 15:
#         return True
#     else:
#         return False
#
#
# # Create keyboard bindings
# turtle.listen()
# turtle.onkey(move_left, "Left")
# turtle.onkey(move_right, "Right")
# turtle.onkey(fire_bullet, "space")
#
# # Main game loop
# while True:
#     for enemy in enemies:
#         # move the enemy
#         x = enemy.xcor()
#         x += enemyspeed
#         enemy.setx(x)
#
#         # Move the enemy back and down
#         if enemy.xcor() > 280:
#             # Move all the enemies down
#             for e in enemies:
#                 y = e.ycor()
#                 y -= 40
#                 e.sety(y)
#             # Change Direction
#             enemyspeed *= -1
#         if enemy.xcor() < -280:
#             # Move all enemies down
#             for e in enemies:
#                 y = e.ycor()
#                 y -= 40
#                 e.sety(y)
#             # Change Direction
#             enemyspeed *= -1
#
#         # Check for a collision between the bullet and the enemy
#         if isCollision(bullet, enemy):
#             os.system("afplay explosion.wav&")
#             # Reset the bullet
#             bullet.hideturtle()
#             bulletstate = "ready"
#             bullet.setposition(0, -400)
#             if number_of_enemies != 0:
#                 # Delete enemy and update number
#                 number_of_enemies -= 1
#                 enemy.hideturtle()
#                 enemy_hit = enemies.index(enemy)
#                 del enemies[enemy_hit]
#             if number_of_enemies == 0:
#                 enemy.hideturtle()
#                 game_over_pen.write(game_over_string, False, align="center", font=("Arial", 14, "normal"))
#                 number_of_enemies = random.randint(5, 10)
#                 for i in range(number_of_enemies):
#                     enemies.append(turtle.Turtle())
#                 for e in enemies:
#                     # Create invader
#                     e.color("red")
#                     e.shape("invader.gif")
#                     e.penup()
#                     e.speed(0)
#                     x = random.randint(-200, 200)
#                     y = random.randint(100, 250)
#                     e.setposition(x, y)
#
#                 enemyspeed = 2
#
#             # Update the score
#             score += 10
#             scorestring = "Score: %s" % score
#             score_pen.clear()
#             score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
#             game_over_pen.clear()
#
#         if isCollision(enemy, player):
#             game_over_string = "Game Over"
#             game_over_pen.color("red")
#             os.system("afplay explosion.wav&")
#             player.hideturtle()
#             for e in enemies:
#                 del enemies[e]
#             game_over_pen.write(game_over_string, False, align="center", font=("Arial", 14, "normal"))
#             break
#
#     # Move bullet
#     if bulletstate == "fire":
#         y = bullet.ycor()
#         y += bulletspeed
#         bullet.sety(y)
#
#     # Check to see if bullet reached the top
#     if bullet.ycor() > 275:
#         bullet.hideturtle()
#         bulletstate = "ready"
#
# mainScreen.exitonclick()
