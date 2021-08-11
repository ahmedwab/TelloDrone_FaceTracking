from djitellopy import Tello


class Drone:

    tello = Tello()
    def __init__(self):
        self.tello.connect()
        self.tello.streamon()
    
   
    def getFrame(self):
        return self.tello.get_frame_read().frame
    def getVideo(self):
        return self.tello.get_video_capture()
    def getBattery(self):
        return self.tello.get_battery()
    
    def getFlightTime(self):
        return self.tello.get_flight_time()
    
    def getState(self):
        return self.tello.get_current_state()

    def first_tracking_position(self):
        self.tello.takeoff()
        self.tello.move_up(80)
     
            

    def adjust(self,x_faceCenter,y_faceCenter,x_center,y_center):
       
        x_difference = x_faceCenter-x_center
        y_difference = y_faceCenter-y_center

        area = x_faceCenter * y_faceCenter

        print(x_difference, y_difference, area)
    
        x_state = True
        y_state = True
        area_state = True

        if(x_difference == 0):
            x_state ==False
        if(y_difference == 0):
            y_state ==False
        if(area == 0):
            area_state ==False

        if not -120 <= x_difference <= 120 and x_state == True:
            if x_difference < 0:
                print("rotating counter clockwise")
                self.tello.rotate_counter_clockwise(15)
            elif x_difference > 0:
                print("rotating  clockwise")
                self.tello.rotate_clockwise(15)
        
       
        if area < 70000:
            self.tello.move_forward(80)
            print("moving forward")
        
         
        elif area < 90000:
            self.tello.move_forward(100)
            print("moving forward")
    
    def close(self):
        self.tello.land()
        self.tello.end()
           
        
    
        


