import turtle

turtle.bgcolor("black")
turtle.pensize(4)
turtle.speed(0)

for i in range(7):
    for colours in["red","blue","white","yellow","cyan"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
        
        
turtle.hideturtle()
