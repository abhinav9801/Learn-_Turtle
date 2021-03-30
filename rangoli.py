import turtle

turtle.bgcolor("black")
turtle.pensize(1)
turtle.speed(1000)
x=1
for x in range(400):
    for colours in["red","white","yellow","cyan"]:
        turtle.color(colours)
        turtle.forward(5+x)
        turtle.left(90.99)
        x=x+1
exitonclick()
        
        
turtle.hideturtle()
