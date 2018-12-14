from time import sleep

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#Run1.py - Steps for Run 1 execution corresponding to pseuedo code. Check run diagram in website to match

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
    """
    1. Rotate right motor counterclockwise to rotate long pole attachment F to back of robot.
    2. Move robot forward with independent attachment on the front till white line is detected on the left color sensor. Wall hugger would release out of Jig 1 and class the West wall.
    3. Move robot slowly forward so that independent attachment is close enough to the ramp such that extension D lifts the end of ramp and allows Vehicle Payload to roll down. (M01-1 : 22 points)
    4. Move robot forward to align forklift C with crew payload and supply payload on top of ramp. (The solar panel should be in pushed out mode at this time using extension B. (M02-1: 18 points)
    5. Operate left motor clockwise to push forklift C down such that the payloads are on ramp
    6. Move robot backward till the crew and supply payload are free. (M01-2 : 14 + M01-3: 10 points)

    """
    Robot.robot_gyro.mode = Constants.MODE_GYRO_ANG
    #Robot.sound.speak('Executing Misson 1 and Mission 2')
    Robot.steer_pair.on_for_rotations(15, -45, 1.85)
    Robot.steer_pair.off()
    Robot.attachment_right.on_for_rotations(-20, 0.25)
    sleep(1)
    #Robot.steer_pair.on_for_rotations(0, -45, 0.15)
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
    while not (Robot.bottom_cl_left.reflected_light_intensity >= Constants.WHITE_LIGHT_INTENSITY): #If bottom left color sensor doesn’t sense white
        Robot.steer_pair.on(0,5) #Moves backward forever
    Robot.steer_pair.off()

    #Robot.sound.speak('Space Travel and solar panel accomplished')
    

def M05():
    """
    7.Move backward on path around such that robot back  with cage E is aligned to be on top of core site 
    8.Move robot backward to pull core samples out of shaft (M05-1 : 16 points)
    """
    #Robot.robot_gyro.mode = Constants.MODE_GYRO_ANG
    #Robot.sound.speak('Executing extraction mission')
    #Robot.steer_pair.on_for_rotations(0,25,1.9) #Moves back

    #move back with gyro
    #current_zero_angle=Robot.robot_gyro.angle
    
    Robot.steer_pair.on_for_rotations(0,12, 0.475)
    Robot.steer_pair.on_for_rotations(0,25,1.13) #Moves back
    Robot.steer_pair.off()

    Robot.steer_pair.off()
    #Robot.attachment_left.on_for_rotations(-100,8) # Forklift Rotates back to start place
    Robot.steer_pair.on_for_rotations(-50,15,0.89) #Rotates such that front is towards the wall
    Robot.steer_pair.off()
    #Robot.steer_pair.on_for_rotations(0, 20, 1.0125) #Moves to extraction
    #Robot.steer_pair.on_for_rotations(2, 20,1.005)
    #Robot.steer_pair.on_for_rotations(0, 20,2)
    #gyro
    
    Robot.steer_pair.on_for_rotations(0, 20,2) #Moves to extraction    
    Robot.steer_pair.off()
    sleep(0.5)
    Robot.steer_pair.on_for_rotations(0, 7.5, 1)
    Robot.steer_pair.off()

    #Robot.attachment_left.on_for_rotations(100,14)#Cage lowers
    #Robot.attachment_left.off()

    Robot.steer_pair.on_for_rotations(0, 25, 1.25) #Distance to travel for return before Gerhard
    Robot.steer_pair.off()
    sleep(0.5)
    #Robot.sound.speak('Extraction Mission accomplished')
    
def MO7_Gerhard():
    """
    9. Move back ward further till end of long pole F is positioned next to loop for Gerard.
    10. Rotate robot counter clockwise so that end of long pole F is able to light Gerard on loop
    11. Rotate right motor counter clockwise so that Gerard is picked up by long pole F and raised above the Air lock chamber
    12. Rotate robot clock clockwise so that Gerard is positioned above Airlock chamber
    13. Rotate right motor clockwise so that Gerard is lowered to the Airlock chamber and long pole F is not holding the loop
    14. Rotate robot counter clockwise so that long pole F releases loop. (M07-1:18 + M07-2: 4 points)
    """
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
    """
    15. Move robot forward on path back to base with all samples inside base. Gas core sample in base (M05-2 : 10 points)
    """
    #Robot.steer_pair.on_for_rotations(-15,15,1)
    Robot.right_wheel.on_for_rotations(15, 0.23)
    Robot.steer_pair.on_for_rotations(0.25,-50, 4)
    #Robot.attachment_left.on_for_rotations(-100,14)

#def run1_return():

def run1():
    """
    Execute Run 1 missions in order
    """
    #Reseting motors
    ResetRobot.reset_wheel_motors()
    ResetRobot.reset_attachment_motors()
    CalibrateRobot.calibrate_gyro()

    #mission M01 and M02 - space travel and solar panel
    M01_M02()
  
    #Mission M05- Extraction 
    if Robot.button.up:
        return
    M05()

    if Robot.button.up:
        return
    
    #Back to base before Gerhard 
    backup_return()

def execute_run1():
    """
    Main execute function for Run 1
    """
    #Robot.sound.speak('Executing Run1')
    run1()
