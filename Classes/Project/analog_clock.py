#!/usr/bin/python

######################
#   Assignment: Designing a clock
#   Name    : Stephanie Mangereza
#   Date    : 08 /06 /2022
######################

import turtle
import time
wndw = turtle.Screen()
wndw.bgcolor("grey")
wndw.setup(width=600, height=600)
wndw.title("Analogue Clock")
wndw.tracer(0)

# Create the drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)
def draw_clock(hr, mn, sec, pen):
    # Draw clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("black")
    pen.pendown()
    pen.circle(210)

    # Draw hour hashes
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)
    
    # Draw the hands
    # Each tuple in list hands describes the color, the length
    # and the divisor for the angle
    hands = [("pink", 80, 12), ("white", 150, 60), ("orange", 110, 60)]
    time_set = (hr, mn, sec)
    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part/hand[2])*360
        pen.penup()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.setheading(90)
        pen.rt(angle)
        pen.pendown()
        pen.fd(hand[1])

    #number 1
    pen.penup()
    pen.hideturtle()
    pen.goto(170, 260)
    pen.write("1", align="center", font=("Kalinga", 25, "bold"))

    #number 2
    pen.penup()
    pen.hideturtle()
    pen.goto(300, 140)
    pen.write("2", align="center", font=("Kalinga", 25, "bold"))

    #number 3
    pen.penup()
    pen.hideturtle()
    pen.goto(340, -30)
    pen.write("3", align="center", font=("Kalinga", 25, "bold"))

    #number 4
    pen.penup()
    pen.hideturtle()
    pen.goto(300, -200)
    pen.write("4", align="center", font=("Kalinga", 25, "bold"))

    #number 5
    pen.penup()
    pen.hideturtle()
    pen.goto(170, -325)
    pen.write("5", align="center", font=("Kalinga", 25, "bold"))

    #number 6 
    pen.penup()
    pen.hideturtle()
    pen.goto(0, -370)
    pen.write("6", align="center", font=("Kalinga", 25, "bold"))

    #number 7 
    pen.penup()
    pen.hideturtle()
    pen.goto(-170, -325)
    pen.write("7", align="center", font=("Kalinga", 25, "bold"))

    #number 8 
    pen.penup()
    pen.hideturtle()
    pen.goto(-300, -200)
    pen.write("8", align="center", font=("Kalinga", 25, "bold"))

    #number 9
    pen.penup()
    pen.hideturtle()
    pen.goto(-340, -30)
    pen.write("9", align="center", font=("Kalinga", 25, "bold"))

    #number 10
    pen.penup()
    pen.hideturtle()
    pen.goto(-280, 140)
    pen.write("10", align="center", font=("Kalinga", 25, "bold"))

    #number 11
    pen.penup()
    pen.hideturtle()
    pen.goto(-160, 260)
    pen.write("11", align="center", font=("Kalinga", 25, "bold"))

    #number 12 
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 300)
    pen.write("12", align="center", font=("Kalinga", 25, "bold"))

while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    draw_clock(hr, mn, sec, pen)
    wndw.update()
    time.sleep(1)
    pen.clear()

wndw.mainloop()
