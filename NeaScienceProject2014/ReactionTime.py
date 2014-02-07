from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import random
# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate(0)
scounter2 = 0
count = 0
# Clear display and show greeting, pause 1 sec
lcd.backlight(lcd.ON)
lcd.clear()
#lcd.message("Sven is Poopy!!!\nKai is awesome!!")
#sleep(3)
#lcd.clear()
lcd.message("BTW This is a\nreaction test")
sleep(3)
lcd.clear()
lcd.message("Press the select\nbutton to start!")
while True:
	if lcd.buttonPressed(lcd.SELECT):
		break
lcd.clear()
lcd.message("When the screen\nturns on,")
sleep(3)
lcd.clear()
lcd.message("Press Select!")
sleep(2)
lcd.clear()
lcd.backlight(lcd.OFF)	
rtime = float(random.randrange(200.0,600.00))
drtime = rtime/100.0
while True:
	scounter2 +=0.001
	
	if lcd.buttonPressed(lcd.SELECT):
		cheat = True
		break
	elif scounter2 <= drtime:
		cheat = False
	sleep(0.001)
if not cheat:	
	lcd.backlight(lcd.ON)
	while True:
		if  lcd.buttonPressed(lcd.SELECT):	
			break
		count += 1
		sleep(0.001)
	secs = count/1000.0
	lcd.message("  Your time is  \n      " + str(secs) )
	sleep(5)
	lcd.clear
	lcd.backlight(lcd.OFF)
else:
	lcd.backlight(lcd.ON)
	lcd.message("YOU CHEATED!\nPress too early")
	sleep(5)
	lcd.clear
	lcd.backlight(lcd.OFF)	
