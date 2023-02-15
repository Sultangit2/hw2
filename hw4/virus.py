import turtle

tt = turtle.Turtle()
turtle.bgcolor("black")
tt.pencolor("pink")

tt.speed(22)
tt.penup()
tt.goto(0, 200)
tt.pendown()
forDis = 0
dR = 0

while (True):
 tt.forward(forDis)
 tt.right(dR)
 forDis += 3
 dR += 1
 if dR == 210:
     break
 tt.hideturtle()

turtle.done()