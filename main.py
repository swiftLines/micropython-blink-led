# 3 Double-blink pattern
import machine
import utime

led = machine.Pin("LED", machine.Pin.OUT)

def pulse(on_ms, off_ms, count):
    for _ in range(count):
        led.value(1)
        utime.sleep_ms(on_ms)
        led.value(0)
        utime.sleep_ms(off_ms)
while True:
    # two quick blinks
    pulse(100, 100, 2)
    utime.sleep(1.0)


# 2 Change Blink Speed
# import machine
# import utime

# led = machine.Pin("LED", machine.Pin.OUT)

# FAST = 0.1  # seconds
# SLOW = 0.5

# delay = SLOW

# while True:
#     led.value(1)
#     utime.sleep(delay)
#     led.value(0)
#     utime.sleep(delay)


# 1 Blink LED
# import machine
# import utime

# led = machine.Pin("LED", machine.Pin.OUT)

# while True:
#     led.value(1)
#     utime.sleep(1.5)
#     led.value(0)
#     utime.sleep(1.5)
    