import machine
import utime

led = machine.Pin("LED", machine.Pin.OUT)

FAST = 0.1  # seconds
SLOW = 0.5

delay = SLOW

while True:
    led.value(1)
    utime.sleep(delay)
    led.value(0)
    utime.sleep(delay)
    
# 1
# import machine
# import utime

# led = machine.Pin("LED", machine.Pin.OUT)

# while True:
#     led.value(1)
#     utime.sleep(1.5)
#     led.value(0)
#     utime.sleep(1.5)
    