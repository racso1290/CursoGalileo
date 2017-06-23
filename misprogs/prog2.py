import mraa
import time
import sys
import signal
def manejadorsenial(signal, frame):
	sys.exit(0)
signal.signal(signal.SIGINT, manejadorsenial)

try:
	pinSensor = mraa.Aio(0)
	pinSensor.setBit(12)
	while True:
		valorSensor = pinSensor.read()
		print "%.6f" % (valorSensor/819.0)
		time.sleep(1)
except:
	print "Seguro que tienes un ADC?"
