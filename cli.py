import cv2
import os
from vidgear.gears import CamGear

stream = CamGear(
    source="https://www.youtube.com/watch?v=69X8ZLj1ukw",
    stream_mode=True,
    time_delay=1,
    logging=True,
).start()

path = "D:\\github codes\\test\\"

currentframe = 0
while True:

    frame = stream.read()
    if frame is None:
        break

    cv2.imshow("Output Frame", frame)

    name = path + "./frames" + str(currentframe) + ".jpg"
    print("Creating..." + name)

    cv2.imwrite(name, frame)
    currentframe += 5

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
stream.stop()
