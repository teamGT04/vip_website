import cv2

# connect to camera
cap = cv2.VideoCapture(0)

# capture video frames
_, prev_frame = cap.read()
while True:
    ret, frame = cap.read()
    # compare frames for motion
    diff = cv2.absdiff(prev_frame, frame)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    # find contours in the thresholded image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # loop over the contours and draw rectangles around the moving objects
    for c in contours:
        if cv2.contourArea(c) > 500:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # take action if a large enough moving object is detected (e.g. sound an alarm or alert law enforcement)
    prev_frame = frame