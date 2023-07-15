from microbit import *
import utime

steps = 0

while True:
  if microphone.sound_level() > 200:
    display.scroll('1 2 3 4 5', delay=150, wait=True)
  if accelerometer.current_gesture() == 'shake' :
    utime.sleep(1)
    steps = steps + 1
  if button_b.is_pressed():
    display.show('T:')
    display.scroll(str(temperature()), delay=150, wait=True)
    display.show('L:')
    display.scroll(str(display.read_light_level()), delay=150, wait=True)
  if button_a.is_pressed():
    display.scroll(str(steps), delay=150, wait=True)