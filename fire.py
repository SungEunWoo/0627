import turtle as t

from tkinter import *
import tkinter.messagebox

color_status = ["White", "Blue", "Red"]
alert_status = ["정상","주의", "화재"]
tempc = 50

def alert():
    messagebox.showinfo("중지", "중지되었습니다.")

def check_fire():
    if tempc < 80 and tempc >= 0:
        status = 0
    elif tempc < 120 and tempc >= 80:
        status = 1
    elif tempc <= 150 and tempc >= 120:
        status = 2
    elif tempc > 150 or tempc < 0 :
        alert()
        turtle.Screen().bye()
        
        
    t.clear()
    t.home()
    t.pendown()
    t.fillcolor(color_status[status])
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()
    t.goto(-22, 50)
    t.write("%s : %d"%(alert_status[status], tempc))
    

def keyUp():
    global tempc
    if tempc < 80:
        tempc += 5
    else :
        tempc += 10
    check_fire()

def keyDown():
    global tempc
    if tempc < 80:
        tempc -= 5
    else :
        tempc -= 10
    check_fire()

t.setup(300, 300)
s = t.Screen()
t.hideturtle()
t.speed(0)
check_fire()
s.onkey(keyUp, "Up")
s.onkey(keyDown, "Down")
s.onkey(s.bye, "q")
s.listen()
