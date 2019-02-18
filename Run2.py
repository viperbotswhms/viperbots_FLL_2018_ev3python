from time import sleep

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#Run2.py - Steps for Run 2 execution corresponding to pseuedo code. Check run diagram in website to match

import Robot
import Constants
import ResetRobot
import Gyro
import CalibrateRobot

def M06_TubeModule():
    '''
    1. Start robot 2A at angle pointing to Tube module missions till left color sensor detects white line
    2. Turn right motor till right sensor detect white line and move till tube module is aligned to space station and inserted and sticks. (M06-2 – 16 points)
    '''
    #Robot.sound.speak('Executing Mission 6 Tube Module')

    #Move forward to leave base
    steering, speed, rotation = -0.75,-40,3
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    '''
    # Move straight to Tube module using PID
    #setting gyro params
    Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
    
    current_value=Robot.robot_gyro.angle
    sleep(0.2)

    #Robot.steer_pair.on_for_rotations(0,-19.5,4.35)

    #trying gyro         
    #Gyro.gyro_mov_on_for_rotations(-19.5,2.3,current_zero_angle)

    Gyro.PID_reset()
    rotations=1
    delta_rotations=0.5
    while rotations <= 4 :
        steering = Gyro.PID_correction(0,current_value)
        Robot.steer_pair.on_for_rotations(steering,-35,delta_rotations)
        Robot.steer_pair.off()
        rotations=rotations+delta_rotations
    Robot.steer_pair.off()
    '''

    #Move forward to reach white line sensed on left sensor
    while not Robot.bottom_cl_left.reflected_light_intensity>=Constants.WHITE_LIGHT_INTENSITY:
        steering, speed = 0,-15
        Robot.steer_pair.on(steering, speed)
    Robot.steer_pair.off()

    #Pivot on left wheel to sense white line on right sensor
    while not Robot.bottom_cl_right.reflected_light_intensity>=Constants.WHITE_LIGHT_INTENSITY:
        speed = -5
        Robot.left_wheel.on(speed) 
    Robot.left_wheel.off()

    #Moves forward to push in tube
    steering, speed, rotation = 0,-5,0.6
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off() 
    sleep(0.2)   

    #Moves back to let tube settle without light sensing
    #Robot.steer_pair.on_for_rotations(0,5,0.68)
    #Robot.steer_pair.off() 

    #Moves back to let tube settle with light sensing on right sensor
    while not Robot.bottom_cl_right.reflected_light_intensity>=Constants.WHITE_LIGHT_INTENSITY:
        steering, speed = 0,5
        Robot.steer_pair.on(steering, speed)
    Robot.steer_pair.off()

    #Robot.sound.speak('Mission Tube Module accomplished')
    
def M04_CraterCrossing():
    '''
    3. Move backward in curve till back of robot is parallel to south wall and position is slightly away from front of crater crossing. 
    4. Move forward till plate 2C with vehicle 2D is aligned on top of crater crossing
    5. Operate left motor to release slip gear to push vehicle across crater crossing. (M04-1 – 20 points)

    '''
    #Robot.sound.speak('Executing Mission 4 Crater crossing')

    #Moves back slightly more
    steering, speed, rotation = 0,5,0.35
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    #turn perpendicular to extraction module for crater crossing
    steering, speed, rotation = -50,15,0.67
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off() 

    #Moves straight to align wheel to crater
    steering, speed, rotation = 0,-30,2.7
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    sleep(0.2)

    #Releases the kraken (wHEEL)
    speed, rotation = -100,1.5
    Robot.attachment_left.on_for_rotations(speed, rotation)
    Robot.attachment_left.off()

    #Robot.sound.speak('Crater crossing accomplished')
    
def M09_StrengthBar():
    '''
    6. Move robot 2A forward along path for front to be aligned to strength mission. Move forward to position 2B below strength bar
    7. Operate right motor to lift strength bar to top (M09-1 – 16 points)
    '''
    #Robot.sound.speak('Executing Mission 9 Strength Bar')

    #Angles and moves to hit north wall
    steering, speed, rotation = -26,-40, 2
    Robot.tank_pair.on_for_rotations(steering, speed, rotation)
    Robot.tank_pair.off()

    #Moves forward to go straigh to strength bar
    steering, speed, rotation = 0,-30,1.5
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    #Lifting Bar
    speed, rotation = 100,23
    Robot.attachment_right.on_for_rotations(speed, rotation)
    Robot.attachment_right.off()

    sleep(0.25)

    #Robot.sound.speak('Strength Bar accomplished')

