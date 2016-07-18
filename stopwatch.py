# Mini-Project 4: The Digital Stop Watch Game!
import simplegui
# Define global variables
mins = 0
sec = 0
count = 0
x = 0
y = 0
a = 0
b = 0
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    global count, sec, mins
    t = count
    if (t == 10):
        sec += 1
        count = 0
    if (sec == 60):
        mins += 1
        sec = 0
# Event handlers for buttons; "Start", "Stop", "Reset" and "Exit"
def start_timer():
    global a, b
    if a-b == 0:
        a += 1
        timer.start()
def stop_timer():
    global x, y, a, b
    if a-b == 1:
        b += 1
        timer.stop()
        y += 1
        if count == 0 :
            x += 1
def reset_timer():
    global count, sec, mins, x, y, a,b
    timer.stop()
    mins, sec, count, x, y,a,b = 0, 0, 0, 0, 0, 0, 0

def exit_timer():
    frame.stop()
# Event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count += 1
def draw_handler(canvas):
    global count, sec, min, x, y
    format(count)
    canvas.draw_text("By Hitvardhan", (305,380), 13, "Green")
    canvas.draw_text("Score:"+str(x)+"/"+str(y), (265,30), 30, "Blue")
    if (sec < 10):
        canvas.draw_text(str(mins)+":"+ "0"+str(sec)+"."+str(count),(80,200),90,"White")
    else:
        canvas.draw_text(str(mins)+":"+str(sec)+"."+str(count),(160,200),30,"White")


# create frame
frame = simplegui.create_frame("Stopwatch",400,400)

# register event handlers
timer = simplegui.create_timer(100,timer_handler)
frame.add_button("Start",start_timer,200)
frame.add_button("Stop ",stop_timer,200)
frame.add_button("Reset",reset_timer,200)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
