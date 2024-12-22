import RPi.GPIO as GPIO
from time import sleep

# Constants
DELAY = 0.1
IN_PIN = 40
OUT_PIN = 38

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(OUT_PIN, GPIO.OUT)
GPIO.setup(IN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initial states
led_state = False
button_state = 1
button_state_old = 1

try:
    while True:
        # Read button state
        button_state = GPIO.input(IN_PIN)
        print(f"Button state: {button_state}")

        # Toggle LED state on button press
        if button_state == 1 and button_state_old == 0:
            led_state = not led_state
            GPIO.output(OUT_PIN, led_state)

        # Update old button state
        button_state_old = button_state

        # Delay to debounce
        sleep(DELAY)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO cleaned up successfully.')
