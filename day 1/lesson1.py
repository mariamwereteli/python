from turtle import *
speed(3)

#background
bgcolor("skyblue")

#we want to paint a house

#step 1: draw square
width(8) 
color("#ffefc9")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing door

forward(80)
color("brown")
begin_fill()
left(90)
forward(90)
right(90)
forward(40)
right(90)
forward(90)
end_fill()


penup()
goto(200, 200)
pendown()
color("#630a00")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

exitonclick()

