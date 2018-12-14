from time import sleep

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#Run3.py - Steps for Run 3 execution corresponding to pseuedo code. Check run diagram in website to match

import Robot
import Constants
import ResetRobot
import Gyro
import CalibrateRobot

#M13- observatory

def M13_Observatory():
    """
    1. Rotate right motor counter clockwise to raise the lever 3C upward after getting out of base (to counter 12” height rule)
    2. Move robot eastward forward till white line is detected on the right color sensor. Jerk motion at the start should push the vertical lever of attachment 3E forward and fall
    3. Move forward till edge of escape velocity. The Observatory arm should be pushed at this time to orange bar (M13 – 1,2,3 – 16 +2+2 points)

    """
    #Robot.sound.speak('Exexuting Mission 13 observatory')

    #wall hugger gear
    Robot.attachment_right.on_for_rotations(75, 0.5)#11/30/2018 7:42
    Robot.steer_pair.off
    sleep(0.3)
    
    #Robot.attachment_right.on_for_rotations(-75,0.5)
    #Move foraward until outside of base for mesasuring white line
    Robot.steer_pair.on_for_rotations(0,-100,3) 
    Robot.steer_pair.off()
    sleep(0.25)

    #applying correction for drift for moving forward until white lne detected
    #Gyro.gyro_mov_straight_until_white_right(-15)
    while not (Robot.bottom_cl_right.reflected_light_intensity >= Constants.WHITE_LIGHT_INTENSITY): #11/30/2018
        Robot.steer_pair.on(0,-25)
    #Robot.sound.speak('First White Line Detected')
    Robot.steer_pair.on_for_rotations(0,-15,0.35) #move forward a little
    Robot.steer_pair.off()
    Robot.steer_pair.on_for_rotations(0, -10, 0.1)
    Robot.steer_pair.off() #stop
    #Robot.sound.speak('Mission 13 Observatory accomplished')

#M11 -Escape Velocity

def M11_EscapeVelocity():
    """
    4. Move back till white line is detected on right color sensor and enough to align striker to hit space craft mission
    5. Rotate right motor clockwise so that lever 3C hits striker with enough force to push space craft on top (M11-1-24 points). Raise lever 3C to full height.

    """
    #Robot.sound.speak('Executing escape velocity')
    Robot.steer_pair.on_for_rotations(0,20,0.38) #move back a little
    Robot.steer_pair.off() #stop
    sleep(0.25)

    #smaaashing
    Robot.attachment_left.on_for_rotations(100,1.5)
    Robot.attachment_left.off()
    sleep(0.5)
    Robot.attachment_left.on_for_rotations(-100,1)
    Robot.attachment_left.off()
    #Robot.sound.speak('Escape velocity accomplished')

#M10 - Food production
def M10_FoodProduction():
    """
    6. Turn ~60 degrees counter clock wise (use gyro sensor) and go forward till right color sensor detects white line 
    7. Turn ~120 degrees clockwise (use gyro sensor) such that Arm C is pointing to striker and robot A is in the middle
    8. Move backward such that both wheels are aligned parallel to the top part of T line, using color sensor and alignment movement.
    9. Slowly move further lower part of bar D pushes bar till grey is dropped after green but before tan (M10-1: 16 points)
    """
    #Robot.sound.speak('Mission food production')
    Robot.steer_pair.on_for_rotations(0,20,0.38) #move back a little
    Robot.steer_pair.off() #stop
    sleep(0.25)

    Robot.left_wheel.on_for_rotations(-20,0.5) #turn 45 degrees
    Robot.steer_pair.off()
    while not (Robot.bottom_cl_left.reflected_light_intensity >=Constants.WHITE_LIGHT_INTENSITY):
        Robot.steer_pair.on(0,-30)    
    Robot.steer_pair.off()
    #Robot.sound.speak('Second White line detected')

    #aligning to food production
    #Robot.steer_pair.on_for_rotations(0,-15,0.85) 26 Nov
    Robot.steer_pair.on_for_rotations(0,-15,1.13) #was 1.14
    Robot.steer_pair.on_for_rotations(50,30,1.3) #was1.35

    #executing food production
    #Robot.steer_pair.on_for_rotations(0,10,0.6) $29nov 5.53pm
    Robot.steer_pair.on_for_rotations(0,10,0.7) #0.6 OG Rotate
    Robot.steer_pair.off()
    #Robot.sound.speak('Mission 10 food production completed')

def M11_EscapeVelocity_PostFoodProduction():
    """
    6. Turn ~60 degrees counter clock wise (use gyro sensor) and go forward till right color sensor detects white line 
    7. Turn ~120 degrees clockwise (use gyro sensor) such that Arm C is pointing to striker and robot A is in the middle
    8. Move backward such that both wheels are aligned parallel to the top part of T line, using color sensor and alignment movement.
    9. Slowly move further lower part of bar D pushes bar till grey is dropped after green but before tan (M10-1: 16 points)
    """

    Robot.steer_pair.on_for_rotations(0,-25,0.95)
    Robot.steer_pair.off
    #smaaashing
    #Robot.attachment_left.on_for_rotations(-100,0.5)
    #Robot.attachment_left.off()
    sleep(0.3)
    Robot.attachment_left.on_for_rotations(100,1.3)
    Robot.attachment_left.off()
    sleep(0.5)
    Robot.attachment_left.on_for_rotations(-100,2)
    Robot.attachment_left.off()
    sleep(0.5)
    #Robot.sound.speak('Escape velocity accomplished')bot


