from time import sleep

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#Run1.py - Steps for Run 1 execution corresponding to pseuedo code

#Import statements 
import Robot
import Constants
import ResetRobot
import Gyro
import CalibrateRobot

#Assigning modes for the color sensor to Reflect
Robot.top_cl.mode = Constants.MODE_COL_REFLECT
Robot.bottom_cl_right.mode = Constants.MODE_COL_REFLECT
Robot.bottom_cl_left.mode = Constants.MODE_COL_REFLECT

#Defining functions for each mission to be executed

#Payload and solar panel mission
def M01_M02():
    Robot.robot_gyro.mode = Constants.MODE_GYRO_ANG
    #Robot.sound.speak('Executing Misson 1 and Mission 2')

    Robot.attachment_right.on_for_rotations(-20, 0.25)
    #Robot.sound.speak('Starting Now')
    #Robot.tank_pair.on_for_rotations(-45, -60, 1)
    #Robot.tank_pair.on_for_rotations(-30, -15, 1) #Tank pair'solution'
    Robot.steer_pair.on_for_rotations(0, -45, 2)
    #current_zero_angle=Robot.robot_gyro.angle
    #Gyro.gyro_mov_on_for_rotations(-25,2,current_zero_angle)
    Robot.steer_pair.on_for_rotations(0, -25,1)
    while not (Robot.bottom_cl_left.reflected_light_intensity >= Constants.WHITE_LIGHT_INTENSITY): #If bottom left color sensor doesn’t sense white
        Robot.steer_pair.on(-1,-10) #Moves forward forever
    #Gyro.gyro_mov_straight_until_white_left(-35)
    Robot.steer_pair.off()
    #Robot.sound.speak('White detected')#sends first payload down
    Robot.steer_pair.off() #Stop the robot #dispatches blue payload
    sleep(1)
    Robot.steer_pair.on_for_rotations(0,-15,0.5)#moves fwd a bit to lower forklift
    Robot.steer_pair.off()
    Robot.attachment_left.on_for_rotations(100, 8) #Lowers Forklift down to set the two other payloads
    Robot.attachment_left.off()
    sleep(0.2)
    #Robot.sound.speak('Space Travel and solar panel accomplished')
    

#Extraction

def M05_trial():
    #Robot.sound.speak('Executing extraction mission')
    #Robot.steer_pair.on_for_rotations(0,25,1.84) #Moves back
    #Robot.steer_pair.off()
    #Robot.steer_pair.on_for_rotations(-50,15,0.869)
    #Robot.steer_pair.off()
    #Robot.steer_pair.on_for_rotations(0, 20, 3.05)
    pass


def M05():
    Robot.robot_gyro.mode = Constants.MODE_GYRO_ANG
    #Robot.sound.speak('Executing extraction mission')
    #Robot.steer_pair.on_for_rotations(0,25,1.9) #Moves back

    #move back with gyro
    #current_zero_angle=Robot.robot_gyro.angle
    Robot.steer_pair.on_for_rotations(0,25,1.9) #Moves back
    Robot.steer_pair.off()

    Robot.steer_pair.off()
    Robot.attachment_left.on_for_rotations(-100,8) # Forklift Rotates back to start place
    Robot.steer_pair.on_for_rotations(-50,15,0.8555) #Rotates such that front is towards the wall
    Robot.steer_pair.off()
    #Robot.steer_pair.on_for_rotations(0, 20, 1.0125) #Moves to extraction
    #Robot.steer_pair.on_for_rotations(2, 20,1.005)
    #Robot.steer_pair.on_for_rotations(0, 20,2)
    #gyro
    
    Robot.steer_pair.on_for_rotations(1, 20, 2.75) #Moves to extraction
    #Gyro.gyro_mov_on_for_rotations(20,2,current_zero_angle)
    Robot.steer_pair.off()

    Robot.attachment_left.on_for_rotations(100,10)#Cage lowers
    Robot.attachment_left.off()
    Robot.steer_pair.on_for_rotations(0, 25, 1) #Distance to travel for return before Gerhard
    Robot.steer_pair.off()
    #Robot.sound.speak('Extraction Mission accomplished')
    


def MO7_Gerhard():
    #Robot.sound.speak('Lets save gerhard')
    Robot.attachment_right.on_for_rotations(-15, 0.7) #Lifts hook
    Robot.steer_pair.on_for_rotations(0, 15, 0.5) #Moves teensy bit forward
    Robot.steer_pair.off()
    Robot.tank_pair.on_for_rotations(0, 10, 0.4) #Rotates so that hook gets Gerhard
    Robot.tank_pair.off()
    Robot.attachment_right.on_for_rotations(15, 0.5) #lifts hook slightly
    Robot.tank_pair.on_for_rotations(0,-15, 0.5) #Pivets back a bit
    Robot.tank_pair.off()
    Robot.steer_pair.on_for_rotations(0, 1, 0.05) #Moves forward a teensy bit
    Robot.steer_pair.off()
    Robot.attachment_right.on_for_rotations(-15, 0.5) #Hook lowers
    Robot.tank_pair.on_for_rotations(0, 10, 0.5)
    Robot.tank_pair.off()
    Robot.steer_pair.on_for_rotations(0,10, 1)
    Robot.steer_pair.off()
    #Robot.sound.speak('I saved Gerhard')

def backup_return():
    #Robot.steer_pair.on_for_rotations(-15,15,1)
    Robot.left_wheel.on_for_rotations(-15, 0.25)
    Robot.steer_pair.on_for_rotations(0,-50, 4)
    Robot.attachment_left.on_for_rotations(-100,10)

#def run1_return():

def run1():
    #Reseting motors
    ResetRobot.reset_wheel_motors()
    ResetRobot.reset_attachment_motors()
    CalibrateRobot.calibrate_gyro()

    #mission M01 and M02 - space travel and solar panel
    M01_M02()
  
    #Mission M05- Extraction 
    M05()
    
    #Back to base before Gerhard (Remove comment if necessary)
    backup_return()


    
   





   

def execute_run1():
    Robot.sound.speak('Executing Run1')
    run1()
