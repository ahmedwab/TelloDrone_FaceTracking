import cv2
from djitellopy import Tello
from drone import Drone


# Initializing the drone from the drone class
drone = Drone()

drone.first_tracking_position()
# Creating the cascade objects
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:

    #Receiving each individual frame from the drone
    frame = drone.getFrame()

    #Receiving video capture from the drone
    video_capture = drone.getVideo()

    #Values retrieved from the video stream
    height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    
   #Creating a rectangle object around faces recognized
    x_center = int(width/2)
    y_center = int(height/2)
    center =  (x_center,y_center)
    cv2.circle(frame, center, 20, (0, 255, 0))

    #Receiving facial images 
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected = face_cascade.detectMultiScale(image=image, scaleFactor=1.3, minNeighbors=4)
    for (x, y, faceWidth, faceHeight) in detected:

        #Creating a rectangle objext around faces recognized
        cv2.rectangle(frame,(x, y),(x + faceWidth, y + faceHeight),(52, 235, 149),thickness=3)

        #Creating a center circle for face object
        x_faceCenter = x + int(faceWidth/2)
        y_faceCenter = y + int(faceHeight/2)
        faceCenter  =  (x_faceCenter,y_faceCenter)
        cv2.circle(frame, faceCenter, 20, (0, 255, 0))

        drone.adjust(x_faceCenter,y_faceCenter,x_center,y_center)


    cv2.imshow('Tello Face Detection', frame)
    if cv2.waitKey(1) == ord('q'):
        break

drone.close()
cv2.destroyAllWindows()