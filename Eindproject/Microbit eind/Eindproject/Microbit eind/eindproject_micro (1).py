from microbit import *
import random

DELAY = 20
FRAMES_PER_BALL_SHIFT = 20
FRAMES_PER_NEW_BALL = 100
FRAMES_PER_SCORE = 50

y = 2
speed = 0
score = 0
frame = 0

def make_ball():
    i = Image("00000:00000:00000:00000:00000")
    gap = random.randint(0,4)
    i.set_pixel(4, gap, 9)
    return i



i = make_ball()

while True:
    frame += 1
    
    display.show(i)
    
    
    if button_a.was_pressed():
        if y > 0:
            y += -1
        
    if button_b.was_pressed():
        if y < 4:
            y += 1
    

    bar = display.set_pixel(0, y, 9)
    
    if(frame % FRAMES_PER_BALL_SHIFT == 0):
        i = i.shift_left(1)
    
    if(frame % FRAMES_PER_NEW_BALL == 0):
        i = make_ball()
        
    if(frame % FRAMES_PER_SCORE == 0):
        score += 1
        
    sleep(20)