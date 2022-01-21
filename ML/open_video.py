import cv2

# Open Video
# capture = cv2.VideoCapture('Computer Vision/Elon Musk 320.mp4')
capture = cv2.VideoCapture(0)

while True:
    # Read Frame
    _, frame = capture.read()
    cv2.imshow("Image", frame)

    # Esc button for closing window
    keyboard = cv2.waitKey(30 & 0xff)
    if keyboard == 27:
        break

capture.release()
