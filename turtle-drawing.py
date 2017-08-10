from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150


### Write your code below:

#draw square

# number of sides drawn
shape1 = 0


length1 = 10

# number of shapes drawn
number_shape1 = 0


shape2 = 0
length2 = 10


# number of sides for shape you want to draw
square = 6
triangle = 3

while length1 > 0:
    t.pendown()
    t.forward(length1)
    t.right(360 / square)
    shape1 +=1
    if shape1 % square == 0:
        length1 -= 0.5

t.penup()
t.forward(50)

while length2 > 0:
    t.pendown()
    t.forward(length2)
    t.right(360 / triangle)
    shape2 +=1
    if shape2 % triangle == 0:
        length2 -= 1

# while shape1 <= square:
#     t.pendown()
#     t.forward(length1)
#     t.right(360 / square)
#     shape1 +=1
#     if shape1 == square:
#         number_shape1 += 1
# #        t.forward(length1 * 2)
#         t.right(360 / square)
#         if number_shape1 != square:
#             shape1 = 0
