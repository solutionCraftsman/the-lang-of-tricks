# import turtle
#
# turtle.forward(30)
# turtle.left(90)
#
# turtle.forward(30)
# turtle.left(90)
#
# turtle.forward(30)
# turtle.left(90)
#
# turtle.shape("turtle")
#
# turtle.forward(25)
# turtle.color("blue")
#
# turtle.exitonclick()


import turtle

ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()

