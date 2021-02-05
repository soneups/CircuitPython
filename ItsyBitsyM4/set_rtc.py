import board
import busio as io
import adafruit_ht16k33.segments
import adafruit_ds3231
from time import sleep

i2c = io.I2C(board.SCL, board.SDA)
display = adafruit_ht16k33.segments.Seg14x4(i2c)
rtc = adafruit_ds3231.DS3231(i2c)
rtcdt = rtc.datetime
rtcmonth = rtcdt.tm_mon
rtcday = rtcdt.tm_mday

# if after doing a print (rtcdt) the year = 2000 its likely something helpfully pressed reset on the RTC
# if you are reading this and its not yet the year 2000 then its likely time travel has been invented!
# struct_time(tm_year=2000, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=7, tm_sec=2, tm_wday=0, tm_yday=-1, tm_isdst=-1)

# set via 'HT: https://learn.adafruit.com/adafruit-ds3231-precision-rtc-breakout/circuitpython
# import time
# rtc.datetime = time.struct_time((2017, 1, 1, 0, 0, 0, 6, 1, -1))

# tm_year - The year of the timestamp
# tm_mon - The month of the timestamp
# tm_mday - The day of the month of the timestamp
# tm_hour - The hour of the timestamp
# tm_min - The minute of the timestamp
# tm_sec - The second of the timestamp
# tm_wday - The day of the week (0 = Monday, 6 = Sunday)
# tm_yday - The day within the year (1-366)
# tm_isdst - 0 if not in daylight savings, 1 if in savings, and -1 if unknown
