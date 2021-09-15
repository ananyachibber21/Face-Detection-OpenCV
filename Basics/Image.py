import cv2, time
img = cv2.VideoCapture(0, cv2.CAP_DSHOW)
check, frame = img.read()
print(check) #returns True or False in case of reading a python file
print(frame) #shows the frame in a form of matrix
time.sleep(10) #time delay for which the camera will be in on mode
cv2.imshow("capture", frame) #creates a separate window to capture the image
cv2.waitKey(0)
img.release()
cv2.destroyAllWindows()