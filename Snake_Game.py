#Snake Game by Mustafa-Kanchwala 
#Step-1 import required module 
import turtle
import time
import random

#Creating a window screen 
wnd = turtle.Screen()
wnd.title("Snake Game by Mustafa-Kanchwala")
wnd.bgcolor("GREEN")
#Setting the Width and Height of Screen
wnd.setup(width=750 , height=650)
wnd.tracer(0)

#UC-2-Creating Mouth of the Snake  
mouth = turtle.Turtle()
mouth.shape("CIRCLE")
mouth.color("BLUE")
mouth.penup()
mouth.goto(0, 0)
mouth.direction = "Stop"

#UC-3-Creating Food in Game
food = turtle.Turtle()
f_color = random.choice(["RED , BLUE , BLACK , ORANGE"])
f_shape = random.choice(["SQUARE , CIRCLE , TRIANGLE"])
food.speed(0)
food.shape(f_shape)
food.color(f_color)
food.penup()
food.goto(0 , 100)

#UC-4-Score Board of the game
pen = turtle.Turtle()
pen.speed(0)
pen.shape("SQUARE")
pen.color("WHITE")
pen.penup()
pen.hideturtle()
pen.goto(0 , 250)
pen.write("Score: 0  High score: 0",align="center",font=("Candara",24,"bold"))

#UC-5-Assigning key Direction
def go_up():
    if mouth.direction !="down":
        mouth.dirrection = "up"
def go_down():
    if mouth.direction != "up":
        mouth.direction = "down"

def go_right():
    if mouth.direction != "left":
        mouth.direction != "right"

def go_left():
    if mouth.direction != "right":
        mouth.direction = "left"

wnd.listen()
wnd.onkeypress(go_up , "w")
wnd.onkeypress(go_down ,"s")
wnd.onkeypress(go_left , "a")
wnd.onkeypress(go_right , "d")
segments =[]

#UC-6-Main Gameplay of Snake Game
while True:
    wnd.update()
    if mouth.xcor() >290 or mouth.xcor() < -290 or mouth.ycor() > 290 or mouth.ycor() < -290:
        time.sleep()
        mouth.goto(0, 0)
        mouth.direction = "Stop"
        colors = random.choice(["Orange , Blue , Grey"])
        shapes = random.choice(["Square","Circle"])
        for segment in segments:
            segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1
            high_score = 0
            pen.clear()
            pen.write("Score :{} High Score: {}".format(
                score,high_score),align="center",font=("Candara",24,"Bold"))
            if mouth.distance(food) < 20:
                x = random.randint(-270,270)
                y = random.randint(-270,270)
                food.goto(x , y)
                