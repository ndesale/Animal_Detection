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
2. Any webcam.

# Step by step process to run the code

1. First install the object detection API from this [link](https://developer.nvidia.com/blog/realtime-object-detection-in-10-lines-of-python-on-jetson-nano/) onto your Nvidia Jetson Nano.
2. Then run this code using "python sample.py"
3. Once camera opens up then put it in front of animals (present on the road) and it will show the animals detected on the screen.
