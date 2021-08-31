from neopixel import NeoPixel
from machine import Pin
import time

np1 = NeoPixel(Pin(4), 52)
# np2 = NeoPixel(Pin(5), 100)


brightness = 225

def clear(leds):
    for i in range(leds.n - 1):
        leds[i] = (0, 0, 0)
    leds.write()

def fade_in(leds, delay = 5):
    global brightness
    i = 0
    while i < brightness:
        for j in range(leds.n):
            leds[j] = (150,196,255)
        leds.write()
        diff = (leds.n - j) + delay
        time.sleep_ms(diff)
        i += 1

def test(leds, color):
    for i in range(leds.n):
        leds[i] = (200, 200, 200)
    leds.write()

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)

def rainbow_cycle(leds, wait):
    for j in range(255):
        for i in range(leds.n):
            pixel_index = (i * 256 // leds.n) + j
            leds[i] = wheel(pixel_index & 255)
        leds.write()
        time.sleep(wait)

def main():
    # while True:
        # rainbow_cycle(np1, 0.001)
    # clear(np1)

    # test(np2, (200, 200, 200))


    # Fade in first strip
    fade_in(np1, delay = 0)

    # Fade in other strip
    # fade_in(np2)
