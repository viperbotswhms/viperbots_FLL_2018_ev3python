import Robot
import Constants
import ResetRobot
import Gyro
import CalibrateRobot

from time import sleep

#M13- observatory

def M13_Observatory():
    #Robot.sound.speak('Exexuting Mission 13 observatory')

    #Move foraward until outside of base for mesasuring white line
    Robot.steer_pair.on_for_rotations(0,-75,3) 
    Robot.steer_pair.off()

    #applying correction for drift for moving forward until white lne detected
    #Gyro.gyro_mov_straight_until_white(-30)  
    Gyro.gyro_mov_straight_until_white_right(-35)
    Robot.steer_pair.off()

    #Robot.sound.speak('First White Line Detected')
    Robot.steer_pair.on_for_rotations(0,-15,0.4) #move forward a little
    Robot.steer_pair.off() #stop
    #Robot.sound.speak('Mission 13 Observatory accomplished')


#M11 -Escape Velocity

def M11_EscapeVelocity():
    #Robot.sound.speak('Executing escape velocity')
    Robot.steer_pair.on_for_rotations(0,20,0.38) #move back a little
    Robot.steer_pair.off() #stop
    sleep(0.25)

    #smaaashing
    #Robot.attachment_left.on_for_rotations(100,1.5)
    #Robot.attachment_left.off()
    #sleep(0.5)
    #Robot.attachment_left.on_for_rotations(-100,1)
    #Robot.attachment_left.off()
    #Robot.sound.speak('Escape velocity accomplished')

#M10 - Food production

def M10_FoodProduction():
    #Robot.sound.speak('Mission food production')
    Robot.steer_pair.on_for_rotations(0,20,0.38) #move back a little
    Robot.steer_pair.off() #stop
    sleep(0.25)

    Robot.left_wheel.on_for_rotations(-20,0.5) #turn 45 degrees
    Robot.steer_pair.off()
    while not (Robot.bottom_cl_left.reflected_light_intensity >=Constants.WHITE_LIGHT_INTENSITY):
        Robot.steer_pair.on(0,-30)
    #Gyro.gyro_mov_straight_until_white(-35)
    Robot.steer_pair.off()
    #Robot.sound.speak('Second White line detected')

    #aligning to food production
    #Robot.steer_pair.on_for_rotations(0,-15,0.85) 26 Nov
    Robot.steer_pair.on_for_rotations(0,-15,0.9)
    Robot.steer_pair.on_for_rotations(50,30,1.35)

    #executing food production
    #Robot.steer_pair.on_for_rotations(0,10,0.6) $29nov 5.53pm
    Robot.steer_pair.on_for_rotations(0,10,0.4)
    Robot.steer_pair.off()
    #Robot.sound.speak('Mission 10 food production completed')

def M11_EscapeVelocity_PostFoodProduction():
    Robot.steer_pair.on_for_rotations(0,-25,1.17)
    Robot.steer_pair.off
     #smaaashing
    Robot.attachment_left.on_for_rotations(100,1.5)
    Robot.attachment_left.off()
    sleep(0.3)
    Robot.attachment_left.on_for_rotations(-100,3)
    Robot.attachment_left.off()
    sleep(0.5)
    #Robot.sound.speak('Escape velocity accomplished')bot


#M15 - Lander
def M15_Lander():
    
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

#Returning to base
def run2_returnbase():

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
   
    #Returning to base
    #run2_returnbase()


    
#function that will be called from other modules
def execute_run3():
    #Robot.sound.speak('Executing Run3')
    run3()