def M03_3DPrinting():
    '''
    8. Move backward and angle by pressing against wall and using gyro sensor to 7 degrees. 
    9. Move back and angle in path to align to 3D Printer, ejecting red brick and dropping on the bottom plate. (M03-1 – 18 points)
    '''
    #Robot.sound.speak('Executing Mission 3 3d Printing')

    #Moves back without sensing
    #Robot.steer_pair.on_for_rotations(0, 50, 0.3)
    #Robot.steer_pair.off()

    #Moves back till left light sensor senses white line
    while not Robot.bottom_cl_left.reflected_light_intensity>=Constants.WHITE_LIGHT_INTENSITY:
        steering, speed = 0,20
        Robot.steer_pair.on(steering, speed)
    Robot.steer_pair.off()

    #Pivets on left wheel ; Value differs per table
    #Robot.right_wheel.on_for_rotations(50, 0.7) #0.7 rotations is fit for mat to wall gap 0.3mm
    #Robot.right_wheel.off()

    #Set up Gyro mode and reset
    CalibrateRobot.calibrate_gyro()
    
    '''
    #measure drift
    counter = 0
    while counter < 20:
        Robot.debug_print("Checking for drift : Value of gyro is :",Robot.robot_gyro.angle)
        counter = counter + 1
        sleep(0.3)
    '''

    current_value = Robot.robot_gyro.angle
    #Robot.debug_print("Current Value is :", current_value)
    while not Robot.robot_gyro.angle>= current_value+9:
        #Robot.debug_print("Value of gyro is :",Robot.robot_gyro.angle)
        #sleep(0.2)
        speed = 10
        Robot.right_wheel.on(speed)
    Robot.right_wheel.off()

    #Moves backwards
    steering, speed, rotation = 0,30,0.6
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()
    sleep(0.3)

    #Pivets the tiniest bit on right wheel
    speed, rotation = -10,0.14
    Robot.right_wheel.on_for_rotations(speed, rotation)
    Robot.right_wheel.off()

    '''
    #Robot.robot_gyro.mode = Constants.MODE_GYRO_ANG
    CalibrateRobot.calibrate_gyro()
    #measure drift
    counter = 0
    while counter < 20:
        Robot.debug_print("Checking for drift : Value of gyro is :",Robot.robot_gyro.angle)
        counter = counter + 1
        sleep(0.3)

    current_value = Robot.robot_gyro.angle
    Robot.debug_print("Current Value is :", current_value)
    while not Robot.robot_gyro.angle<=current_value-15:
        Robot.debug_print("Value of gyro is :",Robot.robot_gyro.angle)
        sleep(0.2)
        Robot.right_wheel.on(-1)
    Robot.right_wheel.off()
    '''

    #Moves forward to eject brick
    steering, speed, rotation = 0,30,1.3
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    #Robot.sound.speak('Mission 3d Printing Accomplished')

def M14_MeteoroidDeflection():
    '''
    10. Go on path aligning to push meteoroid (M14-1 – 12 points)
    '''
    #Robot.sound.speak('Executing Mission 14 Meteoroid Deflection')

    #Move forward from 3D printing
    steering, speed, rotation = 0,-20,1.25
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    #Curves to face South Wall
    left_speed, right_speed, rotation = 10,40,1.05
    Robot.tank_pair.on_for_rotations(left_speed, right_speed, rotation)
    Robot.tank_pair.off()

    #Curves to Angle front to Meteoroid
    left_speed, right_speed, rotation = 45,10,1.2
    Robot.tank_pair.on_for_rotations(left_speed, right_speed, rotation)
    Robot.tank_pair.off()

    #Move forward to hit the Meteoroid
    steering, speed, rotation = 0,-100,1.2
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    #Robot.sound.speak('Mission Meteoroid Deflection Accomplished')

def M06_ConeModule():
    '''
    11. Rotate and move robot backward such that 2G is aligned to cone module
    12. Move forward to position extractor 2G below cone module. 
    13. Rotate robot to Pull back cone module and move backward (M06-1 – 16 points)
    '''
    #Robot.sound.speak('Executing Mission 6 Cone Module')

    #Lowers Forklift down
    speed, rotation = -100,8
    Robot.attachment_right.on_for_rotations(speed, rotation)
    Robot.attachment_right.off()

    #Moves slightly forward
    steering, speed, rotation =  0,-15,0.8
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    #Pivets on right wheel to align grabber to Cone Module
    speed, rotation = 5,0.6
    Robot.left_wheel.on_for_rotations(speed, rotation)
    Robot.left_wheel.off()

    #Moves forward to grab Cone Module
    steering, speed, rotation = 0,-30,0.65
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    #Pivets on left wheel to get Cone out
    speed, rotation = 50,0.8
    Robot.right_wheel.on_for_rotations(speed, rotation)
    Robot.right_wheel.off()
        
    #Robot.sound.speak('Mission Cone Module Accomplished')

def return_to_base2():
    '''
    14. Move on path to base safely 
    '''
    #Go backwards straight
    steering, speed, rotation = 0,40,1.4
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    #Pivets on left wheel angling towards base
    speed, rotation = 20,0.6
    Robot.right_wheel.on_for_rotations( speed, rotation)
    Robot.right_wheel.off()

    #Move forward to be between Space Station and Extraction
    steering, speed, rotation = 0,50,1.8
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    #Turn towards base
    speed, rotation = 50,0.6
    Robot.left_wheel.on_for_rotations(speed, rotation)
    Robot.left_wheel.off()

    #Go forward towards base
    steering, speed, rotation = 0,50,4
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

def run2():
    """
    Execute Run 2 missions in order
    """    
    #CalibrateRobot.calibrate_gyro()
    ResetRobot.reset_attachment_motors()
    ResetRobot.reset_wheel_motors()
    CalibrateRobot.calibrate_gyro()
    
    #Mission M06 - Tube module
    M06_TubeModule()

    #Mission M04 - Crater Crossing
    M04_CraterCrossing()
    
    #Mission M09 - Strength Bar
    M09_StrengthBar()
    
    #Mission M03 - 3DPrinting
    M03_3DPrinting()
    
    #Mission M14 - Meteoroid Deflection
    M14_MeteoroidDeflection()

    #Mission M06 - Cone Module
    M06_ConeModule()

    #Return
    return_to_base2()

def execute_run2():
    #Robot.sound.speak('Executing Run2')
    run2()


