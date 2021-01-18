import sys
import serial
import serial.tools.list_ports
import time
import re

def query_yes_no(question, default="yes"):
	"""Ask a yes/no question via input() and return their answer.

	"question" is a string that is presented to the user.
	"default" is the presumed answer if the user just hits <Enter>.
		It must be "yes" (the default), "no" or None (meaning
		an answer is required of the user).

	The "answer" return value is True for "yes" or False for "no".
	From: https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
	"""
	valid = {"yes": True, "y": True, "ye": True,
			 "no": False, "n": False}
	if default is None:
		prompt = " [y/n] "
	elif default == "yes":
		prompt = " [Y/n] "
	elif default == "no":
		prompt = " [y/N] "
	else:
		raise ValueError("invalid default answer: '%s'" % default)

	while True:
		sys.stdout.write(question + prompt)
		choice = input().lower()
		if default is not None and choice == '':
			return valid[default]
		elif choice in valid:
			return valid[choice]
		else:
			sys.stdout.write("Please respond with 'yes' or 'no' "
							 "(or 'y' or 'n').\n")

class printerInterface():
	def __init__(self):
		self.ser = None
		self.temps = {}
		self.pos = {}
		self.bounds = {'X': (0.0, 125.0), 'Y': (0.0, 123.0), 'Z': (0.0, 120.0)}
		self.fanSpeed = 0
		self.minExtrusionTemp = 180
		self.minFanOnNozzleTemp = 70
		self.minHotNozzleFanSpeed = 100
		self.p1 = re.compile(r'\w+:\d+[.]\d+')
		self.p2 = re.compile(r'\w+:\d+[.]\d+\s/\d+[.]\d+')


	def _sendCommand(self, cmd):
		self.ser.reset_input_buffer()
		self.ser.reset_output_buffer()
		self.ser.write((cmd + "\n").encode())
		self.ser.flush()


	def connect(self, port=None, baudrate=115200):
		if port is None:
			print("No port given")
			for port in serial.tools.list_ports.comports():
				try:
					print("Attempting to connect to {} on port {}".format(port.description, port.device))
					return self.connect(port=port.device, baudrate=baudrate)
				except serial.serialutil.SerialException as e:
					print("SerialException({0}): {1}".format(e.errno, e.strerror))
		else:
			self.ser = serial.Serial(port, baudrate, timeout=None)
			print("Connection successful")
			self._sendCommand("\n")
			time.sleep(1)
			# Need to read line twice for some printers after connecting, not sure why
			out = self.ser.readline().decode()
			print("r1", out)
			out = self.ser.readline().decode()
			print("r2", out)
			return 1, out


	def disconnect(self):
		self.ser.reset_input_buffer()
		self.ser.reset_output_buffer()
		self.ser.close()
		print("Disconnected")
		return 1, ""


	def init(self):
		pos = self.getPosition()
		homed = False
		if pos['X'] == 0 and pos['Y'] == 0 and pos['Z'] == 0:
			homed = True
			print("Homing the axes")
			# Homing XY first to avoid obstacles
			self._sendCommand("G28 X Y")
			time.sleep(3)
			# Homing Z
			self._sendCommand("G28 Z")
			self.ser.readline()
			print("Getting position")
			print(self.getPosition())
		print("Setting coordinates to absolute positioning")
		self._sendCommand("G90")
		out = self.ser.readline()
		return homed, out.decode()


	def moveTo(self, X=None, Y=None, Z=None, E=None, F=None):
		s = "G1"
		new_pos = {}
		if X is not None:
			new_pos['X'] = X
			if new_pos['X'] >= self.bounds['X'][0] and new_pos['X'] <= self.bounds['X'][1]:
				s += " X{:.4f}".format(X)
			else:
				return 0, "X axis out of bound"
		if Y is not None:
			new_pos['Y'] = Y
			if new_pos['Y'] >= self.bounds['Y'][0] and new_pos['Y'] <= self.bounds['Y'][1]:
				s += " Y{:.4f}".format(Y)
			else:
				return 0, "Y axis out of bound"
		if Z is not None:
			new_pos['Z'] = Z
			if new_pos['Z'] >= self.bounds['Z'][0] and new_pos['Z'] <= self.bounds['Z'][1]:
				s += " Z{:.4f}".format(Z)
			else:
				return 0, "Z axis out of bound"
		if E is not None:
			new_pos['E'] = E
			T = self.getTemperature()[1]['T'][0]
			if T < self.minExtrusionTemp:
				return 0, "Extruder temperature too low for extrusion"
			s += " E{:.4f}".format(E)
		if F is not None:
			new_pos['F'] = F
			s += " F{:.4f}".format(F)
		self._sendCommand(s)
		out = self.ser.readline()
		for k, e in new_pos.items():
			self.pos[k] = e
		return 1, out.decode()


	# Really should be called "moveBy"
	def move(self, X=None, Y=None, Z=None, E=None, F=None):
		s = "G1"
		new_pos = {}
		if X is not None:
			new_pos['X'] = self.pos['X'] + X
			if new_pos['X'] >= self.bounds['X'][0] and new_pos['X'] <= self.bounds['X'][1]:
				s += " X{:.4f}".format(new_pos['X'])
			else:
				return 0, "X axis out of bound"
		if Y is not None:
			new_pos['Y'] = self.pos['Y'] + Y
			if new_pos['Y'] >= self.bounds['Y'][0] and new_pos['Y'] <= self.bounds['Y'][1]:
				s += " Y{:.4f}".format(new_pos['Y'])
			else:
				return 0, "Y axis out of bound"
		if Z is not None:
			new_pos['Z'] = self.pos['Z'] + Z
			if new_pos['Z'] >= self.bounds['Z'][0] and new_pos['Z'] <= self.bounds['Z'][1]:
				s += " Z{:.4f}".format(new_pos['Z'])
			else:
				return 0, "Z axis out of bound"
		if E is not None:
			new_pos['E'] = self.pos['E'] + E
			if self.getTemperature()[1]['T'][0] < self.minExtrusionTemp:
				return 0, "Extruder temperature too low for extrusion"
			s += " E{:.4f}".format(new_pos['E'])
		if F is not None:
			s += " F{:.4f}".format(F)
		self._sendCommand(s)
		out = self.ser.readline()
		for k, e in new_pos.items():
			self.pos[k] = e
		return 1, out.decode()


	def waitForMove(self):
		self._sendCommand("M400")
		out = self.ser.readline()
		return 1, out.decode()



	def getPosition(self, k=3):
		self._sendCommand("M114")
		out = self.ser.readline()
		new_elements = []
		for pos in self.p1.findall(out.decode()):
			a, b = pos.split(":")
			self.pos[a] = float(b)
			new_elements.append(a)
		if k < 1 or ('X' in new_elements and 'Y' in new_elements and 'Z' in new_elements):
			return self.pos
		else:
			return self.getPosition(k=k-1)


	def fanOn(self, speed=255):
		if speed < self.minHotNozzleFanSpeed and self.getTemperature()[1]['T'][0] > self.minFanOnNozzleTemp:
			return 0, "Unable to set fan speed. Fan speed needs to be at lease {:d} for temperatures higher than {:d} degrees".format(self.minHotNozzleFanSpeed, self.minFanOnNozzleTemp)
		self._sendCommand("M106 S{:d}".format(speed))
		out = self.ser.readline()
		self.fanSpeed = int(speed)
		return 1, out.decode()


	def fanOff(self):
		if self.getTemperature()[1]['T'][0] > self.minFanOnNozzleTemp:
			return 0, "Unable to turn off the fan, extruder temperature is too high"
		self._sendCommand("M107")
		out = self.ser.readline()
		self.fanSpeed = 0
		return 1, out.decode()


	def setBedTemperature(self, T, wait=True, accurate=True):
		if wait and accurate:
			s = "M190 R{:d}".format(T)
		elif wait and not accurate:
			s = "M190 S{:d}".format(T)
		else:
			s = "M140 S{:d}".format(T)
		print("Setting bed temperature to {:d}".format(T))
		self._sendCommand(s)
		out = self.ser.readline()
		if wait:
			while not self.getTemperature()[0]:
				time.sleep(1)
		return 1, out.decode()


	def setExtruderTemperature(self, T, wait=True, accurate=True):
		if T > self.minFanOnNozzleTemp and self.fanSpeed < self.minHotNozzleFanSpeed:
			return 0, "Unable to set extruder temperature. Fan speed is {:d} but needs to be at lease {:d} for temperatures higher than {:d} degrees".format(self.fanSpeed, self.minHotNozzleFanSpeed, self.minFanOnNozzleTemp)
		if wait and accurate:
			s = "M109 R{:d}".format(T)
		elif wait and not accurate:
			s = "M109 S{:d}".format(T)
		else:
			s = "M104 S{:d}".format(T)
		print("Setting extruder temperature to {}".format(T))
		self._sendCommand(s)
		out = self.ser.readline()
		if wait:
			while not self.getTemperature()[0]:
				time.sleep(1)
		return 1, out.decode()


	def getTemperature(self, k=5):
		self._sendCommand("M105")
		out = self.ser.readline().decode()
		temps = self.p2.findall(out)
		if len(temps) > 0:
			for temp in temps:
				a, b = temp.split(':')
				b, c = b.split('/')
				self.temps[a] = (float(b), float(c))
			return 1, self.temps
		else:
			temps = self.p1.findall(out)
			if len(temps) > 0:
				for temp in temps:
					a, b = temp.split(':')
					if a in self.temps:
						self.temps[a] = (float(b), self.temps[a][1])
					else:
						self.temps[a] = (float(b), 0.0)
				return 0, self.temps
		print("Temperature not found: {}".format(out))
		if k:
			return self.getTemperature(k=k-1)
		else:
			raise Exception



	def prime(self):
		print("Priming...")
		self.fanOn(speed=200)
		self.setExtruderTemperature(210, wait=False)
		# self.setBedTemperature(50, wait=False)
		self.moveTo(X = 0, Y = 5, Z = 5, F = 9000)
		self.setExtruderTemperature(210, accurate=False)
		# self.setBedTemperature(50, accurate=False)
		self.moveTo(X = 0, Y = 0, Z = 0.15, F = 9000)
		self.move(X = 5, E = 2, F=300)
		# self.move(E = -2)
		self.moveTo(Z = 10, F=3000)
		self.moveTo(X = 0, Y = 0, F=3000)
		print("Done.")


	def primeInPlace(self, E=3):
		self.fanOn(speed=200)
		self.setExtruderTemperature(210, accurate=False)
		self.move(E = E, F=300)


	def pause(self):
		self.setExtruderTemperature(170, wait=False)
		self.moveTo(X = 0, Y = 123)



	def end(self):
		self.setExtruderTemperature(0, wait=False)
		self.setBedTemperature(0, wait=False)
		self.moveTo(X = 0, Y = 123)


if __name__ == "__main__":
	pi = printerInterface()
	for port in serial.tools.list_ports.comports():
		if query_yes_no("Want to try connect to {0} on port {1}?".format(port.description, port.device)):
			try:
				print("Attempting to connect to {0} on port {1}".format(port.description, port.device))
				pi.connect(port=port.device)
				break
			except serial.serialutil.SerialException as e:
				print("SerialException({0}): {1}".format(e.errno, e.strerror))
	if pi.ser != None:
		pi.init()
		print(pi.getTemperature())
		# pi.prime()
		# pi.fanOn(100)
		# print(pi.getTemperature())
		# print(pi.moveTo(Z=5))
		# print(pi.moveTo(Z=10))
		# print(pi.moveTo(Z=-10))
		# pi.init()
		# print(pi.getTemperature())
		# print(pi.getPosition())
		# # pi.fanOff()
		pi.disconnect()