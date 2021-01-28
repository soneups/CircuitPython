# import the libraries
import board
import busio as io
import adafruit_ht16k33.segments

i2c = io.I2C(board.SCL, board.SDA)
display = adafruit_ht16k33.segments.Seg14x4(i2c)

#clear the display
display.fill(0)
display.show()

display.print('GARY')
display.show()

#alternative way display[0] = 'G'
#display.brightness = 1 - 15
#display.blink_rate = 0 - 3
