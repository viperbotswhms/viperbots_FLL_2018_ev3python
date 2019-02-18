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

#Space Travel and solar panel mission
def M01_M02():
    '''
    1. Move robot forward with independent attachment on the front till white line is detected on the left color sensor. 
    2. Operate left motor to push kicker gear on C to push Wall hugger to hold to the West wall.
    3. Move robot slowly forward so that independent attachment is close enough to the ramp such that extension D lifts the end of ramp and allows Vehicle Payload to roll down. (M01-1 : 22 points)
    4. Move robot forward to align forklift C with crew payload and supply payload on top of ramp. (The solar panel should be in pushed out mode at this time using extension B. (M02-1: 18 points)
    5. Operate left motor clockwise to push forklift C down such that the payloads are on ramp
    6. Move robot backward till the crew and supply payload are free. (M01-2 : 14 + M01-3: 10 points)
    '''
    #Robot.sound.speak('Exexuting Mission Space Travel and Solar Panel')
    
    #Move forward till out of range of base and adjoining lamp pole
    steer, speed, rotation = 8, -60, 2.5
    Robot.steer_pair.on_for_rotations(steer, speed, rotation)
    Robot.steer_pair.off()

    #Set wall hugger on to table
    speed, rotation = -50, 0.1
    Robot.attachment_left.on_for_rotations(speed, rotation)
    Robot.attachment_left.off()
    sleep(0.5)
    
    #Move forward after wall hugger is activated   
    steer, speed, rotation = 0, -25, 1
    Robot.steer_pair.on_for_rotations(steer, speed, rotation)
    Robot.steer_pair.off()
    
    #Go forward till White Line is detected, and send first payload down the ramp
    while not (Robot.bottom_cl_left.reflected_light_intensity >= Constants.WHITE_LIGHT_INTENSITY):
        steer, speed = -1,-10
        Robot.steer_pair.on(steer, speed) #Moves forward forever
    Robot.steer_pair.off() #Stop the robot #dispatches blue payload
    sleep(1)
    
    #Move forward to align other two payloads on top of ramp and solar panel to be pushed out
    steer, speed, rotation = 0,-30,0.8
    Robot.steer_pair.on_for_rotations(steer, speed, rotation)
    Robot.steer_pair.off()

    #Lower Forklift down to set the two other payloads on ramp
    speed, rotation = 100, 8
    Robot.attachment_left.on_for_rotations(speed, rotation) 
    Robot.attachment_left.off()
    sleep(0.2)
    
    #Move backward to white line to set payloads free to go down ramp
    while not (Robot.bottom_cl_left.reflected_light_intensity >= Constants.WHITE_LIGHT_INTENSITY): #If bottom left color sensor doesn’t sense white
        steer, speed = 0, 5
        Robot.steer_pair.on(steer, speed) #Moves backward forever
    Robot.steer_pair.off()

    #Robot.sound.speak('Space Travel and solar panel accomplished')
    
def M05_M14():
    #Robot.sound.speak('Executing Mission Extraction and Meteoroid')
    '''
    7. Move backward on path around such that robot back  with cage E is aligned to be the core site and Move robot backward till near the core samples shaft. 
    8. Rotate right motor to have Sling attachment thrown meteoroid to target area (M14-2 : 12 points)
    9/ Move robot backward to pull core samples out of shaft (M05-1 : 16 points)
    '''

    #Move back from whiteline 
    steer, speed, rotation = 0,25,1.65
    Robot.steer_pair.on_for_rotations(steer, speed, rotation)
    Robot.steer_pair.off()

    #Rotate such that front is towards the wall and aligned to extraction
    steer, speed, rotation = -50,15,0.97
    Robot.steer_pair.on_for_rotations(steer, speed, rotation)
    Robot.steer_pair.off()
    '''
    #Set up Gyro mode and reset
    CalibrateRobot.calibrate_gyro()
    
    #measure drift
    counter = 0
    while counter < 20:
        Robot.debug_print("Checking for drift : Value of gyro is :",Robot.robot_gyro.angle)
        counter = counter + 1
        sleep(0.3)

    current_value = Robot.robot_gyro.angle
    #Robot.debug_print("Current Value is :", current_value)
    while not Robot.robot_gyro.angle>= current_value+84:
        #Robot.debug_print("Value of gyro is :",Robot.robot_gyro.angle)
        #sleep(0.2)
        steer, speed = -50,4
        Robot.steer_pair.on(steer, speed)
    Robot.right_wheel.off()
    '''

    #Move to extraction module
    steer, speed, rotation = 0, 25,2.2
    Robot.steer_pair.on_for_rotations(steer, speed, rotation)
    Robot.steer_pair.off()  
    sleep(0.2)

    #Rotate Right meteorite holder to throw ball to target.
    speed, rotation = -25,0.3
    Robot.attachment_right.on_for_rotations(speed, rotation) #Throws Ball 
    Robot.steer_pair.off()
    sleep(0.2)
    #Robot.sound.speak('Meteoroid Mission accomplished')
   
    #Move Forward
    steer, speed, rotation = 0,6,1.9
    Robot.steer_pair.on_for_rotations(steer, speed, rotation)
    Robot.steer_pair.off()

    #Move forward to clear off extraction module
    steer, speed, rotation = 0, 35, 0.6
    Robot.steer_pair.on_for_rotations(steer, speed, rotation) #Distance to travel for return before Gerhard
    Robot.steer_pair.off()
    #Robot.sound.speak('Extraction Mission accomplished')

def return_to_base1():
    '''
    10. Turn robot towards base and move to base with all samples inside base. Gas core sample in base (M05-2 : 10 points)
    '''

    #Robot.sound.speak('Go back to base with core modules')
    #Turn back towards base
    speed, rotation = 15, 0.4
    Robot.right_wheel.on_for_rotations(speed, rotation)
    Robot.right_wheel.off()
    
    #Move backward to base
    steer, speed, rotation = 0.25,-50, 3
    Robot.steer_pair.on_for_rotations(steer, speed, rotation)
    Robot.steer_pair.off()
    
    #Turn to align along side base wall
    speed, rotation = -15,0.2
    Robot.right_wheel.on_for_rotations(speed, rotation)
    Robot.right_wheel.off()

    #Move backward so that robot with extracted core modules are in base.
    steer, speed, rotation = 0,-50,1.5
    Robot.steer_pair.on_for_rotations(steer, speed, rotation)
    Robot.steer_pair.off()

    #Robot.sound.speak('Reached base with core modules')

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
    M05_M14()

    #Back to base before Gerhard (Remove comment if necessary)
    return_to_base1()

    # Must delete for competition.. This is to set up forklift to repeat run.
    Robot.attachment_left.on_for_rotations(-100, 8) #Raises Forklift 

    
def execute_run1():
    #Robot.sound.speak('Executing Run1')
    run1()
