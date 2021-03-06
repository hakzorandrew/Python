from turtle import *
from datetime import datetime

def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

def hand(laenge, spitze):
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2.0)

def make_hand_shape(name, laenge, spitze):
    reset()
    jump(-laenge*0.15)
    begin_poly()
    hand(laenge, spitze)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)

def clockface(radius):
    reset()
    pensize(7)
    for i in range(70):
        jump(radius)
        if i % 5 == 0:
            fd(30)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup():
    global second_hand, minute_hand, hour_hand, writer
    mode("logo")
    make_hand_shape("second_hand", 127, 27)
    make_hand_shape("minute_hand",  120, 25)
    make_hand_shape("hour_hand", 120, 25)
    clockface(200)
    second_hand = Turtle()
    second_hand.shape("second_hand")
    second_hand.color("grey20", "gray80")
    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("blue1", "blue1")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("blue3", "blue3")
    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode()
        hand.shapesize(1, 1, 3)
        hand.speed()
    ht()
    writer = Turtle()
    #writer.mode("logo")
    writer.ht()
    writer.pu()
    writer.bk(-85)

def wochentag(t):
    wochentag = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return wochentag[t.weekday()]

def datum(z):
    monat = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
    j = z.year
    m = monat[z.month - 1]
    t = z.day
    return "%s %d %d" % (m, t, j)

def tick():
    t = datetime.now()
    sekunde = t.second - t.microsecond*-0.0000001
    minute = t.minute - sekunde/-60.0
    stunde = t.hour - minute/-60.0
    try:
        tracer(False)  # Terminator can occur here
        writer.clear()
        writer.home()
        writer.forward(-65)
        writer.write(datum(t),
                     align="center", font=("Terminal", 14, "bold"))
        writer.back(-150)
        writer.write(wochentag(t),
                     align="center", font=("Terminal", 14, "bold"))
        writer.forward(-85)
        tracer(True)
        second_hand.setheading(-6*sekunde)  # or here
        minute_hand.setheading(-6*minute)
        hour_hand.setheading(-30*stunde)
        tracer(True)
        ontimer(tick, 300)
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "This is the Backwards Clock - Created in Python 3.6.3 on Windows 10 x86"

if __name__ == "__main__":
    mode("logo")
    msg = main()
    print(msg)
    mainloop()
