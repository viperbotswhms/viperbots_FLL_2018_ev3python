import Robot
import Constants
import ResetRobot
import Gyro
import CalibrateRobot

from time import sleep

def M07_ConeModule():

    #setting gyro params
    Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
    
    current_zero_angle=Robot.robot_gyro.angle

    Robot.sound.speak('Executing Mission 7 cone module')
    #Robot.steer_pair.on_for_rotations(0,-19.5,4.35)

   #trying gyro         
    Gyro.gyro_mov_on_for_rotations(-19.5,2.3,current_zero_angle)
    #Gyro.gyro_mov_on_for_rotations_gain(-19,2.3,current_zero_angle,gain)
    #steering = Gyro.PID_steer
    #Robot.steer_pair.on_for_rotations(0,-50,2.5)
   # while not Robot.bottom_cl_left.reflected_light_intensity >= Constants.WHITE_LIGHT_INTENSITY:
        #steering = Gyro.PID_steer
        #Robot.steer_pair.on(steering,-50)

    Robot.sound.speak('Tube mission accomplished')

    Robot.steer_pair.off()
    

def M04_CraterCrossing():

    Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG

    Robot.sound.speak('Executing Mission 4 Crater crossing')

    #lowering the cone carrier
    Robot.attachment_right.on_for_rotations(-100,4)
    Robot.attachment_right.off()

    #moving back
    Robot.steer_pair.on_for_rotations(0,20,0.2) #move back a bit
    Robot.steer_pair.off()

    #turn perpendicular to extraction module for crater crossing
    #Robot.steer_pair.on_for_rotations(-50,15,0.76) 27 Nov
    Robot.steer_pair.on_for_rotations(-50,15,0.75)
    #Gyro.gyro_speed_direction_control_fwd(90,-50,0.76)

    
    Robot.steer_pair.on_for_rotations(0,-20,2.35)#Move 500mm
    Robot.steer_pair.off()
    Robot.attachment_left.on_for_rotations(-100,1)
    Robot.attachment_left.off()
    Robot.sound.speak('Crater crossing accomplished')

def M09_StrengthBar():
    Robot.sound.speak('Executing Mission 9 Strength bar')
    Robot.attachment_right.on_for_rotations(100,20)
    Robot.attachment_right.off()
    Robot.tank_pair.on_for_rotations(-20,-40,0.9)
    Robot.tank_pair.off()
    Robot.attachment_right.on_for_rotations(-100,35)
    Robot.steer_pair.on_for_rotations(0,-15,1)
    Robot.steer_pair.off()
    Robot.attachment_right.on_for_rotations(100,25)
    Robot.attachment_right.off()

def M03_3DPrintingBackup():
    Robot.sound.speak('Executing Mission 3 3d Printing')
    Robot.attachment_right.on_for_rotations(100,10.5)
    Robot.attachment_right.off()
    Robot.tank_pair.on_for_rotations(-20,-40,0.9)
    Robot.tank_pair.off()
    Robot.steer_pair.on_for_rotations(0,10,1)
    Robot.attachment_left.on_for_rotations(-100,3)
    Robot.attachment_left.off()
    sleep(0.3)

#M14–Meteoroid Deflection
def M14_MeteroidDeflection():
    #moving back from 3D printer
    Robot.steer_pair.on_for_rotations(0, -25, 0.5)
    Robot.steer_pair.off()
    Robot.right_wheel.on_for_rotations(-15,0.3)
    Robot.right_wheel.off()
    #Robot.steer_pair.on_for_rotations(0, -75, 1.3)
    #Robot.steer_pair.off()
    pass

def run2():
    
    #CalibrateRobot.calibrate_gyro()
    ResetRobot.reset_attachment_motors()
    ResetRobot.reset_wheel_motors()
    CalibrateRobot.calibrate_gyro()

    #M07-cone module
    M07_ConeModule()

    #crater crossing
    M04_CraterCrossing()

    #M09_StrengthBar()

    #M03 - 3DPrinting
    M03_3DPrintingBackup()

    #M14 - Meteor Deflection
    M14_MeteroidDeflection()
   
   
              

def execute_run2():
    Robot.sound.speak('Executing Run2')
    run2()


