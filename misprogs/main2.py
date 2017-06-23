#!/usr/bin/python
import time
import sys
import signal
def manejadorsenial(singal, frame):
	sys.exit(0);
signal.signal(signal.SIGINT, manejadorsenial)
while True:
  print "Hola desde el curso de Intel"
  time.sleep(5)

#Fin de archivo
