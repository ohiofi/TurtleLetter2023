from turtle import *
# uppercase letters go up here
from turtle import *

def drawC():
  goto(0, 0)
  penup()
  backward(50)
  left(90)
  forward(25)
  forward(20)
  pendown()
  
  for i in range(17):
    left(20)
    forward(20)

def drawL():
  penup()
  goto(0, -20)
  left(20)
  pendown()
  forward(105)
  penup()
  goto(0, -20)
  right(90)
  pendown()
  forward(75)

drawC()
drawL()






# lowercase letters down here







