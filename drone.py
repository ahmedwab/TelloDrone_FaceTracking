from djitellopy import Tello


class Drone:

    tello = Tello()
    def __init__(self):
        self.tello.connect()
        self.tello.streamon()
    
   
    def getFrame(self):
        """
        getFrame gets video frame from the drone
        :return: tello's frame read
        """ 
        return self.tello.get_frame_read().frame
    def getVideo(self):
        """
        getVideo gets video capture from the drone
        :return: tello's video
        """ 
        return self.tello.get_video_capture()
    def getBattery(self):
        """
        getBattery gets battery percentage from the drone
        :return: int value of percentage
        """ 
        return self.tello.get_battery()
    
        
    def getState(self):
        """
        getState gets current state of the drone
        :return: state value of drone
        """ 
        return self.tello.get_current_state()

    def first_tracking_position(self):
        """
        first_tracking_position allows the drone to takeoff and go up 80 cm
        """ 
        self.tello.takeoff()
        self.tello.move_up(80)
     
            

    def adjust(self,x_faceCenter,y_faceCenter,x_center,y_center):

        """
        adjust function adjusts movement to center face image in the center 
        :param x_faceCenter: int value of center of face x coordinate
        :param y_faceCenter: int value of center of face y coordinate
        :param x_center: int value of center of face x coordinate
        :param y_center: int value of center of face y coordinate
 
        """ 
       
        x_difference = x_faceCenter-x_center
        y_difference = y_faceCenter-y_center

        area = x_faceCenter * y_faceCenter

        print(x_difference, y_difference, area)
    
        x_state = True
        y_state = True
        area_state = True

        if(x_difference == 0):
            x_state = False
        if(y_difference == 0):
            y_state = False
        if(area == 0):
            area_state = False

        if not -120 <= x_difference <= 120 and x_state == True:
            if x_difference < 0:
                print("rotating counter clockwise")
                self.tello.rotate_counter_clockwise(15)
            elif x_difference > 0:
                print("rotating  clockwise")
                self.tello.rotate_clockwise(15)
        
        if not 90000 <= area <= 165000 and area_state == True:

            if area >200000:
                self.tello.move_back(50)
                print("moving back 20")
            elif area < 90000:
                self.tello.move_forward(50)
                print("moving forward 20")
        if not -70 <= y_difference <= 70 and y_state == True:

            if y_difference >0:
                self.tello.move_down(20)
                print("moving down 20")
            elif y_difference < 0:
                self.tello.move_up(20)
                print("moving up 20")
         
            
        

    #closes the drone connection and lands it
    def close(self):
        self.tello.land()
        self.tello.end()
           
        
    
        


