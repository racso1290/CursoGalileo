import mraa
import time
import sys
import signal
def manejadorsenial(signal, frame):
	sys.exit(0)
signal.signal(signal.SIGINT, manejadorsenial)


led = mraa.Gpio(13)
pin2 = mraa.Gpio(2)
pin4 = mraa.Gpio(4)
pin2.dir(mraa.DIR_IN)
pin4.dir(mraa.DIR_IN)
led.dir(mraa.DIR_OUT)

entrada1, entrada2, salida=0,0,0

while True:
	entrada1 = pin2.read()
	entrada2 = pin4.read()
	salida = entrada1 & entrada2
	print salida
	led.write(salida)
	time.sleep(1)