#M15 - Lander
def M15_Lander():
    """
    10. Move forward and Rotate clockwise ~30 degrees such that bar D is pointing to  Lander module.
    11. Move robot A backward such that lander mission bar is pushed and the lander is rested on to of box B.
    12. Move robot A back to base with lander (M15-1 : 16 points)

    """
    #moving away from food production
    Robot.steer_pair.on_for_rotations(0,-20,1.35)

    #turn towards right 45 degrees
    #Robot.right_wheel.on_for_rotations(-27,0.38)
    #Robot.right_wheel.on_for_rotations(-30,0.60)
    Robot.right_wheel.on_for_rotations(-27,0.45)
    Robot.right_wheel.off()

    #move back straight
    Robot.steer_pair.on_for_rotations(0,20,6)
    Robot.steer_pair.off()

    #Robot.sound.speak('Mission 15 lander completed')

#M15 - Lander
def M12_SatelliteOrbits():
    """
    Back up plan : 
    Have Satellites V and C hooked to either sides of the box 3B. 
    As step 16, move forward such that satellites are over the outer orbit from base (M12-2 : 16 points)
    Use robot to move Satellite X to outer orbit (M12-1 – 8 points)
    """
    
    #moving away from escape velocity
    #Robot.steer_pair.on_for_rotations(0,25,0.1)
    #Robot.steer_pair.off()

    #turn towards right 45 degrees
    #Robot.right_wheel.on_for_rotations(-27,0.38)
    #Robot.right_wheel.on_for_rotations(-30,0.60)
    #Robot.right_wheel.on_for_rotations(-27,0.45)
    Robot.right_wheel.on_for_rotations(-30,0.45)
    Robot.right_wheel.off()

    #move back straight
    Robot.steer_pair.on_for_rotations(0,40,2.3)
    Robot.steer_pair.off()

    #move satellitiles between blluseline
    #Robot.left_wheel.on_for_rotations(25,1.15) 29 nov 7.00pm
    Robot.left_wheel.on_for_rotations(25,1.1)
    Robot.left_wheel.off()

    #Robot.sound.speak('Mission 15 lander completed')

def M01_SolarPanel_2():
    """
    Backup Plan :
    Rotate lever 3C to height other team solar panel an push out (M2-2 – 22 points)
    """
    #Robot.attachment_left.on_for_rotations(25,0.9)
   # Robot.attachment_left.off()
    sleep(0.25)
    Robot.steer_pair.on_for_rotations(0,-20,0.6)
    Robot.steer_pair.off()

#Returning to base

def M08_AerobicExercise():
    """
    Backup Plan :
    Turn towards aerobics mission and use lever 3C to hit till end (M08-1/2/3 – 22 points)
    Ensure that that satellites are over the outer orbit from base (M12-2 : 16 points)
    Stay at Base
    """
    n = 0
    Robot.steer_pair.on_for_rotations(0, 5, 0.15)
    Robot.steer_pair.off()
    Robot.tank_pair.on_for_rotations(-40,-20,0.7)
    Robot.steer_pair.on_for_rotations(0,10,0.02 )
    Robot.steer_pair.off()
    Robot.attachment_left.on_for_rotations(50, 1)
    Robot.attachment_left.on_for_rotations(-50, 0.8)
    while True:
        Robot.attachment_left.on_for_rotations(50, 0.8)
        Robot.attachment_left.on_for_rotations(-50, 0.8)
        n = n + 1
    Robot.attachment_left.off()
    #Robot.attachment_left.on_for_rotations()


#Returning to base
def run2_returnbase():
    """
    12. Move robot A back to base with lander (M15-1 : 16 points)
    """

    #Robot.sound.speak('Returning to base')
    #while not Robot.bottom_cl_right.reflected_light_intensity >= Constants.WHITE_LIGHT_INTENSITY :
        #Robot.steer_pair.on(0,-30)
    Robot.steer_pair.on_for_rotations(0,-30,1.5)
    Robot.steer_pair.off()
    
    #rotate to left 10 degrees
    #Robot.left_wheel.on_for_rotations(15,0.5)
    #Robot.left_wheel.on_for_rotations(15,0.1)

    #go straight
    #Robot.steer_pair.on_for_rotations(0,-15,2.6)
    #turn right
    #Robot.tank_pair.on_for_rotations(-15,-25,0.3)

    #straight to base
    #Robot.steer_pair.on_for_rotations(0,-30,5)


#function to execute the run2 mission plan
def run3():
    """
    Execute Run 3 missions in order
    """    
    #Resetting the motors
    ResetRobot.reset_wheel_motors()
    ResetRobot.reset_attachment_motors()
    CalibrateRobot.calibrate_gyro()

    #M13 -Observatory
    M13_Observatory()

    #M11 - Escape velocity
    #M11_EscapeVelocity()

    #M10 - Food Production
    M10_FoodProduction()

    #M15 - Lander
    #M15_Lander()

    #M11- Escape velocity after food production
    M11_EscapeVelocity_PostFoodProduction()

    #M12 - Satellite orbits
    M12_SatelliteOrbits()

    #M01 - Opposite table satellites
    M01_SolarPanel_2()

    #M08 - Aerobic Exercise
    M08_AerobicExercise()

    #Returning to base
    #run2_returnbase()


    
#function that will be called from other modules
def execute_run3():
    """
    Main execute function for Run 2
    """
    #Robot.sound.speak('Executing Run3')
    run3()