import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

###
brushThickness = 15
eraserThickness = 50
###
folderPath = "header"
myList = os.listdir(folderPath)
# print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

header = overlayList[0]
drawColor = (0, 0, 255)

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.85)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)
# imgCanvas.fill(255)
while True:
    # import image
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

