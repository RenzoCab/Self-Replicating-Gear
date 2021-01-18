# Author: Renzo Caballero,
# Association: King Abdullah University of Science and Technology (KAUST),
# email 1: Renzo.CaballeroRosas@kaust.edu.sa,
# email 2: CaballeroRenzo@hotmail.com,
# email 3: CaballeroRen@gmail.com,
# Website: https://renzocaballero.org/,
# January 2021; Last revision: 07/01/2021.

import sys
import random
import serial
import serial.tools.list_ports
import re
import cv2, queue, threading, time, copy
import os
import numpy as np

ports = serial.tools.list_ports.comports()
time.sleep(2)

for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))
    time.sleep(1)

ser = serial.Serial(port, 9600)
print(ser.portstr)
time.sleep(0.5)
serialString = ser.readline()
print(serialString.decode('Ascii'))
time.sleep(0.5)

# send data via serial port
ser.write(b"Yes... We are communicating!")
time.sleep(1)

# read data from serial port
while(1):
    time.sleep(1)
    if(ser.in_waiting > 0):
        serialString = ser.readline()
        print(serialString.decode('Ascii'))
    else:
        print('Waiting...')
        if (random.random() > 0.5):
            ser.write(b"Hello!")
            print('Python sent: Hello Arduino!')