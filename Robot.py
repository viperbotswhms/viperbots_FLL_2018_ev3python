from time import sleep

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#Robot.py - Logical defenition of the robot with defnition of the ports on the EV3 and the sensors / motors connected to 

#import motor modules and the ev3 ports used for it
from ev3dev2.motor import LargeMotor,OUTPUT_B,OUTPUT_C
from ev3dev2.motor import MoveSteering, MoveTank
from ev3dev2.motor import SpeedNativeUnits
from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_D

#import Sensor modules and the ev3 ports used for it
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_4

from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_3

#import sound and button functions for EV3
from ev3dev2.sound import Sound
from ev3dev2.button import Button

#Port assignments
MEDIUM_MOTOR_LEFT=OUTPUT_A
MEDIUM_MOTOR_RIGHT=OUTPUT_D
LARGE_MOTOR_LEFT_PORT=OUTPUT_B
LARGE_MOTOR_RIGHT_PORT=OUTPUT_C

COLORSENSOR_TOP = INPUT_1
COLORSENSOR_BOTTOM_RIGHT = INPUT_2
COLORSENSOR_BOTTOM_LEFT = INPUT_4

GYROSENSOR_PORT = INPUT_3

#Attachment motor direction
CLK_WISE='clock_wise' #positive speed
ANTI_CLK_WISE='anti_clck_wise' #negative speed


#Creat objects for the ev3 buttons, motors and sensors. Only one object will be created for each physical object and used in every program

#LARGEMOTORS USED FOR WHEELS
#Create individual wheel objects
left_wheel=LargeMotor(LARGE_MOTOR_LEFT_PORT)
right_wheel=LargeMotor(LARGE_MOTOR_RIGHT_PORT)

#Create object functions for basic movements for wheel pair blocks
steer_pair=MoveSteering(LARGE_MOTOR_LEFT_PORT,LARGE_MOTOR_RIGHT_PORT)
tank_pair=MoveTank(LARGE_MOTOR_LEFT_PORT,LARGE_MOTOR_RIGHT_PORT)

#MEDIUM MOTORS USED FOR ATTACHMENT GEARS
#Create individual motor objects
attachment_left=MediumMotor(MEDIUM_MOTOR_LEFT)
attachment_right=MediumMotor(MEDIUM_MOTOR_RIGHT)

#TOP COLOR SENSOR IS USED FOR ATTACHMENT VERIFICATION
#BOTTOM COLOR SENSORS ARE USED FOR WHITE LINE DETECTION
#Create Color sensor objects
top_cl=ColorSensor(COLORSENSOR_TOP)
bottom_cl_right=ColorSensor(COLORSENSOR_BOTTOM_RIGHT)
bottom_cl_left=ColorSensor(COLORSENSOR_BOTTOM_LEFT)

#Create GYROSENSOR
robot_gyro=GyroSensor(GYROSENSOR_PORT)

#Create sound and button objects for EV3
sound = Sound()
button = Button()

