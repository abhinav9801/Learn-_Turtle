

import turtle
t= turtle.Turtle()
lst=["red","blue","green","yellow","cyan"]

for i in range(200):

    for i in range(6):
        for colours in["red","blue","yellow","cyan"]:
            t.pensize(3)
            t.color(colours)
            t.circle(100)
            t.right(10)
    t.color(lst[i%4])
    t.pensize(i/9)
    t.forward(i/5)
    t.right(30)
    
    