import time
import RPi.GPIO as GPIO
tnum = 0
t2num = 0
t3num = 0
counter = 0
temps = []
GPIO.setmode(GPIO.BCM)
GREENLED = 17
REDLED = 18
BUTTON = 22
GPIO.setup(GREENLED, GPIO.OUT)
GPIO.setup(REDLED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.output(GREENLED, GPIO.HIGH)
filename = str(input("What should the file name be?"))

while tnum == 0:
	if GPIO.input(BUTTON):
		tnum  = 1
		GPIO.output(GREENLED, GPIO.LOW)
while t3num == 0:
	if not GPIO.input(BUTTON):
		t3num = 1
GPIO.output(REDLED, GPIO.HIGH)
while t2num == 0:
	if not GPIO.input(BUTTON):
		counter += 1
		if counter % 10 == 0:
			secs = counter/10
			tfile = open("/sys/bus/w1/devices/28-00000535db42/w1_slave")
			text = tfile.read()
			tfile.close()
			temperaturedata = text.split("\n")[1].split(" ")[9]
			temperature = float(temperaturedata[2:])
			temperature = temperature / 1000
			print "Temperature after " + str(secs) + " seconds is " + str(temperature) + " degrees Celsius."
			temps.append(temperature)

		time.sleep(0.1)
	else:
		t2num = 1
		GPIO.output(REDLED, GPIO.LOW)

GPIO.cleanup()		

tempfilename = "/var/tmp/" + str(filename) + ".txt"
tempfile = open(tempfilename, "w")
for i in temps:
	tempfile.write(str(i) + "\n")
tempfile.close()
print "File has been saved to " + str(tempfilename)
