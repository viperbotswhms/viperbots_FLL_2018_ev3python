import Robot
import Constants

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#ResetRobot.py - Reset functions for robots and motors

def reset_wheel_motors():
    Robot.right_wheel.reset()
    Robot.left_wheel.reset()

def reset_attachment_motors():
    Robot.attachment_right.reset()
    Robot.attachment_left.reset()

def reset_robot():
    reset_wheel_motors()
    reset_attachment_motors()
