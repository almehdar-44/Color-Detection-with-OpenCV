# Red Color Detection with OpenCV

## Description
This Python project uses OpenCV to detect red-colored objects in real-time from your webcam feed.  
It processes video frames, isolates red regions using HSV color space filtering, and displays both the original frame and the detected red areas.

## How to Use
1. Make sure you have Python 3 installed on your system.
2. Install required libraries:
   ```
   pip install opencv-python numpy
   ```
3. Run the Python script:
   ```
   python your_script_name.py
   ```
4. A window showing the webcam feed and another showing detected red areas will open.
5. Press **q** to quit the application.

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)
- Numpy

## Notes
- The detection works by filtering the HSV color range corresponding to red.
- You can modify the HSV range in the script to detect other colors.

---

