### Capturing images from YouTube videos without downloading Video using Python's VidGear Module
## pip install vidgear
import cv2
import os
from vidgear.gears import CamGear
### Replace this youtube video link with your one
stream = CamGear(source='https://www.youtube.com/watch?v=lQc432kUOpM', y_tube =True,  time_delay=1, logging=True).start()

#this should be the path where u want ur images
path  = 'C:\\Users\\user\\Desktop\\Capture Frames from Online YouTube Video\\cars\\'

currentframe = 0
while True:

    frame = stream.read() ### using functions from vidGear module
    if frame is None:
        break

    cv2.imshow("Output Frame", frame) # optional if u want to show the frames

    name = path + './frames' + str(currentframe) + '.jpg'
    print ('Creating...' + name) 

    cv2.imwrite(name, frame)
    currentframe += 5 ##chnage 5 with the number of frames. Here 5 means capture frame after every 5 frames
    ###usually videos are 30fps so if here 30 is provided a frame will be captures after every second.

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
stream.stop()
stream.stop()