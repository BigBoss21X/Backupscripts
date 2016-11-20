#ds18b20 sensor
#sig = 7
#vcc = 5v
#gnd = gnd

import os
from shutil import copyfile

ds18b20 = ''
f=open("/home/pi/Documents/temp_temp.txt","w")

def setup():



	global ds18b20
	for i in os.listdir('/sys/bus/w1/devices'):
		if i != 'w1_bus_master1':
			ds18b20 = i

def read():
#	global ds18b20
	location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
	tfile = open(location)
	text = tfile.read()
	tfile.close()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
	temperature = temperature / 1000
	return temperature
	
def loop():
	while True:
#		with open("/home/pi/Documents/temp_temp.txt","w") as f:
#			f=open("/home/pi/Documents/temp_temp.txt","w")

			if read() != None:
				print "Current temperature : %0.2f C" % read()
#				f=open("/home/pi/Documents/temp_temp.txt","w")
	                        f.write("%0.2f\n" % read())
				f.flush()
				os.fsync(f)

#				f.close()
#				copyfile("/home/pi/Documents/temp_temp.txt","/home/pi/Documents/temp_temp2.txt")

def destroy():
	f.close()
	pass

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
