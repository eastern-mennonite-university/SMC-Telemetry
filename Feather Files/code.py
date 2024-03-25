import board
import time
import neopixel
import microcontroller
import adafruit_mcp2515
from digitalio import DigitalInOut

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.3

cs = DigitalInOut(board.CAN_CS)
cs.switch_to_output()
spi = board.SPI()
can_bus = adafruit_mcp2515.MCP2515(spi, cs, loopback=False, silent=False)

while True:

    message = adafruit_mcp2515.canio.Listener(can_bus, timeout=1.0)
    print(message.receive())

    temp = microcontroller.cpu.temperature
    if temp < 60:
        pixel.fill((0, 134, 64))
    elif 60 <= temp <= 80:
        pixel.fill((255, 255, 0))
    elif 80 < temp:
        pixel.fill((255, 0, 0))