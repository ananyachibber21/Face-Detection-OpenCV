
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

![Screenshot-4](https://user-images.githubusercontent.com/72216605/133551258-d5fe1446-d89b-45ab-97c0-a03b9033533e.PNG)


2. Difference Frame: Difference frame shows the difference of intensities of first frame to the current frame. 

![Screenshot-2](https://user-images.githubusercontent.com/72216605/133551163-3f5c0905-0b3c-471c-b4b3-21e68876c85d.PNG)

3. Threshold Frame: If the intensity difference for a particular pixel is more than 30(in my case) then that pixel will be white and if the difference is less than 30 that pixel will be black.

![Screenshot-3](https://user-images.githubusercontent.com/72216605/133551213-42ee2a37-abec-4e37-a4b3-b8b4b792bff1.PNG)

4. Color Frame: In this frame, you can see the color images in color frame along with green contour around the moving objects.

![Screenshot-1](https://user-images.githubusercontent.com/72216605/133551114-d0724cd6-e7b3-43a0-a816-c05a6cdfa8c7.PNG)

The time of the occurence of an object will be recorded in Times.csv file. This will record the start and the end time of the motion. 

![Time-Interval](https://user-images.githubusercontent.com/72216605/133551317-eb05f7f7-6a9e-419d-bb0f-3cc4347dbccf.PNG)

A more clear vision is observed when you will be able to see a bokeh graph appear in a separate browser tab after pressing q and closing the 4 windows.

![Screenshot-5](https://user-images.githubusercontent.com/72216605/133551351-5e4dfd3a-f57f-4240-b0d9-b78666db5936.PNG)

### References

[Edureka](https://www.youtube.com/watch?v=-ZrDjwXZGxI)<br />
[Geeksforgeeks](https://www.geeksforgeeks.org/webcam-motion-detector-python/)