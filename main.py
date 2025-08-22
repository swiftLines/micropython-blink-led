import machine
import utime

led = machine.PWM(machine.Pin(25))
led.freq(1000) # 1 kHz PWM

def ramp(start, stop, step, dwell_ms=2):
    for duty in range(start, stop, step):
        led.duty_u16(duty)
        utime.sleep_ms(dwell_ms)

while True:
    ramp(0, 65535, 512)
    ramp(65535, 0, -512)


# 5 Button-controlled blink (input + debounce)
# import machine
# import utime

# led = machine.Pin("LED", machine.Pin.OUT)
# btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# SLOW = 0.5
# FAST = 0.1

# def debounced_pressed(pin, delay_ms=20):
#     v = btn.value()
#     print("button:", v) # 0=not pressed (pull-down), 1=pressed
#     if not pin.value(): 
#         return False
#     utime.sleep_ms(delay_ms)
#     return pin.value()

# while True:
#     delay = FAST if debounced_pressed(btn) else SLOW
#     led.value(1)
#     utime.sleep(delay)
#     led.value(0)
#     utime.sleep(delay)


# 4 Alternate two LEDs (onboard + external)
# import machine
# import utime

# onboard = machine.Pin("LED", machine.Pin.OUT)
# ext = machine.Pin(15, machine.Pin.OUT)  # external LED on GP15

# while True:
#     onboard.value(1)
#     ext.value(0)
#     utime.sleep(0.3)
#     onboard.value(0)
#     ext.value(1)
#     utime.sleep(0.3)


# 3 Double-blink pattern
# import machine
# import utime

# led = machine.Pin("LED", machine.Pin.OUT)

# def pulse(on_ms, off_ms, count):
#     for _ in range(count):
#         led.value(1)
#         utime.sleep_ms(on_ms)
#         led.value(0)
#         utime.sleep_ms(off_ms)
# while True:
#     # two quick blinks
#     pulse(100, 100, 2)
#     utime.sleep(1.0)


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
    