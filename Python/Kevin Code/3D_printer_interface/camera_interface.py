import cv2, queue, threading, time, copy

class cameraInterface():
	def __init__(self):
		self.cap = None
		self.capturing = False

	def connect(self, idx=0, win=False):
		print("Attempting to connect to camera with index {}".format(idx))
		self.idx = idx
		self.cap = cv2.VideoCapture(idx)
		if self.cap.isOpened():
			print("Connection successful")
			self.q = queue.Queue()
			t = threading.Thread(target=self._reader)
			t.daemon = True
			t.start()
			if win:
				self.win = cv2.namedWindow(str(self.idx))
			else:
				self.win = None

	# read frames as soon as they are available, keeping only most recent one
	def _reader(self):
		while True:
			ret, frame = self.cap.read()
			if not ret:
				break
			if not self.q.empty():
				try:
					self.q.get_nowait()   # discard previous (unprocessed) frame
				except Queue.Empty:
					pass
			self.q.put((time.time(), frame))


	def read(self):
		return self.q.get()

	# def capture(self, pathPlaceholder, show=False):
	# 	t, frame = self.read()
	# 	cv2.imwrite(pathPlaceholder.format(t), frame)
	# 	if show and self.win:
	# 		cv2.imshow(str(self.idx), frame)

	def _continuousCapture(self):
		self.frames = []
		while self.capturing:
			try:
				self.frames.append(self.read())
			except Queue.Empty:
				pass

	def startContinuousCapture(self):
		self.capturing = True
		t = threading.Thread(target=self._continuousCapture)
		t.daemon = True
		t.start()
		return t

	def endContinuousCapture(self, thread, pathPlaceholder):
		self.capturing = False
		thread.join()

		t = threading.Thread(target=self._saveFrames, args=(copy.deepcopy(self.frames), pathPlaceholder))
		t.daemon = True
		t.start()

	def _saveFrames(self, frames, pathPlaceholder):
		for t, frame in frames:
			cv2.imwrite(pathPlaceholder.format(t), frame)

	def disconnect(self):
		self.cap.release()
		if self.win:
			cv2.destroyWindow(str(self.idx))
		print("Camera {} disconnected".format(self.idx))

if __name__ == "__main__":
	ci = cameraInterface()
	ci.connect(0)
	if ci.cap.isOpened():
		print("Starting continuous capture")
		t = ci.startContinuousCapture()
		print("Sleeping for one second")
		time.sleep(1)
		print("Ending continuous capture with {} frames captured".format(len(ci.frames)))
		ci.endContinuousCapture(t, "camera_interface_test_0_{}.png")
		print("Disconnecting")
		ci.disconnect()

	ci.connect(0)
	print(ci.cap.isOpened())
	if ci.cap.isOpened():
		print("Starting continuous capture")
		t = ci.startContinuousCapture()
		print("Sleeping for one second")
		time.sleep(1)
		print("Ending continuous capture with {} frames captured".format(len(ci.frames)))
		ci.endContinuousCapture(t, "camera_interface_test_1_{}.png")
		print("Disconnecting")
		ci.disconnect()