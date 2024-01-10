import cv2
import pygetwindow as gw
#import numpy
cap = cv2.VideoCapture(2)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Get the primary screen dimensions
windows = gw.getWindowsWithTitle(gw.getAllTitles()[1])
if windows:
    screen = windows[1]
    screen_width, screen_height = screen.width, screen.height
else:
    # Set default values if no windows are found
    screen_width, screen_height = 1920, 1080  # Replace with your default screen dimensions
cap.set(3, screen_width)  # Set the width
cap.set(4, screen_height)
while True:
    #a=a+1
   # diff = cv2.absdiff(frame1, frame2)
    retV, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    area = 0
    X = Y = W = H = 0
    for (x, y, w, h) in faces:
        if w * h > area:
            area = w * h
            X, Y, W, H = x, y, w, h
    cv2.rectangle(frame, (X, Y), (X + W, Y + H), (0,255,0), 2)

    fil = cv2.flip(frame, 1)
    cv2.imshow("Capture",fil)

    #cv2.imshow("Capture",gray)
    
    key=cv2.waitKey(1)
   # print(gray)

    if key==ord('q'):
        break
#print(a)
#cam.release()
cv2.destroyAllWindows   
