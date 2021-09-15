import cv2
img = cv2.imread("C:\\Users\\HP\\Pictures\\Saved Pictures\\beagle.jpg", 1) 

#prints the size of the image and the matrix
'''print(img) 
print(img.shape)''' 

#prints the resized image
'''resized = cv2.resize(img, (600,600))
cv2.imshow("Dog", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#prints the resized image halved
'''resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Dog", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#prints the resized image doubled
resized = cv2.resize(img, (int(img.shape[1]*2), int(img.shape[0]*2)))
cv2.imshow("Dog", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()



