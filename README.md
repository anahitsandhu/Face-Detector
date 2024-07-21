# Face-Detector
This is a project made in the virtual environment of venv to make a face detector. You should have a functional webcam for this project. It imports cv2 and uses Haar cascade claasifier for face detection. It uses an XML file haarcascade_frontalface_default.xml that contains pre-trained model for detecting frontal faces. 
One your webcam detects a face, it is surrounded by a blue rectangle. Multiple faces can be detected as once. It has a scalefactor of 1.3 to detect faces of different sizes and it has a minNeighbours paramter to reduce false positive, minNeighbours refers to the number of rectangles that should be overlapping for it to be detected as a face, in this code it's 5.
You can press 'q' to release the camera
Make sure that the place is well-lit before running the code.
