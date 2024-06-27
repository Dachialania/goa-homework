from turtle import *
#we want to point a house 

#step 1: draw a square 
width(7)
color("purple")



forward(200)
left(90)


forward(200)
left(90)
 


forward(200)
left(90)



forward(200)
left(90)
#end of square 

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown() 


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

  
penup()

left(30)
forward(80)

pendown()

color("brown")
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(200,200)
pendown()

penup()

left(90)
forward(80)

pendown()

color("brown")
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


exitonclick()