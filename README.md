
This Python Program allows to detect any motion occuring in the webcam and records the time interval for which the object was in front of the screen using a Bokeh graph.

## Installation

Before writing the code make sure you have OpenCV installed in your environment. You can follow the steps to install OpenCV and some other additional libraries required to work with this project:

### OpenCV

pip install opencv-python<br />
pip install opencv-python-headless<br />
pip install opencv-contrib-python

### pandas

pip install pandas

### bokeh

pip install bokeh

## How to use the code

*Basics(Folder)*: This contains the basics of how to apply Computer Vision on images and videos (This is not a part of the project and is only for understanding purposes).

*FaceDetection(Folder)*: This contains a sample code of face detection using python (This is not a part of the project and is only for understanding purposes).

*Motion_Detection.py(File)*: This contains the main code for the project. It will scan the object that comes in front of the webcam neglecting the extra disturbances like shadows, insects or any small creatures by using the concept of background subtraction.

*Graph.py(File)*: This python code allows to record the time interval for which object stayed in front of the webcam. The time is recorded in the form of a graph using the bokeh module.

## Results

After running the final code, you will observe 4 windows opening at the same time, These are:

1. Gray Frame: In Gray frame the image is a bit blur and in grayscale we did so because, In gray pictures there is only one intensity value whereas in RGB(Red, Green and Blue) image thre are three intensity values. So it would be easy to calculate the intensity difference in grayscale. 

2. Difference Frame: Difference frame shows the difference of intensities of first frame to the current frame. 

3. Threshold Frame: If the intensity difference for a particular pixel is more than 30(in my case) then that pixel will be white and if the difference is less than 30 that pixel will be black.

4. Color Frame: In this frame, you can see the color images in color frame along with green contour around the moving objects.

The time of the occurence of an object will be recorded in Times.csv file. This will record the start and the end time of the motion. 

![Time-Interval](https://user-images.githubusercontent.com/72216605/133551317-eb05f7f7-6a9e-419d-bb0f-3cc4347dbccf.PNG)

A more clear vision is observed when you will be able to see a bokeh graph appear in a separate browser tab after pressing q and closing the 4 windows.

![Screenshot-5](https://user-images.githubusercontent.com/72216605/133551351-5e4dfd3a-f57f-4240-b0d9-b78666db5936.PNG)

### References

[Edureka](https://www.youtube.com/watch?v=-ZrDjwXZGxI)<br />
[Geeksforgeeks](https://www.geeksforgeeks.org/webcam-motion-detector-python/)