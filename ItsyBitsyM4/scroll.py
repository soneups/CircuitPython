import board
from time import sleep
import busio as io
i2c = io.I2C(board.SCL, board.SDA)

import adafruit_ht16k33.segments
display = adafruit_ht16k33.segments.Seg14x4(i2c)

message = 'CHARLIE, BILLY BOO & OSCAR ARE THE BEST PETS EVER! ...'

while True:
    for position in range(0, len(message) - 3):
        buffer = message[position:position+4]
        for index, character in enumerate(buffer):
            if character == '.':
                display[index] = ' '
            display[index] = character
        display.show()
        sleep(0.25)
