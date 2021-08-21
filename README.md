# Problem statement:
There are a lot of videos listed on the internet which shows that the animals are hit by the car and then they get injured and some of them died.
One of the videos is here:

"Animals And Car Crashes|Live Cars And Animal Accidents Cought In Camera,Animals Hit By " Cars😱YouTube, uploaded by Gk with Rahul, 4 Feb 2019, https://www.youtube.com/watch?v=5Ql9ayaBPAE&ab_channel=GkwithRahul.

# Goal:
The goal of this project is to detect an animal on the road using the dashcam and if an animal is present on the road, then alert the driver about the presence of an animal (if an animal is present) to avoid the potential crash and injury to an animal.
The alert can be generated using any emergency alarm present inside the vehicle.
The hardware that I used was Nvidia Jetson Nano 4GB device. As I am completely new to computer vision, I had a lot of fun completing the Jetson nano AI course and developing this project. I watched several videos about object detection by Dustin Franklin. Then I used a camera to connect to the Jetson nano and finally I used the pretrained ssd_v2 model to detect animals present on the road. I also used Linux’s built-in system call to display an alert message to the user.
There is still way more that can be done here, for example, right now instead of alarm I am just displaying an alert message to the user, but we can also use an alarm to generate a beep sound (for alarming driver).
I do not have a car, so I have tested the model using the images available on the internet.
Below are some images which shows the detected animal and an alert message at the top-right corner of the screen.

![bear1](https://user-images.githubusercontent.com/42191708/130308753-2e796a98-5225-44d5-9c62-5117d39eddd3.png)

![bear4](https://user-images.githubusercontent.com/42191708/130308763-33289590-7c37-4660-9bd9-53174258ddab.png)

<br />
Animal detection using Nvidia Jetson Nano [YouTube](https://youtu.be/WS0lKG8rBic).


# Hardware Required:
1. Nvidia Jetson Nano 4GB
2. Any USB webcam.

# Step by step process to run the code

1. First install the object detection API from this [link](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md) onto your Nvidia Jetson Nano. This [link](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md) describes how to install object detection API on your nvidia jetson nano.
2. Once you install the object detection API using the above steps. Clone my repository using following command:
```
git clone https://github.com/ndesale/Animal_Detection.git
```
3. Then attach your webcam to jetson nano via USB cable.
4. Find the name of your web cam using following command
```
v4l2-ctl --list-devices
```
It should be something like : /dev/video1  (instead of number 1 there may be different number of your webcam)
5. Then edit my code 'animal_detector.py' using 'vi' or any other editor and edit line number 8 to:
```
camera = jetson.utils.gstCamera(1280, 720, "Specify The Name of YOUR webcam")
```
Here specify the name of your web cam that you obtained in step 4.

6. Once everything is done, run my code 'animal_detector.py' using command:
```
python animal_detector.py
```
7. Initially it will take around 4-5 minutes to load the camera drivers and show up the camera video on the screen.
8. Once the video window pops up, the detection begins, then put your camera in front of any animal present on the road, then it will show the animal detection using bounding box.
9. If an animal is detected on the screen then you can see an alert message on the top-right corner of the screen. Sample error message is shown here:

![image](https://user-images.githubusercontent.com/42191708/130309779-1c2ef8da-6399-43eb-9c17-0964926ab561.png)

10. Once an animal is detected the code waits for 2 seconds because if we dont wait for 2 seconds then it will keep on spamming the alert message for each detection. There may be multiple detections in a second (maybe 10 or may be 20). If you want to reduce the time to wait then go to line number 26 and change the number of seconds from 2 to your desired value.
