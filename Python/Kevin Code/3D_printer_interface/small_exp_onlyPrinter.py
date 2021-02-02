import os, time
import numpy as np

from printer_interface import printerInterface

x_s = [37.0, 50.0]
y_i = 57.5
y_f = 122.0
y_s = [67.7, 89.1, 99.1, 118.1]
z_i = 51.0
z_f = 31.5
z_s = [51.0, 41.0, 41.0, 31.5]

# pt_1 = {'X':37.00, 'Y':57.50, 'Z':51.0}
# pt_2 = {'X':37.00, 'Y':67.50, 'Z':51.0}
# pt_3 = {'X':37.00, 'Y':89.10, 'Z':41.0}
# pt_4 = {'X':37.00, 'Y':99.10, 'Z':41.0}
# pt_5 = {'X':37.00, 'Y':118.10, 'Z':31.50}
# pt_6 = {'X':37.00, 'Y':122.00, 'Z':31.50}
# pt_8 = {'X':37.00, 'Y':122.00, 'Z':31.10}

# gaps = [(1, 2), (3, 4)]

z_offset = 0.6
y_offset = 5.0
extrusion_ratio = 0.06

def capture(ci, path, X, Y, Z):
	pi.moveTo(X, Y, Z, F = 9000)
	pi.waitForMove()

if __name__ == "__main__":
	pi = printerInterface() # We create a printer interface object.
	pi.connect() # We use the method 'connect' to connect to the printer's serial port.
	# When we do this, the printer restarts.

	if pi.ser != None: # If we are connected to a serial port...
		# This also sets the printer to HOME for some reason...
       
		if pi.init()[0]:
			print("Homed")
			pi.prime() # Setting extruder temperature.
			pi.moveTo(Z=70)
			pi.moveTo(X=37, Y=40)
			pi.moveTo(Z = 52)
		else:
			print("Not homed")
			pi.moveTo(Z=70, F=3000)
			pi.moveTo(X=20, Y=40, F=3000)
			pi.moveTo(Z=52, F=3000)
			pi.primeInPlace()
			pi.moveTo(X=37, Y=50, F=3000)

		pi.primeInPlace(E=5)
		E = pi.pos['E']
		direction = 1

		for x in x_s:

			if direction == 1:
				init_pt = {'X':x, 'Y':y_i, 'Z':z_i+z_offset}
				final_pt = {'X':x, 'Y':y_f, 'Z':z_f+1.0}
				gaps = [({'X':x, 'Y':e[0]+y_offset, 'Z':e[1]}, {'X':x, 'Y':e[2], 'Z':e[3]}) for e in
					zip(y_s[::2], z_s[::2], y_s[1::2], z_s[1::2])]
			
			else:
				init_pt = {'X':x, 'Y':y_f, 'Z':z_f+z_offset}
				final_pt = {'X':x, 'Y':y_i, 'Z':z_i+1.0}
				gaps = [({'X':x, 'Y':e[0], 'Z':e[1]}, {'X':x, 'Y':e[2]+y_offset, 'Z':e[3]}) for e in
					zip(y_s[::-2], z_s[::-2], y_s[-2::2], z_s[-2::2])]

			pi.moveTo(X=init_pt['X'], Y=init_pt['Y'], E=E, F=3000)
			pi.moveTo(**init_pt, E=E, F=3000)
			E += 2
			pi.moveTo(E=E, F=300)
			pi.waitForMove()
			cur_pt = init_pt
			exp_dir = str(int(time.time()))
			os.mkdir(exp_dir)

			for i in range(len(gaps)):
	
				print("Starting gap {}".format(i))
				(pta, ptb) = gaps[i]
				start_pt = {'X':pta['X'], 'Y':pta['Y'], 'Z':pta['Z']+z_offset}
				end_pt = {'X':ptb['X'], 'Y':ptb['Y'], 'Z':ptb['Z']+z_offset}
				E += extrusion_ratio*np.linalg.norm(np.array(list(cur_pt.values())) - np.array(list(start_pt.values())))
				t = ci.startContinuousCapture()
				pi.moveTo(**start_pt, E=E, F=200)

				E += extrusion_ratio*np.linalg.norm(np.array(list(start_pt.values())) - np.array(list(end_pt.values())))
				pi.moveTo(**end_pt, E=E, F=200)
				pi.waitForMove()
				ci.endContinuousCapture(t, os.path.join(exp_dir, "{}_{{:.6f}}.png".format(i)))
				cur_pt = end_pt

			pi.moveTo(**final_pt)
			pi.moveTo(E = E + 3)
			pi.move(Z = 5, E = E - 3)
			direction = -direction

pi.pause()
pi.disconnect()