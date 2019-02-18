from time import sleep

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#Run3.py - Steps for Run 3 execution corresponding to pseuedo code. Check run diagram in website to match

import Robot
import Constants
import ResetRobot
import Gyro
import CalibrateRobot

from time import sleep

#M13- observatory
def M13_Observatory():
    '''
    1. Rotate right motor counter clockwise to raise the lever 3C upward after getting out of base and pushing wall hugger to latch to the south wall
    2. Move robot eastward forward till outside of base and stop for jerk motion at the start should push the vertical lever of attachment 3E forward and fall
    3. Move forward till white line is detected and then till edge of escape velocity. The Observatory arm should be pushed at this time to orange bar (M13 – 1,2,3 – 16 +2+2 points)
    '''
    #Robot.sound.speak('Exexuting Mission 13 observatory')

    #wall hugger gear
    speed, rotation = 75, 0.2
    Robot.attachment_right.on_for_rotations(speed, rotation)
    Robot.attachment_right.off()
    sleep(0.3)
    
    #Move forward until outside of base for mesasuring white line
    steering, speed, rotation = 0,-100,3
    Robot.steer_pair.on_for_rotations(steering, speed, rotation) 
    Robot.steer_pair.off()

    #Lift right lever attachment
    speed, rotation = -60, 0.70
    Robot.attachment_right.on_for_rotations(speed, rotation)
    sleep(0.1)

    #Go forward till White Line is detected
    while not (Robot.bottom_cl_right.reflected_light_intensity >= Constants.WHITE_LIGHT_INTENSITY): #11/30/2018
        steering, speed = 0,-25
        Robot.steer_pair.on(steering, speed)
    #Robot.sound.speak('First White Line Detected')
        
    #Move forward a little to have the Observatory hit Orange
    steering, speed, rotation = 0,-15,0.35
    Robot.steer_pair.on_for_rotations(steering, speed, rotation) 
    Robot.steer_pair.off()
    steering, speed, rotation = 0,-10,0.1
    Robot.steer_pair.on_for_rotations(steering, speed, rotation) 
    Robot.steer_pair.off()

    #Robot.sound.speak('Mission 13 Observatory accomplished')

#M11- Escape Velocity
def M11_EscapeVelocity():
    '''
    4. Move back till white line is detected on right color sensor. Weight on column of 3E would fall with enough force to push space craft on top (M11-1-24 points). 
    '''
    #Robot.sound.speak('Mission Escape Velocity')

    #Move back a little to release the weight on top of Escape Velocity
    steering, speed, rotation = 0,20,0.75
    Robot.steer_pair.on_for_rotations(steering, speed, rotation) 
    Robot.steer_pair.off() #stop
    sleep(0.25)

    #Robot.sound.speak('Escape velocity accomplished')

#M10 - Food production
def M10_FoodProduction():
    '''
    5. Turn ~60 degrees counter clock wise (use gyro sensor) and go forward till right color sensor detects white line 
    6. Turn ~120 degrees clockwise (use gyro sensor) such that Arm C is pointing to striker and robot A is in the middle
    7. Move backward till lower part of bar D pushes bar till grey is dropped after green but before tan. (M10-1: 16 points). Water core module would pivot and fall on top of food production (M05-4: 8 points). 
    '''
    #Robot.sound.speak('Mission food production')
    
    #Turn Left 45 degrees
    speed, rotation = -20,0.42
    Robot.left_wheel.on_for_rotations(speed, rotation) 
    Robot.left_wheel.off()

    #Moves straight till the left sensor detects White Light
    while not (Robot.bottom_cl_left.reflected_light_intensity >=Constants.WHITE_LIGHT_INTENSITY):
        steering, speed = 0,-30
        Robot.steer_pair.on(steering, speed)    
    Robot.steer_pair.off()
    #Robot.sound.speak('Second White line detected')

    #Goes forward and turns Clockwise, alligning to Escape Velocity
    steering, speed, rotation = 0,-15,1.41
    Robot.steer_pair.on_for_rotations(steering, speed, rotation) 
    Robot.steer_pair.off()

    #Angles for back towards  food production
    steering, speed, rotation = 50,30,1.22
    Robot.steer_pair.on_for_rotations(steering, speed, rotation) 
    Robot.steer_pair.off()

    #Move backwards to execute food production
    steering, speed, rotation = 0,10,0.5
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()
    #Robot.sound.speak('Mission 10 food production completed')

