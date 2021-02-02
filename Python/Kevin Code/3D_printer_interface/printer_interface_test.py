import os, time
import numpy as np
from printer_interface import printerInterface

if __name__ == "__main__":
    pi = printerInterface()
    pi.connect()

    if pi.ser != None:

        pi.init()[0]
        pi.moveTo(Z = 10, F = 5000) # F is the speed for the action.
        pi.moveTo(X = 10, Y = 10, F = 1000)
        pi.prime() # Setting extruder temperature.
        pi.moveTo(E = 10, F = 5000)
        # We have "moveTo(...) and "move(...)".

        # List of all functions:
            # _sendCommand(self, cmd): # Checked [NON].
            # connect(self, port = None, baudrate = 115200): # Checked [NON].
            # disconnect(self): # Checked [NON].
            # init(self): # Checked [NON].
            # moveTo(self, X=None, Y=None, Z=None, E=None, F=None): # Checked [YES].
            # move(self, X = None, Y = None, Z = None, E = None, F = None): # Checked [YES].
            # waitForMove(self): # Checked [NON].
            # getPosition(self, k=3): # Checked [NON].
            # fanOn(self, speed=255): # Checked [NON].
            # fanOff(self): # Checked [NON].
            # setBedTemperature(self, T, wait=True, accurate=True): # Checked [NON].
            # setExtruderTemperature(self, T, wait=True, accurate=True): # Checked [NON].
            # getTemperature(self, k=5): # Checked [NON].
            # prime(self): # Checked [NON].
            # primeInPlace(self, E=3): # Checked [NON].
            # pause(self): # Checked [NON].
            # end(self): # Checked [NON].

pi.pause()
pi.disconnect()