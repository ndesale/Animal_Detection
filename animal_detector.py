import time
import os
import jetson.inference
import jetson.utils


net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.gstCamera(1280, 720, "/dev/video0")

display = jetson.utils.glDisplay()

animalList = ['cat', 'dog' , 'bear', 'bird', 'dog', 'cow' ,'sheep', 'horse']

while display.IsOpen():
	img, width, height = camera.CaptureRGBA()
	detections = net.Detect(img, width, height)
	display.RenderOnce(img, width, height)
	display.SetTitle("Object Detection | Network (:.0f) FPS".format(net.GetNetworkFPS()))
	if len(detections) >= 1:
		name = net.GetClassDesc(detections[0].ClassID)
		if name.lower() in animalList:
			os.system("/usr/bin/notify-send --icon=error \"There is an animal in the close proximity. Please be cautious. Apply brakes and Drive slowly\".")

			# Below code is to wait for 2 seconds after detecting an animal because if we dont wait then it will keep on spamming the alert message for each detection.
			# There may be multiple detections in a second (maybe 10 or may be 20).
			time.sleep(2)
