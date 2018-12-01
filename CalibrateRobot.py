import Robot
import Constants

from time import sleep

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#CaliberateRobot.py - Caliberate Robot Gyro module by switching between different modes on the gyro sensor 

from time import sleep

def calibrate_gyro():
    """
    Caliberate Robot Gyro module by switching between different modes on the gyro sensor
    Select form Angle mode to Rate code to angle and reading for gyro value in between 
    """
    #Robot.sound.speak('Calibrating gyro')
    Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
    measured_angle = Robot.robot_gyro.angle 
    sleep(0.5)
    while measured_angle != 0:
        Robot.robot_gyro.mode=Constants.MODE_GYRO_RATE        
        measured_angle = Robot.robot_gyro.angle   
        sleep(0.5)
        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        measured_angle=Robot.robot_gyro.angle
    #Robot.sound.speak('Gyro Calibrated')

