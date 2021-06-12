import cv2
video_capture = cv2.VideoCapture(-1) #captureDevice = camera
def nolight():
	return video_capture.read()