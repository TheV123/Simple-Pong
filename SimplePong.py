#Simple Pong
#By Vishal Kamalakrishnan
#This program creates a simple Pong game using Python Turtle graphics

import turtle

#Screen setup
wn = turtle.Screen()
wn.title("Simple Pong Using Turtle") 
wn.bgcolor("black") 
wn.setup(width= 800, height= 600) 
wn.tracer(0)

#Pause Button
is_paused = False
def pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else: is_paused = True
wn.listen()
wn.onkeypress(pause, "p")

#Paddle 1
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.shapesize(stretch_wid= 5, stretch_len= 1)
p1.color("white")
p1.penup()
p1.goto(-350,0)

#Paddle 2
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.shapesize(stretch_wid= 5, stretch_len= 1)
p2.color("white")
p2.penup()
p2.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.dx = 5 #based on computer speed so a higer/lower value maybe required depending on computer
ball.dy = 5

#score
score_p1 = 0
score_p2 = 0

#Setting up Scoreboard Text
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align= "center", font=("Courier", 20, "bold"))

#Other text
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,-200)
pen2.write("Press P to Pause", align= "center", font=("Courier", 10, "bold"))
pen2.goto(0,-230)
pen2.write("First Player to 10 wins", align= "center", font=("Courier", 10, "bold"))

#Functions
def paddle1_up():
    y =p1.ycor() 
    y += 20
    p1.sety(y)
def paddle1_down():
    y =p1.ycor() 
    y -= 20
    p1.sety(y)  
def paddle2_up():
    y =p2.ycor() 
    y += 20
    p2.sety(y)
def paddle2_down():
    y =p2.ycor() 
    y -= 20
    p2.sety(y)

#Key Binds
wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")
wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")

#Main Loop which keeps game running
while True:
    if not is_paused:
        wn.update()

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        if ball.xcor() > 395:
            ball.goto(0, 0)
            ball.dx *= -1
            score_p1 += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_p1, score_p2), align= "center", font=("Courier", 20, "bold")) #increments score
        if ball.xcor() < -395:
            ball.goto(0, 0)
            ball.dx *= -1
            score_p2 += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_p1, score_p2), align= "center", font=("Courier", 20, "bold"))

        #collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < p2.ycor() + 40 and ball.ycor() > p2.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
        
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < p1.ycor() + 50 and ball.ycor() > p1.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
        
        #score 
        if score_p1 == 10:
            pen.clear()
            pen.write("PLAYER 1 WINS", align= "center", font=("Courier", 20, "bold"))
            ball.goto(0,0)
            
        if score_p2 == 10:
            pen.clear()
            pen.write("PLAYER 2 WINS", align= "center", font=("Courier", 20, "bold"))
            ball.goto(0,0)
    else:
        wn.update()
