import board
import busio as io
import adafruit_ht16k33.segments

i2c = io.I2C(board.SCL, board.SDA)

display = adafruit_ht16k33.segments.Seg14x4(i2c)

#clear the display
display.fill(0)
display.show()

display[0] = 'G'
display[1] = 'A'
display[2] = 'R'
display[3] = 'Y'
display.show()

#alternative way
#display.print('CPY!')
#display.show()
