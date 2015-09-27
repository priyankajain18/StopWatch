import simpleguitk as simplegui


#Initialize Global variables
sec = 00;
min = 00;
message = str("0")+str(min)+str(":")+str("0")+str(min);

def tick():
    global sec, min, message;
    if sec == 59:
        sec = 0;
        min += 1;
    sec += 1;
    if min<10:
        if sec<=9:
            message = str("0")+str(min)+str(":")+str("0")+str(sec);
        else:
            message = str("0")+str(min)+str(":")+str(sec);
    else:
        if sec<=9:
            message = str(min)+str(":")+str("0")+str(sec);
        else:
            message = str(min)+str(":")+str(sec);
    return message;

#Start Timer
def start():
    timer.start();
    
#Stop Timer
def stop():
    timer.stop();

#Reset Timer
def reset():
    global sec, min;
    sec, min = 0, 0;

#Message on Canvas
def draw(canvas):
    canvas.draw_text(message, [200, 200], 32, "White");

#Creating Timer
timer = simplegui.create_timer(1000, tick);

#Creating Frame
frame = simplegui.create_frame("StopWatch", 500, 500);

#Creating Buttons
frame.add_button("Start", start, 100);
frame.add_button("Stop", stop, 100);
frame.add_button("Reset", reset, 100);

#Registering message handler to print message on Canvas
frame.set_draw_handler(draw);

#Initializing Frame
frame.start();
