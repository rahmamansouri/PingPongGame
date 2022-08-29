# PING PONG GAME 
import turtle 
import winsound

wn = turtle.Screen()
wn.title("Pong by @Rahma")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=7,  stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)


#Paddle 2

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=7,  stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)


# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1,  stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2


#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player1: 0    Player2: 0" , align="center", font=("courier", 24, "normal"))


#score

score_1 = 0
score_2 = 0

#Up and Down Functions 

# Up and Down Functions for the Paddle 1
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

# Up and Down Functions for the Paddle 2


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)



#call the functions
wn.listen()
wn.onkeypress(paddle_1_up, "a")

wn.onkeypress(paddle_1_down, "z")


wn.onkeypress(paddle_2_up, "1")

wn.onkeypress(paddle_2_down, "2")



# main game loop
while True:
    wn.update()

    # Move the balls
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("courier", 24, "normal"))
        winsound.PlaySound('winsound.wav', winsound.SND_FILENAME)



    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("courier", 24, "normal"))
        winsound.PlaySound('winsound.wav', winsound.SND_FILENAME)



    #Paddle and Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1