#M12 - Satellite Orbits
def M12_SatelliteOrbits():
    '''
    8. Move forward and Rotate clockwise ~30 degrees such that bar D is pointing to  Lander module.
    9. Move robot A backward till it back crosses satellite X. Turn 90 degrees clockwise to push satellite towards the outer orbit. (M12-1 : 8 points)

    '''
    #Robot.sound.speak('Mission Satellite Orbit')
    
    #Moves forward to Escape Velocity mission
    steering, speed, rotation = 0,-25,0.95
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()
    sleep(0.3)

    #Turn towards right 45 degrees
    speed, rotation = -30,0.45
    Robot.right_wheel.on_for_rotations( speed, rotation)
    Robot.right_wheel.off()

    #Move back straight past the satellite
    steering, speed, rotation = 0,40,2.3
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    #Rotates Clockwise and moves satelites between blue line
    speed, rotation = 25,0.9
    Robot.left_wheel.on_for_rotations(speed, rotation)
    Robot.left_wheel.off() 
    sleep(0.25)

    #Robot.sound.speak('Mission 12 satellite completed')

def M01_SolarPanel():
    '''
    10. Move forward and turn towards other teams solar panel
    11. Rotate right motor to push lever down on other teams solar panel and push forward to turn to other side. (M02-1 : 22 points)
    '''
    #Robot.sound.speak('Mission Satellite Orbit')
    
    #Moves forward closer to other solar panel
    steering, speed, rotation = 0,-20,0.6
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    # === Section to comment if Opponents solar panel is not be attempted
    #Pivets on Left Wheel to allign lever to Solar Panel
    speed, rotation = -20,0.2
    Robot.right_wheel.on_for_rotations(speed, rotation)
    Robot.right_wheel.off()
    # === Section end
    
    steering, speed, rotation = 0,-10,0.15
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    # === Section to comment if Opponents solar panel is not be attempted
    #Lever pushes down onto Solar Panel
    speed, rotation = 100,1
    Robot.attachment_right.on_for_rotations(speed, rotation)
    Robot.attachment_right.off()
    sleep(0.1)
    # === Section end

    #Robot pushes Satellite to other side 
    steering, speed, rotation = 0,-20,0.8
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    # === Section to comment if Opponents solar panel is not be attempted
    #Lift up
    speed, rotation = -100,1
    Robot.attachment_right.on_for_rotations( speed, rotation)
    Robot.attachment_right.off()
    sleep(0.1)

    #Goes down again just in case
    #Robot.attachment_right.on_for_rotations(100,1)
    #Robot.attachment_right.off()
    #sleep(0.2)

    #Lever Pulls back up
    #Robot.attachment_right.on_for_rotations(-75,1)
    #Robot.attachment_right.off()
    #sleep(0.2)
    # === Section end

    #Backs up
    steering, speed, rotation = 0,20,0.5
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()
    
    #Robot.sound.speak('Mission Oppenent's solar panel completed')

def M08_AerobicExercise():
    '''
    12. Turn robot 90 degrees counter clockwise and moved towards Aerobics exercise. 
    13. Rotate right motor back and forth such that bar strikes on aerobics bar and moves lever to Orange.  (M08-1,2,3 : 22 points). Satellite V&C would already be on top of outer orbit. (M12-2,3 : 16 points)
    '''
    #Robot.sound.speak('Mission Aerobic Exercise')    

    #Piveting Robot; Aligning to Aerobic Excercies
    speed, rotation = 20,0.8
    Robot.right_wheel.on_for_rotations(speed, rotation) 
    Robot.right_wheel.off()

    #Moving forward to get lever over the excercise
    steering, speed, rotation = 0, -20, 1.0
    Robot.steer_pair.on_for_rotations(steering, speed, rotation)
    Robot.steer_pair.off()

    speed, rotation = 100, 1
    Robot.attachment_right.on_for_rotations(speed, rotation)
    Robot.attachment_right.off()
    sleep(0.1)
    #Keep hitting Aerobics Exercise continuously
    n = 0
    while n < 30:
        speed, rotation = -100, 0.75       
        Robot.attachment_right.on_for_rotations(speed, rotation)
        Robot.attachment_right.off()

        speed, rotation = 100, 0.75
        Robot.attachment_right.on_for_rotations(speed, rotation)
        Robot.attachment_right.off()

        n = n + 1
    
    #Robot.sound.speak('Mission Aerobics Exercise completed')

#function to execute the run3 mission plan
def run3():
    """
    Main execute function for Run 2
    """
    #Resetting the motors
    ResetRobot.reset_wheel_motors()
    ResetRobot.reset_attachment_motors()
    
    #M13 -Observatory
    M13_Observatory()

    #M11- Escape velocity after food production
    M11_EscapeVelocity()

    #M10 - Food Production
    M10_FoodProduction()

    #M12 - Satellite orbits
    M12_SatelliteOrbits()
    
    #M01 - Opposite table satellites
    M01_SolarPanel()
    
    #M08 - Aerobic Exercise
    M08_AerobicExercise()

    
#function that will be called from other modules
def execute_run3():
    #Robot.sound.speak('Executing Run3')
    run3()