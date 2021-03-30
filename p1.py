import turtle
t=turtle.Turtle()

lst=["red","blue","yellow","green"]
t.up()
t.goto(200,0)

for i in range(4):
    t.down()
    
    t.color(lst[i])
    t.pensize(20)
    t.circle(100)
    
    t.up()
    t.bk(100)

t.hideturtle()    