import cv2
import numpy as np
import time
video = cv2.VideoCapture(0)
time.sleep(3)
background = 0

for i in range(30):
    ret,background = video.read()

background = np.flip(background, axis = 1)
while True:
    ret,img = video.read()
    img = np.flip(img, axis = 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv, (35,35), 0)

    lower = np.array([0,120,70])
    upper = np.array([10,255,255])
    mask01 = cv2.inRange(hsv, lower, upper)

    #this code is working for only red color
    lower_hue = np.array([170,120,70]) #red
    upper_hue = np.array([180, 255, 255])

    #lower_hue = np.array([0, 0, 0])  # black
    #upper_hue = np.array([50, 50, 100])

    #lower_hue = np.array([100, 30, 30]) #blue
    #upper_hue = np.array([150, 148, 255])

    mask02 = cv2.inRange(hsv, lower_hue, upper_hue)


    mask = mask01 + mask02

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

    img[np.where(mask == 255)] = background[np.where(mask == 255)]

    cv2.imshow("display", img)
    #cv2.imshow("background", background)
    #cv2.imshow("mask01", mask01)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.capture()
cv2.destroyAllWindows()
