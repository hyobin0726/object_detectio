import cv2

webcam = cv2.VideoCapture(0)  
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_file = "/home/pi/video/output.avi"
frame_rate = 30.0
resolution = (640, 480)
output = cv2.VideoWriter(output_file, fourcc, frame_rate, resolution)

capture_time = 5 
end_time = cv2.getTickCount() + (capture_time * cv2.getTickFrequency())

while cv2.getTickCount() < end_time:
    ret, frame = webcam.read()
    if ret:
        cv2.imshow("Webcam", frame)
        output.write(frame)
        if cv2.waitKey(1) == ord("q"):
            break
    else:
        break
webcam.release()
output.release()
cv2.destroyAllWindows()
