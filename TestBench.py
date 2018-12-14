#!/usr/bin/env python3

import Robot
import ResetRobot
import Constants
import CalibrateRobot
import Gyro

from time import sleep

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#TestBench.py - Test programs for few functions on gyro, PID and motions


def test_calibrateGyro():
    CalibrateRobot.calibrate_gyro()

def run_robo():
    loop = True
    while loop:
        while not Robot.button.any():
            Robot.steer_pair.on(0,-100)
        ResetRobot.reset_robot()
        Robot.sound.speak('Exiting robo move')
        break

def test_move(steering,speed,rotations):
    if rotations>2 and rotations <4:
        rot1=2
        rot2=rotations-rot1
    kp=0.6
    ki=0
    kd=0
    #Robot.steer_pair.on_for_rotations(steering,speed,rot1)
    #Robot.steer_pair.on_for_rotations(steering,speed,rot1)
    #Gyro.gyro_mov_on_for_rotation_PCorrection(speed,rot1,kp)
    Robot.steer_pair.on_for_rotations(0,speed,rot1)
    Robot.steer_pair.off()
    Gyro.gyro_mov_on_for_rotation_PID(speed,rot2,kp,ki,kd)
    Robot.steer_pair.off()

def test_move_seconds(speed,seconds):
    
    kp=0.6
    ki=0
    kd=0
    Gyro.gyro_mov_on_for_rotation_PID_seconds(speed,seconds,kp,ki,kd)


def test_move_st_angle(delta_angle,speed,rotations):
    kp=0.6
    ki=0
    kd=0
    Gyro.gyro_mov_on_for_rotation_PID(speed,rotations,kp,ki,kd)
    Robot.steer_pair.off()
    sleep(0.2)
    Gyro.mov_on_angle_straight(delta_angle,speed,rotations,kp,ki,kd)

def test_run():    
    while True:
        while not Robot.button.any():
            Robot.sound.beep()
        if Robot.button.enter:
            test_calibrateGyro()
        elif Robot.button.right:
            sleep(0.2)
            
            test_move_st_angle(30,-50,4)
        elif Robot.button.left:
            sleep(0.2)
            Robot.sound.speak('Left button movement test')
            steering=0
            speed=-50
            seconds=3
            test_move_seconds(speed,seconds)
            #rotations = 3
            #test_move(speed,rotations
            
        elif Robot.button.up:
            Robot.sound.speak('Exiting test loop')
            break

