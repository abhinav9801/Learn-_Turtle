import turtle

turtle.bgcolor("white")
turtle.pensize(1)
turtle.speed(100000)
x=1
for x in range(200):
    for colours in["red","white","yellow","cyan"]:
        turtle.color(colours)
        turtle.forward(20+x)
        turtle.right(60)
        x=x+1
exitonclick()
        
        
turtle.hideturtle()
