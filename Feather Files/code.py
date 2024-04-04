import board
import time
import neopixel
import microcontroller
import adafruit_mcp2515
from adafruit_mcp2515.canio import Message, RemoteTransmissionRequest
from digitalio import DigitalInOut

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.3

cs = DigitalInOut(board.CAN_CS)
cs.switch_to_output()
spi = board.SPI()
can_bus = adafruit_mcp2515.MCP2515(spi, cs, loopback=False, silent=False)

while True:
    with can_bus.listen(timeout=1.0) as listener:
        message_count = listener.in_waiting()
        print(message_count, "messages available")
        for _i in range(message_count):
            msg = listener.receive()
            print("Message from ", hex(msg.id))
            if isinstance(msg, Message):
                print("message data:", msg.data)
            if isinstance(msg, RemoteTransmissionRequest):
                print("RTR length:", msg.length)

    temp = microcontroller.cpu.temperature
    if temp < 60:
        pixel.fill((0, 134, 64))
    elif 60 <= temp <= 80:
        pixel.fill((255, 255, 0))
    elif 80 < temp:
        pixel.fill((255, 0, 0))