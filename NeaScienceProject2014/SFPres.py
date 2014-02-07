from time import sleep
import RPi.GPIO as GPIO
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
lcd = Adafruit_CharLCDPlate(0)
lcd.clear
lcd.backlight(lcd.ON)

#Gets temperature and returns it
def get_temp():
	tfile = open("/sys/bus/w1/devices/28-00000535db42/w1_slave")
	text = tfile.read()
	tfile.close()
	temperaturedata = text.split("\n")[1].split(" ")[9]
	temperature = float(temperaturedata[2:])
	temperature = temperature / 1000
	return temperature

#Changes message on lcd Screen
def change_message(message):
	lcd.clear()
	lcd.message(message)

#Only continues once select button is pressed
def button_press_check():
	while True:
		if lcd.buttonPressed(lcd.SELECT):
			break
	
	while True:
		if not lcd.buttonPressed(lcd.SELECT):
			break

#Start Screen
change_message("Press the select\nbutton to begin!")
button_press_check()

#Gets temperature and displays it every second
while True:
	temp = get_temp()
	change_message("Current temp is:\n    " + str(temp) + " C")
	sleep(1)
