
def Triangle (length,color):
  turtle.color(color)
  turtle.fillcolor(fillColor)
  turtle.begin_fill()
  turtle.forward(length)
  turtle.left (120)
  turtle.forward(length)
  turtle.left (120)
  turtle.forward (length)
  turtle.end_fill()
  print ("Triangle Drawn!")
def Circle(length,color):
  turtle.color(color)
  turtle.fillcolor(fillColor)
  turtle.begin_fill()
  turtle.circle(length)
  turtle.end_fill()
  print ("Circle drawn!")
def Star(length,color):
  turtle.left (45)
  turtle.forward (length)
  turtle.right (45)

def Square(length,color):
  turtle.color(color)
  turtle.fillcolor(fillColor)
  turtle.begin_fill()
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(length)
  turtle.end_fill()
  print ("Square drawn!")

import turtle
turtle=turtle.Turtle()


shape=input ("What shape do you want turtle to draw?")
length=input ("What should the length (or radius for a circle) of the shape be?(in pixils)")
length=int(length)
color=input ("What color do you want the shape's outline to be?")
fillColor=input ("What color do you want the shape's inside to be?")

if shape=="triangle":
  print (Triangle(length,color))
elif shape=="star":
  print (Star(length,color))
elif shape=="circle":
  print (Circle(length,color))
elif shape=="square":
  print(Square(length,color))

  