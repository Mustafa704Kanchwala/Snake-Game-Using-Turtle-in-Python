#Snake Game by Mustafa-Kanchwala 
#Step-1 import required module 
import turtle
import time
import random

#Creating a window screen 
wnd = turtle.Screen()
wnd.title("Snake Game by Mustafa-Kanchwala")
wnd.bgcolor("RED")
#Setting the Width and Height of Screen
wnd.setup(width=750 , height=750)
wnd.tracer(0)

#UC-2-Creating Mouth of the Snake  
mouth = turtle.Turtle()
mouth.shape("CIRCLE")
mouth.color("BLUE")
mouth.penup()
mouth.goto(0, 0)
mouth.direction = "Stop"

