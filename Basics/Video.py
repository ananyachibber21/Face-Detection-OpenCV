import cv2, time
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
a = 1
while True:
    a=a+1
    check, frame = video.read()
    print(frame)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capture", gray_img)
    key = cv2.waitKey(1) #creates a new frame after every 1 milli second
    if key == ord("q"): 
        break #breaks the loop when q is pressed from the keyboard
print(a) #prints the number of frames
video.release()
cv2.destroyAllWindows()
