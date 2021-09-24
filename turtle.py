
# 海龟画图
import turtle

try:
    t = turtle.pen()

    turtle.bgcolor("black")
    side2 = 2
    colors = ["red", "yellow", "blue", "orange"]

    for x in range(360):
        turtle.pencolor(colors[x % side2])
        turtle.forward(x)
        turtle.left(360 / side2 + 1)

    turtle.width(x * side2 / 200)

    # turtle.home()
    # turtle.circle(80)

    turtle.done()
    print(len(t))

except turtle.Terminator:
    print("error")


